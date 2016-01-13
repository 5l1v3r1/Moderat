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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.startStreaming = QtGui.QPushButton(Form)
        self.startStreaming.setGeometry(QtCore.QRect(30, 10, 75, 23))
        self.startStreaming.setObjectName(_fromUtf8("startStreaming"))
        self.screenshotLabel = QtGui.QLabel(Form)
        self.screenshotLabel.setGeometry(QtCore.QRect(60, 80, 291, 171))
        self.screenshotLabel.setText(_fromUtf8(""))
        self.screenshotLabel.setObjectName(_fromUtf8("screenshotLabel"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.startStreaming.setText(_translate("Form", "Start", None))

