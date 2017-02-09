# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'p2p_ui.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(412, 300)
        Dialog.setMinimumSize(QtCore.QSize(412, 300))
        Dialog.setMaximumSize(QtCore.QSize(412, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(_fromUtf8("background-color: #2c3e50;\n"
"color: #c9f5f7;"))
        self.gridLayout_3 = QtGui.QGridLayout(Dialog)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.portGroup = QtGui.QGroupBox(Dialog)
        self.portGroup.setStyleSheet(_fromUtf8("background-color: #34495e;\n"
"border: 1px solid #2c3e50;"))
        self.portGroup.setTitle(_fromUtf8(""))
        self.portGroup.setObjectName(_fromUtf8("portGroup"))
        self.gridLayout_2 = QtGui.QGridLayout(self.portGroup)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.portLine = QtGui.QLineEdit(self.portGroup)
        self.portLine.setMinimumSize(QtCore.QSize(0, 34))
        self.portLine.setStyleSheet(_fromUtf8("background-color: #455F7A;\n"
"padding: 5px;"))
        self.portLine.setEchoMode(QtGui.QLineEdit.Normal)
        self.portLine.setObjectName(_fromUtf8("portLine"))
        self.horizontalLayout_3.addWidget(self.portLine)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.portGroup, 1, 0, 1, 1)
        self.ipaddressGroup = QtGui.QGroupBox(Dialog)
        self.ipaddressGroup.setStyleSheet(_fromUtf8("background-color: #34495e;\n"
"border: 1px solid #2c3e50;"))
        self.ipaddressGroup.setTitle(_fromUtf8(""))
        self.ipaddressGroup.setObjectName(_fromUtf8("ipaddressGroup"))
        self.gridLayout = QtGui.QGridLayout(self.ipaddressGroup)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.ipaddressLine = QtGui.QLineEdit(self.ipaddressGroup)
        self.ipaddressLine.setMinimumSize(QtCore.QSize(0, 34))
        self.ipaddressLine.setStyleSheet(_fromUtf8("background-color: #455F7A;\n"
"padding: 5px;\n"
"border-right: none;"))
        self.ipaddressLine.setText(_fromUtf8(""))
        self.ipaddressLine.setObjectName(_fromUtf8("ipaddressLine"))
        self.horizontalLayout_2.addWidget(self.ipaddressLine)
        self.internalIpButton = QtGui.QPushButton(self.ipaddressGroup)
        self.internalIpButton.setMinimumSize(QtCore.QSize(0, 34))
        self.internalIpButton.setStyleSheet(_fromUtf8("background-color: #455F7A;\n"
"padding: 5px;\n"
"border-left: none;\n"
"border-right: none;"))
        self.internalIpButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/lan.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.internalIpButton.setIcon(icon1)
        self.internalIpButton.setIconSize(QtCore.QSize(20, 20))
        self.internalIpButton.setObjectName(_fromUtf8("internalIpButton"))
        self.horizontalLayout_2.addWidget(self.internalIpButton)
        self.externalIpButton = QtGui.QPushButton(self.ipaddressGroup)
        self.externalIpButton.setMinimumSize(QtCore.QSize(0, 34))
        self.externalIpButton.setStyleSheet(_fromUtf8("background-color: #455F7A;\n"
"padding: 5px;\n"
"border-left: none;"))
        self.externalIpButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/wan.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.externalIpButton.setIcon(icon2)
        self.externalIpButton.setIconSize(QtCore.QSize(20, 20))
        self.externalIpButton.setObjectName(_fromUtf8("externalIpButton"))
        self.horizontalLayout_2.addWidget(self.externalIpButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.ipaddressGroup, 0, 0, 1, 1)
        self.messageGroup = QtGui.QGroupBox(Dialog)
        self.messageGroup.setStyleSheet(_fromUtf8("background-color: #34495e;\n"
"border: 1px solid #2c3e50;"))
        self.messageGroup.setTitle(_fromUtf8(""))
        self.messageGroup.setObjectName(_fromUtf8("messageGroup"))
        self.gridLayout_4 = QtGui.QGridLayout(self.messageGroup)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.messageText = QtGui.QTextEdit(self.messageGroup)
        self.messageText.setStyleSheet(_fromUtf8("background-color: #455F7A;\n"
"padding: 5px;"))
        self.messageText.setObjectName(_fromUtf8("messageText"))
        self.gridLayout_4.addWidget(self.messageText, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.messageGroup, 2, 0, 1, 1)
        self.connectP2pButton = QtGui.QPushButton(Dialog)
        self.connectP2pButton.setStyleSheet(_fromUtf8("QPushButton#connectP2pButton {\n"
"            background-color: #27ae60;\n"
"            font: 14pt \"MS Shell Dlg 2\";\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 15px;\n"
"            margin: 0px;\n"
"            }\n"
"\n"
"QPushButton#connectP2pButton:pressed {\n"
"            background-color: #2ecc71;\n"
"            }"))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/connect.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.connectP2pButton.setIcon(icon3)
        self.connectP2pButton.setIconSize(QtCore.QSize(20, 20))
        self.connectP2pButton.setObjectName(_fromUtf8("connectP2pButton"))
        self.gridLayout_3.addWidget(self.connectP2pButton, 4, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 3, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.ipaddressLine, self.portLine)
        Dialog.setTabOrder(self.portLine, self.messageText)
        Dialog.setTabOrder(self.messageText, self.connectP2pButton)
        Dialog.setTabOrder(self.connectP2pButton, self.internalIpButton)
        Dialog.setTabOrder(self.internalIpButton, self.externalIpButton)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Direct Connetion", None))
        self.portLine.setText(_translate("Dialog", "5545", None))
        self.portLine.setPlaceholderText(_translate("Dialog", "Port", None))
        self.ipaddressLine.setPlaceholderText(_translate("Dialog", "IP Address", None))
        self.connectP2pButton.setText(_translate("Dialog", "Connect", None))

