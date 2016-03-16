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
        Form.resize(411, 227)
        Form.setMinimumSize(QtCore.QSize(255, 41))
        Form.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/maudio.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(_fromUtf8("background-color: #2c3e50;\n"
"color: #bdc3c7;"))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.listenButton = QtGui.QPushButton(Form)
        self.listenButton.setMinimumSize(QtCore.QSize(0, 24))
        self.listenButton.setStyleSheet(_fromUtf8("QPushButton#listenButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            border-right: none;\n"
"            }\n"
"\n"
"QPushButton#listenButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.listenButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/start.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.listenButton.setIcon(icon1)
        self.listenButton.setIconSize(QtCore.QSize(18, 18))
        self.listenButton.setObjectName(_fromUtf8("listenButton"))
        self.horizontalLayout_2.addWidget(self.listenButton)
        self.recordButton = QtGui.QPushButton(Form)
        self.recordButton.setMinimumSize(QtCore.QSize(0, 24))
        self.recordButton.setStyleSheet(_fromUtf8("QPushButton#recordButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            border-right: none;\n"
"            border-left: none;\n"
"            }\n"
"\n"
"QPushButton#recordButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.recordButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/record.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.recordButton.setIcon(icon2)
        self.recordButton.setIconSize(QtCore.QSize(18, 18))
        self.recordButton.setObjectName(_fromUtf8("recordButton"))
        self.horizontalLayout_2.addWidget(self.recordButton)
        self.stopButton = QtGui.QPushButton(Form)
        self.stopButton.setMinimumSize(QtCore.QSize(0, 24))
        self.stopButton.setStyleSheet(_fromUtf8("QPushButton#stopButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            border-left: none;\n"
"            }\n"
"\n"
"QPushButton#stopButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.stopButton.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopButton.setIcon(icon3)
        self.stopButton.setIconSize(QtCore.QSize(18, 18))
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.horizontalLayout_2.addWidget(self.stopButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/always_top.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.alwaysTopButton.setIcon(icon4)
        self.alwaysTopButton.setCheckable(True)
        self.alwaysTopButton.setObjectName(_fromUtf8("alwaysTopButton"))
        self.gridLayout.addWidget(self.alwaysTopButton, 0, 2, 1, 1)
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
        self.rateDrop.setObjectName(_fromUtf8("rateDrop"))
        self.rateDrop.addItem(_fromUtf8(""))
        self.rateDrop.addItem(_fromUtf8(""))
        self.rateDrop.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.rateDrop)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 3)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 4, 0, 1, 3)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.detectRecordLabel = QtGui.QLabel(self.groupBox)
        self.detectRecordLabel.setObjectName(_fromUtf8("detectRecordLabel"))
        self.verticalLayout_2.addWidget(self.detectRecordLabel)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.volumeProgress = QtGui.QProgressBar(self.groupBox)
        self.volumeProgress.setStyleSheet(_fromUtf8("QProgressBar:horizontal {\n"
"border: 1px solid #0F2D40;\n"
"border-radius: 0px;\n"
"background: #0F2D40;\n"
"padding: 1px;\n"
"text-align: top;\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"background: #bdc3c7;\n"
"margin-right: 1px;\n"
"width: 5px;\n"
"}"))
        self.volumeProgress.setMaximum(100000)
        self.volumeProgress.setProperty("value", 1000)
        self.volumeProgress.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.volumeProgress.setTextVisible(False)
        self.volumeProgress.setOrientation(QtCore.Qt.Horizontal)
        self.volumeProgress.setInvertedAppearance(False)
        self.volumeProgress.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.volumeProgress.setObjectName(_fromUtf8("volumeProgress"))
        self.verticalLayout.addWidget(self.volumeProgress)
        self.volumeSlider = QtGui.QSlider(self.groupBox)
        self.volumeSlider.setEnabled(True)
        self.volumeSlider.setStyleSheet(_fromUtf8("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: #0F2D40;\n"
"height: 10px;\n"
"border-radius: 0px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: #bdc3c7;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 0px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #0F2D40;\n"
"height: 10px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: #34495e;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border: 1px ridge;\n"
"border-color: #34495e;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: #7f8c8d;\n"
"}"))
        self.volumeSlider.setMaximum(100000)
        self.volumeSlider.setProperty("value", 1000)
        self.volumeSlider.setSliderPosition(1000)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setInvertedAppearance(False)
        self.volumeSlider.setInvertedControls(False)
        self.volumeSlider.setTickPosition(QtGui.QSlider.NoTicks)
        self.volumeSlider.setObjectName(_fromUtf8("volumeSlider"))
        self.verticalLayout.addWidget(self.volumeSlider)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 6, 0, 1, 3)
        self.statusLabel = QtGui.QLabel(Form)
        self.statusLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statusLabel.setObjectName(_fromUtf8("statusLabel"))
        self.gridLayout.addWidget(self.statusLabel, 7, 0, 1, 3)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 1, 0, 1, 3)

        self.retranslateUi(Form)
        self.rateDrop.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Audio Streaming", None))
        self.defaultInputDeviceLavel.setText(_translate("Form", "Default Input Device:", None))
        self.rateLabel.setText(_translate("Form", "Rate:", None))
        self.rateDrop.setItemText(0, _translate("Form", "5120", None))
        self.rateDrop.setItemText(1, _translate("Form", "10240", None))
        self.rateDrop.setItemText(2, _translate("Form", "44100", None))
        self.groupBox.setTitle(_translate("Form", "Automatic Recording Settings", None))
        self.detectRecordLabel.setText(_translate("Form", "Detect Sound \n"
" and Record:", None))
        self.volumeProgress.setFormat(_translate("Form", "Volume", None))
        self.statusLabel.setText(_translate("Form", "Not Recording", None))

