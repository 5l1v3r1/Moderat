from PyQt4.QtGui import *

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
        self.horizontalLayout_2.addWidget(self.idle)

        self.outputText.setVisible(False)

        self.runButton.clicked.connect(self.run_script)
        self.closeOutputButton.clicked.connect(self.close_output)
        self.fromFileButton.clicked.connect(self.from_file)

    def run_script(self):
        script = self.idle.getTextEdit()
        output = data_get(self.sock, str(script), 'scriptingMode', session_id=self.session_id, to=self.client)
        self.outputText.setVisible(True)
        self.outputText.setHtml(output['payload'])

    def close_output(self):
        self.outputText.setVisible(False)

    def from_file(self):
        filename = QFileDialog.getOpenFileName(self, 'Open Python File', '', 'Python Files (*.py)')
        if filename:
            with open(filename, 'r') as f_:
                self.idle.setText(f_.read())
