from PyQt4.QtGui import *
from PyQt4.QtCore import *

from libs.modechat import get, send

class mainPopup(QWidget):

    def __init__(self, args):
        QWidget.__init__(self)
        #self.setupUi(self)

        self.sock = args['sock']
        self.socket = args['socket']
        self.ipAddress = args['ipAddress']

        self.setWindowTitle('Desktop Streaming from - %s - Socket #%s' % (self.ipAddress, self.socket))

    def closeEvent(self, event):
        pass