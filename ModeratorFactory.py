import struct
import ast

from twisted.internet.protocol import Protocol, ClientFactory


class SocketModeratorProtocol(Protocol):

    def __init__(self):

        self.__buffer__ = ''

    # New Connection Made
    def connectionMade(self):
        self.factory.clientReady(self)

    def connectionLost(self, reason):
        self.factory.clientConnectionFailed(self, reason)

    def dataReceived(self, data, end='[ENDOFMESSAGE]'):
        try:
            # Data Received
            self.__buffer__ += data
            if self.__buffer__.endswith(end):
                self.__buffer__ = self.__buffer__[:-len(end)]
                if end in self.__buffer__:
                    self.__buffer__ = self.__buffer__.split(end)[0]
                command = ast.literal_eval(self.__buffer__)
                self.__buffer__ = ''

            self.factory.got_msg(command)
        except Exception as errMessage:
            self.factory.got_msg(errMessage)

    # Send Message To Client
    def send_message_to_server(self, client, message, mode, _from='server', session_id='', end='[ENDOFMESSAGE]'):
        # Send Data Function
        self.transport.write(str({
            'payload': message,
            'mode': mode,
            'from': _from,
            'session_id': session_id,
        })+end)


class SocketModeratorFactory(ClientFactory):
    """ Created with callbacks for connection and receiving.
        send_msg can be used to send messages when connected.
    """
    protocol = SocketModeratorProtocol

    def __init__(
            self,
            connect_success_callback,
            connect_fail_callback,
            recv_callback):
        self.connect_success_callback = connect_success_callback
        self.connect_fail_callback = connect_fail_callback
        self.recv_callback = recv_callback
        self.moderator = None

        self.__buffer__ = ''

    def clientConnectionFailed(self, connector, reason):
        self.connect_fail_callback(reason)

    def clientReady(self, moderator):
        self.moderator = moderator
        self.connect_success_callback()

    def got_msg(self, data):
        self.recv_callback(data)

    def send_msg(self, msg):
        if self.moderator:
            self.moderator.send_message_to_server(self.moderator, self.moderator, 'auth', 'auth')