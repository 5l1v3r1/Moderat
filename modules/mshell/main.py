from PyQt4.QtGui import *
from PyQt4.QtCore import *

import socket

import main_ui
import console

from libs.data_transfer import data_get, data_send
from libs.language import Translate

# Multi Lang
translate = Translate()
_ = lambda _word: translate.word(_word)


class mainPopup(QWidget, main_ui.Ui_Form):

    def __init__(self, args):
        QWidget.__init__(self)
        self.setupUi(self)

        self.moderator = args['moderator']
        self.client = args['client']
        self.session_id = args['session_id']
        self.module_id = args['module_id']

        self.setWindowTitle(_('MSHELL_TITLE'))

        self.console = console.Console()
        self.gridLayout.addWidget(self.console)

        self.connect(self.console, SIGNAL("returnPressed"), self.runCommand)

    def signal(self, data):
        self.callback(data)

    # run shell command
    def runCommand(self):
        command = self.console.command[1:] if self.console.command.startswith(' ') else self.console.command
        self.moderator.send_msg(command, 'shellMode', session_id=self.session_id, _to=self.client, module_id=self.module_id)
        self.callback = self.recvOutput

    def recvOutput(self, data):
        data['payload'] = data['payload'].replace('\n', '<br>')
        self.console.append('<br><font color=#c9f5f7>'+data['payload']+'</font>')
        self.console.newPrompt()
