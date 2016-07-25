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
        print 'new connection'
        self.send_message_to_client(self, 'connectSuccess', 'welcome')

    def connectionLost(self, reason):
        pass

    def dataReceived(self, data):
        # Get Data
        command = self.recieve_message(data)
        # Switch to client commands
        if command['source'] == 'client':
            self.client_commands(command['payload'], command['mode'])
        # Switch to moderator commands
        elif command['source'] == 'moderator':
            pass

    def client_commands(self, payload, mode):
        # Check client for keys
        if mode == 'clientInitializing':
            print payload
            if payload == 'noKey':
                print 'no key'
                self.send_message_to_client(self, id_generator(), 'clientInitializing')
            else:
                # TODO: Write db
                self.send_message_to_client(self, id_generator(), 'clientInitializing')
            print self.factory.clients
            print 'New Connection from %s' % self.transport.getHost().host

    def recieve_message(self, data, end='[ENDOFMESSAGE]'):
        return ast.literal_eval(data[:-len(end)].decode('utf-8'))

    def send_message_to_client(self, client, message, mode, end='[ENDOFMESSAGE]'):
        # Send Data Function
        message = {
            'payload': message,
            'mode': mode,
            'source': 'server',
        }
        client.transport.write(str(message)+end)

    def send_message_to_moderator(self, moderator, message):
        self.factory.clients[moderator]['sock'].transport.write(str(message))


class ModeratServerFactory(ServerFactory):

    protocol = ModeratServerProtocol

    def __init__(self):
        self.clients = {}
        self.clients_checker = task.LoopingCall(self.check_for_clients)
        self.clients_checker.start(10)

    def check_for_clients(self):
        for client in self.clients:
            client.transport.write("10 seconds has passed\n")

    def clientConnectionMade(self, id, client, ip_address):
        if self.clients.has_key(id):
            return
        self.clients.append(client)

    def clientConnectionLost(self, client):
        self.clients.remove(client)

#factory = Factory()
#factory.protocol = ModeratServerProtocol

reactor.listenTCP(4434, ModeratServerFactory())

reactor.run()