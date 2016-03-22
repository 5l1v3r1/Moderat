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
        MainWindow.resize(984, 607)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("background-color: #2c3e50;\n"
"color: #bdc3c7;"))
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
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.clientButtonsGroup = QtGui.QGroupBox(self.centralwidget)
        self.clientButtonsGroup.setStyleSheet(_fromUtf8("border: 1px ridge;\n"
"border-color: #34495e;\n"
"background-color: #2c3e50;\n"
"border: none;"))
        self.clientButtonsGroup.setTitle(_fromUtf8(""))
        self.clientButtonsGroup.setCheckable(False)
        self.clientButtonsGroup.setObjectName(_fromUtf8("clientButtonsGroup"))
        self.gridLayout = QtGui.QGridLayout(self.clientButtonsGroup)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.startListenButton = QtGui.QPushButton(self.clientButtonsGroup)
        self.startListenButton.setMinimumSize(QtCore.QSize(32, 32))
        self.startListenButton.setMaximumSize(QtCore.QSize(32, 32))
        self.startListenButton.setStyleSheet(_fromUtf8("QPushButton#startListenButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#startListenButton:checked {\n"
"            border-color: #27ae60;\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.startListenButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/connect.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startListenButton.setIcon(icon1)
        self.startListenButton.setIconSize(QtCore.QSize(18, 18))
        self.startListenButton.setCheckable(True)
        self.startListenButton.setObjectName(_fromUtf8("startListenButton"))
        self.horizontalLayout.addWidget(self.startListenButton)
        self.stopListenButton = QtGui.QPushButton(self.clientButtonsGroup)
        self.stopListenButton.setMinimumSize(QtCore.QSize(32, 32))
        self.stopListenButton.setMaximumSize(QtCore.QSize(32, 32))
        self.stopListenButton.setStyleSheet(_fromUtf8("QPushButton#stopListenButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#stopListenButton:checked {\n"
"            border-color: #27ae60;\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.stopListenButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/disconnect.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopListenButton.setIcon(icon2)
        self.stopListenButton.setIconSize(QtCore.QSize(18, 18))
        self.stopListenButton.setCheckable(True)
        self.stopListenButton.setChecked(True)
        self.stopListenButton.setObjectName(_fromUtf8("stopListenButton"))
        self.horizontalLayout.addWidget(self.stopListenButton)
        self.line = QtGui.QFrame(self.clientButtonsGroup)
        self.line.setMinimumSize(QtCore.QSize(20, 0))
        self.line.setStyleSheet(_fromUtf8("border: none;"))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        self.unlockServerButton = QtGui.QPushButton(self.clientButtonsGroup)
        self.unlockServerButton.setMinimumSize(QtCore.QSize(32, 32))
        self.unlockServerButton.setMaximumSize(QtCore.QSize(32, 32))
        self.unlockServerButton.setStyleSheet(_fromUtf8("QPushButton#unlockServerButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            border-right: none\n"
"            }\n"
"\n"
"QPushButton#unlockServerButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.unlockServerButton.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/unlock.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.unlockServerButton.setIcon(icon3)
        self.unlockServerButton.setObjectName(_fromUtf8("unlockServerButton"))
        self.horizontalLayout.addWidget(self.unlockServerButton)
        self.lockServerButton = QtGui.QPushButton(self.clientButtonsGroup)
        self.lockServerButton.setMinimumSize(QtCore.QSize(32, 32))
        self.lockServerButton.setMaximumSize(QtCore.QSize(32, 32))
        self.lockServerButton.setStyleSheet(_fromUtf8("QPushButton#lockServerButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            border-right: none\n"
"            }\n"
"\n"
"QPushButton#lockServerButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.lockServerButton.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/lock.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lockServerButton.setIcon(icon4)
        self.lockServerButton.setIconSize(QtCore.QSize(18, 18))
        self.lockServerButton.setObjectName(_fromUtf8("lockServerButton"))
        self.horizontalLayout.addWidget(self.lockServerButton)
        self.quitServerButton = QtGui.QPushButton(self.clientButtonsGroup)
        self.quitServerButton.setMinimumSize(QtCore.QSize(32, 32))
        self.quitServerButton.setMaximumSize(QtCore.QSize(32, 32))
        self.quitServerButton.setStyleSheet(_fromUtf8("QPushButton#quitServerButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            border-left: none;\n"
"            }\n"
"\n"
"QPushButton#quitServerButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.quitServerButton.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/terminate.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.quitServerButton.setIcon(icon5)
        self.quitServerButton.setIconSize(QtCore.QSize(18, 18))
        self.quitServerButton.setObjectName(_fromUtf8("quitServerButton"))
        self.horizontalLayout.addWidget(self.quitServerButton)
        self.line_2 = QtGui.QFrame(self.clientButtonsGroup)
        self.line_2.setMinimumSize(QtCore.QSize(20, 0))
        self.line_2.setStyleSheet(_fromUtf8("border: none;"))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout.addWidget(self.line_2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.clientSettingsButton = QtGui.QPushButton(self.clientButtonsGroup)
        self.clientSettingsButton.setMinimumSize(QtCore.QSize(32, 32))
        self.clientSettingsButton.setMaximumSize(QtCore.QSize(32, 32))
        self.clientSettingsButton.setStyleSheet(_fromUtf8("QPushButton#clientSettingsButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#clientSettingsButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.clientSettingsButton.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/settings.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clientSettingsButton.setIcon(icon6)
        self.clientSettingsButton.setIconSize(QtCore.QSize(20, 20))
        self.clientSettingsButton.setObjectName(_fromUtf8("clientSettingsButton"))
        self.horizontalLayout.addWidget(self.clientSettingsButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.clientButtonsGroup, 2, 0, 1, 1)
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout_3.addWidget(self.line_4, 3, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.creditLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.creditLabel.setFont(font)
        self.creditLabel.setStyleSheet(_fromUtf8("font: 8pt \"MS Shell Dlg 2\";"))
        self.creditLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.creditLabel.setObjectName(_fromUtf8("creditLabel"))
        self.horizontalLayout_4.addWidget(self.creditLabel)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.clientStatusLabel = QtGui.QLabel(self.centralwidget)
        self.clientStatusLabel.setStyleSheet(_fromUtf8("border: none;"))
        self.clientStatusLabel.setObjectName(_fromUtf8("clientStatusLabel"))
        self.horizontalLayout_4.addWidget(self.clientStatusLabel)
        self.statusLabel = QtGui.QLabel(self.centralwidget)
        self.statusLabel.setStyleSheet(_fromUtf8("border: none;\n"
"color: #e74c3c;\n"
"font: 8pt \"MS Shell Dlg 2\";"))
        self.statusLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statusLabel.setObjectName(_fromUtf8("statusLabel"))
        self.horizontalLayout_4.addWidget(self.statusLabel)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.portTextLabel = QtGui.QLabel(self.centralwidget)
        self.portTextLabel.setStyleSheet(_fromUtf8("border: none;"))
        self.portTextLabel.setObjectName(_fromUtf8("portTextLabel"))
        self.horizontalLayout_2.addWidget(self.portTextLabel)
        self.portLabel = QtGui.QLabel(self.centralwidget)
        self.portLabel.setStyleSheet(_fromUtf8("border: none;\n"
"font: 8pt \"MS Shell Dlg 2\";"))
        self.portLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.portLabel.setObjectName(_fromUtf8("portLabel"))
        self.horizontalLayout_2.addWidget(self.portLabel)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.serversOnlineStatus = QtGui.QLabel(self.centralwidget)
        self.serversOnlineStatus.setStyleSheet(_fromUtf8("border: none;"))
        self.serversOnlineStatus.setObjectName(_fromUtf8("serversOnlineStatus"))
        self.horizontalLayout_5.addWidget(self.serversOnlineStatus)
        self.onlineStatus = QtGui.QLabel(self.centralwidget)
        self.onlineStatus.setStyleSheet(_fromUtf8("border: none;\n"
"font: 8pt \"MS Shell Dlg 2\";"))
        self.onlineStatus.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.onlineStatus.setObjectName(_fromUtf8("onlineStatus"))
        self.horizontalLayout_5.addWidget(self.onlineStatus)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 5, 0, 1, 1)
        self.MainTabWidget = QtGui.QTabWidget(self.centralwidget)
        self.MainTabWidget.setStyleSheet(_fromUtf8(" QTabBar::tab {\n"
"  padding: 10px;\n"
"  padding-left: 15px;\n"
"  margin-left: 9px;\n"
"  width: 110%;\n"
"  border: 1px ridge;\n"
"  border-color: #2c3e50;\n"
" }\n"
"\n"
" QTabBar::tab:selected {\n"
"   background: #34495e;\n"
" }\n"
"\n"
" QTabBar::pane {\n"
"   background-color: #2c3e50;\n"
" }\n"
"\n"
"QTabWidget::pane {\n"
"    color: rgb(246, 246, 244);\n"
"    margin: 0px,1px,1px,1px;\n"
"    border: 1px ridge;\n"
"    border-color: #0F2D40;\n"
"    background-color: #194759;\n"
"    background-position: center;\n"
"    border: none;\n"
"      }"))
        self.MainTabWidget.setObjectName(_fromUtf8("MainTabWidget"))
        self.windowsTab = QtGui.QWidget()
        self.windowsTab.setObjectName(_fromUtf8("windowsTab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.windowsTab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 26, 0, -1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.remoteShellButton = QtGui.QPushButton(self.windowsTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remoteShellButton.sizePolicy().hasHeightForWidth())
        self.remoteShellButton.setSizePolicy(sizePolicy)
        self.remoteShellButton.setMinimumSize(QtCore.QSize(36, 36))
        self.remoteShellButton.setMaximumSize(QtCore.QSize(36, 36))
        self.remoteShellButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.remoteShellButton.setAcceptDrops(False)
        self.remoteShellButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.remoteShellButton.setAutoFillBackground(False)
        self.remoteShellButton.setStyleSheet(_fromUtf8("QPushButton#remoteShellButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            border-bottom: none;\n"
"            border-right: none;\n"
"            }\n"
"\n"
"QPushButton#remoteShellButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.remoteShellButton.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/mshell.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remoteShellButton.setIcon(icon7)
        self.remoteShellButton.setIconSize(QtCore.QSize(25, 25))
        self.remoteShellButton.setAutoRepeat(False)
        self.remoteShellButton.setAutoExclusive(False)
        self.remoteShellButton.setAutoDefault(False)
        self.remoteShellButton.setDefault(False)
        self.remoteShellButton.setFlat(False)
        self.remoteShellButton.setObjectName(_fromUtf8("remoteShellButton"))
        self.verticalLayout.addWidget(self.remoteShellButton)
        self.remoteExplorerButton = QtGui.QPushButton(self.windowsTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remoteExplorerButton.sizePolicy().hasHeightForWidth())
        self.remoteExplorerButton.setSizePolicy(sizePolicy)
        self.remoteExplorerButton.setMinimumSize(QtCore.QSize(36, 36))
        self.remoteExplorerButton.setMaximumSize(QtCore.QSize(36, 36))
        self.remoteExplorerButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.remoteExplorerButton.setStyleSheet(_fromUtf8("QPushButton#remoteExplorerButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            border-top: none;\n"
"            border-bottom: none;\n"
"            border-right: none;\n"
"            }\n"
"\n"
"QPushButton#remoteExplorerButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.remoteExplorerButton.setText(_fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/mexplorer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remoteExplorerButton.setIcon(icon8)
        self.remoteExplorerButton.setIconSize(QtCore.QSize(25, 25))
        self.remoteExplorerButton.setObjectName(_fromUtf8("remoteExplorerButton"))
        self.verticalLayout.addWidget(self.remoteExplorerButton)
        self.remoteProcessesButton = QtGui.QPushButton(self.windowsTab)
        self.remoteProcessesButton.setMinimumSize(QtCore.QSize(36, 36))
        self.remoteProcessesButton.setMaximumSize(QtCore.QSize(36, 36))
        self.remoteProcessesButton.setStyleSheet(_fromUtf8("QPushButton#remoteProcessesButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            border-top: none;\n"
"            border-bottom: none;\n"
"            border-right: none;\n"
"            }\n"
"\n"
"QPushButton#remoteProcessesButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.remoteProcessesButton.setText(_fromUtf8(""))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/mprocesses.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remoteProcessesButton.setIcon(icon9)
        self.remoteProcessesButton.setIconSize(QtCore.QSize(25, 25))
        self.remoteProcessesButton.setObjectName(_fromUtf8("remoteProcessesButton"))
        self.verticalLayout.addWidget(self.remoteProcessesButton)
        self.remoteAudioButton = QtGui.QPushButton(self.windowsTab)
        self.remoteAudioButton.setMinimumSize(QtCore.QSize(36, 36))
        self.remoteAudioButton.setMaximumSize(QtCore.QSize(36, 36))
        self.remoteAudioButton.setStyleSheet(_fromUtf8("QPushButton#remoteAudioButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            border-top: none;\n"
"            border-bottom: none;\n"
"            border-right: none;\n"
"            }\n"
"\n"
"QPushButton#remoteAudioButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.remoteAudioButton.setText(_fromUtf8(""))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/maudio.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remoteAudioButton.setIcon(icon10)
        self.remoteAudioButton.setIconSize(QtCore.QSize(25, 25))
        self.remoteAudioButton.setObjectName(_fromUtf8("remoteAudioButton"))
        self.verticalLayout.addWidget(self.remoteAudioButton)
        self.remoteScriptingButton = QtGui.QPushButton(self.windowsTab)
        self.remoteScriptingButton.setMinimumSize(QtCore.QSize(36, 36))
        self.remoteScriptingButton.setMaximumSize(QtCore.QSize(36, 36))
        self.remoteScriptingButton.setStyleSheet(_fromUtf8("QPushButton#remoteScriptingButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            border-top: none;\n"
"            border-bottom: none;\n"
"            border-right: none;\n"
"            }\n"
"\n"
"QPushButton#remoteScriptingButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.remoteScriptingButton.setText(_fromUtf8(""))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/script.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remoteScriptingButton.setIcon(icon11)
        self.remoteScriptingButton.setIconSize(QtCore.QSize(25, 25))
        self.remoteScriptingButton.setObjectName(_fromUtf8("remoteScriptingButton"))
        self.verticalLayout.addWidget(self.remoteScriptingButton)
        self.remoteKeyloggerButton = QtGui.QPushButton(self.windowsTab)
        self.remoteKeyloggerButton.setMinimumSize(QtCore.QSize(36, 36))
        self.remoteKeyloggerButton.setMaximumSize(QtCore.QSize(36, 36))
        self.remoteKeyloggerButton.setStyleSheet(_fromUtf8("QPushButton#remoteKeyloggerButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            border-top: none;\n"
"            border-right: none;\n"
"            }\n"
"\n"
"QPushButton#remoteKeyloggerButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.remoteKeyloggerButton.setText(_fromUtf8(""))
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/mkeylogger.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remoteKeyloggerButton.setIcon(icon12)
        self.remoteKeyloggerButton.setIconSize(QtCore.QSize(25, 25))
        self.remoteKeyloggerButton.setObjectName(_fromUtf8("remoteKeyloggerButton"))
        self.verticalLayout.addWidget(self.remoteKeyloggerButton)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.serversTable = QtGui.QTableWidget(self.windowsTab)
        self.serversTable.setFocusPolicy(QtCore.Qt.NoFocus)
        self.serversTable.setAutoFillBackground(False)
        self.serversTable.setStyleSheet(_fromUtf8("QHeaderView::section {\n"
"    background-color: #34495e;\n"
"    padding: 2px;\n"
"    color: #bdc3c7;\n"
"    font: 75 8pt \"MS Shell Dlg 2\";\n"
"    border: 1px ridge;\n"
"    border-right: none;\n"
"    border-color: #2c3e50;\n"
"}\n"
"\n"
"QTableWidget#serversTable {\n"
"    background-position: center;\n"
"    border: 1px ridge;\n"
"    padding: 5px;\n"
"    color: #ecf0f1;\n"
"    border-color: #2c3e50;\n"
"    font: 8pt \"MS Shell Dlg 2\";\n"
"    background-color: #34495e;\n"
"}\n"
"\n"
"QTableWidget#serversTable:item:selected {\n"
"background-color: #2c3e50;\n"
"color: #ecf0f1;\n"
"}"))
        self.serversTable.setFrameShadow(QtGui.QFrame.Plain)
        self.serversTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.serversTable.setDragDropOverwriteMode(False)
        self.serversTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.serversTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.serversTable.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.serversTable.setShowGrid(False)
        self.serversTable.setGridStyle(QtCore.Qt.NoPen)
        self.serversTable.setWordWrap(False)
        self.serversTable.setCornerButtonEnabled(False)
        self.serversTable.setObjectName(_fromUtf8("serversTable"))
        self.serversTable.setColumnCount(8)
        self.serversTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.serversTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.serversTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.serversTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.serversTable.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.serversTable.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.serversTable.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.serversTable.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.serversTable.setHorizontalHeaderItem(7, item)
        self.serversTable.horizontalHeader().setCascadingSectionResizes(True)
        self.serversTable.horizontalHeader().setDefaultSectionSize(100)
        self.serversTable.horizontalHeader().setSortIndicatorShown(False)
        self.serversTable.horizontalHeader().setStretchLastSection(True)
        self.serversTable.verticalHeader().setVisible(False)
        self.horizontalLayout_3.addWidget(self.serversTable)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(1, 0, -1, -1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem4 = QtGui.QSpacerItem(160, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.screenSaveButton = QtGui.QPushButton(self.windowsTab)
        self.screenSaveButton.setMinimumSize(QtCore.QSize(30, 30))
        self.screenSaveButton.setMaximumSize(QtCore.QSize(30, 30))
        self.screenSaveButton.setStyleSheet(_fromUtf8("QPushButton#screenSaveButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            border-right: none;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            margin-bottom: 3px;\n"
"            }\n"
"\n"
"QPushButton#screenSaveButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.screenSaveButton.setText(_fromUtf8(""))
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.screenSaveButton.setIcon(icon13)
        self.screenSaveButton.setIconSize(QtCore.QSize(16, 16))
        self.screenSaveButton.setObjectName(_fromUtf8("screenSaveButton"))
        self.horizontalLayout_7.addWidget(self.screenSaveButton)
        self.getWebcamButton = QtGui.QPushButton(self.windowsTab)
        self.getWebcamButton.setMinimumSize(QtCore.QSize(30, 30))
        self.getWebcamButton.setMaximumSize(QtCore.QSize(30, 30))
        self.getWebcamButton.setStyleSheet(_fromUtf8("QPushButton#getWebcamButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            margin-bottom: 3px;\n"
"            }\n"
"\n"
"QPushButton#getWebcamButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.getWebcamButton.setText(_fromUtf8(""))
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/webcam.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.getWebcamButton.setIcon(icon14)
        self.getWebcamButton.setIconSize(QtCore.QSize(16, 16))
        self.getWebcamButton.setObjectName(_fromUtf8("getWebcamButton"))
        self.horizontalLayout_7.addWidget(self.getWebcamButton)
        self.updatePreviewButton = QtGui.QPushButton(self.windowsTab)
        self.updatePreviewButton.setMinimumSize(QtCore.QSize(30, 30))
        self.updatePreviewButton.setMaximumSize(QtCore.QSize(30, 50))
        self.updatePreviewButton.setStyleSheet(_fromUtf8("QPushButton#updatePreviewButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            border-left: none;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            margin-bottom: 3px;\n"
"            }\n"
"\n"
"QPushButton#updatePreviewButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.updatePreviewButton.setText(_fromUtf8(""))
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/mdesktop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.updatePreviewButton.setIcon(icon15)
        self.updatePreviewButton.setIconSize(QtCore.QSize(16, 16))
        self.updatePreviewButton.setObjectName(_fromUtf8("updatePreviewButton"))
        self.horizontalLayout_7.addWidget(self.updatePreviewButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.previewLabel = QtGui.QLabel(self.windowsTab)
        self.previewLabel.setMinimumSize(QtCore.QSize(250, 150))
        self.previewLabel.setMaximumSize(QtCore.QSize(250, 150))
        self.previewLabel.setStyleSheet(_fromUtf8("color: grey;\n"
"border: 1px ridge;\n"
"border-color: #2c3e50;\n"
"border-left: none;\n"
"border-bottom: none;\n"
"background-color: #34495e;\n"
"font: 7pt \"MS Shell Dlg 2\";"))
        self.previewLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.previewLabel.setObjectName(_fromUtf8("previewLabel"))
        self.verticalLayout_2.addWidget(self.previewLabel)
        self.deviceNameLabel = QtGui.QLabel(self.windowsTab)
        self.deviceNameLabel.setMinimumSize(QtCore.QSize(250, 0))
        self.deviceNameLabel.setMaximumSize(QtCore.QSize(250, 16777215))
        self.deviceNameLabel.setStyleSheet(_fromUtf8("font: 7pt \"MS Shell Dlg 2\";\n"
"background-color: #34495e;\n"
"border: 1px ridge;\n"
"border-color: #2c3e50;\n"
"border-top: none;\n"
"border-left: none;"))
        self.deviceNameLabel.setText(_fromUtf8(""))
        self.deviceNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.deviceNameLabel.setObjectName(_fromUtf8("deviceNameLabel"))
        self.verticalLayout_2.addWidget(self.deviceNameLabel)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/windows.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MainTabWidget.addTab(self.windowsTab, icon16, _fromUtf8(""))
        self.androidsTab = QtGui.QWidget()
        self.androidsTab.setObjectName(_fromUtf8("androidsTab"))
        self.gridLayout_4 = QtGui.QGridLayout(self.androidsTab)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.androidsTable = QtGui.QTableWidget(self.androidsTab)
        self.androidsTable.setFocusPolicy(QtCore.Qt.NoFocus)
        self.androidsTable.setAutoFillBackground(False)
        self.androidsTable.setStyleSheet(_fromUtf8("QHeaderView::section {\n"
"    background-color: #34495e;\n"
"    padding: 2px;\n"
"    color: #bdc3c7;\n"
"    font: 75 8pt \"MS Shell Dlg 2\";\n"
"    border: 1px ridge;\n"
"    border-right: none;\n"
"    border-color: #2c3e50;\n"
"}\n"
"\n"
"QTableWidget#androidsTable {\n"
"    background-position: center;\n"
"    border: 1px ridge;\n"
"    padding: 5px;\n"
"    color: #ecf0f1;\n"
"    border-color: #2c3e50;\n"
"    font: 8pt \"MS Shell Dlg 2\";\n"
"    background-color: #34495e;\n"
"}\n"
"\n"
"QTableWidget#androidsTable:item:selected {\n"
"background-color: #2c3e50;\n"
"color: #ecf0f1;\n"
"}"))
        self.androidsTable.setFrameShadow(QtGui.QFrame.Plain)
        self.androidsTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.androidsTable.setDragDropOverwriteMode(False)
        self.androidsTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.androidsTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.androidsTable.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.androidsTable.setShowGrid(False)
        self.androidsTable.setGridStyle(QtCore.Qt.NoPen)
        self.androidsTable.setWordWrap(False)
        self.androidsTable.setCornerButtonEnabled(False)
        self.androidsTable.setObjectName(_fromUtf8("androidsTable"))
        self.androidsTable.setColumnCount(0)
        self.androidsTable.setRowCount(0)
        self.androidsTable.horizontalHeader().setCascadingSectionResizes(True)
        self.androidsTable.horizontalHeader().setDefaultSectionSize(100)
        self.androidsTable.horizontalHeader().setSortIndicatorShown(False)
        self.androidsTable.horizontalHeader().setStretchLastSection(True)
        self.androidsTable.verticalHeader().setVisible(False)
        self.gridLayout_4.addWidget(self.androidsTable, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.androidsTab)
        self.label.setStyleSheet(_fromUtf8("font: 36pt \"MS Shell Dlg 2\";"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/android.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MainTabWidget.addTab(self.androidsTab, icon17, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.MainTabWidget, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 984, 23))
        self.menubar.setStyleSheet(_fromUtf8("QMenuBar {\n"
"            background-color: #34495e;\n"
"            border: 1px ridge #000;\n"
"        }\n"
"\n"
"        QMenuBar::item {\n"
"            background-color: #34495e;\n"
"            color: #ecf0f1;\n"
"        }\n"
"\n"
"        QMenuBar::item::selected {\n"
"            background-color: #2c3e50;\n"
"        }\n"
"\n"
"        QMenu {\n"
"            background-color: #34495e;\n"
"            border: 1px ridge #000;           \n"
"        }\n"
"\n"
"        QMenu::item::selected {\n"
"            background-color: #2c3e50;\n"
"            color: #ecf0f1;\n"
"        }"))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuClient = QtGui.QMenu(self.menubar)
        self.menuClient.setTearOffEnabled(True)
        self.menuClient.setSeparatorsCollapsible(False)
        self.menuClient.setObjectName(_fromUtf8("menuClient"))
        MainWindow.setMenuBar(self.menubar)
        self.actionStartListen_for_connections = QtGui.QAction(MainWindow)
        self.actionStartListen_for_connections.setIcon(icon1)
        self.actionStartListen_for_connections.setObjectName(_fromUtf8("actionStartListen_for_connections"))
        self.actionStopListen_for_connections = QtGui.QAction(MainWindow)
        self.actionStopListen_for_connections.setIcon(icon2)
        self.actionStopListen_for_connections.setObjectName(_fromUtf8("actionStopListen_for_connections"))
        self.actionClient_Configuration = QtGui.QAction(MainWindow)
        self.actionClient_Configuration.setIcon(icon6)
        self.actionClient_Configuration.setObjectName(_fromUtf8("actionClient_Configuration"))
        self.menuClient.addAction(self.actionStartListen_for_connections)
        self.menuClient.addAction(self.actionStopListen_for_connections)
        self.menuClient.addSeparator()
        self.menuClient.addAction(self.actionClient_Configuration)
        self.menubar.addAction(self.menuClient.menuAction())

        self.retranslateUi(MainWindow)
        self.MainTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Moderat Client", None))
        self.creditLabel.setText(_translate("MainWindow", "© Uri Patton", None))
        self.clientStatusLabel.setText(_translate("MainWindow", "Status: ", None))
        self.statusLabel.setText(_translate("MainWindow", "Offline", None))
        self.portTextLabel.setText(_translate("MainWindow", "Port:", None))
        self.portLabel.setText(_translate("MainWindow", "N/A", None))
        self.serversOnlineStatus.setText(_translate("MainWindow", "Servers Online: ", None))
        self.onlineStatus.setText(_translate("MainWindow", "0", None))
        self.serversTable.setSortingEnabled(False)
        item = self.serversTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ip Address", None))
        item = self.serversTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Socket", None))
        item = self.serversTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Protection", None))
        item = self.serversTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "OS", None))
        item = self.serversTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "User", None))
        item = self.serversTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Mic", None))
        item = self.serversTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Cam", None))
        item = self.serversTable.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Active Window Title", None))
        self.previewLabel.setText(_translate("MainWindow", "Preview", None))
        self.MainTabWidget.setTabText(self.MainTabWidget.indexOf(self.windowsTab), _translate("MainWindow", "Windows Servers", None))
        self.androidsTable.setSortingEnabled(False)
        self.label.setText(_translate("MainWindow", "Soon, If I Can Do It :)", None))
        self.MainTabWidget.setTabText(self.MainTabWidget.indexOf(self.androidsTab), _translate("MainWindow", "Android Servers", None))
        self.menuClient.setTitle(_translate("MainWindow", "Client", None))
        self.actionStartListen_for_connections.setText(_translate("MainWindow", "Start Listening", None))
        self.actionStopListen_for_connections.setText(_translate("MainWindow", "Stop Listening", None))
        self.actionClient_Configuration.setText(_translate("MainWindow", "Client Configuration", None))

import res_rc
