from PyQt4.QtGui import *
from PyQt4.QtCore import *
import os
from libs.language import Translate
from libs.gui import tables

# Multi Lang
translate = Translate()
_ = lambda _word: translate.word(_word)


class updateUi:

    def __init__(self, moderat):
        self.moderat = moderat

        self.tables = tables.updateClientsTable(self.moderat)

    def on_moderator_connected(self):
        """
        If Moderator Connected To Server
        :return:
        """
        self.moderat.connectButton.setChecked(True)
        self.moderat.connectButton.setDisabled(True)

    # TODO: style
    def on_moderator_not_connected(self):
        '''
        If Moderator Disconnected From Server
        :return:
        '''
        self.moderat.connectButton.setDisabled(False)
        self.moderat.connectButton.setChecked(False)

    def clear_tables(self):
        '''
        Clear Tables
        :return:
        '''
        self.tables.clean_tables()


    # Enable Administrators Features
    def enable_administrator(self):
        # Enable Buttons
        self.moderat.setModeratorButton.setHidden(False)
        # Online Clients Moderators
        self.moderat.clientsTable.showColumn(0)
        # Offline Clients Moderators
        self.moderat.offlineClientsTable.showColumn(0)
        # Moderators Tab
        self.moderat.clientsTabs.setTabEnabled(2, True)
        self.moderat.clientsTabs.setTabText(2, _('CLIENTS_TAB_MODERATORS'))
        self.moderat.clientsTabs.setTabIcon(2, QIcon(QPixmap(":/icons/assets/moderators.png")))

    # Disable Administrators Features
    def disable_administrator(self):
        # Disable Buttons
        self.moderat.setModeratorButton.setHidden(True)
        # Online Clients Moderators
        self.moderat.clientsTable.setColumnHidden(0, True)
        # Offline Clients Moderators
        self.moderat.offlineClientsTable.setColumnHidden(0, True)
        # Moderators Tab
        self.moderat.clientsTabs.setTabEnabled(2, False)
        self.moderat.clientsTabs.setTabText(2, '')
        self.moderat.clientsTabs.setTabIcon(2, QIcon(QPixmap(":/icons/assets/none.png")))