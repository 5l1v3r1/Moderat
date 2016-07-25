# -*- coding: utf-8 -*-
# !/usr/bin/python

import socket
import time
import ast
import sys
import os
import platform
import ctypes

HOST = '127.0.0.1'
PORT = 4434


def get_key():
    if os.path.exists('info.nfo'):
        key_output = open('about.nfo', 'r').read()
        return key_output
    else:
        return ''


def set_key(key):
    key_input_file = open('about.nfo', 'w')
    key_input_file.write(key)
    key_input_file.close()
    return


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
        return {'payload': '', 'mode': '', 'source': ''}


# Send Data Function
def data_send(sock, message, mode, end='[ENDOFMESSAGE]'):
    message = {
        'payload': message,
        'mode': mode,
        'source': 'client',
    }
    sock.sendall(str(message)+end)


def start_from_autorun():
    while 1:
        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.connect((HOST, PORT))
        except:
            time.sleep(5)
            continue

        while 1:
            try:
                data = data_receive(server_socket)
                if data['payload'] == 'connectSuccess':
                    key = get_key()
                    print key
                    if len(key) != 0:
                        data_send(server_socket, key, 'clientInitializing')
                    else:
                        data_send(server_socket, 'noKey', 'clientInitializing')
                        print 'sent'
                        new_key = data_receive(server_socket)
                        print new_key
                        print 'received'
                        set_key(new_key)
            except socket.error:
                server_socket.close()
                time.sleep(10)
                break

start_from_autorun()
