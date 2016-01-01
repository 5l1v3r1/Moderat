import socket
import sys


# send socket
def send(Sock, cmd, mode='example', splitter='%:::%', end='[ENDOFMESSAGE]'):
    try:
        Sock.sendall((mode + splitter + cmd + end).encode('utf-8'))
    except socket.error:
        pass


def get(Sock, cmd, mode, splitter='%:::%', end='[ENDOFMESSAGE]'):
    data = ''
    Sock.sendall((mode + splitter + cmd + end).encode('utf-8'))
    l = Sock.recv(1024)
    while l:
        data += l
        if data.endswith(end):
            if data.count(splitter) == 2:
                size_of_package, server_mode, message = data.split(splitter)
                try:
                    if int(size_of_package) != sys.getsizeof(message) or mode != server_mode:
                        return ''
                except ValueError:
                    return ''
                break
            else:
                return ''
        else:
             l = Sock.recv(1024)
    return message[:-len(end)].decode('utf-8')

def upload():
    pass

def download():
    pass