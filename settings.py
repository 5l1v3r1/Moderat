import ConfigParser


class Config:

    def __init__(self):

        self.config_file = 'settings.ini'

        self.config = ConfigParser.ConfigParser()
        self.config.read(self.config_file)

        try:
            self.ip_address = str(self.config.get('connection_settings', 'ip_address'))
            self.port = int(self.config.get('connection_settings', 'port'))
            self.timeout = int(self.config.get('connection_settings', 'timeout'))
            self.max_connections = int(self.config.get('connection_settings', 'max_connections'))
        except:
            self.set_default_settings()


    def set_default_settings(self):

        open(self.config_file, 'w').close()

        self.config.read(self.config_file)

        # add connection settings
        self.config.add_section('connection_settings')
        self.config.set('connection_settings', 'ip_address', '0.0.0.0')
        self.config.set('connection_settings', 'port', 4434)
        self.config.set('connection_settings', 'timeout', 5)
        self.config.set('connection_settings', 'max_connections', 127)

        with open(self.config_file, 'w') as config_file:
            self.config.write(config_file)
