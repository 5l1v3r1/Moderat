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
        Form.resize(400, 330)
        Form.setStyleSheet(_fromUtf8("background-color: #0F2D40;\n"
"color: #2ecc71;"))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.alwaysTopButton = QtGui.QPushButton(Form)
        self.alwaysTopButton.setMinimumSize(QtCore.QSize(0, 24))
        self.alwaysTopButton.setStyleSheet(_fromUtf8("QPushButton#alwaysTopButton {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            padding-right: 3px;\n"
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
        self.alwaysTopButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/always_top.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.alwaysTopButton.setIcon(icon)
        self.alwaysTopButton.setCheckable(True)
        self.alwaysTopButton.setObjectName(_fromUtf8("alwaysTopButton"))
        self.gridLayout.addWidget(self.alwaysTopButton, 0, 3, 1, 1)
        self.stopKeyloggingButton = QtGui.QPushButton(Form)
        self.stopKeyloggingButton.setMinimumSize(QtCore.QSize(53, 24))
        self.stopKeyloggingButton.setStyleSheet(_fromUtf8("QPushButton#stopKeyloggingButton {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            padding-right: 5px;\n"
"            color: white;\n"
"            text-decoration: none;\n"
"            background-color: #225E75\n"
"            }\n"
"\n"
"QPushButton#stopKeyloggingButton:checked {\n"
"            background: #194759;\n"
"            color: grey;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            background-color:#1B4C5E;\n"
"            }"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopKeyloggingButton.setIcon(icon1)
        self.stopKeyloggingButton.setCheckable(False)
        self.stopKeyloggingButton.setChecked(False)
        self.stopKeyloggingButton.setObjectName(_fromUtf8("stopKeyloggingButton"))
        self.gridLayout.addWidget(self.stopKeyloggingButton, 0, 1, 1, 1)
        self.startKeyloggingButton = QtGui.QPushButton(Form)
        self.startKeyloggingButton.setMinimumSize(QtCore.QSize(53, 24))
        self.startKeyloggingButton.setStyleSheet(_fromUtf8("QPushButton#startKeyloggingButton {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            padding-right: 5px;\n"
"            color: white;\n"
"            text-decoration: none;\n"
"            background-color: #225E75\n"
"            }\n"
"\n"
"QPushButton#startKeyloggingButton:checked {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            color: grey;\n"
"            border-color: #0F2D40;\n"
"            background-color:#1B4C5E;\n"
"            }"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/play.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startKeyloggingButton.setIcon(icon2)
        self.startKeyloggingButton.setIconSize(QtCore.QSize(18, 18))
        self.startKeyloggingButton.setCheckable(False)
        self.startKeyloggingButton.setObjectName(_fromUtf8("startKeyloggingButton"))
        self.gridLayout.addWidget(self.startKeyloggingButton, 0, 0, 1, 1)
        self.keystokesText = QtGui.QTextEdit(Form)
        self.keystokesText.setStyleSheet(_fromUtf8("background-position: center;\n"
"border: 1px outset;\n"
"border-color: #0F2D40;\n"
"border-radius: 2px;\n"
"background-color: #081621;"))
        self.keystokesText.setDocumentTitle(_fromUtf8(""))
        self.keystokesText.setUndoRedoEnabled(False)
        self.keystokesText.setReadOnly(True)
        self.keystokesText.setObjectName(_fromUtf8("keystokesText"))
        self.gridLayout.addWidget(self.keystokesText, 1, 0, 1, 4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.stopKeyloggingButton.setText(_translate("Form", "Stop", None))
        self.startKeyloggingButton.setText(_translate("Form", "Start", None))

import res_rc
