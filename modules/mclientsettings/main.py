from PyQt4.QtGui import *
from PyQt4.QtCore import *
from libs.gui.loading import Loading
import main_ui
import ast
import zlib
from PIL import Image, ImageQt


class mainPopup(QMainWindow, main_ui.Ui_Form):

    def __init__(self, args):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.moderat = args['moderat']
        self.client = args['client']
        self.module_id = args['module_id']
        self.alias = args['alias']
        self.ip_address = args['ip_address']
        self.p2p = args['p2p']

        title_prefix = self.alias if len(self.alias) > 0 else self.ip_address
        self.setWindowTitle(u'{}[{}] {}'.format('(P2P)' if self.p2p else '', title_prefix, self.moderat.MString('MCLIENTSETTINGS_TITLE')))

        self.loading = Loading(self)
        self.loading.hide()

    def signal(self, data):
        self.callback(data)

    def get_settings(self):
        self.moderat.send_message('getSettings', 'getSettings', session_id=self.moderat.session_id, _to=self.client,
                                  module_id=self.module_id, p2p=self.p2p)
        self.callback = self.settings_received
        self.loading.show()

    def settings_received(self, data):
        if type(data['payload']) is dict:
            # TODO: Settings Received
            self.loading.hide()

    def set_settings(self):
        # TODO: Set Settings
        pass

    def resizeEvent(self, event):
        self.loading.resize(event.size())
        event.accept()
