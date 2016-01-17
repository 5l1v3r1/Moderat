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
        Form.resize(400, 124)
        Form.setMinimumSize(QtCore.QSize(255, 41))
        Form.setMaximumSize(QtCore.QSize(800, 600))
        Form.setStyleSheet(_fromUtf8("background-color: #0F2D40;\n"
"color: #2ecc71;"))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
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
        self.horizontalLayout_2.addWidget(self.listenButton)
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
        self.horizontalLayout_2.addWidget(self.recordButton)
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
        self.horizontalLayout_2.addWidget(self.stopButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.defaultInputDeviceLavel = QtGui.QLabel(Form)
        self.defaultInputDeviceLavel.setObjectName(_fromUtf8("defaultInputDeviceLavel"))
        self.horizontalLayout.addWidget(self.defaultInputDeviceLavel)
        self.defaultInputDeviceNameLabel = QtGui.QLabel(Form)
        self.defaultInputDeviceNameLabel.setStyleSheet(_fromUtf8("color: white;"))
        self.defaultInputDeviceNameLabel.setText(_fromUtf8(""))
        self.defaultInputDeviceNameLabel.setObjectName(_fromUtf8("defaultInputDeviceNameLabel"))
        self.horizontalLayout.addWidget(self.defaultInputDeviceNameLabel)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.rateLabel = QtGui.QLabel(Form)
        self.rateLabel.setObjectName(_fromUtf8("rateLabel"))
        self.horizontalLayout.addWidget(self.rateLabel)
        self.rateDrop = QtGui.QComboBox(Form)
        self.rateDrop.setStyleSheet(_fromUtf8("color: white;"))
        self.rateDrop.setObjectName(_fromUtf8("rateDrop"))
        self.rateDrop.addItem(_fromUtf8(""))
        self.rateDrop.addItem(_fromUtf8(""))
        self.rateDrop.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.rateDrop)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 3)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.volumeLabel = QtGui.QLabel(Form)
        self.volumeLabel.setObjectName(_fromUtf8("volumeLabel"))
        self.horizontalLayout_3.addWidget(self.volumeLabel)
        self.volumeProgress = QtGui.QProgressBar(Form)
        self.volumeProgress.setStyleSheet(_fromUtf8("QProgressBar:horizontal {\n"
"border: 1px solid #0F2D40;\n"
"border-radius: 3px;\n"
"background: #0F2D40;\n"
"padding: 1px;\n"
"text-align: top;\n"
"margin-right: 4ex;\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"background: #2ecc71;\n"
"margin-right: 1px;\n"
"width: 5px;\n"
"}"))
        self.volumeProgress.setMaximum(10000)
        self.volumeProgress.setProperty("value", 50)
        self.volumeProgress.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.volumeProgress.setTextVisible(False)
        self.volumeProgress.setOrientation(QtCore.Qt.Horizontal)
        self.volumeProgress.setInvertedAppearance(False)
        self.volumeProgress.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.volumeProgress.setObjectName(_fromUtf8("volumeProgress"))
        self.horizontalLayout_3.addWidget(self.volumeProgress)
        self.gridLayout.addLayout(self.horizontalLayout_3, 5, 0, 1, 3)
        self.alwaysTopButton = QtGui.QPushButton(Form)
        self.alwaysTopButton.setMinimumSize(QtCore.QSize(0, 24))
        self.alwaysTopButton.setStyleSheet(_fromUtf8("QPushButton#alwaysTopButton {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            color: white;\n"
"            padding-right: 3px;\n"
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/assets/always_top.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.alwaysTopButton.setIcon(icon3)
        self.alwaysTopButton.setCheckable(True)
        self.alwaysTopButton.setObjectName(_fromUtf8("alwaysTopButton"))
        self.gridLayout.addWidget(self.alwaysTopButton, 1, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 4, 0, 1, 3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Audio Streaming", None))
        self.listenButton.setText(_translate("Form", "Listen", None))
        self.recordButton.setText(_translate("Form", "Record", None))
        self.stopButton.setText(_translate("Form", "Stop", None))
        self.defaultInputDeviceLavel.setText(_translate("Form", "Default Input Device:", None))
        self.rateLabel.setText(_translate("Form", "Rate:", None))
        self.rateDrop.setItemText(0, _translate("Form", "5120", None))
        self.rateDrop.setItemText(1, _translate("Form", "10240", None))
        self.rateDrop.setItemText(2, _translate("Form", "44100", None))
        self.volumeLabel.setText(_translate("Form", "Volume:", None))
        self.volumeProgress.setFormat(_translate("Form", "Volume", None))

import res_rc
