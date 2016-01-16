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
        Form.resize(491, 370)
        Form.setStyleSheet(_fromUtf8("background-color: #0F2D40;\n"
"color: #2ecc71;"))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.startStreamingButton = QtGui.QPushButton(Form)
        self.startStreamingButton.setMinimumSize(QtCore.QSize(0, 24))
        self.startStreamingButton.setStyleSheet(_fromUtf8("QPushButton#startStreamingButton {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            padding-right: 5px;\n"
"            color: white;\n"
"            text-decoration: none;\n"
"            background-color: #225E75\n"
"            }\n"
"\n"
"QPushButton#startStreamingButton:checked {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            color: grey;\n"
"            border-color: #0F2D40;\n"
"            background-color:#1B4C5E;\n"
"            }"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/assets/start.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startStreamingButton.setIcon(icon)
        self.startStreamingButton.setIconSize(QtCore.QSize(18, 18))
        self.startStreamingButton.setCheckable(True)
        self.startStreamingButton.setObjectName(_fromUtf8("startStreamingButton"))
        self.gridLayout.addWidget(self.startStreamingButton, 0, 0, 1, 1)
        self.stopStreamingButton = QtGui.QPushButton(Form)
        self.stopStreamingButton.setMinimumSize(QtCore.QSize(0, 24))
        self.stopStreamingButton.setStyleSheet(_fromUtf8("QPushButton#stopStreamingButton {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            padding-right: 5px;\n"
"            color: white;\n"
"            text-decoration: none;\n"
"            background-color: #225E75\n"
"            }\n"
"\n"
"QPushButton#stopStreamingButton:checked {\n"
"            background: #194759;\n"
"            color: grey;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            background-color:#1B4C5E;\n"
"            }"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/assets/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopStreamingButton.setIcon(icon1)
        self.stopStreamingButton.setCheckable(True)
        self.stopStreamingButton.setChecked(True)
        self.stopStreamingButton.setObjectName(_fromUtf8("stopStreamingButton"))
        self.gridLayout.addWidget(self.stopStreamingButton, 0, 1, 1, 1)
        self.alwaysTopButton = QtGui.QPushButton(Form)
        self.alwaysTopButton.setMinimumSize(QtCore.QSize(0, 24))
        self.alwaysTopButton.setStyleSheet(_fromUtf8("QPushButton#alwaysTopButton {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            padding-right: 5px;\n"
"            color: white;\n"
"            text-decoration: none;\n"
"            background-color: #225E75\n"
"            }\n"
"\n"
"QPushButton#alwaysTopButton:checked {\n"
"            background: #194759;\n"
"            color: grey;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            background-color:#1B4C5E;\n"
"            }"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/assets/always_top.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.alwaysTopButton.setIcon(icon2)
        self.alwaysTopButton.setCheckable(True)
        self.alwaysTopButton.setObjectName(_fromUtf8("alwaysTopButton"))
        self.gridLayout.addWidget(self.alwaysTopButton, 0, 3, 1, 1)
        self.screenshotLabel = QtGui.QLabel(Form)
        self.screenshotLabel.setStyleSheet(_fromUtf8("background-color: rgb(18, 35, 44);"))
        self.screenshotLabel.setText(_fromUtf8(""))
        self.screenshotLabel.setObjectName(_fromUtf8("screenshotLabel"))
        self.gridLayout.addWidget(self.screenshotLabel, 1, 0, 1, 4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.startStreamingButton.setText(_translate("Form", "Start", None))
        self.stopStreamingButton.setText(_translate("Form", "Stop", None))
        self.alwaysTopButton.setText(_translate("Form", "Always on top", None))

import res_rc
