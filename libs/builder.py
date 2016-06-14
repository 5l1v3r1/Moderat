from ui.builder import Ui_Form as builderUi
from PyQt4.QtGui import *

import random
import string


class Builder(QWidget, builderUi):

    def __init__(self, args):
        QWidget.__init__(self)
        self.setupUi(self)

        # START: triggers
        self.showPasswordButton.clicked.connect(self.set_password_echo_mode)
        self.generateRandomNameButton.clicked.connect(self.set_new_file_name)
        # END: triggers

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

