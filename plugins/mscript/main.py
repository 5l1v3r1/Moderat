from PyQt4.QtGui import *
from PyQt4.QtCore import *

import socket

import main_ui
import linesnum

from libs.modechat import get


class mainPopup(QWidget, main_ui.Ui_Form):

    def __init__(self, args):
        QWidget.__init__(self)
        self.setupUi(self)

        self.sock = args['sock']
        self.socket = args['socket']
        self.ipAddress = args['ipAddress']

        self.setWindowTitle('Remote Scripting in - %s - Socket #%s' % (self.ipAddress, self.socket))

        # init idle with lines
        self.idle = linesnum.LineTextWidget()
        self.horizontalLayout_2.addWidget(self.idle)

        self.outputText.setVisible(False)

        self.runButton.clicked.connect(self.run_script)

    def run_script(self):
        script = self.idle.getTextEdit()
        output = get(self.sock, 'runscript %s' % script, 'getoutput')
        self.outputText.setVisible(True)
        self.outputText.setHtml(output)