# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(794, 361)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("background-color: #2c3e50;\n"
"color: #c9f5f7;"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(_fromUtf8("QWidget#centralwidget {\n"
"background-color: #2c3e50;\n"
"color: #2ecc71;\n"
"border-radius: 3px;\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"     border: 1px outset;\n"
"     border-color: #0F2D40;\n"
"     width: 10px;\n"
"     margin: 22px 0 22px 0;\n"
" }\n"
" QScrollBar::handle:vertical {\n"
"     background: #95a5a6;\n"
"     min-height: 20px;\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: 1px outset;\n"
"     border-color: #0F2D40;\n"
"     background: #95a5a6;\n"
"     height: 16px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:vertical {\n"
"     border: 1px outset;\n"
"     border-color: #0F2D40;\n"
"     background: #95a5a6;\n"
"     height: 16px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     width: 3px;\n"
"     height: 3px;\n"
"     background: white;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar:horizontal {\n"
"border: 1px outset;\n"
"     border-color: #0F2D40;\n"
"     height: 10px;\n"
"     margin: 0px 40px 0 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #95a5a6;\n"
"    min-width: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    border: 1px outset;\n"
"    border-color: #0F2D40;\n"
"    background: #95a5a6;\n"
"    width: 16px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: 1px outset;\n"
"    border-color: #0F2D40;\n"
"    background: #95a5a6;\n"
"    width: 16px;\n"
"    subcontrol-position: top right;\n"
"    subcontrol-origin: margin;\n"
"    position: absolute;\n"
"    right: 20px;\n"
"}\n"
"\n"
"QScrollBar:left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}"))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.bottomGroup = QtGui.QGroupBox(self.centralwidget)
        self.bottomGroup.setStyleSheet(_fromUtf8("background-color: #182733;\n"
"border: 1px solid #2c3e50;\n"
""))
        self.bottomGroup.setTitle(_fromUtf8(""))
        self.bottomGroup.setObjectName(_fromUtf8("bottomGroup"))
        self.gridLayout_5 = QtGui.QGridLayout(self.bottomGroup)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(50)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.connectButton = QtGui.QPushButton(self.bottomGroup)
        self.connectButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.connectButton.setStyleSheet(_fromUtf8("QPushButton#connectButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 5px;\n"
"            }\n"
"\n"
"QPushButton#connectButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }\n"
"\n"
"QPushButton#connectButton:checked {\n"
"            border: 1px ridge #cff7f8;\n"
"            }"))
        self.connectButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/connect.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.connectButton.setIcon(icon1)
        self.connectButton.setIconSize(QtCore.QSize(18, 18))
        self.connectButton.setCheckable(True)
        self.connectButton.setObjectName(_fromUtf8("connectButton"))
        self.horizontalLayout.addWidget(self.connectButton)
        self.disconnectButton = QtGui.QPushButton(self.bottomGroup)
        self.disconnectButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.disconnectButton.setStyleSheet(_fromUtf8("QPushButton#disconnectButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 5px;\n"
"            }\n"
"\n"
"QPushButton#disconnectButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.disconnectButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/disconnect.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.disconnectButton.setIcon(icon2)
        self.disconnectButton.setIconSize(QtCore.QSize(18, 18))
        self.disconnectButton.setCheckable(False)
        self.disconnectButton.setChecked(False)
        self.disconnectButton.setObjectName(_fromUtf8("disconnectButton"))
        self.horizontalLayout.addWidget(self.disconnectButton)
        self.settingsButton = QtGui.QPushButton(self.bottomGroup)
        self.settingsButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.settingsButton.setStyleSheet(_fromUtf8("QPushButton#settingsButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 5px;\n"
"            background-color: #182733;\n"
"            }\n"
"\n"
"QPushButton#settingsButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.settingsButton.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/client_settings.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsButton.setIcon(icon3)
        self.settingsButton.setObjectName(_fromUtf8("settingsButton"))
        self.horizontalLayout.addWidget(self.settingsButton)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.connectionStatusButton = QtGui.QPushButton(self.bottomGroup)
        self.connectionStatusButton.setStyleSheet(_fromUtf8("border: none;"))
        self.connectionStatusButton.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/no_connection.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.connectionStatusButton.setIcon(icon4)
        self.connectionStatusButton.setIconSize(QtCore.QSize(20, 20))
        self.connectionStatusButton.setObjectName(_fromUtf8("connectionStatusButton"))
        self.horizontalLayout_4.addWidget(self.connectionStatusButton)
        self.loginStatusLabel = QtGui.QLabel(self.bottomGroup)
        self.loginStatusLabel.setStyleSheet(_fromUtf8("border: none;\n"
"padding-left: 5px;"))
        self.loginStatusLabel.setObjectName(_fromUtf8("loginStatusLabel"))
        self.horizontalLayout_4.addWidget(self.loginStatusLabel)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.ipv4TextLabel = QtGui.QLabel(self.bottomGroup)
        self.ipv4TextLabel.setStyleSheet(_fromUtf8("border: none;"))
        self.ipv4TextLabel.setObjectName(_fromUtf8("ipv4TextLabel"))
        self.horizontalLayout_2.addWidget(self.ipv4TextLabel)
        self.ipv4Label = QtGui.QLabel(self.bottomGroup)
        self.ipv4Label.setStyleSheet(_fromUtf8("border: none;"))
        self.ipv4Label.setObjectName(_fromUtf8("ipv4Label"))
        self.horizontalLayout_2.addWidget(self.ipv4Label)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.serversOnlineStatus = QtGui.QLabel(self.bottomGroup)
        self.serversOnlineStatus.setMaximumSize(QtCore.QSize(16777215, 20))
        self.serversOnlineStatus.setStyleSheet(_fromUtf8("border: none;"))
        self.serversOnlineStatus.setObjectName(_fromUtf8("serversOnlineStatus"))
        self.horizontalLayout_5.addWidget(self.serversOnlineStatus)
        self.onlineStatus = QtGui.QLabel(self.bottomGroup)
        self.onlineStatus.setMaximumSize(QtCore.QSize(16777215, 20))
        self.onlineStatus.setStyleSheet(_fromUtf8("border: none;\n"
"font: 8pt \"MS Shell Dlg 2\";"))
        self.onlineStatus.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.onlineStatus.setObjectName(_fromUtf8("onlineStatus"))
        self.horizontalLayout_5.addWidget(self.onlineStatus)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)
        self.gridLayout_5.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.bottomGroup, 2, 0, 1, 1)
        self.clientsTabs = QtGui.QTabWidget(self.centralwidget)
        self.clientsTabs.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clientsTabs.setStyleSheet(_fromUtf8("QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 2px solid #34495e;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 5px; /* move to the right by 5px */\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {   \n"
"    border: 1px ridge;\n"
"    border-bottom: none;\n"
"    border-color: #2c3e50;\n"
"    min-width: 30ex;\n"
"    padding: 10px;\n"
"    color: #c9f5f7;\n"
"}\n"
"QTabBar::tab::disabled {   \n"
"    border: none;\n"
"    style: none;\n"
"    background: transparent;\n"
"    color: #2c3e50;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #34495e, stop: 0.4 #34495e,\n"
"                                stop: 0.5 #34495e, stop: 1.0 #34495e);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border: 1px ridge;\n"
"    border-bottom: none;\n"
"    border-color: #2c3e50;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}"))
        self.clientsTabs.setIconSize(QtCore.QSize(18, 18))
        self.clientsTabs.setDocumentMode(False)
        self.clientsTabs.setTabsClosable(False)
        self.clientsTabs.setMovable(False)
        self.clientsTabs.setObjectName(_fromUtf8("clientsTabs"))
        self.onlineClientsTab = QtGui.QWidget()
        self.onlineClientsTab.setObjectName(_fromUtf8("onlineClientsTab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.onlineClientsTab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.onlineGroup = QtGui.QGroupBox(self.onlineClientsTab)
        self.onlineGroup.setStyleSheet(_fromUtf8("background-color: #34495e;\n"
"border: 1px solid #2c3e50;\n"
"border-radius: 5px;\n"
"padding: -3px;"))
        self.onlineGroup.setTitle(_fromUtf8(""))
        self.onlineGroup.setObjectName(_fromUtf8("onlineGroup"))
        self.gridLayout_8 = QtGui.QGridLayout(self.onlineGroup)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem1, 0, 15, 1, 1)
        self.webcamButton = QtGui.QPushButton(self.onlineGroup)
        self.webcamButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.webcamButton.setStyleSheet(_fromUtf8("QPushButton#webcamButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 5px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#webcamButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.webcamButton.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/webcam.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.webcamButton.setIcon(icon5)
        self.webcamButton.setIconSize(QtCore.QSize(18, 18))
        self.webcamButton.setObjectName(_fromUtf8("webcamButton"))
        self.gridLayout_8.addWidget(self.webcamButton, 0, 14, 1, 1)
        self.setAliasButton = QtGui.QPushButton(self.onlineGroup)
        self.setAliasButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setAliasButton.setStyleSheet(_fromUtf8("QPushButton#setAliasButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 5px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#setAliasButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.setAliasButton.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/set_alias.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setAliasButton.setIcon(icon6)
        self.setAliasButton.setIconSize(QtCore.QSize(18, 18))
        self.setAliasButton.setObjectName(_fromUtf8("setAliasButton"))
        self.gridLayout_8.addWidget(self.setAliasButton, 0, 3, 1, 1)
        self.viewLogsButton = QtGui.QPushButton(self.onlineGroup)
        self.viewLogsButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.viewLogsButton.setStyleSheet(_fromUtf8("QPushButton#viewLogsButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 5px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#viewLogsButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.viewLogsButton.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/log_viewer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.viewLogsButton.setIcon(icon7)
        self.viewLogsButton.setIconSize(QtCore.QSize(18, 18))
        self.viewLogsButton.setObjectName(_fromUtf8("viewLogsButton"))
        self.gridLayout_8.addWidget(self.viewLogsButton, 0, 0, 1, 1)
        self.line = QtGui.QFrame(self.onlineGroup)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_8.addWidget(self.line, 0, 8, 1, 1)
        self.screenshotButton = QtGui.QPushButton(self.onlineGroup)
        self.screenshotButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.screenshotButton.setStyleSheet(_fromUtf8("QPushButton#screenshotButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 5px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#screenshotButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.screenshotButton.setText(_fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/desktop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.screenshotButton.setIcon(icon8)
        self.screenshotButton.setIconSize(QtCore.QSize(18, 18))
        self.screenshotButton.setObjectName(_fromUtf8("screenshotButton"))
        self.gridLayout_8.addWidget(self.screenshotButton, 0, 13, 1, 1)
        self.shellButton = QtGui.QPushButton(self.onlineGroup)
        self.shellButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.shellButton.setStyleSheet(_fromUtf8("QPushButton#shellButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 5px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#shellButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.shellButton.setText(_fromUtf8(""))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/remote_shell.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shellButton.setIcon(icon9)
        self.shellButton.setIconSize(QtCore.QSize(18, 18))
        self.shellButton.setObjectName(_fromUtf8("shellButton"))
        self.gridLayout_8.addWidget(self.shellButton, 0, 9, 1, 1)
        self.line_2 = QtGui.QFrame(self.onlineGroup)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_8.addWidget(self.line_2, 0, 2, 1, 1)
        self.explorerButton = QtGui.QPushButton(self.onlineGroup)
        self.explorerButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.explorerButton.setStyleSheet(_fromUtf8("QPushButton#explorerButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 5px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#explorerButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.explorerButton.setText(_fromUtf8(""))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/remote_explorer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.explorerButton.setIcon(icon10)
        self.explorerButton.setIconSize(QtCore.QSize(18, 18))
        self.explorerButton.setObjectName(_fromUtf8("explorerButton"))
        self.gridLayout_8.addWidget(self.explorerButton, 0, 10, 1, 1)
        self.proccessesButton = QtGui.QPushButton(self.onlineGroup)
        self.proccessesButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.proccessesButton.setStyleSheet(_fromUtf8("QPushButton#proccessesButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 5px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#proccessesButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.proccessesButton.setText(_fromUtf8(""))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/remote_proccesses.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.proccessesButton.setIcon(icon11)
        self.proccessesButton.setIconSize(QtCore.QSize(18, 18))
        self.proccessesButton.setObjectName(_fromUtf8("proccessesButton"))
        self.gridLayout_8.addWidget(self.proccessesButton, 0, 11, 1, 1)
        self.lockedButton = QtGui.QPushButton(self.onlineGroup)
        self.lockedButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lockedButton.setStyleSheet(_fromUtf8("QPushButton#lockedButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 5px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#lockedButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.lockedButton.setText(_fromUtf8(""))
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/locked.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lockedButton.setIcon(icon12)
        self.lockedButton.setIconSize(QtCore.QSize(18, 18))
        self.lockedButton.setObjectName(_fromUtf8("lockedButton"))
        self.gridLayout_8.addWidget(self.lockedButton, 0, 4, 1, 1)
        self.unlockedButton = QtGui.QPushButton(self.onlineGroup)
        self.unlockedButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.unlockedButton.setStyleSheet(_fromUtf8("QPushButton#unlockedButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 5px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#unlockedButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.unlockedButton.setText(_fromUtf8(""))
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/unlocked.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.unlockedButton.setIcon(icon13)
        self.unlockedButton.setIconSize(QtCore.QSize(18, 18))
        self.unlockedButton.setObjectName(_fromUtf8("unlockedButton"))
        self.gridLayout_8.addWidget(self.unlockedButton, 0, 5, 1, 1)
        self.scriptingButton = QtGui.QPushButton(self.onlineGroup)
        self.scriptingButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.scriptingButton.setStyleSheet(_fromUtf8("QPushButton#scriptingButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 5px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#scriptingButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.scriptingButton.setText(_fromUtf8(""))
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/remote_scripting.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.scriptingButton.setIcon(icon14)
        self.scriptingButton.setIconSize(QtCore.QSize(18, 18))
        self.scriptingButton.setObjectName(_fromUtf8("scriptingButton"))
        self.gridLayout_8.addWidget(self.scriptingButton, 0, 12, 1, 1)
        self.logSettingsButton = QtGui.QPushButton(self.onlineGroup)
        self.logSettingsButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.logSettingsButton.setStyleSheet(_fromUtf8("QPushButton#logSettingsButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 5px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#logSettingsButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.logSettingsButton.setText(_fromUtf8(""))
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/other_settings.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logSettingsButton.setIcon(icon15)
        self.logSettingsButton.setIconSize(QtCore.QSize(18, 18))
        self.logSettingsButton.setObjectName(_fromUtf8("logSettingsButton"))
        self.gridLayout_8.addWidget(self.logSettingsButton, 0, 1, 1, 1)
        self.setModeratorButton = QtGui.QPushButton(self.onlineGroup)
        self.setModeratorButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setModeratorButton.setStyleSheet(_fromUtf8("QPushButton#setModeratorButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 5px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#setModeratorButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.setModeratorButton.setText(_fromUtf8(""))
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/set_moderator.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setModeratorButton.setIcon(icon16)
        self.setModeratorButton.setIconSize(QtCore.QSize(18, 18))
        self.setModeratorButton.setObjectName(_fromUtf8("setModeratorButton"))
        self.gridLayout_8.addWidget(self.setModeratorButton, 0, 16, 1, 1)
        self.updateSourceButton = QtGui.QPushButton(self.onlineGroup)
        self.updateSourceButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.updateSourceButton.setStyleSheet(_fromUtf8("QPushButton#updateSourceButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 5px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#updateSourceButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.updateSourceButton.setText(_fromUtf8(""))
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/update_source.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.updateSourceButton.setIcon(icon17)
        self.updateSourceButton.setIconSize(QtCore.QSize(18, 18))
        self.updateSourceButton.setObjectName(_fromUtf8("updateSourceButton"))
        self.gridLayout_8.addWidget(self.updateSourceButton, 0, 6, 1, 1)
        self.gridLayout_2.addWidget(self.onlineGroup, 0, 0, 1, 1)
        self.clientsTable = QtGui.QTableWidget(self.onlineClientsTab)
        self.clientsTable.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clientsTable.setAutoFillBackground(False)
        self.clientsTable.setStyleSheet(_fromUtf8("QHeaderView::section {\n"
"    background-color: #34495e;\n"
"    padding: 2px;\n"
"    color: #cff7f8;\n"
"    font: 75 10px \"MS Shell Dlg 2\";\n"
"    border: 1px ridge;\n"
"    border-right: none;\n"
"    border-color: #2c3e50;\n"
"}\n"
"\n"
"QTableWidget#clientsTable {\n"
"    background-position: center;\n"
"    border: 1px ridge;\n"
"    padding: 5px;\n"
"    color: #cff7f8;\n"
"    border-color: #2c3e50;\n"
"    font: 8pt \"MS Shell Dlg 2\";\n"
"    background-color: #34495e;\n"
"\n"
"    background-image: url(assets/bg.png);\n"
"    background-repeat: no-repeat;\n"
"}\n"
"\n"
"QTableWidget#clientsTable:item:selected {\n"
"background-color: #2c3e50;\n"
"color: #cff7f8;\n"
"}"))
        self.clientsTable.setFrameShadow(QtGui.QFrame.Plain)
        self.clientsTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.clientsTable.setDragDropOverwriteMode(False)
        self.clientsTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.clientsTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.clientsTable.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.clientsTable.setShowGrid(False)
        self.clientsTable.setGridStyle(QtCore.Qt.NoPen)
        self.clientsTable.setWordWrap(False)
        self.clientsTable.setCornerButtonEnabled(False)
        self.clientsTable.setObjectName(_fromUtf8("clientsTable"))
        self.clientsTable.setColumnCount(11)
        self.clientsTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.clientsTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.clientsTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.clientsTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.clientsTable.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.clientsTable.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.clientsTable.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.clientsTable.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.clientsTable.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.clientsTable.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.clientsTable.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.clientsTable.setHorizontalHeaderItem(10, item)
        self.clientsTable.horizontalHeader().setCascadingSectionResizes(True)
        self.clientsTable.horizontalHeader().setDefaultSectionSize(100)
        self.clientsTable.horizontalHeader().setSortIndicatorShown(False)
        self.clientsTable.horizontalHeader().setStretchLastSection(True)
        self.clientsTable.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.clientsTable, 1, 0, 1, 1)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/online_clients.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clientsTabs.addTab(self.onlineClientsTab, icon18, _fromUtf8(""))
        self.offlineClientsTab = QtGui.QWidget()
        self.offlineClientsTab.setObjectName(_fromUtf8("offlineClientsTab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.offlineClientsTab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.onlineGroup_2 = QtGui.QGroupBox(self.offlineClientsTab)
        self.onlineGroup_2.setStyleSheet(_fromUtf8("background-color: #34495e;\n"
"border: 1px solid #2c3e50;\n"
"border-radius: 5px;\n"
"padding: -3px;"))
        self.onlineGroup_2.setTitle(_fromUtf8(""))
        self.onlineGroup_2.setObjectName(_fromUtf8("onlineGroup_2"))
        self.gridLayout_9 = QtGui.QGridLayout(self.onlineGroup_2)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem2, 0, 3, 1, 1)
        self.viewOfflineLogsButton = QtGui.QPushButton(self.onlineGroup_2)
        self.viewOfflineLogsButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.viewOfflineLogsButton.setStyleSheet(_fromUtf8("QPushButton#viewOfflineLogsButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 5px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#viewOfflineLogsButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.viewOfflineLogsButton.setText(_fromUtf8(""))
        self.viewOfflineLogsButton.setIcon(icon7)
        self.viewOfflineLogsButton.setIconSize(QtCore.QSize(18, 18))
        self.viewOfflineLogsButton.setObjectName(_fromUtf8("viewOfflineLogsButton"))
        self.gridLayout_9.addWidget(self.viewOfflineLogsButton, 0, 0, 1, 1)
        self.setOfflineAliasButton = QtGui.QPushButton(self.onlineGroup_2)
        self.setOfflineAliasButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setOfflineAliasButton.setStyleSheet(_fromUtf8("QPushButton#setOfflineAliasButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 5px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#setOfflineAliasButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.setOfflineAliasButton.setText(_fromUtf8(""))
        self.setOfflineAliasButton.setIcon(icon6)
        self.setOfflineAliasButton.setIconSize(QtCore.QSize(18, 18))
        self.setOfflineAliasButton.setObjectName(_fromUtf8("setOfflineAliasButton"))
        self.gridLayout_9.addWidget(self.setOfflineAliasButton, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.onlineGroup_2, 0, 0, 1, 1)
        self.offlineClientsTable = QtGui.QTableWidget(self.offlineClientsTab)
        self.offlineClientsTable.setFocusPolicy(QtCore.Qt.NoFocus)
        self.offlineClientsTable.setAutoFillBackground(False)
        self.offlineClientsTable.setStyleSheet(_fromUtf8("QHeaderView::section {\n"
"    background-color: #34495e;\n"
"    padding: 2px;\n"
"    color: #cff7f8;\n"
"    font: 75 10px \"MS Shell Dlg 2\";\n"
"    border: 1px ridge;\n"
"    border-right: none;\n"
"    border-color: #2c3e50;\n"
"}\n"
"\n"
"QTableWidget#offlineClientsTable {\n"
"    background-position: center;\n"
"    border: 1px ridge;\n"
"    padding: 5px;\n"
"    color: #cff7f8;\n"
"    border-color: #2c3e50;\n"
"    font: 8pt \"MS Shell Dlg 2\";\n"
"    background-color: #34495e;\n"
"\n"
"    background-image: url(assets/bg.png);\n"
"    background-repeat: no-repeat;\n"
"}\n"
"\n"
"QTableWidget#offlineClientsTable:item:selected {\n"
"background-color: #2c3e50;\n"
"color: #cff7f8;\n"
"}"))
        self.offlineClientsTable.setFrameShadow(QtGui.QFrame.Plain)
        self.offlineClientsTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.offlineClientsTable.setDragDropOverwriteMode(False)
        self.offlineClientsTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.offlineClientsTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.offlineClientsTable.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.offlineClientsTable.setShowGrid(False)
        self.offlineClientsTable.setGridStyle(QtCore.Qt.NoPen)
        self.offlineClientsTable.setWordWrap(False)
        self.offlineClientsTable.setCornerButtonEnabled(False)
        self.offlineClientsTable.setObjectName(_fromUtf8("offlineClientsTable"))
        self.offlineClientsTable.setColumnCount(5)
        self.offlineClientsTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.offlineClientsTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.offlineClientsTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.offlineClientsTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.offlineClientsTable.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.offlineClientsTable.setHorizontalHeaderItem(4, item)
        self.offlineClientsTable.horizontalHeader().setCascadingSectionResizes(True)
        self.offlineClientsTable.horizontalHeader().setDefaultSectionSize(100)
        self.offlineClientsTable.horizontalHeader().setSortIndicatorShown(False)
        self.offlineClientsTable.horizontalHeader().setStretchLastSection(True)
        self.offlineClientsTable.verticalHeader().setVisible(False)
        self.gridLayout_3.addWidget(self.offlineClientsTable, 1, 0, 1, 1)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/offline_clients.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clientsTabs.addTab(self.offlineClientsTab, icon19, _fromUtf8(""))
        self.moderatorsTab = QtGui.QWidget()
        self.moderatorsTab.setObjectName(_fromUtf8("moderatorsTab"))
        self.gridLayout_4 = QtGui.QGridLayout(self.moderatorsTab)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.moderatorsTable = QtGui.QTableWidget(self.moderatorsTab)
        self.moderatorsTable.setFocusPolicy(QtCore.Qt.NoFocus)
        self.moderatorsTable.setAutoFillBackground(False)
        self.moderatorsTable.setStyleSheet(_fromUtf8("QHeaderView::section {\n"
"    background-color: #34495e;\n"
"    padding: 2px;\n"
"    color: #cff7f8;\n"
"    font: 75 10px \"MS Shell Dlg 2\";\n"
"    border: 1px ridge;\n"
"    border-right: none;\n"
"    border-color: #2c3e50;\n"
"}\n"
"\n"
"QTableWidget#moderatorsTable {\n"
"    background-position: center;\n"
"    border: 1px ridge;\n"
"    padding: 5px;\n"
"    color: #cff7f8;\n"
"    border-color: #2c3e50;\n"
"    font: 8pt \"MS Shell Dlg 2\";\n"
"    background-color: #34495e;\n"
"\n"
"    background-image: url(assets/bg.png);\n"
"    background-repeat: no-repeat;\n"
"}\n"
"\n"
"QTableWidget#moderatorsTable:item:selected {\n"
"background-color: #2c3e50;\n"
"color: #cff7f8;\n"
"}"))
        self.moderatorsTable.setFrameShadow(QtGui.QFrame.Plain)
        self.moderatorsTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.moderatorsTable.setDragDropOverwriteMode(False)
        self.moderatorsTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.moderatorsTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.moderatorsTable.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.moderatorsTable.setShowGrid(False)
        self.moderatorsTable.setGridStyle(QtCore.Qt.NoPen)
        self.moderatorsTable.setWordWrap(False)
        self.moderatorsTable.setCornerButtonEnabled(False)
        self.moderatorsTable.setObjectName(_fromUtf8("moderatorsTable"))
        self.moderatorsTable.setColumnCount(6)
        self.moderatorsTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.moderatorsTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.moderatorsTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.moderatorsTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.moderatorsTable.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.moderatorsTable.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.moderatorsTable.setHorizontalHeaderItem(5, item)
        self.moderatorsTable.horizontalHeader().setCascadingSectionResizes(True)
        self.moderatorsTable.horizontalHeader().setDefaultSectionSize(100)
        self.moderatorsTable.horizontalHeader().setSortIndicatorShown(False)
        self.moderatorsTable.horizontalHeader().setStretchLastSection(True)
        self.moderatorsTable.verticalHeader().setVisible(False)
        self.gridLayout_4.addWidget(self.moderatorsTable, 2, 0, 1, 3)
        self.moderatorsGroup = QtGui.QGroupBox(self.moderatorsTab)
        self.moderatorsGroup.setStyleSheet(_fromUtf8("background-color: #34495e;\n"
"border: 1px solid #2c3e50;\n"
"border-radius: 5px;\n"
"padding: -3px;"))
        self.moderatorsGroup.setTitle(_fromUtf8(""))
        self.moderatorsGroup.setObjectName(_fromUtf8("moderatorsGroup"))
        self.gridLayout_7 = QtGui.QGridLayout(self.moderatorsGroup)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.addModeratorButton = QtGui.QPushButton(self.moderatorsGroup)
        self.addModeratorButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.addModeratorButton.setStyleSheet(_fromUtf8("QPushButton#addModeratorButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 5px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#addModeratorButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.addModeratorButton.setText(_fromUtf8(""))
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/add_moderator.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addModeratorButton.setIcon(icon20)
        self.addModeratorButton.setIconSize(QtCore.QSize(18, 18))
        self.addModeratorButton.setObjectName(_fromUtf8("addModeratorButton"))
        self.gridLayout_7.addWidget(self.addModeratorButton, 0, 1, 1, 1)
        self.getModeratorsButton = QtGui.QPushButton(self.moderatorsGroup)
        self.getModeratorsButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.getModeratorsButton.setStyleSheet(_fromUtf8("QPushButton#getModeratorsButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 5px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#getModeratorsButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.getModeratorsButton.setText(_fromUtf8(""))
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/get_moderators.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.getModeratorsButton.setIcon(icon21)
        self.getModeratorsButton.setIconSize(QtCore.QSize(18, 18))
        self.getModeratorsButton.setObjectName(_fromUtf8("getModeratorsButton"))
        self.gridLayout_7.addWidget(self.getModeratorsButton, 0, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem3, 0, 2, 1, 1)
        self.gridLayout_4.addWidget(self.moderatorsGroup, 0, 0, 1, 3)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/moderators.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clientsTabs.addTab(self.moderatorsTab, icon22, _fromUtf8(""))
        self.gridLayout.addWidget(self.clientsTabs, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 34))
        self.menubar.setStyleSheet(_fromUtf8("QMenuBar {\n"
"            background-color: #34495e;\n"
"            border: 1px ridge #000;\n"
"        }\n"
"\n"
"        QMenuBar::item {\n"
"            background-color: #34495e;\n"
"            color: #c9f5f7;\n"
"            padding: 8px;\n"
"            margin-left: 5px;\n"
"        }\n"
"\n"
"        QMenuBar::item::selected {\n"
"            background-color: #2c3e50;\n"
"        }\n"
"\n"
"        QMenuBar::item::checked{\n"
"            border-color: red;\n"
"        }\n"
"\n"
"        QMenu {\n"
"            background-color: #34495e;       \n"
"        }\n"
"        \n"
"        QMenu::item {\n"
"            border: none;\n"
"            padding: 5px;\n"
"            padding-left: 20px;\n"
"        }\n"
"\n"
"        QMenu::item::selected {\n"
"            background-color: #2c3e50;\n"
"            color: #ecf0f1;\n"
"        }"))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.actionStartListen_for_connections = QtGui.QAction(MainWindow)
        self.actionStartListen_for_connections.setCheckable(True)
        self.actionStartListen_for_connections.setIcon(icon1)
        self.actionStartListen_for_connections.setObjectName(_fromUtf8("actionStartListen_for_connections"))
        self.actionStopListen_for_connections = QtGui.QAction(MainWindow)
        self.actionStopListen_for_connections.setCheckable(True)
        self.actionStopListen_for_connections.setIcon(icon2)
        self.actionStopListen_for_connections.setObjectName(_fromUtf8("actionStopListen_for_connections"))
        self.actionViewer_Configuration = QtGui.QAction(MainWindow)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/settings.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionViewer_Configuration.setIcon(icon23)
        self.actionViewer_Configuration.setObjectName(_fromUtf8("actionViewer_Configuration"))
        self.actionRemote_Shell = QtGui.QAction(MainWindow)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/mshell.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemote_Shell.setIcon(icon24)
        self.actionRemote_Shell.setObjectName(_fromUtf8("actionRemote_Shell"))
        self.actionRemote_Explorer = QtGui.QAction(MainWindow)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/mexplorer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemote_Explorer.setIcon(icon25)
        self.actionRemote_Explorer.setObjectName(_fromUtf8("actionRemote_Explorer"))
        self.actionRemote_Process_Manager = QtGui.QAction(MainWindow)
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/mprocesses.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemote_Process_Manager.setIcon(icon26)
        self.actionRemote_Process_Manager.setObjectName(_fromUtf8("actionRemote_Process_Manager"))
        self.actionRemote_Microphone = QtGui.QAction(MainWindow)
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/maudio.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemote_Microphone.setIcon(icon27)
        self.actionRemote_Microphone.setObjectName(_fromUtf8("actionRemote_Microphone"))
        self.actionRemote_Scripting = QtGui.QAction(MainWindow)
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/script.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemote_Scripting.setIcon(icon28)
        self.actionRemote_Scripting.setObjectName(_fromUtf8("actionRemote_Scripting"))
        self.actionRemote_Keylogger = QtGui.QAction(MainWindow)
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/mkeylogger.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemote_Keylogger.setIcon(icon29)
        self.actionRemote_Keylogger.setObjectName(_fromUtf8("actionRemote_Keylogger"))
        self.actionDesktop_Preview = QtGui.QAction(MainWindow)
        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/mdesktop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDesktop_Preview.setIcon(icon30)
        self.actionDesktop_Preview.setObjectName(_fromUtf8("actionDesktop_Preview"))
        self.actionWebcam_Preview = QtGui.QAction(MainWindow)
        self.actionWebcam_Preview.setIcon(icon5)
        self.actionWebcam_Preview.setObjectName(_fromUtf8("actionWebcam_Preview"))
        self.actionStop_Client = QtGui.QAction(MainWindow)
        icon31 = QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/terminate.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStop_Client.setIcon(icon31)
        self.actionStop_Client.setObjectName(_fromUtf8("actionStop_Client"))
        self.actionLock_Client = QtGui.QAction(MainWindow)
        icon32 = QtGui.QIcon()
        icon32.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/lock.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLock_Client.setIcon(icon32)
        self.actionLock_Client.setObjectName(_fromUtf8("actionLock_Client"))
        self.actionLog_off = QtGui.QAction(MainWindow)
        self.actionLog_off.setObjectName(_fromUtf8("actionLog_off"))
        self.actionReboot = QtGui.QAction(MainWindow)
        self.actionReboot.setObjectName(_fromUtf8("actionReboot"))
        self.actionShutdown = QtGui.QAction(MainWindow)
        self.actionShutdown.setObjectName(_fromUtf8("actionShutdown"))
        self.actionUnlock_Client = QtGui.QAction(MainWindow)
        icon33 = QtGui.QIcon()
        icon33.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/unlock.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUnlock_Client.setIcon(icon33)
        self.actionUnlock_Client.setObjectName(_fromUtf8("actionUnlock_Client"))
        self.actionSet_Alias = QtGui.QAction(MainWindow)
        icon34 = QtGui.QIcon()
        icon34.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/add_alias.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSet_Alias.setIcon(icon34)
        self.actionSet_Alias.setObjectName(_fromUtf8("actionSet_Alias"))
        self.actionRun_As_Admin = QtGui.QAction(MainWindow)
        icon35 = QtGui.QIcon()
        icon35.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/run_as_admin.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRun_As_Admin.setIcon(icon35)
        self.actionRun_As_Admin.setObjectName(_fromUtf8("actionRun_As_Admin"))
        self.actionTerminate_Client = QtGui.QAction(MainWindow)
        icon36 = QtGui.QIcon()
        icon36.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTerminate_Client.setIcon(icon36)
        self.actionTerminate_Client.setObjectName(_fromUtf8("actionTerminate_Client"))
        self.actionWindows_Client_PyInstaller = QtGui.QAction(MainWindow)
        self.actionWindows_Client_PyInstaller.setObjectName(_fromUtf8("actionWindows_Client_PyInstaller"))

        self.retranslateUi(MainWindow)
        self.clientsTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Moderat Viewer", None))
        self.loginStatusLabel.setText(_translate("MainWindow", "Not Authorized", None))
        self.ipv4TextLabel.setText(_translate("MainWindow", "IPv4:", None))
        self.ipv4Label.setText(_translate("MainWindow", "N/A", None))
        self.serversOnlineStatus.setText(_translate("MainWindow", "CLIENTS TOTAL:", None))
        self.onlineStatus.setText(_translate("MainWindow", "0", None))
        self.clientsTable.setSortingEnabled(False)
        item = self.clientsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Moderator", None))
        item = self.clientsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ip Address", None))
        item = self.clientsTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Alias", None))
        item = self.clientsTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "ID", None))
        item = self.clientsTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "OS", None))
        item = self.clientsTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "User", None))
        item = self.clientsTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Privs", None))
        item = self.clientsTable.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Lock", None))
        item = self.clientsTable.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Mic", None))
        item = self.clientsTable.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Cam", None))
        item = self.clientsTable.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Active Window Title", None))
        self.clientsTabs.setTabText(self.clientsTabs.indexOf(self.onlineClientsTab), _translate("MainWindow", "Online", None))
        self.offlineClientsTable.setSortingEnabled(False)
        item = self.offlineClientsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Moderator", None))
        item = self.offlineClientsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ID", None))
        item = self.offlineClientsTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Alias", None))
        item = self.offlineClientsTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Ip Address", None))
        item = self.offlineClientsTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Last Online", None))
        self.clientsTabs.setTabText(self.clientsTabs.indexOf(self.offlineClientsTab), _translate("MainWindow", "Offline", None))
        self.moderatorsTable.setSortingEnabled(False)
        item = self.moderatorsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID", None))
        item = self.moderatorsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Online Clients", None))
        item = self.moderatorsTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Offline Clients", None))
        item = self.moderatorsTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Privileges", None))
        item = self.moderatorsTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Status", None))
        item = self.moderatorsTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Last Online", None))
        self.clientsTabs.setTabText(self.clientsTabs.indexOf(self.moderatorsTab), _translate("MainWindow", "Moderators", None))
        self.actionStartListen_for_connections.setText(_translate("MainWindow", "Connect", None))
        self.actionStopListen_for_connections.setText(_translate("MainWindow", "Disconnect", None))
        self.actionViewer_Configuration.setText(_translate("MainWindow", "Settings", None))
        self.actionRemote_Shell.setText(_translate("MainWindow", "Remote Shell", None))
        self.actionRemote_Explorer.setText(_translate("MainWindow", "Remote File Manager", None))
        self.actionRemote_Process_Manager.setText(_translate("MainWindow", "Remote Process Manager", None))
        self.actionRemote_Microphone.setText(_translate("MainWindow", "Remote Microphone", None))
        self.actionRemote_Scripting.setText(_translate("MainWindow", "Remote Scripting", None))
        self.actionRemote_Keylogger.setText(_translate("MainWindow", "Remote Keylogger", None))
        self.actionDesktop_Preview.setText(_translate("MainWindow", "Desktop Preview", None))
        self.actionWebcam_Preview.setText(_translate("MainWindow", "Webcam Preview", None))
        self.actionStop_Client.setText(_translate("MainWindow", "Stop", None))
        self.actionLock_Client.setText(_translate("MainWindow", "Lock", None))
        self.actionLog_off.setText(_translate("MainWindow", "Log off", None))
        self.actionReboot.setText(_translate("MainWindow", "Reboot", None))
        self.actionShutdown.setText(_translate("MainWindow", "Shutdown", None))
        self.actionUnlock_Client.setText(_translate("MainWindow", "Unlock", None))
        self.actionSet_Alias.setText(_translate("MainWindow", "Set Alias", None))
        self.actionRun_As_Admin.setText(_translate("MainWindow", "Run As Admin", None))
        self.actionTerminate_Client.setText(_translate("MainWindow", "Terminate", None))
        self.actionWindows_Client_PyInstaller.setText(_translate("MainWindow", "Windows Client (PyInstaller 3.0)", None))

import res_rc
