from PyQt4.QtGui import *
from PyQt4.QtCore import *
from p2p_ui import Ui_Dialog


class P2p(QDialog, Ui_Dialog):
    def __init__(self, moderat, message):
        QWidget.__init__(self)
        self.moderat = moderat
        self.setupUi(self)
        self.anim = QPropertyAnimation(self, 'windowOpacity')
        self.anim.setDuration(500)
        self.anim.setStartValue(0)
        self.anim.setEndValue(1)
        self.anim.start()

        self.setWindowFlags(Qt.WindowSystemMenuHint | Qt.WindowTitleHint)

        self.connectP2pButton.clicked.connect(self.getCredentials)
        self.internalIpButton.clicked.connect(self.getInternalIpAddress)
        self.externalIpButton.clicked.connect(self.getExternalIpAddress)

        self.setWindowTitle(self.moderat.MString('P2P_TITLE'))
        self.ipaddressLine.setPlaceholderText(self.moderat.MString('P2P_IPADDRESS'))
        self.portLine.setPlaceholderText(self.moderat.MString('P2P_PORT'))
        self.connectP2pButton.setText(self.moderat.MString('P2P_CONNECT'))

        self.messageText.setText(message)

    def getCredentials(self):
        self.accept()
        return {
            'ip_address': str(self.ipaddressLine.text()),
            'port': str(self.portLine.text()),
            'message': str(self.messageText.toPlainText())
        }

    def getInternalIpAddress(self):
        import socket
        ip = socket.gethostbyname(socket.gethostname())
        self.ipaddressLine.setText(ip)

    def getExternalIpAddress(self):
        from requests import get
        ip = get('https://api.ipify.org').text
        self.ipaddressLine.setText(ip)

    def closeEvent(self, QCloseEvent):
        pass


def get(parent, alias):
    dialog = P2p(parent, alias)
    result = dialog.exec_()
    return result == QDialog.Accepted, dialog.getCredentials()
