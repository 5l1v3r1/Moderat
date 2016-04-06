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
        self.serversTable = QtGui.QTableWidget(self.centralwidget)
        self.serversTable.setFocusPolicy(QtCore.Qt.NoFocus)
        self.serversTable.setAutoFillBackground(False)
        self.serversTable.setStyleSheet(_fromUtf8("QHeaderView::section {\n"
"    background-color: #34495e;\n"
"    padding: 2px;\n"
"    color: #cff7f8;\n"
"    font: 75 10px \"MS Shell Dlg 2\";\n"
"    border: 1px ridge;\n"
"    border-right: none;\n"
"    border-color: #2c3e50;\n"
"}\n"
"\n"
"QTableWidget#serversTable {\n"
"    background-position: center;\n"
"    border: 1px ridge;\n"
"    padding: 5px;\n"
"    color: #cff7f8;\n"
"    border-color: #2c3e50;\n"
"    font: 8pt \"MS Shell Dlg 2\";\n"
"    background-color: #34495e;\n"
"\n"
"    background-image: url(assets/bg.png);\n"
"}\n"
"\n"
"QTableWidget#serversTable:item:selected {\n"
"background-color: #2c3e50;\n"
"color: #cff7f8;\n"
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
        self.serversTable.setColumnCount(10)
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
        item = QtGui.QTableWidgetItem()
        self.serversTable.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.serversTable.setHorizontalHeaderItem(9, item)
        self.serversTable.horizontalHeader().setCascadingSectionResizes(True)
        self.serversTable.horizontalHeader().setDefaultSectionSize(100)
        self.serversTable.horizontalHeader().setSortIndicatorShown(False)
        self.serversTable.horizontalHeader().setStretchLastSection(True)
        self.serversTable.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.serversTable, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(50)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.madeByLabel = QtGui.QLabel(self.centralwidget)
        self.madeByLabel.setObjectName(_fromUtf8("madeByLabel"))
        self.horizontalLayout_4.addWidget(self.madeByLabel)
        self.creditFlagLabel = QtGui.QLabel(self.centralwidget)
        self.creditFlagLabel.setText(_fromUtf8(""))
        self.creditFlagLabel.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/flags/ge.png")))
        self.creditFlagLabel.setObjectName(_fromUtf8("creditFlagLabel"))
        self.horizontalLayout_4.addWidget(self.creditFlagLabel)
        self.creditLabel = QtGui.QLabel(self.centralwidget)
        self.creditLabel.setMaximumSize(QtCore.QSize(16777215, 20))
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
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.clientStatusLabel = QtGui.QLabel(self.centralwidget)
        self.clientStatusLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.clientStatusLabel.setStyleSheet(_fromUtf8("border: none;"))
        self.clientStatusLabel.setObjectName(_fromUtf8("clientStatusLabel"))
        self.horizontalLayout_6.addWidget(self.clientStatusLabel)
        self.statusLabel = QtGui.QLabel(self.centralwidget)
        self.statusLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.statusLabel.setStyleSheet(_fromUtf8("border: none;\n"
"color: #e74c3c;\n"
"font: 8pt \"MS Shell Dlg 2\";"))
        self.statusLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statusLabel.setObjectName(_fromUtf8("statusLabel"))
        self.horizontalLayout_6.addWidget(self.statusLabel)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.ipv4TextLabel = QtGui.QLabel(self.centralwidget)
        self.ipv4TextLabel.setObjectName(_fromUtf8("ipv4TextLabel"))
        self.horizontalLayout_2.addWidget(self.ipv4TextLabel)
        self.ipv4Label = QtGui.QLabel(self.centralwidget)
        self.ipv4Label.setObjectName(_fromUtf8("ipv4Label"))
        self.horizontalLayout_2.addWidget(self.ipv4Label)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.portTextLabel = QtGui.QLabel(self.centralwidget)
        self.portTextLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.portTextLabel.setStyleSheet(_fromUtf8("border: none;"))
        self.portTextLabel.setObjectName(_fromUtf8("portTextLabel"))
        self.horizontalLayout.addWidget(self.portTextLabel)
        self.portLabel = QtGui.QLabel(self.centralwidget)
        self.portLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.portLabel.setStyleSheet(_fromUtf8("border: none;\n"
"font: 8pt \"MS Shell Dlg 2\";"))
        self.portLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.portLabel.setObjectName(_fromUtf8("portLabel"))
        self.horizontalLayout.addWidget(self.portLabel)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.serversOnlineStatus = QtGui.QLabel(self.centralwidget)
        self.serversOnlineStatus.setMaximumSize(QtCore.QSize(16777215, 20))
        self.serversOnlineStatus.setStyleSheet(_fromUtf8("border: none;"))
        self.serversOnlineStatus.setObjectName(_fromUtf8("serversOnlineStatus"))
        self.horizontalLayout_5.addWidget(self.serversOnlineStatus)
        self.onlineStatus = QtGui.QLabel(self.centralwidget)
        self.onlineStatus.setMaximumSize(QtCore.QSize(16777215, 20))
        self.onlineStatus.setStyleSheet(_fromUtf8("border: none;\n"
"font: 8pt \"MS Shell Dlg 2\";"))
        self.onlineStatus.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.onlineStatus.setObjectName(_fromUtf8("onlineStatus"))
        self.horizontalLayout_5.addWidget(self.onlineStatus)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
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
"        }\n"
"        QMenu::item::checked {\n"
"            border: 1px ridge;\n"
"            border-color: #27ae60;\n"
"        }"))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.serverMenu = QtGui.QMenu(self.menubar)
        self.serverMenu.setTearOffEnabled(False)
        self.serverMenu.setSeparatorsCollapsible(False)
        self.serverMenu.setObjectName(_fromUtf8("serverMenu"))
        self.menuAction = QtGui.QMenu(self.menubar)
        self.menuAction.setTearOffEnabled(False)
        self.menuAction.setObjectName(_fromUtf8("menuAction"))
        self.menuServer = QtGui.QMenu(self.menubar)
        self.menuServer.setTearOffEnabled(False)
        self.menuServer.setSeparatorsCollapsible(False)
        self.menuServer.setObjectName(_fromUtf8("menuServer"))
        MainWindow.setMenuBar(self.menubar)
        self.actionStartListen_for_connections = QtGui.QAction(MainWindow)
        self.actionStartListen_for_connections.setCheckable(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/connect.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStartListen_for_connections.setIcon(icon1)
        self.actionStartListen_for_connections.setObjectName(_fromUtf8("actionStartListen_for_connections"))
        self.actionStopListen_for_connections = QtGui.QAction(MainWindow)
        self.actionStopListen_for_connections.setCheckable(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/disconnect.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStopListen_for_connections.setIcon(icon2)
        self.actionStopListen_for_connections.setObjectName(_fromUtf8("actionStopListen_for_connections"))
        self.actionClient_Configuration = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/settings.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClient_Configuration.setIcon(icon3)
        self.actionClient_Configuration.setObjectName(_fromUtf8("actionClient_Configuration"))
        self.actionRemote_Shell = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/mshell.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemote_Shell.setIcon(icon4)
        self.actionRemote_Shell.setObjectName(_fromUtf8("actionRemote_Shell"))
        self.actionRemote_Explorer = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/mexplorer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemote_Explorer.setIcon(icon5)
        self.actionRemote_Explorer.setObjectName(_fromUtf8("actionRemote_Explorer"))
        self.actionRemote_Process_Manager = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/mprocesses.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemote_Process_Manager.setIcon(icon6)
        self.actionRemote_Process_Manager.setObjectName(_fromUtf8("actionRemote_Process_Manager"))
        self.actionRemote_Microphone = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/maudio.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemote_Microphone.setIcon(icon7)
        self.actionRemote_Microphone.setObjectName(_fromUtf8("actionRemote_Microphone"))
        self.actionRemote_Scripting = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/script.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemote_Scripting.setIcon(icon8)
        self.actionRemote_Scripting.setObjectName(_fromUtf8("actionRemote_Scripting"))
        self.actionRemote_Keylogger = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/mkeylogger.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemote_Keylogger.setIcon(icon9)
        self.actionRemote_Keylogger.setObjectName(_fromUtf8("actionRemote_Keylogger"))
        self.actionDesktop_Preview = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/mdesktop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDesktop_Preview.setIcon(icon10)
        self.actionDesktop_Preview.setObjectName(_fromUtf8("actionDesktop_Preview"))
        self.actionWebcam_Preview = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/webcam.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionWebcam_Preview.setIcon(icon11)
        self.actionWebcam_Preview.setObjectName(_fromUtf8("actionWebcam_Preview"))
        self.actionStop_Client = QtGui.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/terminate.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStop_Client.setIcon(icon12)
        self.actionStop_Client.setObjectName(_fromUtf8("actionStop_Client"))
        self.actionLock_Client = QtGui.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/lock.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLock_Client.setIcon(icon13)
        self.actionLock_Client.setObjectName(_fromUtf8("actionLock_Client"))
        self.actionLog_off = QtGui.QAction(MainWindow)
        self.actionLog_off.setObjectName(_fromUtf8("actionLog_off"))
        self.actionReboot = QtGui.QAction(MainWindow)
        self.actionReboot.setObjectName(_fromUtf8("actionReboot"))
        self.actionShutdown = QtGui.QAction(MainWindow)
        self.actionShutdown.setObjectName(_fromUtf8("actionShutdown"))
        self.actionUnlock_Client = QtGui.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/unlock.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUnlock_Client.setIcon(icon14)
        self.actionUnlock_Client.setObjectName(_fromUtf8("actionUnlock_Client"))
        self.actionSet_Alias = QtGui.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/add_alias.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSet_Alias.setIcon(icon15)
        self.actionSet_Alias.setObjectName(_fromUtf8("actionSet_Alias"))
        self.actionRun_As_Admin = QtGui.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/run_as_admin.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRun_As_Admin.setIcon(icon16)
        self.actionRun_As_Admin.setObjectName(_fromUtf8("actionRun_As_Admin"))
        self.actionTerminate_Client = QtGui.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTerminate_Client.setIcon(icon17)
        self.actionTerminate_Client.setObjectName(_fromUtf8("actionTerminate_Client"))
        self.serverMenu.addAction(self.actionStartListen_for_connections)
        self.serverMenu.addAction(self.actionStopListen_for_connections)
        self.serverMenu.addSeparator()
        self.serverMenu.addAction(self.actionClient_Configuration)
        self.menuAction.addAction(self.actionRemote_Shell)
        self.menuAction.addAction(self.actionRemote_Explorer)
        self.menuAction.addAction(self.actionRemote_Process_Manager)
        self.menuAction.addAction(self.actionRemote_Microphone)
        self.menuAction.addAction(self.actionRemote_Scripting)
        self.menuAction.addAction(self.actionRemote_Keylogger)
        self.menuAction.addSeparator()
        self.menuAction.addAction(self.actionDesktop_Preview)
        self.menuAction.addAction(self.actionWebcam_Preview)
        self.menuServer.addAction(self.actionUnlock_Client)
        self.menuServer.addAction(self.actionLock_Client)
        self.menuServer.addAction(self.actionStop_Client)
        self.menuServer.addSeparator()
        self.menuServer.addAction(self.actionSet_Alias)
        self.menuServer.addAction(self.actionRun_As_Admin)
        self.menubar.addAction(self.serverMenu.menuAction())
        self.menubar.addAction(self.menuServer.menuAction())
        self.menubar.addAction(self.menuAction.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Moderat Monitoring Server", None))
        self.serversTable.setSortingEnabled(False)
        item = self.serversTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ip Address", None))
        item = self.serversTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Alias", None))
        item = self.serversTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Socket", None))
        item = self.serversTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "OS", None))
        item = self.serversTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "User", None))
        item = self.serversTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Privs", None))
        item = self.serversTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Lock", None))
        item = self.serversTable.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Mic", None))
        item = self.serversTable.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Cam", None))
        item = self.serversTable.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Active Window Title", None))
        self.madeByLabel.setText(_translate("MainWindow", "Made By ", None))
        self.creditLabel.setText(_translate("MainWindow", " Uri Patton", None))
        self.clientStatusLabel.setText(_translate("MainWindow", "STATUS:", None))
        self.statusLabel.setText(_translate("MainWindow", "Offline", None))
        self.ipv4TextLabel.setText(_translate("MainWindow", "IPv4:", None))
        self.ipv4Label.setText(_translate("MainWindow", "N/A", None))
        self.portTextLabel.setText(_translate("MainWindow", "PORT:", None))
        self.portLabel.setText(_translate("MainWindow", "N/A", None))
        self.serversOnlineStatus.setText(_translate("MainWindow", "SERVERS TOTAL:", None))
        self.onlineStatus.setText(_translate("MainWindow", "0", None))
        self.serverMenu.setTitle(_translate("MainWindow", "Server", None))
        self.menuAction.setTitle(_translate("MainWindow", "Plugins", "asd"))
        self.menuServer.setTitle(_translate("MainWindow", "Client", None))
        self.actionStartListen_for_connections.setText(_translate("MainWindow", "Start Server", None))
        self.actionStopListen_for_connections.setText(_translate("MainWindow", "Stop Server", None))
        self.actionClient_Configuration.setText(_translate("MainWindow", "Server Configuration", None))
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

import res_rc
