from PyQt4.QtGui import *
from PyQt4.QtCore import *
import os

from libs.language import Translate

# Multi Lang
translate = Translate()
_ = lambda _word: translate.word(_word)

class initFilters:

    def __init__(self, window, assets, parent=None):

        self.assets = assets
        self.moderat = window

        self.filter_style = '''
        background-color: #2c3e50;
        padding: 2px;
        color: #cff7f8;
        border: 1px solid;
        border-top: none;
        border-bottom: none;
        border-color: #34495e;
        '''

        # init filters
        self.filters = {
            'moderator': '',
            'ip_address': '',
            'alias': '',
            'key': '',
            'os': '',
            'user': '',
            'privs': '',
            'audio': '',
            'camera': '',
            'title': '',
        }

        self.offline_filters = {
            'moderator': '',
            'key': '',
            'alias': '',
            'ip_address': '',
        }

        self.init_filters()

        # UI FILTERS
    def init_filters(self):

        self.moderat.clientsTable.setRowCount(1)

        self.moderat.offlineClientsTable.setRowCount(1)

        # Moderators
        self.filter_moderator_line = QLineEdit()
        self.filter_moderator_line.setStyleSheet(self.filter_style)
        self.filter_moderator_line.setPlaceholderText(_('FILTER_FILTER'))
        self.filter_moderator_line.textChanged.connect(self.filter_clients)
        self.moderat.clientsTable.setCellWidget(0, 0, self.filter_moderator_line)

        # Ip Address
        self.filter_ipaddress_line = QLineEdit()
        self.filter_ipaddress_line.setStyleSheet(self.filter_style)
        self.filter_ipaddress_line.setPlaceholderText(_('FILTER_FILTER'))
        self.filter_ipaddress_line.textChanged.connect(self.filter_clients)
        self.moderat.clientsTable.setCellWidget(0, 1, self.filter_ipaddress_line)

        # Alias
        self.filter_alias_line = QLineEdit()
        self.filter_alias_line.setStyleSheet(self.filter_style)
        self.filter_alias_line.setPlaceholderText(_('FILTER_FILTER'))
        self.filter_alias_line.textChanged.connect(self.filter_clients)
        self.moderat.clientsTable.setCellWidget(0, 2, self.filter_alias_line)

        # Socket
        self.filter_socket_line = QLineEdit()
        self.filter_socket_line.setStyleSheet(self.filter_style)
        self.filter_socket_line.setPlaceholderText(_('FILTER_FILTER'))
        self.filter_socket_line.textChanged.connect(self.filter_clients)
        self.moderat.clientsTable.setCellWidget(0, 3, self.filter_socket_line)

        # Os
        self.filter_os_line = QLineEdit()
        self.filter_os_line.setStyleSheet(self.filter_style)
        self.filter_os_line.setPlaceholderText(_('FILTER_FILTER'))
        self.filter_os_line.textChanged.connect(self.filter_clients)
        self.moderat.clientsTable.setCellWidget(0, 4, self.filter_os_line)

        # User
        self.filter_user_line = QLineEdit()
        self.filter_user_line.setStyleSheet(self.filter_style)
        self.filter_user_line.setPlaceholderText(_('FILTER_FILTER'))
        self.filter_user_line.textChanged.connect(self.filter_clients)
        self.moderat.clientsTable.setCellWidget(0, 5, self.filter_user_line)

        # privs
        self.filter_privs_combo = QComboBox()
        self.filter_privs_combo.setEditable(True)
        self.filter_privs_combo.addItem(QIcon(os.path.join(self.assets, 'false.png')), _('FILTER_ALL'), '')
        self.filter_privs_combo.addItem(QIcon(os.path.join(self.assets, 'admin.png')), _('INFO_ADMIN'), '1')
        self.filter_privs_combo.addItem(QIcon(os.path.join(self.assets, 'user.png')), _('INFO_USER'), '0')
        self.filter_privs_combo.setStyleSheet(self.filter_style)
        self.filter_privs_combo.currentIndexChanged.connect(self.filter_clients)
        self.moderat.clientsTable.setCellWidget(0, 6, self.filter_privs_combo)

        # Audio
        self.filter_audio_combo = QComboBox()
        self.filter_audio_combo.setEditable(True)
        self.filter_audio_combo.addItem(QIcon(os.path.join(self.assets, 'false.png')), _('FILTER_ALL'), '')
        self.filter_audio_combo.addItem(QIcon(os.path.join(self.assets, 'mic_yes.png')), _('INFO_YES'), ' ')
        self.filter_audio_combo.addItem(QIcon(os.path.join(self.assets, 'mic_no.png')), _('INFO_NO'), 'NoDevice')
        self.filter_audio_combo.setStyleSheet(self.filter_style)
        self.filter_audio_combo.currentIndexChanged.connect(self.filter_clients)
        self.moderat.clientsTable.setCellWidget(0, 7, self.filter_audio_combo)

        # Camera
        self.filter_camera_combo = QComboBox()
        self.filter_camera_combo.setEditable(True)
        self.filter_camera_combo.addItem(QIcon(os.path.join(self.assets, 'false.png')), _('FILTER_ALL'), '')
        self.filter_camera_combo.addItem(QIcon(os.path.join(self.assets, 'web_camera.png')), _('INFO_YES'), ' ')
        self.filter_camera_combo.addItem(QIcon(os.path.join(self.assets, 'web_camera_no.png')), _('INFO_NO'), 'NoDevice')
        self.filter_camera_combo.setStyleSheet(self.filter_style)
        self.filter_camera_combo.currentIndexChanged.connect(self.filter_clients)
        self.moderat.clientsTable.setCellWidget(0, 8, self.filter_camera_combo)

        # Active Window Title
        self.filter_title_line = QLineEdit()
        self.filter_title_line.setStyleSheet(self.filter_style)
        self.filter_title_line.setPlaceholderText(_('FILTER_FILTER'))
        self.filter_title_line.textChanged.connect(self.filter_clients)
        self.moderat.clientsTable.setCellWidget(0, 9, self.filter_title_line)

        # OFFLINE Clinets

        # Offline Moderators
        self.filter_moderator_line_offline = QLineEdit()
        self.filter_moderator_line_offline.setStyleSheet(self.filter_style)
        self.filter_moderator_line_offline.setPlaceholderText(_('FILTER_FILTER'))
        self.filter_moderator_line_offline.textChanged.connect(self.filter_offline_clients)
        self.moderat.offlineClientsTable.setCellWidget(0, 0, self.filter_moderator_line_offline)

        # Offline ID
        self.filter_id_line_offline = QLineEdit()
        self.filter_id_line_offline.setStyleSheet(self.filter_style)
        self.filter_id_line_offline.setPlaceholderText(_('FILTER_FILTER'))
        self.filter_id_line_offline.textChanged.connect(self.filter_offline_clients)
        self.moderat.offlineClientsTable.setCellWidget(0, 1, self.filter_id_line_offline)

        # Offline ID
        self.filter_alias_line_offline = QLineEdit()
        self.filter_alias_line_offline.setStyleSheet(self.filter_style)
        self.filter_alias_line_offline.setPlaceholderText(_('FILTER_FILTER'))
        self.filter_alias_line_offline.textChanged.connect(self.filter_offline_clients)
        self.moderat.offlineClientsTable.setCellWidget(0, 2, self.filter_alias_line_offline)

        # Offline Ip Address
        self.filter_ipaddress_line_offline = QLineEdit()
        self.filter_ipaddress_line_offline.setStyleSheet(self.filter_style)
        self.filter_ipaddress_line_offline.setPlaceholderText(_('FILTER_FILTER'))
        self.filter_ipaddress_line_offline.textChanged.connect(self.filter_offline_clients)
        self.moderat.offlineClientsTable.setCellWidget(0, 3, self.filter_ipaddress_line_offline)

    def filter_clients(self):
        self.filters = {
            'moderator': str(self.filter_moderator_line.text()),
            'ip_address': str(self.filter_ipaddress_line.text()),
            'alias': str(self.filter_alias_line.text()),
            'key': str(self.filter_socket_line.text()),
            'os': str(self.filter_os_line.text()),
            'user': str(self.filter_user_line.text()),
            'privs': str(self.filter_privs_combo.itemData(self.filter_privs_combo.currentIndex()).toPyObject()),
            'audio': str(self.filter_audio_combo.itemData(self.filter_audio_combo.currentIndex()).toPyObject()),
            'camera': str(self.filter_camera_combo.itemData(self.filter_camera_combo.currentIndex()).toPyObject()),
            'title': str(self.filter_title_line.text()),
        }

    def filter_offline_clients(self):
        self.offline_filters = {
            'moderator': str(self.filter_moderator_line_offline.text()),
            'key': str(self.filter_id_line_offline.text()),
            'alias': str(self.filter_alias_line_offline.text()),
            'ip_address': str(self.filter_ipaddress_line_offline.text()),
        }