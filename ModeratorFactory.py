import struct
import ast

from twisted.internet.protocol import Protocol, ClientFactory


class SocketModeratorProtocol(Protocol):

    def __init__(self):

        pass

    # New Connection Made
    def connectionMade(self):
        self.factory.clientReady(self)

    def connectionLost(self, reason):
        self.factory.clientConnectionFailed(self, reason)

    def dataReceived(self, data):
        self.factory.got_msg(data)

    # Send Message To Server
    def send_message_to_server(self, payload):
        # Send Data Function
        self.transport.write(payload)


class SocketModeratorFactory(ClientFactory):
    """ Created with callbacks for connection and receiving.
        send_msg can be used to send messages when connected.
    """
    protocol = SocketModeratorProtocol
    __buffer__ = ''

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

    def got_msg(self, data, end='[ENDOFMESSAGE]'):
        try:
            # Data Received
            self.__buffer__ += data
            if end in self.__buffer__:
                commands = self.__buffer__.split(end)
                command = ast.literal_eval(commands[0])
                self.__buffer__ = self.__buffer__[len(commands[0]+end):]
            else:
                return
        except Exception as errMessage:
            self.recv_callback(errMessage)
            return
        self.recv_callback(command)

    def send_msg(self, message, mode, _to='', session_id='', module_id='', end='[ENDOFMESSAGE]'):
        if self.moderator:
            payload = str({
                'payload': message,
                'mode': mode,
                'from': 'moderator',
                'session_id': session_id,
                'to': _to,
                'module_id': module_id,
            })+end
            self.moderator.send_message_to_server(payload)