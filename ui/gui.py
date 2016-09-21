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
        MainWindow.resize(765, 361)
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
        self.clientsTabs = QtGui.QTabWidget(self.centralwidget)
        self.clientsTabs.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clientsTabs.setStyleSheet(_fromUtf8("QTabWidget::pane { /* The tab widget frame */\n"
"border: none;\n"
"padding-top: -10px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"left: 10px; /* move to the right by 5px */\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {   \n"
"border: none;\n"
"min-width: 30ex;\n"
"padding: 10px;\n"
"color: #c9f5f7;\n"
"}\n"
"QTabBar::tab::disabled { \n"
"  width: 0; \n"
"  height: 0; \n"
"  margin: 0; \n"
"  padding: 0;\n"
"  border: none;\n"
"  color: #2c3e50;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"background: #34495e;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"border: none;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"margin-top: 2px; /* make non-selected tabs look smaller */\n"
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
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.onlineGroup = QtGui.QGroupBox(self.onlineClientsTab)
        self.onlineGroup.setStyleSheet(_fromUtf8("background-color: #34495e;\n"
"border: none;\n"
"margin-left: 1px;\n"
"margin-right: 1px;"))
        self.onlineGroup.setTitle(_fromUtf8(""))
        self.onlineGroup.setObjectName(_fromUtf8("onlineGroup"))
        self.gridLayout_6 = QtGui.QGridLayout(self.onlineGroup)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.viewLogsButton = QtGui.QPushButton(self.onlineGroup)
        self.viewLogsButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.viewLogsButton.setStyleSheet(_fromUtf8("QPushButton#viewLogsButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 3px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#viewLogsButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.viewLogsButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/log_viewer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.viewLogsButton.setIcon(icon1)
        self.viewLogsButton.setIconSize(QtCore.QSize(16, 16))
        self.viewLogsButton.setObjectName(_fromUtf8("viewLogsButton"))
        self.horizontalLayout_6.addWidget(self.viewLogsButton)
        self.logSettingsButton = QtGui.QPushButton(self.onlineGroup)
        self.logSettingsButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.logSettingsButton.setStyleSheet(_fromUtf8("QPushButton#logSettingsButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 3px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#logSettingsButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.logSettingsButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/other_settings.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logSettingsButton.setIcon(icon2)
        self.logSettingsButton.setIconSize(QtCore.QSize(16, 16))
        self.logSettingsButton.setObjectName(_fromUtf8("logSettingsButton"))
        self.horizontalLayout_6.addWidget(self.logSettingsButton)
        self.line_2 = QtGui.QFrame(self.onlineGroup)
        self.line_2.setStyleSheet(_fromUtf8("border: 1px ridge #2c3e50;"))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout_6.addWidget(self.line_2)
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/set_alias.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setAliasButton.setIcon(icon3)
        self.setAliasButton.setIconSize(QtCore.QSize(16, 16))
        self.setAliasButton.setObjectName(_fromUtf8("setAliasButton"))
        self.horizontalLayout_6.addWidget(self.setAliasButton)
        self.updateSourceButton = QtGui.QPushButton(self.onlineGroup)
        self.updateSourceButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.updateSourceButton.setStyleSheet(_fromUtf8("QPushButton#updateSourceButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 3px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#updateSourceButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.updateSourceButton.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/update_source.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.updateSourceButton.setIcon(icon4)
        self.updateSourceButton.setIconSize(QtCore.QSize(16, 16))
        self.updateSourceButton.setObjectName(_fromUtf8("updateSourceButton"))
        self.horizontalLayout_6.addWidget(self.updateSourceButton)
        self.line = QtGui.QFrame(self.onlineGroup)
        self.line.setStyleSheet(_fromUtf8("border: 1px ridge #2c3e50;"))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_6.addWidget(self.line)
        self.shellButton = QtGui.QPushButton(self.onlineGroup)
        self.shellButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.shellButton.setStyleSheet(_fromUtf8("QPushButton#shellButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 3px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#shellButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.shellButton.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/remote_shell.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shellButton.setIcon(icon5)
        self.shellButton.setIconSize(QtCore.QSize(16, 16))
        self.shellButton.setObjectName(_fromUtf8("shellButton"))
        self.horizontalLayout_6.addWidget(self.shellButton)
        self.explorerButton = QtGui.QPushButton(self.onlineGroup)
        self.explorerButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.explorerButton.setStyleSheet(_fromUtf8("QPushButton#explorerButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 3px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#explorerButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.explorerButton.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/remote_explorer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.explorerButton.setIcon(icon6)
        self.explorerButton.setIconSize(QtCore.QSize(16, 16))
        self.explorerButton.setObjectName(_fromUtf8("explorerButton"))
        self.horizontalLayout_6.addWidget(self.explorerButton)
        self.scriptingButton = QtGui.QPushButton(self.onlineGroup)
        self.scriptingButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.scriptingButton.setStyleSheet(_fromUtf8("QPushButton#scriptingButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 3px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#scriptingButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.scriptingButton.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/remote_scripting.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.scriptingButton.setIcon(icon7)
        self.scriptingButton.setIconSize(QtCore.QSize(16, 16))
        self.scriptingButton.setObjectName(_fromUtf8("scriptingButton"))
        self.horizontalLayout_6.addWidget(self.scriptingButton)
        self.screenshotButton = QtGui.QPushButton(self.onlineGroup)
        self.screenshotButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.screenshotButton.setStyleSheet(_fromUtf8("QPushButton#screenshotButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 3px;\n"
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
        self.screenshotButton.setIconSize(QtCore.QSize(16, 16))
        self.screenshotButton.setObjectName(_fromUtf8("screenshotButton"))
        self.horizontalLayout_6.addWidget(self.screenshotButton)
        self.webcamButton = QtGui.QPushButton(self.onlineGroup)
        self.webcamButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.webcamButton.setStyleSheet(_fromUtf8("QPushButton#webcamButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 3px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#webcamButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.webcamButton.setText(_fromUtf8(""))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/webcam.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.webcamButton.setIcon(icon9)
        self.webcamButton.setIconSize(QtCore.QSize(16, 16))
        self.webcamButton.setObjectName(_fromUtf8("webcamButton"))
        self.horizontalLayout_6.addWidget(self.webcamButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.setModeratorButton = QtGui.QPushButton(self.onlineGroup)
        self.setModeratorButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setModeratorButton.setStyleSheet(_fromUtf8("QPushButton#setModeratorButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 3px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#setModeratorButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.setModeratorButton.setText(_fromUtf8(""))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/set_moderator.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setModeratorButton.setIcon(icon10)
        self.setModeratorButton.setIconSize(QtCore.QSize(16, 16))
        self.setModeratorButton.setObjectName(_fromUtf8("setModeratorButton"))
        self.horizontalLayout_6.addWidget(self.setModeratorButton)
        self.gridLayout_6.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.onlineGroup)
        self.clientsTable = QtGui.QTableWidget(self.onlineClientsTab)
        self.clientsTable.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clientsTable.setAutoFillBackground(False)
        self.clientsTable.setStyleSheet(_fromUtf8("QHeaderView::section {\n"
"background-color: #2c3e50;\n"
"padding: 2px;\n"
"color: #cff7f8;\n"
"font: 75 10px \"MS Shell Dlg 2\";\n"
"border: 1px solid;\n"
"border-top: none;\n"
"border-bottom: none;\n"
"border-color: #34495e;\n"
"}\n"
"\n"
"QTableWidget#clientsTable {\n"
"background-position: center;\n"
"border:  none;\n"
"padding: 5px;\n"
"margin-left: 1px;\n"
"margin-right: 1px;\n"
"color: #cff7f8;\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"background-color: #34495e;\n"
"alternate-background-color: #384E63;\n"
"\n"
"background-image: url(assets/bg.png);\n"
"background-repeat: no-repeat;\n"
"}\n"
"\n"
"QTableWidget#clientsTable:item:selected {\n"
"background-color: #2c3e50;\n"
"color: #cff7f8;\n"
"}"))
        self.clientsTable.setFrameShadow(QtGui.QFrame.Plain)
        self.clientsTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.clientsTable.setDragDropOverwriteMode(False)
        self.clientsTable.setAlternatingRowColors(True)
        self.clientsTable.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.clientsTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.clientsTable.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.clientsTable.setShowGrid(False)
        self.clientsTable.setGridStyle(QtCore.Qt.NoPen)
        self.clientsTable.setWordWrap(False)
        self.clientsTable.setCornerButtonEnabled(False)
        self.clientsTable.setObjectName(_fromUtf8("clientsTable"))
        self.clientsTable.setColumnCount(10)
        self.clientsTable.setRowCount(6)
        item = QtGui.QTableWidgetItem()
        self.clientsTable.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.clientsTable.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.clientsTable.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.clientsTable.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.clientsTable.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.clientsTable.setVerticalHeaderItem(5, item)
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
        self.clientsTable.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.clientsTable.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.clientsTable.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        self.clientsTable.setItem(2, 1, item)
        item = QtGui.QTableWidgetItem()
        self.clientsTable.setItem(3, 0, item)
        self.clientsTable.horizontalHeader().setCascadingSectionResizes(True)
        self.clientsTable.horizontalHeader().setDefaultSectionSize(100)
        self.clientsTable.horizontalHeader().setSortIndicatorShown(False)
        self.clientsTable.horizontalHeader().setStretchLastSection(True)
        self.clientsTable.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.clientsTable)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/online_clients.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clientsTabs.addTab(self.onlineClientsTab, icon11, _fromUtf8(""))
        self.offlineClientsTab = QtGui.QWidget()
        self.offlineClientsTab.setObjectName(_fromUtf8("offlineClientsTab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.offlineClientsTab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.offlineGroup = QtGui.QGroupBox(self.offlineClientsTab)
        self.offlineGroup.setStyleSheet(_fromUtf8("background-color: #34495e;\n"
"border: none;\n"
"margin-left: 1px;\n"
"margin-right: 1px;"))
        self.offlineGroup.setTitle(_fromUtf8(""))
        self.offlineGroup.setObjectName(_fromUtf8("offlineGroup"))
        self.gridLayout_8 = QtGui.QGridLayout(self.offlineGroup)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.viewOfflineLogsButton = QtGui.QPushButton(self.offlineGroup)
        self.viewOfflineLogsButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.viewOfflineLogsButton.setStyleSheet(_fromUtf8("QPushButton#viewOfflineLogsButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 3px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#viewOfflineLogsButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.viewOfflineLogsButton.setText(_fromUtf8(""))
        self.viewOfflineLogsButton.setIcon(icon1)
        self.viewOfflineLogsButton.setIconSize(QtCore.QSize(16, 16))
        self.viewOfflineLogsButton.setObjectName(_fromUtf8("viewOfflineLogsButton"))
        self.horizontalLayout_7.addWidget(self.viewOfflineLogsButton)
        self.setOfflineAliasButton = QtGui.QPushButton(self.offlineGroup)
        self.setOfflineAliasButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setOfflineAliasButton.setStyleSheet(_fromUtf8("QPushButton#setOfflineAliasButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 3px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#setOfflineAliasButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.setOfflineAliasButton.setText(_fromUtf8(""))
        self.setOfflineAliasButton.setIcon(icon3)
        self.setOfflineAliasButton.setIconSize(QtCore.QSize(16, 16))
        self.setOfflineAliasButton.setObjectName(_fromUtf8("setOfflineAliasButton"))
        self.horizontalLayout_7.addWidget(self.setOfflineAliasButton)
        self.removeClientButton = QtGui.QPushButton(self.offlineGroup)
        self.removeClientButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.removeClientButton.setStyleSheet(_fromUtf8("QPushButton#removeModeratorButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 3px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#removeModeratorButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.removeClientButton.setText(_fromUtf8(""))
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/trash.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeClientButton.setIcon(icon12)
        self.removeClientButton.setIconSize(QtCore.QSize(16, 16))
        self.removeClientButton.setObjectName(_fromUtf8("removeClientButton"))
        self.horizontalLayout_7.addWidget(self.removeClientButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.gridLayout_8.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.offlineGroup)
        self.offlineClientsTable = QtGui.QTableWidget(self.offlineClientsTab)
        self.offlineClientsTable.setFocusPolicy(QtCore.Qt.NoFocus)
        self.offlineClientsTable.setAutoFillBackground(False)
        self.offlineClientsTable.setStyleSheet(_fromUtf8("QHeaderView::section {\n"
"background-color: #2c3e50;\n"
"padding: 2px;\n"
"color: #cff7f8;\n"
"font: 75 10px \"MS Shell Dlg 2\";\n"
"border: 1px solid;\n"
"border-top: none;\n"
"border-bottom: none;\n"
"border-color: #34495e;\n"
"}\n"
"\n"
"QTableWidget#offlineClientsTable {\n"
"background-position: center;\n"
"border:  none;\n"
"padding: 5px;\n"
"margin-left: 1px;\n"
"margin-right: 1px;\n"
"color: #cff7f8;\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"background-color: #34495e;\n"
"alternate-background-color: #384E63;\n"
"\n"
"background-image: url(assets/bg.png);\n"
"background-repeat: no-repeat;\n"
"}\n"
"\n"
"QTableWidget#offlineClientsTable:item:selected {\n"
"background-color: #2c3e50;\n"
"color: #cff7f8;\n"
"}"))
        self.offlineClientsTable.setFrameShadow(QtGui.QFrame.Plain)
        self.offlineClientsTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.offlineClientsTable.setDragDropOverwriteMode(False)
        self.offlineClientsTable.setAlternatingRowColors(True)
        self.offlineClientsTable.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
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
        self.verticalLayout_2.addWidget(self.offlineClientsTable)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/offline_clients.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clientsTabs.addTab(self.offlineClientsTab, icon13, _fromUtf8(""))
        self.moderatorsTab = QtGui.QWidget()
        self.moderatorsTab.setObjectName(_fromUtf8("moderatorsTab"))
        self.gridLayout_4 = QtGui.QGridLayout(self.moderatorsTab)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.moderatorsGroup = QtGui.QGroupBox(self.moderatorsTab)
        self.moderatorsGroup.setStyleSheet(_fromUtf8("background-color: #34495e;\n"
"border: none;\n"
"margin-left: 1px;\n"
"margin-right: 1px;"))
        self.moderatorsGroup.setTitle(_fromUtf8(""))
        self.moderatorsGroup.setObjectName(_fromUtf8("moderatorsGroup"))
        self.gridLayout_7 = QtGui.QGridLayout(self.moderatorsGroup)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.addModeratorButton = QtGui.QPushButton(self.moderatorsGroup)
        self.addModeratorButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.addModeratorButton.setStyleSheet(_fromUtf8("QPushButton#addModeratorButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 3px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#addModeratorButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.addModeratorButton.setText(_fromUtf8(""))
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/add_moderator.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addModeratorButton.setIcon(icon14)
        self.addModeratorButton.setIconSize(QtCore.QSize(16, 16))
        self.addModeratorButton.setObjectName(_fromUtf8("addModeratorButton"))
        self.horizontalLayout_8.addWidget(self.addModeratorButton)
        self.changePasswordButton = QtGui.QPushButton(self.moderatorsGroup)
        self.changePasswordButton.setStyleSheet(_fromUtf8("QPushButton#changePasswordButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 3px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#changePasswordButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.changePasswordButton.setText(_fromUtf8(""))
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/password.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.changePasswordButton.setIcon(icon15)
        self.changePasswordButton.setIconSize(QtCore.QSize(16, 16))
        self.changePasswordButton.setObjectName(_fromUtf8("changePasswordButton"))
        self.horizontalLayout_8.addWidget(self.changePasswordButton)
        self.changePrivilegesButton = QtGui.QPushButton(self.moderatorsGroup)
        self.changePrivilegesButton.setStyleSheet(_fromUtf8("QPushButton#changePrivilegesButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 3px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#changePrivilegesButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.changePrivilegesButton.setText(_fromUtf8(""))
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/privileges.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.changePrivilegesButton.setIcon(icon16)
        self.changePrivilegesButton.setIconSize(QtCore.QSize(16, 16))
        self.changePrivilegesButton.setObjectName(_fromUtf8("changePrivilegesButton"))
        self.horizontalLayout_8.addWidget(self.changePrivilegesButton)
        self.removeModeratorButton = QtGui.QPushButton(self.moderatorsGroup)
        self.removeModeratorButton.setStyleSheet(_fromUtf8("QPushButton#removeModeratorButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 3px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#removeModeratorButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.removeModeratorButton.setText(_fromUtf8(""))
        self.removeModeratorButton.setIcon(icon12)
        self.removeModeratorButton.setIconSize(QtCore.QSize(16, 16))
        self.removeModeratorButton.setObjectName(_fromUtf8("removeModeratorButton"))
        self.horizontalLayout_8.addWidget(self.removeModeratorButton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.gridLayout_7.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.moderatorsGroup)
        self.moderatorsTable = QtGui.QTableWidget(self.moderatorsTab)
        self.moderatorsTable.setFocusPolicy(QtCore.Qt.NoFocus)
        self.moderatorsTable.setAutoFillBackground(False)
        self.moderatorsTable.setStyleSheet(_fromUtf8("QHeaderView::section {\n"
"background-color: #2c3e50;\n"
"padding: 2px;\n"
"color: #cff7f8;\n"
"font: 75 10px \"MS Shell Dlg 2\";\n"
"border: 1px solid;\n"
"border-top: none;\n"
"border-bottom: none;\n"
"border-color: #34495e;\n"
"}\n"
"\n"
"QTableWidget#moderatorsTable {\n"
"background-position: center;\n"
"border:  none;\n"
"padding: 5px;\n"
"margin-left: 1px;\n"
"margin-right: 1px;\n"
"color: #cff7f8;\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"background-color: #34495e;\n"
"alternate-background-color: #384E63;\n"
"\n"
"background-image: url(assets/bg.png);\n"
"background-repeat: no-repeat;\n"
"}\n"
"\n"
"QTableWidget#moderatorsTable:item:selected {\n"
"background-color: #2c3e50;\n"
"color: #cff7f8;\n"
"}"))
        self.moderatorsTable.setFrameShadow(QtGui.QFrame.Plain)
        self.moderatorsTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.moderatorsTable.setDragDropOverwriteMode(False)
        self.moderatorsTable.setAlternatingRowColors(True)
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
        self.verticalLayout_3.addWidget(self.moderatorsTable)
        self.gridLayout_4.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/moderators.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clientsTabs.addTab(self.moderatorsTab, icon17, _fromUtf8(""))
        self.gridLayout.addWidget(self.clientsTabs, 1, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setStyleSheet(_fromUtf8("background-color: #2c3e50; \n"
"border: none;\n"
"margin-left: 6px;\n"
"margin-right: 6px;\n"
"padding: -5px;\n"
"padding-top: -7px;\n"
"padding-bottom: -7px;"))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.connectButton = QtGui.QPushButton(self.groupBox)
        self.connectButton.setMinimumSize(QtCore.QSize(0, 0))
        self.connectButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.connectButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.connectButton.setToolTip(_fromUtf8(""))
        self.connectButton.setStyleSheet(_fromUtf8("QPushButton#connectButton {\n"
"            background-color: #34495e;\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 5px;\n"
"            margin: 0px;\n"
"            }\n"
"\n"
"QPushButton#connectButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }\n"
"\n"
"QPushButton#connectButton:checked {\n"
"            border: 1px ridge #c9f5f7;\n"
"            }"))
        self.connectButton.setText(_fromUtf8(""))
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/connect.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.connectButton.setIcon(icon18)
        self.connectButton.setIconSize(QtCore.QSize(16, 16))
        self.connectButton.setCheckable(True)
        self.connectButton.setObjectName(_fromUtf8("connectButton"))
        self.horizontalLayout.addWidget(self.connectButton)
        self.disconnectButton = QtGui.QPushButton(self.groupBox)
        self.disconnectButton.setMinimumSize(QtCore.QSize(0, 0))
        self.disconnectButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.disconnectButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.disconnectButton.setStyleSheet(_fromUtf8("QPushButton#disconnectButton {\n"
"            background-color: #34495e;\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 5px;\n"
"            margin: 0px;\n"
"            }\n"
"\n"
"QPushButton#disconnectButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.disconnectButton.setText(_fromUtf8(""))
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/disconnect.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.disconnectButton.setIcon(icon19)
        self.disconnectButton.setIconSize(QtCore.QSize(16, 16))
        self.disconnectButton.setCheckable(False)
        self.disconnectButton.setChecked(False)
        self.disconnectButton.setObjectName(_fromUtf8("disconnectButton"))
        self.horizontalLayout.addWidget(self.disconnectButton)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.settingsButton = QtGui.QPushButton(self.groupBox)
        self.settingsButton.setStyleSheet(_fromUtf8("QPushButton#settingsButton {\n"
"            background-color: #34495e;\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 5px;\n"
"            margin: 0px;\n"
"            }\n"
"\n"
"QPushButton#settingsButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }\n"
"\n"
"QPushButton#settingsButton:checked {\n"
"            border: 1px ridge #c9f5f7;\n"
"            }"))
        self.settingsButton.setText(_fromUtf8(""))
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/settings.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsButton.setIcon(icon20)
        self.settingsButton.setIconSize(QtCore.QSize(16, 16))
        self.settingsButton.setCheckable(True)
        self.settingsButton.setChecked(False)
        self.settingsButton.setObjectName(_fromUtf8("settingsButton"))
        self.horizontalLayout.addWidget(self.settingsButton)
        self.gridLayout_5.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 765, 34))
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
        self.actionStartListen_for_connections.setIcon(icon18)
        self.actionStartListen_for_connections.setObjectName(_fromUtf8("actionStartListen_for_connections"))
        self.actionStopListen_for_connections = QtGui.QAction(MainWindow)
        self.actionStopListen_for_connections.setCheckable(True)
        self.actionStopListen_for_connections.setIcon(icon19)
        self.actionStopListen_for_connections.setObjectName(_fromUtf8("actionStopListen_for_connections"))
        self.actionViewer_Configuration = QtGui.QAction(MainWindow)
        self.actionViewer_Configuration.setIcon(icon20)
        self.actionViewer_Configuration.setObjectName(_fromUtf8("actionViewer_Configuration"))
        self.actionRemote_Shell = QtGui.QAction(MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/mshell.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemote_Shell.setIcon(icon21)
        self.actionRemote_Shell.setObjectName(_fromUtf8("actionRemote_Shell"))
        self.actionRemote_Explorer = QtGui.QAction(MainWindow)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/mexplorer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemote_Explorer.setIcon(icon22)
        self.actionRemote_Explorer.setObjectName(_fromUtf8("actionRemote_Explorer"))
        self.actionRemote_Process_Manager = QtGui.QAction(MainWindow)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/mprocesses.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemote_Process_Manager.setIcon(icon23)
        self.actionRemote_Process_Manager.setObjectName(_fromUtf8("actionRemote_Process_Manager"))
        self.actionRemote_Microphone = QtGui.QAction(MainWindow)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/maudio.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemote_Microphone.setIcon(icon24)
        self.actionRemote_Microphone.setObjectName(_fromUtf8("actionRemote_Microphone"))
        self.actionRemote_Scripting = QtGui.QAction(MainWindow)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/script.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemote_Scripting.setIcon(icon25)
        self.actionRemote_Scripting.setObjectName(_fromUtf8("actionRemote_Scripting"))
        self.actionRemote_Keylogger = QtGui.QAction(MainWindow)
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/mkeylogger.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemote_Keylogger.setIcon(icon26)
        self.actionRemote_Keylogger.setObjectName(_fromUtf8("actionRemote_Keylogger"))
        self.actionDesktop_Preview = QtGui.QAction(MainWindow)
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/mdesktop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDesktop_Preview.setIcon(icon27)
        self.actionDesktop_Preview.setObjectName(_fromUtf8("actionDesktop_Preview"))
        self.actionWebcam_Preview = QtGui.QAction(MainWindow)
        self.actionWebcam_Preview.setIcon(icon9)
        self.actionWebcam_Preview.setObjectName(_fromUtf8("actionWebcam_Preview"))
        self.actionStop_Client = QtGui.QAction(MainWindow)
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/terminate.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStop_Client.setIcon(icon28)
        self.actionStop_Client.setObjectName(_fromUtf8("actionStop_Client"))
        self.actionLock_Client = QtGui.QAction(MainWindow)
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/lock.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLock_Client.setIcon(icon29)
        self.actionLock_Client.setObjectName(_fromUtf8("actionLock_Client"))
        self.actionLog_off = QtGui.QAction(MainWindow)
        self.actionLog_off.setObjectName(_fromUtf8("actionLog_off"))
        self.actionReboot = QtGui.QAction(MainWindow)
        self.actionReboot.setObjectName(_fromUtf8("actionReboot"))
        self.actionShutdown = QtGui.QAction(MainWindow)
        self.actionShutdown.setObjectName(_fromUtf8("actionShutdown"))
        self.actionUnlock_Client = QtGui.QAction(MainWindow)
        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/unlock.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUnlock_Client.setIcon(icon30)
        self.actionUnlock_Client.setObjectName(_fromUtf8("actionUnlock_Client"))
        self.actionSet_Alias = QtGui.QAction(MainWindow)
        icon31 = QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/add_alias.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSet_Alias.setIcon(icon31)
        self.actionSet_Alias.setObjectName(_fromUtf8("actionSet_Alias"))
        self.actionRun_As_Admin = QtGui.QAction(MainWindow)
        icon32 = QtGui.QIcon()
        icon32.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/run_as_admin.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRun_As_Admin.setIcon(icon32)
        self.actionRun_As_Admin.setObjectName(_fromUtf8("actionRun_As_Admin"))
        self.actionTerminate_Client = QtGui.QAction(MainWindow)
        icon33 = QtGui.QIcon()
        icon33.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTerminate_Client.setIcon(icon33)
        self.actionTerminate_Client.setObjectName(_fromUtf8("actionTerminate_Client"))
        self.actionWindows_Client_PyInstaller = QtGui.QAction(MainWindow)
        self.actionWindows_Client_PyInstaller.setObjectName(_fromUtf8("actionWindows_Client_PyInstaller"))

        self.retranslateUi(MainWindow)
        self.clientsTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Moderat Viewer", None))
        self.clientsTable.setSortingEnabled(False)
        item = self.clientsTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row", None))
        item = self.clientsTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row", None))
        item = self.clientsTable.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row", None))
        item = self.clientsTable.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row", None))
        item = self.clientsTable.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Row", None))
        item = self.clientsTable.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "New Row", None))
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
        item.setText(_translate("MainWindow", "Mic", None))
        item = self.clientsTable.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Cam", None))
        item = self.clientsTable.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Active Window Title", None))
        __sortingEnabled = self.clientsTable.isSortingEnabled()
        self.clientsTable.setSortingEnabled(False)
        item = self.clientsTable.item(0, 0)
        item.setText(_translate("MainWindow", "fasf", None))
        item = self.clientsTable.item(1, 0)
        item.setText(_translate("MainWindow", "asda", None))
        item = self.clientsTable.item(2, 0)
        item.setText(_translate("MainWindow", "sfa", None))
        item = self.clientsTable.item(2, 1)
        item.setText(_translate("MainWindow", "sasf", None))
        item = self.clientsTable.item(3, 0)
        item.setText(_translate("MainWindow", "sfas", None))
        self.clientsTable.setSortingEnabled(__sortingEnabled)
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
