# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logViewer.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1098, 643)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/unhide.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(_fromUtf8("background-color: #2c3e50;\n"
"color: #c9f5f7;"))
        self.gridLayout_5 = QtGui.QGridLayout(Form)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.logsTab = QtGui.QTabWidget(Form)
        self.logsTab.setFocusPolicy(QtCore.Qt.NoFocus)
        self.logsTab.setStyleSheet(_fromUtf8("QTabWidget::pane { /* The tab widget frame */\n"
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
        self.logsTab.setMovable(True)
        self.logsTab.setObjectName(_fromUtf8("logsTab"))
        self.screenshotsTab = QtGui.QWidget()
        self.screenshotsTab.setObjectName(_fromUtf8("screenshotsTab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.screenshotsTab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.screenshotsTable = QtGui.QTableWidget(self.screenshotsTab)
        self.screenshotsTable.setFocusPolicy(QtCore.Qt.NoFocus)
        self.screenshotsTable.setStyleSheet(_fromUtf8("QHeaderView::section {\n"
"    background-color: #34495e;\n"
"    padding: 2px;\n"
"    color: #cff7f8;\n"
"    font: 75 10px \"MS Shell Dlg 2\";\n"
"    border: 1px ridge;\n"
"    border-right: none;\n"
"    border-color: #2c3e50;\n"
"}\n"
"\n"
"QTableWidget#screenshotsTable {\n"
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
"QTableWidget#screenshotsTable:item:selected {\n"
"background-color: #2c3e50;\n"
"color: #cff7f8;\n"
"}"))
        self.screenshotsTable.setFrameShadow(QtGui.QFrame.Plain)
        self.screenshotsTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.screenshotsTable.setProperty("showDropIndicator", True)
        self.screenshotsTable.setDragDropOverwriteMode(False)
        self.screenshotsTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.screenshotsTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.screenshotsTable.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.screenshotsTable.setShowGrid(False)
        self.screenshotsTable.setGridStyle(QtCore.Qt.NoPen)
        self.screenshotsTable.setWordWrap(False)
        self.screenshotsTable.setCornerButtonEnabled(False)
        self.screenshotsTable.setObjectName(_fromUtf8("screenshotsTable"))
        self.screenshotsTable.setColumnCount(3)
        self.screenshotsTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.screenshotsTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.screenshotsTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.screenshotsTable.setHorizontalHeaderItem(2, item)
        self.screenshotsTable.horizontalHeader().setCascadingSectionResizes(True)
        self.screenshotsTable.horizontalHeader().setStretchLastSection(True)
        self.screenshotsTable.verticalHeader().setVisible(False)
        self.screenshotsTable.verticalHeader().setCascadingSectionResizes(False)
        self.screenshotsTable.verticalHeader().setDefaultSectionSize(120)
        self.screenshotsTable.verticalHeader().setMinimumSectionSize(120)
        self.gridLayout_2.addWidget(self.screenshotsTable, 0, 0, 1, 1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/mdesktop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logsTab.addTab(self.screenshotsTab, icon1, _fromUtf8(""))
        self.keylogsTab = QtGui.QWidget()
        self.keylogsTab.setObjectName(_fromUtf8("keylogsTab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.keylogsTab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.keylogsTable = QtGui.QTableWidget(self.keylogsTab)
        self.keylogsTable.setFocusPolicy(QtCore.Qt.NoFocus)
        self.keylogsTable.setStyleSheet(_fromUtf8("QHeaderView::section {\n"
"    background-color: #34495e;\n"
"    padding: 2px;\n"
"    color: #cff7f8;\n"
"    font: 75 10px \"MS Shell Dlg 2\";\n"
"    border: 1px ridge;\n"
"    border-right: none;\n"
"    border-color: #2c3e50;\n"
"}\n"
"\n"
"QTableWidget#keylogsTable {\n"
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
"QTableWidget#keylogsTable:item:selected {\n"
"background-color: #2c3e50;\n"
"color: #cff7f8;\n"
"}"))
        self.keylogsTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.keylogsTable.setTabKeyNavigation(False)
        self.keylogsTable.setProperty("showDropIndicator", False)
        self.keylogsTable.setDragDropOverwriteMode(False)
        self.keylogsTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.keylogsTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.keylogsTable.setShowGrid(False)
        self.keylogsTable.setWordWrap(False)
        self.keylogsTable.setCornerButtonEnabled(False)
        self.keylogsTable.setObjectName(_fromUtf8("keylogsTable"))
        self.keylogsTable.setColumnCount(3)
        self.keylogsTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.keylogsTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.keylogsTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.keylogsTable.setHorizontalHeaderItem(2, item)
        self.keylogsTable.horizontalHeader().setStretchLastSection(True)
        self.keylogsTable.verticalHeader().setVisible(False)
        self.gridLayout_3.addWidget(self.keylogsTable, 0, 0, 1, 1)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/mkeylogger.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logsTab.addTab(self.keylogsTab, icon2, _fromUtf8(""))
        self.audioTab = QtGui.QWidget()
        self.audioTab.setObjectName(_fromUtf8("audioTab"))
        self.gridLayout_4 = QtGui.QGridLayout(self.audioTab)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.audioTable = QtGui.QTableWidget(self.audioTab)
        self.audioTable.setFocusPolicy(QtCore.Qt.NoFocus)
        self.audioTable.setStyleSheet(_fromUtf8("QHeaderView::section {\n"
"    background-color: #34495e;\n"
"    padding: 2px;\n"
"    color: #cff7f8;\n"
"    font: 75 10px \"MS Shell Dlg 2\";\n"
"    border: 1px ridge;\n"
"    border-right: none;\n"
"    border-color: #2c3e50;\n"
"}\n"
"\n"
"QTableWidget#audioTable {\n"
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
"QTableWidget#audioTable:item:selected {\n"
"background-color: #2c3e50;\n"
"color: #cff7f8;\n"
"}"))
        self.audioTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.audioTable.setProperty("showDropIndicator", False)
        self.audioTable.setDragDropOverwriteMode(False)
        self.audioTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.audioTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.audioTable.setShowGrid(False)
        self.audioTable.setWordWrap(False)
        self.audioTable.setCornerButtonEnabled(False)
        self.audioTable.setObjectName(_fromUtf8("audioTable"))
        self.audioTable.setColumnCount(4)
        self.audioTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.audioTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.audioTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.audioTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.audioTable.setHorizontalHeaderItem(3, item)
        self.audioTable.horizontalHeader().setStretchLastSection(True)
        self.audioTable.verticalHeader().setVisible(False)
        self.audioTable.verticalHeader().setDefaultSectionSize(80)
        self.gridLayout_4.addWidget(self.audioTable, 0, 0, 1, 1)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/maudio.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logsTab.addTab(self.audioTab, icon3, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.logsTab)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.downloadProgress = QtGui.QProgressBar(Form)
        self.downloadProgress.setEnabled(True)
        self.downloadProgress.setStyleSheet(_fromUtf8("QProgressBar:horizontal {\n"
"border: 1px ridge;\n"
"border-color: #2c3e50;\n"
"background: #34495e;\n"
"padding: 1px;\n"
"text-align: top;\n"
"text-color: #d35400;\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"background: #2c3e50;\n"
"margin-right: 1px;\n"
"width: 5px;\n"
"border-bottom: 8px ridge #16a085;\n"
"}"))
        self.downloadProgress.setProperty("value", 1)
        self.downloadProgress.setObjectName(_fromUtf8("downloadProgress"))
        self.verticalLayout_2.addWidget(self.downloadProgress)
        self.downloadedLabel = QtGui.QLabel(Form)
        self.downloadedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.downloadedLabel.setObjectName(_fromUtf8("downloadedLabel"))
        self.verticalLayout_2.addWidget(self.downloadedLabel)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout_5.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.endTimeLayout = QtGui.QVBoxLayout()
        self.endTimeLayout.setObjectName(_fromUtf8("endTimeLayout"))
        self.clientInformationGroup = QtGui.QGroupBox(Form)
        self.clientInformationGroup.setMaximumSize(QtCore.QSize(300, 16777215))
        self.clientInformationGroup.setStyleSheet(_fromUtf8("background-color: #34495e; \n"
"border: none;\n"
"border: 1px ridge;\n"
"border-color: #2c3e50;\n"
"padding-top: 10px;"))
        self.clientInformationGroup.setObjectName(_fromUtf8("clientInformationGroup"))
        self.gridLayout = QtGui.QGridLayout(self.clientInformationGroup)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.clientAliasLabel = QtGui.QLabel(self.clientInformationGroup)
        self.clientAliasLabel.setMaximumSize(QtCore.QSize(50, 16777215))
        self.clientAliasLabel.setStyleSheet(_fromUtf8("padding: 2px;\n"
"border: none;"))
        self.clientAliasLabel.setObjectName(_fromUtf8("clientAliasLabel"))
        self.horizontalLayout_3.addWidget(self.clientAliasLabel)
        self.clientAliasLine = QtGui.QLineEdit(self.clientInformationGroup)
        self.clientAliasLine.setMaximumSize(QtCore.QSize(200, 16777215))
        self.clientAliasLine.setStyleSheet(_fromUtf8("background: #2c3e50;\n"
"border: none;\n"
"border: 1px ridge;\n"
"border-color: #2c3e50;\n"
"padding: 3px;"))
        self.clientAliasLine.setReadOnly(True)
        self.clientAliasLine.setObjectName(_fromUtf8("clientAliasLine"))
        self.horizontalLayout_3.addWidget(self.clientAliasLine)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.clientIdLabel = QtGui.QLabel(self.clientInformationGroup)
        self.clientIdLabel.setMaximumSize(QtCore.QSize(50, 16777215))
        self.clientIdLabel.setStyleSheet(_fromUtf8("padding: 2px;\n"
"border: none;"))
        self.clientIdLabel.setObjectName(_fromUtf8("clientIdLabel"))
        self.horizontalLayout_2.addWidget(self.clientIdLabel)
        self.clientIdLine = QtGui.QLineEdit(self.clientInformationGroup)
        self.clientIdLine.setMaximumSize(QtCore.QSize(200, 16777215))
        self.clientIdLine.setStyleSheet(_fromUtf8("background: #2c3e50;\n"
"border: none;\n"
"border: 1px ridge;\n"
"border-color: #2c3e50;\n"
"padding: 3px;"))
        self.clientIdLine.setReadOnly(True)
        self.clientIdLine.setObjectName(_fromUtf8("clientIdLine"))
        self.horizontalLayout_2.addWidget(self.clientIdLine)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.clientIpLabel = QtGui.QLabel(self.clientInformationGroup)
        self.clientIpLabel.setMaximumSize(QtCore.QSize(50, 16777215))
        self.clientIpLabel.setStyleSheet(_fromUtf8("padding: 2px;\n"
"border: none;"))
        self.clientIpLabel.setObjectName(_fromUtf8("clientIpLabel"))
        self.horizontalLayout_4.addWidget(self.clientIpLabel)
        self.clientIpLine = QtGui.QLineEdit(self.clientInformationGroup)
        self.clientIpLine.setMaximumSize(QtCore.QSize(200, 16777215))
        self.clientIpLine.setStyleSheet(_fromUtf8("background: #2c3e50;\n"
"border: none;\n"
"border: 1px ridge;\n"
"border-color: #2c3e50;\n"
"padding: 3px;"))
        self.clientIpLine.setReadOnly(True)
        self.clientIpLine.setObjectName(_fromUtf8("clientIpLine"))
        self.horizontalLayout_4.addWidget(self.clientIpLine)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.clientOsLabel = QtGui.QLabel(self.clientInformationGroup)
        self.clientOsLabel.setMaximumSize(QtCore.QSize(50, 16777215))
        self.clientOsLabel.setStyleSheet(_fromUtf8("padding: 2px;\n"
"border: none;"))
        self.clientOsLabel.setObjectName(_fromUtf8("clientOsLabel"))
        self.horizontalLayout_5.addWidget(self.clientOsLabel)
        self.clientOsLine = QtGui.QLineEdit(self.clientInformationGroup)
        self.clientOsLine.setMaximumSize(QtCore.QSize(200, 16777215))
        self.clientOsLine.setStyleSheet(_fromUtf8("background: #2c3e50;\n"
"border: none;\n"
"border: 1px ridge;\n"
"border-color: #2c3e50;\n"
"padding: 3px;"))
        self.clientOsLine.setReadOnly(True)
        self.clientOsLine.setObjectName(_fromUtf8("clientOsLine"))
        self.horizontalLayout_5.addWidget(self.clientOsLine)
        self.gridLayout.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)
        self.endTimeLayout.addWidget(self.clientInformationGroup)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.endTimeLayout.addItem(spacerItem)
        self.downloadGroup = QtGui.QGroupBox(Form)
        self.downloadGroup.setMaximumSize(QtCore.QSize(300, 16777215))
        self.downloadGroup.setStyleSheet(_fromUtf8("background-color: #34495e; \n"
"border: none;\n"
"border: 1px ridge;\n"
"border-color: #2c3e50;\n"
"padding-top: 10px;\n"
"padding-bottom: 10px;"))
        self.downloadGroup.setAlignment(QtCore.Qt.AlignCenter)
        self.downloadGroup.setFlat(False)
        self.downloadGroup.setObjectName(_fromUtf8("downloadGroup"))
        self.gridLayout_6 = QtGui.QGridLayout(self.downloadGroup)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.screenshotCheckLayout = QtGui.QVBoxLayout()
        self.screenshotCheckLayout.setSpacing(0)
        self.screenshotCheckLayout.setObjectName(_fromUtf8("screenshotCheckLayout"))
        self.screenshotsEnableButton = QtGui.QPushButton(self.downloadGroup)
        self.screenshotsEnableButton.setStyleSheet(_fromUtf8("QPushButton#screenshotsEnableButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            border-bottom: none;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#screenshotsEnableButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }\n"
"\n"
"QPushButton#screenshotsEnableButton:checked {\n"
"            border: 3px ridge lime;\n"
"            border-top: none;\n"
"            border-bottom: none;\n"
"            border-radius: 3px;\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.screenshotsEnableButton.setText(_fromUtf8(""))
        self.screenshotsEnableButton.setIcon(icon1)
        self.screenshotsEnableButton.setIconSize(QtCore.QSize(24, 24))
        self.screenshotsEnableButton.setCheckable(True)
        self.screenshotsEnableButton.setChecked(False)
        self.screenshotsEnableButton.setObjectName(_fromUtf8("screenshotsEnableButton"))
        self.screenshotCheckLayout.addWidget(self.screenshotsEnableButton)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.screenshotsCountNewLabel = QtGui.QLabel(self.downloadGroup)
        self.screenshotsCountNewLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.screenshotsCountNewLabel.setMaximumSize(QtCore.QSize(16777215, 14))
        self.screenshotsCountNewLabel.setStyleSheet(_fromUtf8("border: none;\n"
"background: #2c3e50;\n"
"color: #2ecc71;"))
        self.screenshotsCountNewLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.screenshotsCountNewLabel.setObjectName(_fromUtf8("screenshotsCountNewLabel"))
        self.horizontalLayout_6.addWidget(self.screenshotsCountNewLabel)
        self.screenshotsCountSplitterLabel = QtGui.QLabel(self.downloadGroup)
        self.screenshotsCountSplitterLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.screenshotsCountSplitterLabel.setMaximumSize(QtCore.QSize(16777215, 14))
        self.screenshotsCountSplitterLabel.setStyleSheet(_fromUtf8("border: none;\n"
"background: #2c3e50;"))
        self.screenshotsCountSplitterLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.screenshotsCountSplitterLabel.setObjectName(_fromUtf8("screenshotsCountSplitterLabel"))
        self.horizontalLayout_6.addWidget(self.screenshotsCountSplitterLabel)
        self.screenshotsCountOldLabel = QtGui.QLabel(self.downloadGroup)
        self.screenshotsCountOldLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.screenshotsCountOldLabel.setMaximumSize(QtCore.QSize(16777215, 14))
        self.screenshotsCountOldLabel.setStyleSheet(_fromUtf8("border: none;\n"
"background: #2c3e50;\n"
"color: #e74c3c;"))
        self.screenshotsCountOldLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.screenshotsCountOldLabel.setObjectName(_fromUtf8("screenshotsCountOldLabel"))
        self.horizontalLayout_6.addWidget(self.screenshotsCountOldLabel)
        self.screenshotCheckLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout.addLayout(self.screenshotCheckLayout)
        self.keylogsCheckLayout = QtGui.QVBoxLayout()
        self.keylogsCheckLayout.setSpacing(0)
        self.keylogsCheckLayout.setObjectName(_fromUtf8("keylogsCheckLayout"))
        self.keylogsEnableButton = QtGui.QPushButton(self.downloadGroup)
        self.keylogsEnableButton.setStyleSheet(_fromUtf8("QPushButton#keylogsEnableButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            border-bottom: none;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#keylogsEnableButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }\n"
"\n"
"QPushButton#keylogsEnableButton:checked {\n"
"            border: 3px ridge lime;\n"
"            border-top: none;\n"
"            border-bottom: none;\n"
"            border-radius: 3px;\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.keylogsEnableButton.setText(_fromUtf8(""))
        self.keylogsEnableButton.setIcon(icon2)
        self.keylogsEnableButton.setIconSize(QtCore.QSize(24, 24))
        self.keylogsEnableButton.setCheckable(True)
        self.keylogsEnableButton.setChecked(False)
        self.keylogsEnableButton.setObjectName(_fromUtf8("keylogsEnableButton"))
        self.keylogsCheckLayout.addWidget(self.keylogsEnableButton)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.keylogsCountNewLabel = QtGui.QLabel(self.downloadGroup)
        self.keylogsCountNewLabel.setMaximumSize(QtCore.QSize(16777215, 14))
        self.keylogsCountNewLabel.setStyleSheet(_fromUtf8("border: none;\n"
"background: #2c3e50;\n"
"color: #2ecc71;"))
        self.keylogsCountNewLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.keylogsCountNewLabel.setObjectName(_fromUtf8("keylogsCountNewLabel"))
        self.horizontalLayout_7.addWidget(self.keylogsCountNewLabel)
        self.keylogsCountSplitterLabel = QtGui.QLabel(self.downloadGroup)
        self.keylogsCountSplitterLabel.setMaximumSize(QtCore.QSize(16777215, 14))
        self.keylogsCountSplitterLabel.setStyleSheet(_fromUtf8("border: none;\n"
"background: #2c3e50;"))
        self.keylogsCountSplitterLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.keylogsCountSplitterLabel.setObjectName(_fromUtf8("keylogsCountSplitterLabel"))
        self.horizontalLayout_7.addWidget(self.keylogsCountSplitterLabel)
        self.keylogsCountOldLabel = QtGui.QLabel(self.downloadGroup)
        self.keylogsCountOldLabel.setMaximumSize(QtCore.QSize(16777215, 14))
        self.keylogsCountOldLabel.setStyleSheet(_fromUtf8("border: none;\n"
"background: #2c3e50;\n"
"color: #e74c3c;"))
        self.keylogsCountOldLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.keylogsCountOldLabel.setObjectName(_fromUtf8("keylogsCountOldLabel"))
        self.horizontalLayout_7.addWidget(self.keylogsCountOldLabel)
        self.keylogsCheckLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout.addLayout(self.keylogsCheckLayout)
        self.audioCheckLayout = QtGui.QVBoxLayout()
        self.audioCheckLayout.setSpacing(0)
        self.audioCheckLayout.setObjectName(_fromUtf8("audioCheckLayout"))
        self.audioEnableButton = QtGui.QPushButton(self.downloadGroup)
        self.audioEnableButton.setStyleSheet(_fromUtf8("QPushButton#audioEnableButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            border-bottom: none;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#audioEnableButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }\n"
"\n"
"QPushButton#audioEnableButton:checked {\n"
"            border: 3px ridge lime;\n"
"            border-top: none;\n"
"            border-bottom: none;\n"
"            border-radius: 3px;\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.audioEnableButton.setText(_fromUtf8(""))
        self.audioEnableButton.setIcon(icon3)
        self.audioEnableButton.setIconSize(QtCore.QSize(24, 24))
        self.audioEnableButton.setCheckable(True)
        self.audioEnableButton.setChecked(False)
        self.audioEnableButton.setObjectName(_fromUtf8("audioEnableButton"))
        self.audioCheckLayout.addWidget(self.audioEnableButton)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.audioCountNewLabel = QtGui.QLabel(self.downloadGroup)
        self.audioCountNewLabel.setMaximumSize(QtCore.QSize(16777215, 14))
        self.audioCountNewLabel.setStyleSheet(_fromUtf8("border: none;\n"
"background: #2c3e50;\n"
"color: #2ecc71;"))
        self.audioCountNewLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.audioCountNewLabel.setObjectName(_fromUtf8("audioCountNewLabel"))
        self.horizontalLayout_8.addWidget(self.audioCountNewLabel)
        self.audioCountSplitterLabel = QtGui.QLabel(self.downloadGroup)
        self.audioCountSplitterLabel.setMaximumSize(QtCore.QSize(16777215, 14))
        self.audioCountSplitterLabel.setStyleSheet(_fromUtf8("border: none;\n"
"background: #2c3e50;"))
        self.audioCountSplitterLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.audioCountSplitterLabel.setObjectName(_fromUtf8("audioCountSplitterLabel"))
        self.horizontalLayout_8.addWidget(self.audioCountSplitterLabel)
        self.audioCountOldLabel = QtGui.QLabel(self.downloadGroup)
        self.audioCountOldLabel.setMaximumSize(QtCore.QSize(16777215, 14))
        self.audioCountOldLabel.setStyleSheet(_fromUtf8("border: none;\n"
"background: #2c3e50;\n"
"color: #e74c3c;"))
        self.audioCountOldLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.audioCountOldLabel.setObjectName(_fromUtf8("audioCountOldLabel"))
        self.horizontalLayout_8.addWidget(self.audioCountOldLabel)
        self.audioCheckLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout.addLayout(self.audioCheckLayout)
        self.gridLayout_6.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.timeCalendar = QtGui.QCalendarWidget(self.downloadGroup)
        self.timeCalendar.setMinimumSize(QtCore.QSize(280, 200))
        self.timeCalendar.setMaximumSize(QtCore.QSize(280, 200))
        self.timeCalendar.setStyleSheet(_fromUtf8("/* navigation bar */\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar { background-color: #2c3e50; }\n"
"QCalendarWidget QToolButton {\n"
"    height: 16px;\n"
"    padding: 1px;\n"
"    width: 150px;\n"
"    color: #c9f5f7;\n"
"    font-size: 12px;\n"
"    icon-size: 16px, 16px;\n"
"    background-color: #2c3e50;\n"
"    border: none;\n"
"}\n"
"QCalendarWidget QMenu {\n"
"    width: 150px;\n"
"    left: 20px;\n"
"    color: #c9f5f7;\n"
"    font-size: 12px;\n"
"    background-color: #2c3e50;\n"
"}\n"
"QCalendarWidget QSpinBox { \n"
"    width: 150px; \n"
"    font-size:12px; \n"
"    color: white; \n"
"    background-color: #2c3e50;\n"
"    selection-color: #2c3e50;\n"
"}\n"
"QCalendarWidget QSpinBox::up-button { subcontrol-origin: border;  subcontrol-position: top right;  width:12px; }\n"
"QCalendarWidget QSpinBox::down-button {subcontrol-origin: border; subcontrol-position: bottom right;  width:12px;}\n"
"QCalendarWidget QSpinBox::up-arrow { width:12px;  height:12px; }\n"
"QCalendarWidget QSpinBox::down-arrow { width:12px;  height:12px; }\n"
" \n"
"/* header row */\n"
"QCalendarWidget QWidget { alternate-background-color: #34495e; }\n"
" \n"
"/* normal days */\n"
"QCalendarWidget QAbstractItemView:enabled \n"
"{\n"
"    font-size:12px;  \n"
"    color: #c9f5f7; \n"
"    background-color: #2c3e50;\n"
"    selection-background-color: #d35400; \n"
"    selection-color: lime; \n"
"}\n"
" \n"
"/* days in other months */\n"
"QCalendarWidget QAbstractItemView:disabled { color: grey; }"))
        self.timeCalendar.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.timeCalendar.setGridVisible(True)
        self.timeCalendar.setHorizontalHeaderFormat(QtGui.QCalendarWidget.ShortDayNames)
        self.timeCalendar.setVerticalHeaderFormat(QtGui.QCalendarWidget.NoVerticalHeader)
        self.timeCalendar.setNavigationBarVisible(True)
        self.timeCalendar.setDateEditEnabled(True)
        self.timeCalendar.setObjectName(_fromUtf8("timeCalendar"))
        self.gridLayout_6.addWidget(self.timeCalendar, 0, 0, 1, 1)
        self.downloadButton = QtGui.QPushButton(self.downloadGroup)
        self.downloadButton.setMinimumSize(QtCore.QSize(0, 0))
        self.downloadButton.setStyleSheet(_fromUtf8("QPushButton#downloadButton {\n"
"position: relative;\n"
"    padding: 10px 40px;\n"
"    margin: 10px 10px 10px 10px;\n"
"    float: left;\n"
"    border-radius: 4px;\n"
"    font-family: \'Helvetica\', cursive;\n"
"    font-size: 18px;\n"
"    text-decoration: none;  \n"
"    background-color: #2c3e50;\n"
"    border-bottom: 5px solid #232a39; }\n"
"QPushButton#downloadButton::pressed {\n"
"    border-bottom: 1px solid;\n"
"}"))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/download.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.downloadButton.setIcon(icon4)
        self.downloadButton.setIconSize(QtCore.QSize(24, 24))
        self.downloadButton.setObjectName(_fromUtf8("downloadButton"))
        self.gridLayout_6.addWidget(self.downloadButton, 3, 0, 1, 1)
        self.ignoreViewedCheck = QtGui.QPushButton(self.downloadGroup)
        self.ignoreViewedCheck.setStyleSheet(_fromUtf8("QPushButton#ignoreViewedCheck {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            border-bottom: none;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#ignoreViewedCheck:pressed {\n"
"            background-color: #2c3e50;\n"
"            }\n"
"\n"
"QPushButton#ignoreViewedCheck:checked {\n"
"            border: 3px ridge lime;\n"
"            border-top: none;\n"
"            border-bottom: none;\n"
"            border-radius: 3px;\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.ignoreViewedCheck.setCheckable(True)
        self.ignoreViewedCheck.setChecked(True)
        self.ignoreViewedCheck.setObjectName(_fromUtf8("ignoreViewedCheck"))
        self.gridLayout_6.addWidget(self.ignoreViewedCheck, 2, 0, 1, 1)
        self.endTimeLayout.addWidget(self.downloadGroup)
        self.verticalLayout.addLayout(self.endTimeLayout)
        self.gridLayout_5.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.retranslateUi(Form)
        self.logsTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Moderat Log Viewer", None))
        item = self.screenshotsTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Preview", None))
        item = self.screenshotsTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Info", None))
        item = self.screenshotsTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "path", None))
        self.logsTab.setTabText(self.logsTab.indexOf(self.screenshotsTab), _translate("Form", "Screenshots", None))
        item = self.keylogsTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Date", None))
        item = self.keylogsTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Logs", None))
        item = self.keylogsTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "path", None))
        self.logsTab.setTabText(self.logsTab.indexOf(self.keylogsTab), _translate("Form", "Keylogs", None))
        item = self.audioTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Duration", None))
        item = self.audioTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Spectrum", None))
        item = self.audioTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Date Time", None))
        item = self.audioTable.horizontalHeaderItem(3)
        item.setText(_translate("Form", "path", None))
        self.logsTab.setTabText(self.logsTab.indexOf(self.audioTab), _translate("Form", "Audio", None))
        self.downloadedLabel.setText(_translate("Form", "Downloaded Na Na/Na", None))
        self.clientInformationGroup.setTitle(_translate("Form", "Client Information", None))
        self.clientAliasLabel.setText(_translate("Form", "Alias: ", None))
        self.clientIdLabel.setText(_translate("Form", "ID: ", None))
        self.clientIpLabel.setText(_translate("Form", "IP: ", None))
        self.clientOsLabel.setText(_translate("Form", "OS: ", None))
        self.downloadGroup.setTitle(_translate("Form", "Download Logs", None))
        self.screenshotsCountNewLabel.setText(_translate("Form", "0", None))
        self.screenshotsCountSplitterLabel.setText(_translate("Form", "/", None))
        self.screenshotsCountOldLabel.setText(_translate("Form", "0", None))
        self.keylogsCountNewLabel.setText(_translate("Form", "0", None))
        self.keylogsCountSplitterLabel.setText(_translate("Form", "/", None))
        self.keylogsCountOldLabel.setText(_translate("Form", "0", None))
        self.audioCountNewLabel.setText(_translate("Form", "0", None))
        self.audioCountSplitterLabel.setText(_translate("Form", "/", None))
        self.audioCountOldLabel.setText(_translate("Form", "0", None))
        self.downloadButton.setText(_translate("Form", "Download", None))
        self.ignoreViewedCheck.setText(_translate("Form", "Ignore Viewed", None))

import res_rc
