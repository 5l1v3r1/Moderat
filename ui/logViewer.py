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
        Form.resize(1098, 607)
        Form.setStyleSheet(_fromUtf8("background-color: #2c3e50;\n"
"color: #c9f5f7;"))
        self.gridLayout_5 = QtGui.QGridLayout(Form)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setStyleSheet(_fromUtf8("QTabWidget::pane { /* The tab widget frame */\n"
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
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.screenshotsTab = QtGui.QWidget()
        self.screenshotsTab.setObjectName(_fromUtf8("screenshotsTab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.screenshotsTab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.screenshotsTable = QtGui.QTableWidget(self.screenshotsTab)
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
"}\n"
"\n"
"QTableWidget#screenshotsTable:item:selected {\n"
"background-color: #2c3e50;\n"
"color: #cff7f8;\n"
"}"))
        self.screenshotsTable.setObjectName(_fromUtf8("screenshotsTable"))
        self.screenshotsTable.setColumnCount(3)
        self.screenshotsTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.screenshotsTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.screenshotsTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.screenshotsTable.setHorizontalHeaderItem(2, item)
        self.screenshotsTable.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.screenshotsTable, 0, 0, 1, 1)
        self.tabWidget.addTab(self.screenshotsTab, _fromUtf8(""))
        self.keylogsTab = QtGui.QWidget()
        self.keylogsTab.setObjectName(_fromUtf8("keylogsTab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.keylogsTab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.keylogsTable = QtGui.QTableWidget(self.keylogsTab)
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
"}\n"
"\n"
"QTableWidget#keylogsTable:item:selected {\n"
"background-color: #2c3e50;\n"
"color: #cff7f8;\n"
"}"))
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
        self.gridLayout_3.addWidget(self.keylogsTable, 0, 0, 1, 1)
        self.tabWidget.addTab(self.keylogsTab, _fromUtf8(""))
        self.audioTab = QtGui.QWidget()
        self.audioTab.setObjectName(_fromUtf8("audioTab"))
        self.gridLayout_4 = QtGui.QGridLayout(self.audioTab)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.audioTable = QtGui.QTableWidget(self.audioTab)
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
"}\n"
"\n"
"QTableWidget#audioTable:item:selected {\n"
"background-color: #2c3e50;\n"
"color: #cff7f8;\n"
"}"))
        self.audioTable.setObjectName(_fromUtf8("audioTable"))
        self.audioTable.setColumnCount(2)
        self.audioTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.audioTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.audioTable.setHorizontalHeaderItem(1, item)
        self.audioTable.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_4.addWidget(self.audioTable, 0, 0, 1, 1)
        self.tabWidget.addTab(self.audioTab, _fromUtf8(""))
        self.gridLayout_5.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.endTimeLayout = QtGui.QVBoxLayout()
        self.endTimeLayout.setObjectName(_fromUtf8("endTimeLayout"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox.setStyleSheet(_fromUtf8("background-color: #34495e; \n"
"border: none;\n"
"border: 1px ridge;\n"
"border-color: #2c3e50;\n"
"padding-top: 10px;"))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.clientAliasLabel = QtGui.QLabel(self.groupBox)
        self.clientAliasLabel.setMaximumSize(QtCore.QSize(50, 16777215))
        self.clientAliasLabel.setStyleSheet(_fromUtf8("padding: 2px;\n"
"border: none;"))
        self.clientAliasLabel.setObjectName(_fromUtf8("clientAliasLabel"))
        self.horizontalLayout_3.addWidget(self.clientAliasLabel)
        self.clientAliasLine = QtGui.QLineEdit(self.groupBox)
        self.clientAliasLine.setMaximumSize(QtCore.QSize(200, 16777215))
        self.clientAliasLine.setStyleSheet(_fromUtf8("background-color: #34495e; \n"
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
        self.clientIdLabel = QtGui.QLabel(self.groupBox)
        self.clientIdLabel.setMaximumSize(QtCore.QSize(50, 16777215))
        self.clientIdLabel.setStyleSheet(_fromUtf8("padding: 2px;\n"
"border: none;"))
        self.clientIdLabel.setObjectName(_fromUtf8("clientIdLabel"))
        self.horizontalLayout_2.addWidget(self.clientIdLabel)
        self.clientIdLine = QtGui.QLineEdit(self.groupBox)
        self.clientIdLine.setMaximumSize(QtCore.QSize(200, 16777215))
        self.clientIdLine.setStyleSheet(_fromUtf8("background-color: #34495e; \n"
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
        self.clientIpLabel = QtGui.QLabel(self.groupBox)
        self.clientIpLabel.setMaximumSize(QtCore.QSize(50, 16777215))
        self.clientIpLabel.setStyleSheet(_fromUtf8("padding: 2px;\n"
"border: none;"))
        self.clientIpLabel.setObjectName(_fromUtf8("clientIpLabel"))
        self.horizontalLayout_4.addWidget(self.clientIpLabel)
        self.clientIpLine = QtGui.QLineEdit(self.groupBox)
        self.clientIpLine.setMaximumSize(QtCore.QSize(200, 16777215))
        self.clientIpLine.setStyleSheet(_fromUtf8("background-color: #34495e; \n"
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
        self.clientOsLabel = QtGui.QLabel(self.groupBox)
        self.clientOsLabel.setMaximumSize(QtCore.QSize(50, 16777215))
        self.clientOsLabel.setStyleSheet(_fromUtf8("padding: 2px;\n"
"border: none;"))
        self.clientOsLabel.setObjectName(_fromUtf8("clientOsLabel"))
        self.horizontalLayout_5.addWidget(self.clientOsLabel)
        self.clientOsLine = QtGui.QLineEdit(self.groupBox)
        self.clientOsLine.setMaximumSize(QtCore.QSize(200, 16777215))
        self.clientOsLine.setStyleSheet(_fromUtf8("background-color: #34495e; \n"
"border: none;\n"
"border: 1px ridge;\n"
"border-color: #2c3e50;\n"
"padding: 3px;"))
        self.clientOsLine.setReadOnly(True)
        self.clientOsLine.setObjectName(_fromUtf8("clientOsLine"))
        self.horizontalLayout_5.addWidget(self.clientOsLine)
        self.gridLayout.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)
        self.endTimeLayout.addWidget(self.groupBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.endTimeLayout.addItem(spacerItem)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox_2.setStyleSheet(_fromUtf8("background-color: #34495e; \n"
"border: none;\n"
"border: 1px ridge;\n"
"border-color: #2c3e50;\n"
"padding-top: 10px;\n"
"padding-bottom: 10px;"))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.screenshotCheckLayout = QtGui.QVBoxLayout()
        self.screenshotCheckLayout.setSpacing(3)
        self.screenshotCheckLayout.setObjectName(_fromUtf8("screenshotCheckLayout"))
        self.screenshotsEnableButton = QtGui.QPushButton(self.groupBox_2)
        self.screenshotsEnableButton.setStyleSheet(_fromUtf8("QPushButton#screenshotsEnableButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#screenshotsEnableButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }\n"
"\n"
"QPushButton#screenshotsEnableButton:checked {\n"
"            border-color: lime;\n"
"            }"))
        self.screenshotsEnableButton.setCheckable(True)
        self.screenshotsEnableButton.setChecked(False)
        self.screenshotsEnableButton.setObjectName(_fromUtf8("screenshotsEnableButton"))
        self.screenshotCheckLayout.addWidget(self.screenshotsEnableButton)
        self.screenshotsCountLabel = QtGui.QLabel(self.groupBox_2)
        self.screenshotsCountLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.screenshotsCountLabel.setMaximumSize(QtCore.QSize(16777215, 14))
        self.screenshotsCountLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.screenshotsCountLabel.setObjectName(_fromUtf8("screenshotsCountLabel"))
        self.screenshotCheckLayout.addWidget(self.screenshotsCountLabel)
        self.horizontalLayout.addLayout(self.screenshotCheckLayout)
        self.keylogsCheckLayout = QtGui.QVBoxLayout()
        self.keylogsCheckLayout.setSpacing(3)
        self.keylogsCheckLayout.setObjectName(_fromUtf8("keylogsCheckLayout"))
        self.keylogsEnableButton = QtGui.QPushButton(self.groupBox_2)
        self.keylogsEnableButton.setStyleSheet(_fromUtf8("QPushButton#keylogsEnableButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#keylogsEnableButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }\n"
"\n"
"QPushButton#keylogsEnableButton:checked {\n"
"            border-color: lime;\n"
"            }"))
        self.keylogsEnableButton.setCheckable(True)
        self.keylogsEnableButton.setChecked(False)
        self.keylogsEnableButton.setObjectName(_fromUtf8("keylogsEnableButton"))
        self.keylogsCheckLayout.addWidget(self.keylogsEnableButton)
        self.keylogsCountLabel = QtGui.QLabel(self.groupBox_2)
        self.keylogsCountLabel.setMaximumSize(QtCore.QSize(16777215, 14))
        self.keylogsCountLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.keylogsCountLabel.setObjectName(_fromUtf8("keylogsCountLabel"))
        self.keylogsCheckLayout.addWidget(self.keylogsCountLabel)
        self.horizontalLayout.addLayout(self.keylogsCheckLayout)
        self.audioCheckLayout = QtGui.QVBoxLayout()
        self.audioCheckLayout.setSpacing(3)
        self.audioCheckLayout.setObjectName(_fromUtf8("audioCheckLayout"))
        self.audioEnableButton = QtGui.QPushButton(self.groupBox_2)
        self.audioEnableButton.setStyleSheet(_fromUtf8("QPushButton#audioEnableButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#audioEnableButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }\n"
"\n"
"QPushButton#audioEnableButton:checked {\n"
"            border-color: lime;\n"
"            }"))
        self.audioEnableButton.setCheckable(True)
        self.audioEnableButton.setChecked(False)
        self.audioEnableButton.setObjectName(_fromUtf8("audioEnableButton"))
        self.audioCheckLayout.addWidget(self.audioEnableButton)
        self.audioCountLabel = QtGui.QLabel(self.groupBox_2)
        self.audioCountLabel.setMaximumSize(QtCore.QSize(16777215, 14))
        self.audioCountLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.audioCountLabel.setObjectName(_fromUtf8("audioCountLabel"))
        self.audioCheckLayout.addWidget(self.audioCountLabel)
        self.horizontalLayout.addLayout(self.audioCheckLayout)
        self.gridLayout_6.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(True)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_6.addWidget(self.pushButton, 2, 0, 1, 1)
        self.timeCalendar = QtGui.QCalendarWidget(self.groupBox_2)
        self.timeCalendar.setMaximumSize(QtCore.QSize(280, 180))
        self.timeCalendar.setStyleSheet(_fromUtf8("/* navigation bar */\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar { background-color: #2c3e50; }\n"
"QCalendarWidget QToolButton {\n"
"    height: 12px;\n"
"    width: 150px;\n"
"    color: #c9f5f7;\n"
"    font-size: 12px;\n"
"    icon-size: 16px, 16px;\n"
"    background-color: #2c3e50;\n"
"    border: 1px ridge #2c3e50;\n"
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
"    font-size:24px; \n"
"    color: white; \n"
"    background-color: #2c3e50;\n"
"    selection-color: #2c3e50;\n"
"}\n"
"QCalendarWidget QSpinBox::up-button { subcontrol-origin: border;  subcontrol-position: top right;  width:65px; }\n"
"QCalendarWidget QSpinBox::down-button {subcontrol-origin: border; subcontrol-position: bottom right;  width:65px;}\n"
"QCalendarWidget QSpinBox::up-arrow { width:56px;  height:56px; }\n"
"QCalendarWidget QSpinBox::down-arrow { width:56px;  height:56px; }\n"
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
        self.downloadButton = QtGui.QPushButton(self.groupBox_2)
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
"    background-color: #34495e;\n"
"    border-bottom: 5px solid #232a39; }\n"
"QPushButton#downloadButton::pressed {\n"
"    border-bottom: 1px solid;\n"
"}"))
        self.downloadButton.setObjectName(_fromUtf8("downloadButton"))
        self.gridLayout_6.addWidget(self.downloadButton, 3, 0, 1, 1)
        self.endTimeLayout.addWidget(self.groupBox_2)
        self.verticalLayout.addLayout(self.endTimeLayout)
        self.gridLayout_5.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        item = self.screenshotsTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Preview", None))
        item = self.screenshotsTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Window Title", None))
        item = self.screenshotsTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Date Time", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.screenshotsTab), _translate("Form", "Screenshots", None))
        item = self.keylogsTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Date", None))
        item = self.keylogsTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Window Title", None))
        item = self.keylogsTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Logs", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.keylogsTab), _translate("Form", "Keylogs", None))
        item = self.audioTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Duration", None))
        item = self.audioTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Date", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.audioTab), _translate("Form", "Audio", None))
        self.groupBox.setTitle(_translate("Form", "Client Information", None))
        self.clientAliasLabel.setText(_translate("Form", "Alias: ", None))
        self.clientIdLabel.setText(_translate("Form", "ID: ", None))
        self.clientIpLabel.setText(_translate("Form", "IP: ", None))
        self.clientOsLabel.setText(_translate("Form", "OS: ", None))
        self.groupBox_2.setTitle(_translate("Form", "Download Logs", None))
        self.screenshotsEnableButton.setText(_translate("Form", "Screenshots", None))
        self.screenshotsCountLabel.setText(_translate("Form", "0/0", None))
        self.keylogsEnableButton.setText(_translate("Form", "Keylogs", None))
        self.keylogsCountLabel.setText(_translate("Form", "0/0", None))
        self.audioEnableButton.setText(_translate("Form", "Audio", None))
        self.audioCountLabel.setText(_translate("Form", "0/0", None))
        self.pushButton.setText(_translate("Form", "Ignore Viewed", None))
        self.downloadButton.setText(_translate("Form", "Download", None))

