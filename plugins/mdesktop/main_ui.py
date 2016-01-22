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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/mdesktop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(_fromUtf8("background-color: #2c3e50;\n"
"color: #bdc3c7;"))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.startStreamingButton = QtGui.QPushButton(Form)
        self.startStreamingButton.setMinimumSize(QtCore.QSize(53, 24))
        self.startStreamingButton.setStyleSheet(_fromUtf8("QPushButton#startStreamingButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#startStreamingButton:checked {\n"
"            border-color: #27ae60;\n"
"            background-color: #2c3e50;\n"
"            }"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/start.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startStreamingButton.setIcon(icon1)
        self.startStreamingButton.setIconSize(QtCore.QSize(18, 18))
        self.startStreamingButton.setCheckable(True)
        self.startStreamingButton.setObjectName(_fromUtf8("startStreamingButton"))
        self.gridLayout.addWidget(self.startStreamingButton, 0, 0, 1, 1)
        self.stopStreamingButton = QtGui.QPushButton(Form)
        self.stopStreamingButton.setMinimumSize(QtCore.QSize(53, 24))
        self.stopStreamingButton.setStyleSheet(_fromUtf8("QPushButton#stopStreamingButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#stopStreamingButton:checked {\n"
"            border-color: #27ae60;\n"
"            background-color: #2c3e50;\n"
"            }"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopStreamingButton.setIcon(icon2)
        self.stopStreamingButton.setIconSize(QtCore.QSize(18, 18))
        self.stopStreamingButton.setCheckable(True)
        self.stopStreamingButton.setChecked(True)
        self.stopStreamingButton.setObjectName(_fromUtf8("stopStreamingButton"))
        self.gridLayout.addWidget(self.stopStreamingButton, 0, 1, 1, 1)
        self.alwaysTopButton = QtGui.QPushButton(Form)
        self.alwaysTopButton.setMinimumSize(QtCore.QSize(0, 24))
        self.alwaysTopButton.setStyleSheet(_fromUtf8("QPushButton#alwaysTopButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#alwaysTopButton:checked {\n"
"            border-color: #27ae60;\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.alwaysTopButton.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/always_top.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.alwaysTopButton.setIcon(icon3)
        self.alwaysTopButton.setIconSize(QtCore.QSize(18, 18))
        self.alwaysTopButton.setCheckable(True)
        self.alwaysTopButton.setObjectName(_fromUtf8("alwaysTopButton"))
        self.gridLayout.addWidget(self.alwaysTopButton, 0, 3, 1, 1)
        self.screenshotLabel = QtGui.QLabel(Form)
        self.screenshotLabel.setStyleSheet(_fromUtf8("background-color: #34495e;\n"
"padding: 2px;\n"
"color: #bdc3c7;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border: 1px ridge;\n"
"border-right: none;\n"
"border-color: #2c3e50;"))
        self.screenshotLabel.setScaledContents(True)
        self.screenshotLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.screenshotLabel.setObjectName(_fromUtf8("screenshotLabel"))
        self.gridLayout.addWidget(self.screenshotLabel, 1, 0, 1, 4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.startStreamingButton.setText(_translate("Form", "Start", None))
        self.stopStreamingButton.setText(_translate("Form", "Stop", None))
        self.screenshotLabel.setText(_translate("Form", "Press Start", None))
