from ui.settings_ui import Ui_Form
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class SettingsWindow(QWidget, Ui_Form):

    def __init__(self, moderat):
        QWidget.__init__(self)
        self.setupUi(self)

        self.moderat = moderat

        self.languageCombo.setCurrentIndex(
            self.languageCombo.findText(
                self.moderat.settings.moderatLanguage, Qt.MatchFixedString))
        self.themeCombo.setCurrentIndex(
            self.themeCombo.findText(
                self.moderat.settings.moderatTheme, Qt.MatchFixedString))
        self.opacitySlider.setValue(self.moderat.settings.moderatOpacity*100)
        self.onlinePerPageLine.setText(str(self.moderat.settings.onlineClientsPerPage))
        self.ipaddressHeaderCheck.setChecked(self.moderat.settings.headerIpAddress)
        self.clientIdHeaderCheck.setChecked(self.moderat.settings.headerClientId)
        self.userHeaderCheck.setChecked(self.moderat.settings.headerUser)
        self.aliasHeaderCheck.setChecked(self.moderat.settings.headerAlias)
        self.titleHeaderCheck.setChecked(self.moderat.settings.headerTitle)
        self.logViewerCheck.setChecked(self.moderat.settings.menuLogViewer)
        self.noteCheck.setChecked(self.moderat.settings.menuNote)
        self.aliasCheck.setChecked(self.moderat.settings.menuAlias)
        self.shellCheck.setChecked(self.moderat.settings.menuUpdate)
        self.explorerCheck.setChecked(self.moderat.settings.menuExplorer)
        self.scriptingCheck.setChecked(self.moderat.settings.menuScripting)
        self.screenshotCheck.setChecked(self.moderat.settings.menuScreenshot)
        self.webcamCheck.setChecked(self.moderat.settings.menuWebcam)

        self.offlinePerPageLine.setText(str(self.moderat.settings.offlineClientsPerPage))
        self.offlineIpaddressHeaderCheck.setChecked(self.moderat.settings.offlineHeaderIpAddress)
        self.offlineClientIdHeaderCheck.setChecked(self.moderat.settings.offlineHeaderClientId)
        self.offlineAliasHeaderCheck.setChecked(self.moderat.settings.offlineHeaderAlias)
        self.offlineLastOnlineHeaderCheck.setChecked(self.moderat.settings.offlineHeaderLastOnline)
        self.offlineLogViewerCheck.setChecked(self.moderat.settings.offlineMenuLogViewer)
        self.offlineAliasCheck.setChecked(self.moderat.settings.offlineMenuAlias)
        self.offlineNoteCheck.setChecked(self.moderat.settings.offlineMenuNote)
        self.offlineRemoveCheck.setChecked(self.moderat.settings.offlineMenuRemove)
        self.directIpaddressHeaderCheck.setChecked(self.moderat.settings.directHeaderIpAddress)
        self.directClientIdHeaderCheck.setChecked(self.moderat.settings.directHeaderClientId)
        self.directCommentHeaderCheck.setChecked(self.moderat.settings.directHeaderComment)
        self.directShellCheck.setChecked(self.moderat.settings.directMenuShell)
        self.directExplorerCheck.setChecked(self.moderat.settings.directMenuExplorer)
        self.directScriptingCheck.setChecked(self.moderat.settings.directMenuScripting)
        self.directScreenshotCheck.setChecked(self.moderat.settings.directMenuScreenshot)
        self.directWebcamCheck.setChecked(self.moderat.settings.directMenuWebcam)

        self.remoteServerIpAddressLine.setText(self.moderat.settings.serverIpAddress)
        self.remoteServerPortLine.setText(str(self.moderat.settings.serverPort))
        self.remoteServerUsernameLine.setText(self.moderat.settings.serverUsername)

        self.directServerPortLine.setText(str(self.moderat.settings.directServerPort))
        self.directIpAddressValueLine.setText(str(self.moderat.settings.directServerDefaultIpAddress))
        self.directPortValueLine.setText(str(self.moderat.settings.directServerDefaultPort))
        self.directCommentValueLine.setText(str(self.moderat.settings.directServerDefaultComment))

        self.applyButton.clicked.connect(self.apply_settings)
        self.closeButton.clicked.connect(self.close_settings)
        self.saveButton.clicked.connect(self.save_settings)

        self.set_config()

    def set_icons(self):
        self.appearanceIcon = QPushButton()
        self.appearanceIcon.setObjectName('appearanceButton')
        self.appearanceIcon.clicked.connect(lambda: self.settingsTab.setCurrentIndex(0))
        self.settingsTab.tabBar().setTabButton(0, QTabBar.LeftSide, self.appearanceIcon)
        self.rserverIcon = QPushButton()
        self.rserverIcon.setObjectName('rserverButton')
        self.rserverIcon.clicked.connect(lambda: self.settingsTab.setCurrentIndex(1))
        self.settingsTab.tabBar().setTabButton(1, QTabBar.LeftSide, self.rserverIcon)
        self.dserverIcon = QPushButton()
        self.dserverIcon.setObjectName('dserverButton')
        self.dserverIcon.clicked.connect(lambda: self.settingsTab.setCurrentIndex(2))
        self.settingsTab.tabBar().setTabButton(2, QTabBar.LeftSide, self.dserverIcon)

    def set_config(self):
        self.setStyleSheet(self.moderat.theme.stylesheet)
        self.set_icons()
        self.setWindowTitle(self.moderat.MString('SETTINGS_TITLE'))
        self.settingsTab.setTabText(0, self.moderat.MString('SETTINGS_TAB_APPEARANCE'))
        self.settingsTab.setTabText(1, self.moderat.MString('SETTINGS_TAB_RSERVER'))
        self.settingsTab.setTabText(2, self.moderat.MString('SETTINGS_TAB_DSERVER'))
        self.settingsAppearanceTab.setTabText(0, self.moderat.MString('SETTINGS_TAB_GENERAL'))
        self.settingsAppearanceTab.setTabText(1, self.moderat.MString('SETTINGS_TAB_ONLINE'))
        self.settingsAppearanceTab.setTabText(2, self.moderat.MString('SETTINGS_TAB_OFFLINE'))
        self.settingsAppearanceTab.setTabText(3, self.moderat.MString('SETTINGS_TAB_DIRECT'))
        self.interfaceGroup.setTitle(self.moderat.MString('SETTINGS_INTERFACE'))
        self.languageLabel.setText(self.moderat.MString('SETTINGS_LANGUAGE'))
        self.opacityLabel.setText(self.moderat.MString('SETTINGS_OPACITY'))
        self.themeLabel.setText(self.moderat.MString('SETTINGS_THEME'))
        self.appearanceGroup.setTitle(self.moderat.MString('SETTINGS_APPEARANCE'))
        self.onlinePerPageLabel.setText(self.moderat.MString('SETTINGS_ONLINE_PER_PAGE'))
        self.headersGroup.setTitle(self.moderat.MString('SETTINGS_HEADERS'))
        self.ipaddressHeaderCheck.setText(self.moderat.MString('HEADER_IP_ADDRESS'))
        self.clientIdHeaderCheck.setText(self.moderat.MString('HEADER_ID'))
        self.userHeaderCheck.setText(self.moderat.MString('HEADER_USER'))
        self.aliasHeaderCheck.setText(self.moderat.MString('HEADER_ALIAS'))
        self.titleHeaderCheck.setText(self.moderat.MString('HEADER_ACTIVE_WINDOW_TITLE'))
        self.menuGroup.setTitle(self.moderat.MString('SETTINGS_MENU'))
        self.logViewerCheck.setText(self.moderat.MString('MVIEWER_TITLE'))
        self.noteCheck.setText(self.moderat.MString('MNOTE_TITLE'))
        self.aliasCheck.setText(self.moderat.MString('SET_ALIAS'))
        self.updateCheck.setText(self.moderat.MString('RELOAD_CLIENT'))
        self.shellCheck.setText(self.moderat.MString('MSHELL_TITLE'))
        self.explorerCheck.setText(self.moderat.MString('MEXPLORER_TITLE'))
        self.scriptingCheck.setText(self.moderat.MString('MSCRIPTING_TITLE'))
        self.screenshotCheck.setText(self.moderat.MString('MDESKTOP_TITLE'))
        self.webcamCheck.setText(self.moderat.MString('MWEBCAM_TITLE'))

    def apply_settings(self):
        self.moderat.settings.moderatLanguage = str(self.languageCombo.currentText()).lower()
        self.moderat.settings.moderatTheme = str(self.themeCombo.currentText())
        self.moderat.settings.moderatOpacity = float(self.opacitySlider.value())/100
        self.moderat.settings.onlineClientsPerPage = int(self.onlinePerPageLine.text())
        self.moderat.settings.headerIpAddress = self.ipaddressHeaderCheck.isChecked()
        self.moderat.settings.headerClientId = self.clientIdHeaderCheck.isChecked()
        self.moderat.settings.headerUser = self.userHeaderCheck.isChecked()
        self.moderat.settings.headerAlias = self.aliasHeaderCheck.isChecked()
        self.moderat.settings.headerTitle = self.titleHeaderCheck.isChecked()
        self.moderat.settings.menuLogViewer = self.logViewerCheck.isChecked()
        self.moderat.settings.menuNote = self.noteCheck.isChecked()
        self.moderat.settings.menuAlias = self.aliasCheck.isChecked()
        self.moderat.settings.menuUpdate = self.updateCheck.isChecked()
        self.moderat.settings.menuShell = self.shellCheck.isChecked()
        self.moderat.settings.menuExplorer = self.explorerCheck.isChecked()
        self.moderat.settings.menuScripting = self.scriptingCheck.isChecked()
        self.moderat.settings.menuScreenshot = self.screenshotCheck.isChecked()
        self.moderat.settings.menuWebcam = self.webcamCheck.isChecked()
        self.moderat.settings.offlineClientsPerPage = int(self.offlinePerPageLine.text())
        self.moderat.settings.offlineHeaderIpAddress = self.offlineIpaddressHeaderCheck.isChecked()
        self.moderat.settings.offlineHeaderClientId = self.offlineClientIdHeaderCheck.isChecked()
        self.moderat.settings.offlineHeaderAlias = self.offlineAliasHeaderCheck.isChecked()
        self.moderat.settings.offlineHeaderLastOnline = self.offlineLastOnlineHeaderCheck.isChecked()
        self.moderat.settings.offlineMenuLogViewer = self.offlineLogViewerCheck.isChecked()
        self.moderat.settings.offlineMenuAlias = self.offlineAliasCheck.isChecked()
        self.moderat.settings.offlineMenuNote = self.offlineNoteCheck.isChecked()
        self.moderat.settings.offlineMenuRemove = self.offlineRemoveCheck.isChecked()
        self.moderat.settings.directHeaderIpAddress = self.directIpaddressHeaderCheck.isChecked()
        self.moderat.settings.directHeaderClientId = self.directClientIdHeaderCheck.isChecked()
        self.moderat.settings.directHeaderComment = self.directCommentHeaderCheck.isChecked()
        self.moderat.settings.directMenuShell = self.directShellCheck.isChecked()
        self.moderat.settings.directMenuExplorer = self.directExplorerCheck.isChecked()
        self.moderat.settings.directMenuScripting = self.directScriptingCheck.isChecked()
        self.moderat.settings.directMenuScreenshot = self.directScreenshotCheck.isChecked()
        self.moderat.settings.directMenuWebcam = self.directWebcamCheck.isChecked()

        self.moderat.settings.serverIpAddress = str(self.remoteServerIpAddressLine.text())
        self.moderat.settings.serverPort = int(self.remoteServerPortLine.text())
        self.moderat.settings.serverUsername = str(self.remoteServerUsernameLine.text())

        self.moderat.settings.directServerPort = int(self.directServerPortLine.text())
        self.moderat.settings.directServerDefaultIpAddress = self.directIpAddressValueLine.text()
        self.moderat.settings.directServerDefaultPort = int(self.directPortValueLine.text())
        self.moderat.settings.directServerDefaultComment = self.directCommentValueLine.text()

        self.moderat.set_config()
        self.set_config()
        self.moderat.settings.save_settings()

    def close_settings(self):
        self.close()

    def save_settings(self):
        self.apply_settings()
        self.close_settings()