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
        Form.resize(400, 188)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/settings.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setWindowOpacity(1.0)
        Form.setStyleSheet(_fromUtf8("background-color: #2c3e50;\n"
"color: #bdc3c7;"))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
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
        self.gridLayout.addWidget(self.saveButton, 5, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.timeoutLabel = QtGui.QLabel(Form)
        self.timeoutLabel.setMinimumSize(QtCore.QSize(150, 0))
        self.timeoutLabel.setObjectName(_fromUtf8("timeoutLabel"))
        self.horizontalLayout_3.addWidget(self.timeoutLabel)
        self.timeoutLine = QtGui.QLineEdit(Form)
        self.timeoutLine.setStyleSheet(_fromUtf8("background-color: #34495e; \n"
"border: none;\n"
"border: 1px ridge;\n"
"border-color: #2c3e50;"))
        self.timeoutLine.setObjectName(_fromUtf8("timeoutLine"))
        self.horizontalLayout_3.addWidget(self.timeoutLine)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.ipAddressLabel = QtGui.QLabel(Form)
        self.ipAddressLabel.setMinimumSize(QtCore.QSize(150, 0))
        self.ipAddressLabel.setObjectName(_fromUtf8("ipAddressLabel"))
        self.horizontalLayout.addWidget(self.ipAddressLabel)
        self.ipAddressLine = QtGui.QLineEdit(Form)
        self.ipAddressLine.setStyleSheet(_fromUtf8("background-color: #34495e; \n"
"border: none;\n"
"border: 1px ridge;\n"
"border-color: #2c3e50;"))
        self.ipAddressLine.setObjectName(_fromUtf8("ipAddressLine"))
        self.horizontalLayout.addWidget(self.ipAddressLine)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.portLabel = QtGui.QLabel(Form)
        self.portLabel.setMinimumSize(QtCore.QSize(150, 0))
        self.portLabel.setObjectName(_fromUtf8("portLabel"))
        self.horizontalLayout_2.addWidget(self.portLabel)
        self.portLine = QtGui.QLineEdit(Form)
        self.portLine.setStyleSheet(_fromUtf8("background-color: #34495e; \n"
"border: none;\n"
"border: 1px ridge;\n"
"border-color: #2c3e50;"))
        self.portLine.setObjectName(_fromUtf8("portLine"))
        self.horizontalLayout_2.addWidget(self.portLine)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.maxConnectionsLabel = QtGui.QLabel(Form)
        self.maxConnectionsLabel.setMinimumSize(QtCore.QSize(150, 0))
        self.maxConnectionsLabel.setObjectName(_fromUtf8("maxConnectionsLabel"))
        self.horizontalLayout_4.addWidget(self.maxConnectionsLabel)
        self.maxConnectionsLine = QtGui.QLineEdit(Form)
        self.maxConnectionsLine.setStyleSheet(_fromUtf8("background-color: #34495e; \n"
"border: none;\n"
"border: 1px ridge;\n"
"border-color: #2c3e50;"))
        self.maxConnectionsLine.setObjectName(_fromUtf8("maxConnectionsLine"))
        self.horizontalLayout_4.addWidget(self.maxConnectionsLine)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "ModeRat Settings", None))
        self.saveButton.setText(_translate("Form", "Save", None))
        self.timeoutLabel.setText(_translate("Form", "Connection Timeout:", None))
        self.ipAddressLabel.setText(_translate("Form", "Ip Address:", None))
        self.portLabel.setText(_translate("Form", "Port:", None))
        self.maxConnectionsLabel.setText(_translate("Form", "Maximum Connections:", None))

