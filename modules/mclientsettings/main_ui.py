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
        Form.resize(557, 404)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.logSettingsGroup = QtGui.QGroupBox(Form)
        self.logSettingsGroup.setObjectName(_fromUtf8("logSettingsGroup"))
        self.gridLayout_2 = QtGui.QGridLayout(self.logSettingsGroup)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.keyloggerCheck = QtGui.QCheckBox(self.logSettingsGroup)
        self.keyloggerCheck.setObjectName(_fromUtf8("keyloggerCheck"))
        self.gridLayout_2.addWidget(self.keyloggerCheck, 3, 0, 1, 1)
        self.audioCheck = QtGui.QCheckBox(self.logSettingsGroup)
        self.audioCheck.setObjectName(_fromUtf8("audioCheck"))
        self.gridLayout_2.addWidget(self.audioCheck, 5, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.screenshotDelayLabel = QtGui.QLabel(self.logSettingsGroup)
        self.screenshotDelayLabel.setObjectName(_fromUtf8("screenshotDelayLabel"))
        self.horizontalLayout.addWidget(self.screenshotDelayLabel)
        self.screenshotDelayLine = QtGui.QLineEdit(self.logSettingsGroup)
        self.screenshotDelayLine.setObjectName(_fromUtf8("screenshotDelayLine"))
        self.horizontalLayout.addWidget(self.screenshotDelayLine)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.line = QtGui.QFrame(self.logSettingsGroup)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 2, 0, 1, 1)
        self.line_2 = QtGui.QFrame(self.logSettingsGroup)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_2.addWidget(self.line_2, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.audioLengthLabel = QtGui.QLabel(self.logSettingsGroup)
        self.audioLengthLabel.setObjectName(_fromUtf8("audioLengthLabel"))
        self.horizontalLayout_2.addWidget(self.audioLengthLabel)
        self.audioLengthLine = QtGui.QLineEdit(self.logSettingsGroup)
        self.audioLengthLine.setObjectName(_fromUtf8("audioLengthLine"))
        self.horizontalLayout_2.addWidget(self.audioLengthLine)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 6, 0, 1, 1)
        self.screenshotCheck = QtGui.QCheckBox(self.logSettingsGroup)
        self.screenshotCheck.setObjectName(_fromUtf8("screenshotCheck"))
        self.gridLayout_2.addWidget(self.screenshotCheck, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.logSettingsGroup, 0, 0, 1, 1)
        self.screadingSettingsGroup = QtGui.QGroupBox(Form)
        self.screadingSettingsGroup.setObjectName(_fromUtf8("screadingSettingsGroup"))
        self.gridLayout_3 = QtGui.QGridLayout(self.screadingSettingsGroup)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.usbSpreadingCheck = QtGui.QCheckBox(self.screadingSettingsGroup)
        self.usbSpreadingCheck.setObjectName(_fromUtf8("usbSpreadingCheck"))
        self.gridLayout_3.addWidget(self.usbSpreadingCheck, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.screadingSettingsGroup, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Client Settings", None))
        self.logSettingsGroup.setTitle(_translate("Form", "Log Settings", None))
        self.keyloggerCheck.setText(_translate("Form", "Keylogger", None))
        self.audioCheck.setText(_translate("Form", "Microphone Recorder", None))
        self.screenshotDelayLabel.setText(_translate("Form", "Screenshot Delay: ", None))
        self.screenshotDelayLine.setText(_translate("Form", "30", None))
        self.audioLengthLabel.setText(_translate("Form", "Recording Length: ", None))
        self.audioLengthLine.setText(_translate("Form", "300", None))
        self.screenshotCheck.setText(_translate("Form", "Screenshot", None))
        self.screadingSettingsGroup.setTitle(_translate("Form", "Spreading Settings", None))
        self.usbSpreadingCheck.setText(_translate("Form", "USB Spreading", None))

