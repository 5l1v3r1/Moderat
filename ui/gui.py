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
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(50)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.loginStatusLabel = QtGui.QLabel(self.centralwidget)
        self.loginStatusLabel.setObjectName(_fromUtf8("loginStatusLabel"))
        self.horizontalLayout_4.addWidget(self.loginStatusLabel)
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
        self.clientsTabs = QtGui.QTabWidget(self.centralwidget)
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
"    min-width: 6ex;\n"
"    padding: 10px;\n"
"    color: #c9f5f7;\n"
"}\n"
"QTabBar::tab::disabled {   \n"
"    border: none;\n"
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
        self.clientsTabs.setDocumentMode(False)
        self.clientsTabs.setTabsClosable(False)
        self.clientsTabs.setMovable(False)
        self.clientsTabs.setObjectName(_fromUtf8("clientsTabs"))
        self.onlineClientsTab = QtGui.QWidget()
        self.onlineClientsTab.setObjectName(_fromUtf8("onlineClientsTab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.onlineClientsTab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
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
        self.gridLayout_2.addWidget(self.clientsTable, 0, 0, 1, 1)
        self.clientsTabs.addTab(self.onlineClientsTab, _fromUtf8(""))
        self.offlineClientsTab = QtGui.QWidget()
        self.offlineClientsTab.setObjectName(_fromUtf8("offlineClientsTab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.offlineClientsTab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
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
        self.gridLayout_3.addWidget(self.offlineClientsTable, 0, 0, 1, 1)
        self.clientsTabs.addTab(self.offlineClientsTab, _fromUtf8(""))
        self.moderatorsTab = QtGui.QWidget()
        self.moderatorsTab.setObjectName(_fromUtf8("moderatorsTab"))
        self.gridLayout_4 = QtGui.QGridLayout(self.moderatorsTab)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.getModeratorsButton = QtGui.QPushButton(self.moderatorsTab)
        self.getModeratorsButton.setStyleSheet(_fromUtf8("QPushButton#getModeratorsButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 3px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#getModeratorsButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/update.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.getModeratorsButton.setIcon(icon1)
        self.getModeratorsButton.setObjectName(_fromUtf8("getModeratorsButton"))
        self.gridLayout_4.addWidget(self.getModeratorsButton, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 0, 2, 1, 1)
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
        self.moderatorsTable.setColumnCount(5)
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
        self.moderatorsTable.horizontalHeader().setCascadingSectionResizes(True)
        self.moderatorsTable.horizontalHeader().setDefaultSectionSize(100)
        self.moderatorsTable.horizontalHeader().setSortIndicatorShown(False)
        self.moderatorsTable.horizontalHeader().setStretchLastSection(True)
        self.moderatorsTable.verticalHeader().setVisible(False)
        self.gridLayout_4.addWidget(self.moderatorsTable, 1, 0, 1, 3)
        self.addModeratorButton = QtGui.QPushButton(self.moderatorsTab)
        self.addModeratorButton.setStyleSheet(_fromUtf8("QPushButton#addModeratorButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 3px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#addModeratorButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/add_alias.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addModeratorButton.setIcon(icon2)
        self.addModeratorButton.setObjectName(_fromUtf8("addModeratorButton"))
        self.gridLayout_4.addWidget(self.addModeratorButton, 0, 1, 1, 1)
        self.clientsTabs.addTab(self.moderatorsTab, _fromUtf8(""))
        self.gridLayout.addWidget(self.clientsTabs, 0, 0, 1, 1)
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
        self.menuBuilder = QtGui.QMenu(self.menubar)
        self.menuBuilder.setObjectName(_fromUtf8("menuBuilder"))
        MainWindow.setMenuBar(self.menubar)
        self.actionStartListen_for_connections = QtGui.QAction(MainWindow)
        self.actionStartListen_for_connections.setCheckable(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/connect.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStartListen_for_connections.setIcon(icon3)
        self.actionStartListen_for_connections.setObjectName(_fromUtf8("actionStartListen_for_connections"))
        self.actionStopListen_for_connections = QtGui.QAction(MainWindow)
        self.actionStopListen_for_connections.setCheckable(True)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/disconnect.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStopListen_for_connections.setIcon(icon4)
        self.actionStopListen_for_connections.setObjectName(_fromUtf8("actionStopListen_for_connections"))
        self.actionClient_Configuration = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/settings.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClient_Configuration.setIcon(icon5)
        self.actionClient_Configuration.setObjectName(_fromUtf8("actionClient_Configuration"))
        self.actionRemote_Shell = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/mshell.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemote_Shell.setIcon(icon6)
        self.actionRemote_Shell.setObjectName(_fromUtf8("actionRemote_Shell"))
        self.actionRemote_Explorer = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/mexplorer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemote_Explorer.setIcon(icon7)
        self.actionRemote_Explorer.setObjectName(_fromUtf8("actionRemote_Explorer"))
        self.actionRemote_Process_Manager = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/mprocesses.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemote_Process_Manager.setIcon(icon8)
        self.actionRemote_Process_Manager.setObjectName(_fromUtf8("actionRemote_Process_Manager"))
        self.actionRemote_Microphone = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/maudio.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemote_Microphone.setIcon(icon9)
        self.actionRemote_Microphone.setObjectName(_fromUtf8("actionRemote_Microphone"))
        self.actionRemote_Scripting = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/script.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemote_Scripting.setIcon(icon10)
        self.actionRemote_Scripting.setObjectName(_fromUtf8("actionRemote_Scripting"))
        self.actionRemote_Keylogger = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/mkeylogger.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemote_Keylogger.setIcon(icon11)
        self.actionRemote_Keylogger.setObjectName(_fromUtf8("actionRemote_Keylogger"))
        self.actionDesktop_Preview = QtGui.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/mdesktop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDesktop_Preview.setIcon(icon12)
        self.actionDesktop_Preview.setObjectName(_fromUtf8("actionDesktop_Preview"))
        self.actionWebcam_Preview = QtGui.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/webcam.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionWebcam_Preview.setIcon(icon13)
        self.actionWebcam_Preview.setObjectName(_fromUtf8("actionWebcam_Preview"))
        self.actionStop_Client = QtGui.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/terminate.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStop_Client.setIcon(icon14)
        self.actionStop_Client.setObjectName(_fromUtf8("actionStop_Client"))
        self.actionLock_Client = QtGui.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/lock.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLock_Client.setIcon(icon15)
        self.actionLock_Client.setObjectName(_fromUtf8("actionLock_Client"))
        self.actionLog_off = QtGui.QAction(MainWindow)
        self.actionLog_off.setObjectName(_fromUtf8("actionLog_off"))
        self.actionReboot = QtGui.QAction(MainWindow)
        self.actionReboot.setObjectName(_fromUtf8("actionReboot"))
        self.actionShutdown = QtGui.QAction(MainWindow)
        self.actionShutdown.setObjectName(_fromUtf8("actionShutdown"))
        self.actionUnlock_Client = QtGui.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/unlock.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUnlock_Client.setIcon(icon16)
        self.actionUnlock_Client.setObjectName(_fromUtf8("actionUnlock_Client"))
        self.actionSet_Alias = QtGui.QAction(MainWindow)
        self.actionSet_Alias.setIcon(icon2)
        self.actionSet_Alias.setObjectName(_fromUtf8("actionSet_Alias"))
        self.actionRun_As_Admin = QtGui.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/run_as_admin.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRun_As_Admin.setIcon(icon17)
        self.actionRun_As_Admin.setObjectName(_fromUtf8("actionRun_As_Admin"))
        self.actionTerminate_Client = QtGui.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTerminate_Client.setIcon(icon18)
        self.actionTerminate_Client.setObjectName(_fromUtf8("actionTerminate_Client"))
        self.actionWindows_Client_PyInstaller = QtGui.QAction(MainWindow)
        self.actionWindows_Client_PyInstaller.setObjectName(_fromUtf8("actionWindows_Client_PyInstaller"))
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
        self.menuBuilder.addAction(self.actionWindows_Client_PyInstaller)
        self.menubar.addAction(self.serverMenu.menuAction())
        self.menubar.addAction(self.menuServer.menuAction())
        self.menubar.addAction(self.menuAction.menuAction())
        self.menubar.addAction(self.menuBuilder.menuAction())

        self.retranslateUi(MainWindow)
        self.clientsTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Moderat Monitoring Server", None))
        self.loginStatusLabel.setText(_translate("MainWindow", "Not Authorized", None))
        self.clientStatusLabel.setText(_translate("MainWindow", "STATUS:", None))
        self.statusLabel.setText(_translate("MainWindow", "Offline", None))
        self.ipv4TextLabel.setText(_translate("MainWindow", "IPv4:", None))
        self.ipv4Label.setText(_translate("MainWindow", "N/A", None))
        self.portTextLabel.setText(_translate("MainWindow", "PORT:", None))
        self.portLabel.setText(_translate("MainWindow", "N/A", None))
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
        item.setText(_translate("MainWindow", "Socket", None))
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
        self.getModeratorsButton.setText(_translate("MainWindow", "Get Moderators", None))
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
        self.addModeratorButton.setText(_translate("MainWindow", "Add Moderator", None))
        self.clientsTabs.setTabText(self.clientsTabs.indexOf(self.moderatorsTab), _translate("MainWindow", "Moderators", None))
        self.serverMenu.setTitle(_translate("MainWindow", "Server", None))
        self.menuAction.setTitle(_translate("MainWindow", "Plugins", "asd"))
        self.menuServer.setTitle(_translate("MainWindow", "Client", None))
        self.menuBuilder.setTitle(_translate("MainWindow", "Builder", None))
        self.actionStartListen_for_connections.setText(_translate("MainWindow", "Connect", None))
        self.actionStopListen_for_connections.setText(_translate("MainWindow", "Disconnect", None))
        self.actionClient_Configuration.setText(_translate("MainWindow", "Settings", None))
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
