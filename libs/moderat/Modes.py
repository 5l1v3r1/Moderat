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
        self.tables = tables.updateClientsTable(self.moderat, self.moderat.assets)

        # Init Modes
        self.modes = {
            'moderatorInitializing': self.moderatorInitializing,
            'getClients': self.getClients,
        }

    def check_mode(self, data):
        if type(data) is dict:
            if self.modes.has_key(data['mode']):
                self.modes[data['mode']](data)
            # TODO: DEBUG
            else:
                print 'UNKNOWN MODE [%s]' % data['mode']
        else:
            print type(data)

    # get online client
    def current_client(self):
        try:
            return str(self.moderat.clientsTable.item(self.moderat.clientsTable.currentRow(), 4).text())
        except AttributeError:
            return False

    # get offline client
    def current_offline_client(self):
        try:
            return str(self.moderat.offlineClientsTable.item(self.moderat.offlineClientsTable.currentRow(), 2).text())
        except AttributeError:
            return False

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
            self.clients_checker.timeout.connect(self.moderat.check_clients)
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