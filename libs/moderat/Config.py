import ConfigParser
import os

class Config:

    def __init__(self):

        self.config_file = 'settings.ini'

        if not os.path.exists(self.config_file):
            open(self.config_file, 'w').close()

        self.config = ConfigParser.ConfigParser()
        self.config.read(self.config_file)

        try:
            self.ip_address = str(self.config.get('connection_settings', 'ip_address'))
            self.port = int(self.config.get('connection_settings', 'port'))
            self.language = str(self.config.get('interface', 'language'))
        except:
            self.set_default_settings()

    def set_default_settings(self):

        open(self.config_file, 'w').close()

        self.config.read(self.config_file)

        # add connection settings
        try:
            self.config.add_section('connection_settings')
        except ConfigParser.DuplicateSectionError:
            pass
        self.config.set('connection_settings', 'ip_address', '192.168.1.2')
        self.config.set('connection_settings', 'port', 1313)
        try:
            self.config.add_section('interface')
        except ConfigParser.DuplicateSectionError:
            pass
        self.config.set('interface', 'language', 'english')

        with open(self.config_file, 'w') as config_file:
            self.config.write(config_file)