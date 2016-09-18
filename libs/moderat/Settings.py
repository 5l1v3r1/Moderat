from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import os

from libs.language import Translate

#Multi Lang
translate = Translate()
_ = lambda _word: translate.word(_word)


class Settings:
    def __init__(self, moderat):
        self.moderat = moderat

    def set_settings(self):
        if self.moderat.settingsButton.isChecked():
            self.build_settings()
            self.moderat.settingsButton.setChecked(True)
            self.moderat.clientsTabs.setCurrentIndex(2)
        else:
            self.destroy_settings()
            self.moderat.settingsButton.setChecked(False)
            self.moderat.clientsTabs.setCurrentIndex(0)

    def close_settings(self):
        if self.moderat.settingsButton.isChecked():
            self.destroy_settings()
            self.moderat.settingsButton.setChecked(False)
            self.moderat.clientsTabs.setCurrentIndex(0)

    def destroy_settings(self):
        self.moderat.clientsTabs.removeTab(2)

    def save_settings(self):
        with open('settings.ini', 'w') as _settings:
            _settings.write(self.settingsEditor.toPlainText())
        reply = QMessageBox.question(self.moderat, _('RESTART_PROMPT'), _('RESTART_PROMPT'), QMessageBox.Yes,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            os.execv(sys.executable, ['python'] + sys.argv)

    def build_settings(self):
        icon = QIcon()
        icon.addPixmap(QPixmap(":/icons/assets/close.png"), QIcon.Normal, QIcon.Off)
        hide_button = QPushButton()
        hide_button.setStyleSheet('border: none; background: none;')
        hide_button.setIcon(icon)
        hide_button.setIconSize(QSize(12, 12))
        hide_button.clicked.connect(self.close_settings)
        settings_icon = QIcon()
        settings_icon.addPixmap(QPixmap(":/icons/assets/settings.png"), QIcon.Normal, QIcon.Off)
        self.settingsTab = QWidget()
        self.settingsTab.setObjectName("offlineClientsTab")
        self.gridLayout_3 = QGridLayout(self.settingsTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.settingsGroup = QGroupBox(self.settingsTab)
        self.settingsGroup.setStyleSheet("background-color: #34495e;\n"
                                         "border: none;\n"
                                         "margin-left: 1px;\n"
                                         "margin-right: 1px;")
        self.settingsGroup.setTitle("")
        self.settingsGroup.setObjectName("offlineGroup")
        self.gridLayout_8 = QGridLayout(self.settingsGroup)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.saveSettingsButton = QPushButton(self.settingsGroup)
        self.saveSettingsButton.setFocusPolicy(Qt.NoFocus)
        self.saveSettingsButton.setStyleSheet("QPushButton#saveSettingsButton {\n"
                                              "            border: none;\n"
                                              "            border-radius: none;\n"
                                              "            padding: 5px;\n"
                                              "            background-color: #34495e;\n"
                                              "            }\n"
                                              "\n"
                                              "QPushButton#saveSettingsButton:pressed {\n"
                                              "            background-color: #2c3e50;\n"
                                              "            }")
        self.saveSettingsButton.setText("")
        icon12 = QIcon()
        icon12.addPixmap(QPixmap(":/icons/assets/mark.png"), QIcon.Normal, QIcon.Off)
        self.saveSettingsButton.setIcon(icon12)
        self.saveSettingsButton.setIconSize(QSize(18, 18))
        self.saveSettingsButton.setObjectName("saveSettingsButton")
        self.saveSettingsButton.clicked.connect(self.save_settings)
        self.horizontalLayout_7.addWidget(self.saveSettingsButton)
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.gridLayout_8.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.settingsGroup)

        self.settingsEditor = QTextEdit(self.settingsTab)
        self.settingsEditor.setStyleSheet('''
        color: #c9f5f7;
        border: 1px ridge #263238;
        background-color: #2c3e50;
        background-repeat: no-repeat;
        background-position: center;
        padding: 5px;
        padding-top: 1px;''')
        self.verticalLayout_2.addWidget(self.settingsEditor)

        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        icon13 = QIcon()
        icon13.addPixmap(QPixmap(":/icons/assets/settings.png"), QIcon.Normal, QIcon.Off)
        self.moderat.clientsTabs.addTab(self.settingsTab, icon13, "")
        self.moderat.clientsTabs.insertTab(2, self.settingsTab, settings_icon, _('MODERAT_SETTINGS'))
        self.moderat.clientsTabs.tabBar().setTabButton(2, QTabBar.RightSide, hide_button)

        with open('settings.ini', 'r') as _settings:
            self.settingsEditor.setText(_settings.read())