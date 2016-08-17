from PyQt4.QtGui import *
from PyQt4.QtCore import *

import main_ui
import linesnum

from libs.data_transfer import data_get


class mainPopup(QWidget, main_ui.Ui_Form):

    def __init__(self, args):
        QWidget.__init__(self)
        self.setupUi(self)

        self.sock = args['sock']
        self.client = args['client']
        self.session_id = args['session_id']

        self.setWindowTitle('Remote Scripting')

        # init idle with lines
        self.idle = linesnum.LineTextWidget()
        self.idleLayout.addWidget(self.idle)

        self.runButton.clicked.connect(self.run_script)
        self.fromFileButton.clicked.connect(self.from_file)
        self.clearButton.clicked.connect(self.clear_script)

        # Shortcuts
        self.connect(QShortcut(QKeySequence('Ctrl+Return'), self), SIGNAL('activated()'), self.run_script)
        self.connect(QShortcut(QKeySequence('Ctrl+P'), self.idle), SIGNAL('activated()'), self.insert_mprint)

    def run_script(self):
        script = self.idle.getTextEdit()
        output = data_get(self.sock, str(script), 'scriptingMode', session_id=self.session_id, to=self.client)
        # TODO: OUTPUT
        print output['payload']

    def from_file(self):
        filename = QFileDialog.getOpenFileName(self, 'Open Python File', '', 'Python Files (*.py)')
        if filename:
            with open(filename, 'r') as f_:
                self.idle.setText(f_.read())

    def clear_script(self):
        self.idle.clearText()

    def insert_mprint(self):
        self.idle.appendText('mprint = ')
