import socket


# send socket
def client_send(Sock, cmd, mode='example', splitter='%:::%', end='[ENDOFMESSAGE]'):
    try:
        Sock.sendall((mode + splitter + cmd + end).encode('utf-8'))
    except socket.error:
        pass


def client_get(Sock, cmd, mode, splitter='%:::%', end='[ENDOFMESSAGE]'):
    data = ''
    try:
        Sock.sendall((mode + splitter + cmd + end).encode('utf-8'))
        l = Sock.recv(1024)
        while l:
            data += l
            if data.endswith(end):
                if data.count(splitter) == 2:
                    size_of_package, server_mode, message = data.split(splitter)
                    try:
                        if int(size_of_package) != len(message) or mode != server_mode:
                            print len(size_of_package), ' ', len(message)
                            print mode, ' ', server_mode
                            print message
                            print 'Size Error (%s)' % data
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
        return message[:-len(end)].decode('utf-8')
    except socket.error:
        return ''


def moderator_receive(sock, splitter='%:::%', end="[ENDOFMESSAGE]"):
        received_data = ""
        l = sock.recv(1024)
        while l:
            received_data = received_data + l
            if received_data.endswith(end):
                break
            else:
                l = sock.recv(1024)
        if received_data.count(splitter):
            _type, message = received_data.split(splitter)
            return _type, message[:-len(end)].decode('utf-8')
        else:
            return 'info', ''


def moderator_send(sock, _data, mode, splitter='%:::%', end="[ENDOFMESSAGE]"):
    msg = (_data + end).encode('utf-8')
    size = len(msg)
    msg = mode + splitter + msg
    sock.sendall(str(size) + '%:::%' + msg)
