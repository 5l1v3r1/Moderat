import socket

# send socket
def send(Sock, cmd, socket_id, splitter='%:::%', end='[ENDOFMESSAGE]'):
    try:
        Sock.sendall((socket_id + splitter + cmd + end).encode('utf-8'))
    except socket.error:
        pass


def get(Sock, cmd, socket_id, splitter='%:::%', end='[ENDOFMESSAGE]'):
    data = ''
    try:
        Sock.sendall((str(socket_id) + splitter + cmd + end).encode('utf-8'))
        l = Sock.recv(1024)
        while l:
            data += l
            if data.endswith(end):
                if data.count(splitter) == 2:
                    size_of_package, server_mode, message = data.split(splitter)
                    try:
                        if int(size_of_package) != len(message):
                            print 'Size Error'
                            return ''
                    except ValueError:
                        print 'Value Error'
                        return ''
                    break
                else:
                    print 'Data Count Error'
                    return ''
            else:
                l = Sock.recv(1024)
                continue
        return message[:-len(end)].decode('utf-8')
    except socket.error:
        return ''
