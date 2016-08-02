import ConfigParser
import languages
import os


def _(tr, word):
    if word in tr:
        return tr[word]
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
        self.config.set('connection_settings', 'port', 4434)
        try:
            self.config.add_section('interface')
        except ConfigParser.DuplicateSectionError:
            pass
        self.config.set('interface', 'language', 'english')

        with open(self.config_file, 'w') as config_file:
            self.config.write(config_file)


from ui.settings import Ui_Form as settingsUi
from PyQt4.QtGui import *


class Settings(QWidget, settingsUi):

    def __init__(self, args):
        QWidget.__init__(self)
        self.setupUi(self)

        self.config_file = 'settings.ini'

        self.LANGUAGE = args['language']
        self.t = self.get_language()

        self.settingsTab.setTabText(0, _(self.t, 'TAB_CONNECTION_SETTINGS'))
        self.ipAddressLabel.setText(_(self.t, 'SETTINGS_IP_ADDRESS'))
        self.portLabel.setText(_(self.t, 'SETTINGS_PORT'))
        self.saveButton.setText(_(self.t, 'SETTINGS_SAVE'))

        self.check_settings()
        self.get_settings()
        self.saveButton.clicked.connect(self.save_settings)

    def get_language(self):
        if self.LANGUAGE in languages.__all__:
            lang = __import__('libs.languages.%s' % self.LANGUAGE, globals(), locals(), ['tr'], -1)
            return lang.tr

    def get_settings(self):
        config = ConfigParser.ConfigParser()
        config.read(self.config_file)

        self.ipAddressLine.setText(str(config.get('connection_settings', 'ip_address')))
        self.portLine.setText(str(config.get('connection_settings', 'port')))

    def check_settings(self):
        Config()

    def save_settings(self):
        # Connection values
        ip_address = str(self.ipAddressLine.text())
        port = str(self.portLine.text())
        # Interface Values

        config = ConfigParser.ConfigParser()
        config.read(self.config_file)

        # add connection settings
        config.set('connection_settings', 'ip_address', ip_address)
        config.set('connection_settings', 'port', port)
        # add interface settings

        with open(self.config_file, 'wb') as config_file:
            config.write(config_file)

        msg = QMessageBox(QMessageBox.Information, _(self.t, 'SETTINGS_MSG_INFO'), _(self.t, 'SETTINGS_MSG_TEXT'))
        msg.exec_()
