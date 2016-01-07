# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
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
        Form.resize(255, 41)
        Form.setMinimumSize(QtCore.QSize(255, 41))
        Form.setMaximumSize(QtCore.QSize(255, 41))
        Form.setStyleSheet(_fromUtf8("background-color: #0F2D40;"))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.listenButton = QtGui.QPushButton(Form)
        self.listenButton.setMinimumSize(QtCore.QSize(0, 24))
        self.listenButton.setStyleSheet(_fromUtf8("QPushButton#listenButton {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            padding-right: 5px;\n"
"            color: white;\n"
"            text-decoration: none;\n"
"            background-color: #225E75\n"
"            }\n"
"\n"
"QPushButton#listenButton:pressed {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #112F3B, stop:1 #1B4C5E);\n"
"            }"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/assets/play.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.listenButton.setIcon(icon)
        self.listenButton.setObjectName(_fromUtf8("listenButton"))
        self.gridLayout.addWidget(self.listenButton, 0, 0, 1, 1)
        self.recordButton = QtGui.QPushButton(Form)
        self.recordButton.setMinimumSize(QtCore.QSize(0, 24))
        self.recordButton.setStyleSheet(_fromUtf8("QPushButton#recordButton {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            padding-right: 5px;\n"
"            color: white;\n"
"            text-decoration: none;\n"
"            background-color: #225E75\n"
"            }\n"
"\n"
"QPushButton#recordButton:pressed {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #112F3B, stop:1 #1B4C5E);\n"
"            }"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/assets/record.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.recordButton.setIcon(icon1)
        self.recordButton.setObjectName(_fromUtf8("recordButton"))
        self.gridLayout.addWidget(self.recordButton, 0, 1, 1, 1)
        self.stopButton = QtGui.QPushButton(Form)
        self.stopButton.setMinimumSize(QtCore.QSize(0, 24))
        self.stopButton.setStyleSheet(_fromUtf8("QPushButton#stopButton {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            padding-right: 5px;\n"
"            color: white;\n"
"            text-decoration: none;\n"
"            background-color: #225E75\n"
"            }\n"
"\n"
"QPushButton#stopButton:pressed {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #112F3B, stop:1 #1B4C5E);\n"
"            }"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/assets/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopButton.setIcon(icon2)
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.gridLayout.addWidget(self.stopButton, 0, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Audio Streaming", None))
        self.listenButton.setText(_translate("Form", "Listen", None))
        self.recordButton.setText(_translate("Form", "Record", None))
        self.stopButton.setText(_translate("Form", "Stop", None))

import res_rc
