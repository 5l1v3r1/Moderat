# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
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
        Form.resize(400, 207)
        Form.setMinimumSize(QtCore.QSize(400, 207))
        Form.setMaximumSize(QtCore.QSize(400, 207))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/settings.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setWindowOpacity(1.0)
        Form.setStyleSheet(_fromUtf8("background-color: #2c3e50;\n"
"color: #c9f5f7;"))
        self.gridLayout_2 = QtGui.QGridLayout(Form)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.settingsTab = QtGui.QTabWidget(Form)
        self.settingsTab.setStyleSheet(_fromUtf8("QTabBar::tab {\n"
"padding: 5px;\n"
"margin-left: 2px;\n"
"border: 1px ridge;\n"
"border-color: #2c3e50;\n"
"background-color: #34495e;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"background-color: #2c3e50;\n"
"border-bottom: none;\n"
"}\n"
"\n"
"QTabBar::pane {\n"
"background-color: #fff;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"color: rgb(246, 246, 244);\n"
"margin: 0px,1px,1px,1px;\n"
"border: 1px ridge;\n"
"border-color: #2c3e50;\n"
"background-color: #fff;\n"
"background-position: center;\n"
"}"))
        self.settingsTab.setTabPosition(QtGui.QTabWidget.North)
        self.settingsTab.setMovable(True)
        self.settingsTab.setObjectName(_fromUtf8("settingsTab"))
        self.connectionTab = QtGui.QWidget()
        self.connectionTab.setObjectName(_fromUtf8("connectionTab"))
        self.gridLayout = QtGui.QGridLayout(self.connectionTab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.line = QtGui.QFrame(self.connectionTab)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.ipAddressLabel = QtGui.QLabel(self.connectionTab)
        self.ipAddressLabel.setMinimumSize(QtCore.QSize(150, 0))
        self.ipAddressLabel.setObjectName(_fromUtf8("ipAddressLabel"))
        self.horizontalLayout.addWidget(self.ipAddressLabel)
        self.ipAddressLine = QtGui.QLineEdit(self.connectionTab)
        self.ipAddressLine.setStyleSheet(_fromUtf8("background-color: #34495e; \n"
"border: none;\n"
"border: 1px ridge;\n"
"border-color: #2c3e50;"))
        self.ipAddressLine.setObjectName(_fromUtf8("ipAddressLine"))
        self.horizontalLayout.addWidget(self.ipAddressLine)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.portLabel = QtGui.QLabel(self.connectionTab)
        self.portLabel.setMinimumSize(QtCore.QSize(150, 0))
        self.portLabel.setObjectName(_fromUtf8("portLabel"))
        self.horizontalLayout_2.addWidget(self.portLabel)
        self.portLine = QtGui.QLineEdit(self.connectionTab)
        self.portLine.setStyleSheet(_fromUtf8("background-color: #34495e; \n"
"border: none;\n"
"border: 1px ridge;\n"
"border-color: #2c3e50;"))
        self.portLine.setObjectName(_fromUtf8("portLine"))
        self.horizontalLayout_2.addWidget(self.portLine)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.usernameLabel = QtGui.QLabel(self.connectionTab)
        self.usernameLabel.setMinimumSize(QtCore.QSize(150, 0))
        self.usernameLabel.setObjectName(_fromUtf8("usernameLabel"))
        self.horizontalLayout_3.addWidget(self.usernameLabel)
        self.usernameEntry = QtGui.QLineEdit(self.connectionTab)
        self.usernameEntry.setStyleSheet(_fromUtf8("background-color: #34495e; \n"
"border: none;\n"
"border: 1px ridge;\n"
"border-color: #2c3e50;"))
        self.usernameEntry.setObjectName(_fromUtf8("usernameEntry"))
        self.horizontalLayout_3.addWidget(self.usernameEntry)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.settingsTab.addTab(self.connectionTab, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.settingsTab, 0, 1, 1, 1)
        self.saveButton = QtGui.QPushButton(Form)
        self.saveButton.setMinimumSize(QtCore.QSize(0, 30))
        self.saveButton.setStyleSheet(_fromUtf8("QPushButton#saveButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            border-left: none;\n"
"            }\n"
"\n"
"QPushButton#saveButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.gridLayout_2.addWidget(self.saveButton, 1, 0, 1, 2)

        self.retranslateUi(Form)
        self.settingsTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "ModeRat Settings", None))
        self.ipAddressLabel.setText(_translate("Form", "Ip Address:", None))
        self.portLabel.setText(_translate("Form", "Port:", None))
        self.usernameLabel.setText(_translate("Form", "Username:", None))
        self.settingsTab.setTabText(self.settingsTab.indexOf(self.connectionTab), _translate("Form", "Connection Settings", None))
        self.saveButton.setText(_translate("Form", "Save", None))

import res_rc
