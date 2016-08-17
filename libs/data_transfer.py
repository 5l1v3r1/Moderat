import socket
import ast


def data_receive(sock, end='[ENDOFMESSAGE]'):
    received_data = ''
    try:
        payload = sock.recv(1024)
        while payload:
            received_data = received_data + payload
            if received_data.endswith(end):
                received_data = received_data[:-len(end)].decode('utf-8')
                break
            else:
                payload = sock.recv(1024)
                continue
        return ast.literal_eval(received_data)
    except socket.error:
        return {'payload': '', 'mode': '', 'frome': '', 'to': '',}


# Send Data Function
def data_send(sock, message, mode, session_id, to='', end='[ENDOFMESSAGE]'):
    message = {
        'payload': message,
        'mode': mode,
        'from': 'moderator',
        'to': to,
        'session_id': session_id,
    }
    sock.sendall(str(message)+end)


def data_get(sock, message, mode, session_id, to=''):
    data_send(sock, message, mode, session_id, to)
    return data_receive(sock)
