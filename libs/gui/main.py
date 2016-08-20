from PyQt4.QtGui import *
from PyQt4.QtCore import *
import os
from libs.language import Translate

from libs.gui import triggers

# Multi Lang
translate = Translate()
_ = lambda _word: translate.word(_word)


class updateUi:

    def __init__(self, moderat):
        self.moderat = moderat

        # Init Triggers
        triggers.mainTriggers(self.moderat)

    def on_moderator_connected(self):
        """
        If Moderator Connected To Server
        :return:
        """
        self.moderat.loginStatusLabel.setText(self.moderat.session_id)
        self.moderat.loginStatusLabel.setStyleSheet('color: #2ecc71')
        self.moderat.connectionStatusButton.setIcon(QIcon(QPixmap(":/icons/assets/connection.png")))
        self.moderat.connectButton.setChecked(True)

    # TODO: style
    def on_moderator_not_connected(self):
        '''
        If Moderator Disconnected From Server
        :return:
        '''
        self.moderat.loginStatusLabel.setText('Not Connected')
        self.moderat.loginStatusLabel.setStyleSheet('color: red')
        self.moderat.connectionStatusButton.setIcon(QIcon(QPixmap(":/icons/assets/no_connection.png")))
        self.moderat.connectButton.setChecked(False)

    # Enable Administrators Features
    def enable_administrator(self):
        # Online Clients Moderators
        self.moderat.clientsTable.showColumn(0)
        # Offline Clients Moderators
        self.moderat.offlineClientsTable.showColumn(0)
        # Moderators Tab
        self.moderat.clientsTabs.setTabEnabled(2, True)
        self.moderat.clientsTabs.setTabIcon(2, QIcon(QPixmap(":/icons/assets/moderators.png")))

    # Disable Administrators Features
    def disable_administrator(self):
        # Online Clients Moderators
        self.moderat.clientsTable.setColumnHidden(0, True)
        # Offline Clients Moderators
        self.moderat.offlineClientsTable.setColumnHidden(0, True)
        # Moderators Tab
        self.moderat.clientsTabs.setTabEnabled(2, False)
        self.moderat.clientsTabs.setTabIcon(2, QIcon(QPixmap(":/icons/assets/none.png")))