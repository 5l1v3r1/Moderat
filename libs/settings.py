import ConfigParser
import os


def _(tr3, word):
    if word in tr3:
        return tr3[word]
    else:
        return word


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
            self.timeout = int(self.config.get('connection_settings', 'timeout'))
            self.max_connections = int(self.config.get('connection_settings', 'max_connections'))
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
        self.config.set('connection_settings', 'ip_address', '0.0.0.0')
        self.config.set('connection_settings', 'port', 4434)
        self.config.set('connection_settings', 'timeout', 5)
        self.config.set('connection_settings', 'max_connections', 127)
        try:
            self.config.add_section('interface')
        except ConfigParser.DuplicateSectionError:
            pass
        self.config.set('interface', 'language', 'english')

        with open(self.config_file, 'w') as config_file:
            self.config.write(config_file)


from ui.settings import Ui_Form
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Settings(QWidget, Ui_Form):

    def __init__(self, args):
        QWidget.__init__(self)
        self.setupUi(self)

        self.config_file = 'settings.ini'

        self.t = args['language']

        self.settingsTab.setTabText(0, _(self.t, 'TAB_CONNECTION_SETTINGS'))
        self.settingsTab.setTabText(1, _(self.t, 'INTERFACE'))
        self.ipAddressLabel.setText(_(self.t, 'SETTINGS_IP_ADDRESS'))
        self.portLabel.setText(_(self.t, 'SETTINGS_PORT'))
        self.timeoutLabel.setText(_(self.t, 'SETTINGS_TIMEOUT'))
        self.maxConnectionsLabel.setText(_(self.t, 'SETTINGS_MAX_CONNECTIONS'))
        self.languageLabel.setText(_(self.t, 'SETTINGS_LANGUAGE'))
        self.saveButton.setText(_(self.t, 'SETTINGS_SAVE'))

        self.check_settings()
        self.get_settings()
        self.saveButton.clicked.connect(self.save_settings)

    def get_settings(self):
        config = ConfigParser.ConfigParser()
        config.read(self.config_file)

        self.ipAddressLine.setText(str(config.get('connection_settings', 'ip_address')))
        self.portLine.setText(str(config.get('connection_settings', 'port')))
        self.timeoutLine.setText(str(config.get('connection_settings', 'timeout')))
        self.maxConnectionsLine.setText(str(config.get('connection_settings', 'max_connections')))

    def check_settings(self):
        Config()

    def save_settings(self):
        ip_address = str(self.ipAddressLine.text())
        port = str(self.portLine.text())
        timeout = str(self.timeoutLine.text())
        max_connections = str(self.maxConnectionsLine.text())

        config = ConfigParser.ConfigParser()
        config.read(self.config_file)

        # add connection settings
        config.set('connection_settings', 'ip_address', ip_address)
        config.set('connection_settings', 'port', port)
        config.set('connection_settings', 'timeout', timeout)
        config.set('connection_settings', 'max_connections', max_connections)

        with open(self.config_file, 'wb') as config_file:
            config.write(config_file)

        msg = QMessageBox(QMessageBox.Information, _(self.t, 'SETTINGS_MSG_INFO'), _(self.t, 'SETTINGS_MSG_TEXT'))
        msg.exec_()

