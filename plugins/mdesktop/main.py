from PyQt4.QtGui import *
from PyQt4.QtCore import *

import main_ui

from libs.modechat import get

import ast
import zlib
from PIL import Image, ImageQt


class mainPopup(QWidget, main_ui.Ui_Form):

    def __init__(self, args):
        QWidget.__init__(self)
        self.setupUi(self)

        self.sock = args['sock']
        self.socket = args['socket']
        self.ipAddress = args['ipAddress']

        self.setWindowTitle('%s - Desktop Preview - Socket #%s' % (self.ipAddress, self.socket))

        self.saveButton.setDisabled(True)

        self.screenshotButton.clicked.connect(self.get_screenshot)
        self.saveButton.clicked.connect(self.save_preview)
        self.clearButton.clicked.connect(self.clear_preview)
        self.alwaysTopButton.clicked.connect(self.always_top)

    def get_screenshot(self):
        screen_dict = get(self.sock, 'getScreen', 'screenshot')
        try:
            screen_info = ast.literal_eval(screen_dict)
            im = Image.frombuffer('RGB', (int(screen_info['width']), int(screen_info['height'])),
                                  zlib.decompress(screen_info['screenshotbits']), 'raw', 'BGRX', 0, 1)
            screen_bits = im.convert('RGBA')
            self.screenshotLabel.setPixmap(QPixmap.fromImage(ImageQt.ImageQt(screen_bits)).scaled(
                    self.screenshotLabel.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.current_bits = screen_bits
            self.saveButton.setDisabled(False)
            self.clearButton.setDisabled(False)
        except SyntaxError:
            pass

    def save_preview(self):
        if self.current_bits:
            file_name = QFileDialog.getSaveFileName(self, 'Save file', '', 'Image (*.png)')
            windows_path = str(file_name).replace('/', '\\')
            if file_name:
                self.current_bits.save(windows_path, 'png')
        else:
            self.saveButton.setDisabled(True)
            self.clearButton.setDisabled(True)

    def clear_preview(self):
        self.current_bits = None
        self.screenshotLabel.clear()
        self.saveButton.setDisabled(True)
        self.clearButton.setDisabled(True)

    def resizeEvent(self, event):
        self.screenshotLabel.setPixmap(QPixmap.fromImage(ImageQt.ImageQt(self.current_bits)).scaled(
            self.screenshotLabel.width(), self.screenshotLabel.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def always_top(self):
        if self.alwaysTopButton.isChecked():
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
            self.show()
        else:
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowStaysOnTopHint)
            self.show()

