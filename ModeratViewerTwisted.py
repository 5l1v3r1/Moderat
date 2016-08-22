# -*- coding: utf-8 -*-

import sys
import os

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from ModeratorFactory import *

from libs.language import Translate
from libs.moderat.Actions import Actions
from libs.moderat.Modes import Modes
from libs.gui import triggers
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
        # Privileges
        self.privs = 0
        # Checkers
        self.moderators_checker = None
        self.clients_checker = None
        # Modules Bank
        self.modulesBank = {}

        # Create Protocol
        self.create_moderator()
        # Init Triggers
        triggers.mainTriggers(self)
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
        '''
        Try Connect To Server
        :return:
        '''
        self.connection = self.reactor.connectTCP(SERVER_HOST, SERVER_PORT, self.moderator)

    def on_moderator_connect_success(self):
        '''
        On Moderator Connected To Server
        :return:
        '''
        self.action.login()

    def on_moderator_connect_fail(self, reason):
        '''
        On Moderator Disconnected From Server
        :param reason:
        :return:
        '''
        self.action.disconnect()

    # Callbacks
    def on_moderator_receive(self, data):
        '''
        Data Received From Server
        :param data:
        :return:
        '''
        self.modes.check_mode(data)

    def set_alias(self):
        '''
        Set Alias For Client
        :return:
        '''
        self.action.set_alias()

    def execute_module(self, module):
        '''
        execute module
        :param module:
        :return:
        '''
        self.action.execute_module(module)

    def check_clients(self):
        '''
        Update Clients Information
        :return:
        '''
        self.moderator.send_msg(message='getClients', mode='getClients', session_id=self.session_id)

    def check_moderators(self):
        '''
        Update Moderators Information
        :return:
        '''
        self.moderator.send_msg(message='getModerators', mode='getModerators', session_id=self.session_id)

    def send_signal(self, data):
        if self.modulesBank.has_key(data['module_id']):
            self.modulesBank[data['module_id']].signal(data)

    def closeEvent(self, *args, **kwargs):
        '''
        Moderat Close Event Detected
        :param args:
        :param kwargs:
        :return:
        '''
        self.action.close_moderat()


# -------------------------------------------------------------------------------
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
