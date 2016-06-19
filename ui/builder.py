# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'builder.ui'
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
        Form.resize(755, 583)
        Form.setStyleSheet(_fromUtf8("background-color: #2c3e50;\n"
"color: #c9f5f7;"))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.toolBox = QtGui.QToolBox(Form)
        self.toolBox.setStyleSheet(_fromUtf8(" QToolBox::tab {\n"
"  padding-left: 15px;\n"
"  width: 110%;\n"
"  border: 1px ridge;\n"
"  border-color: #2c3e50;\n"
"  color: \n"
" }\n"
"\n"
" QToolBox::tab:selected {\n"
"   background: #34495e;\n"
" }\n"
"\n"
" QToolBox::panel {\n"
"   background-color: #2c3e50;\n"
" }\n"
"\n"
" QToolBox{\n"
"}"))
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.clientOptionsTab = QtGui.QWidget()
        self.clientOptionsTab.setGeometry(QtCore.QRect(0, 0, 737, 435))
        self.clientOptionsTab.setStyleSheet(_fromUtf8("border: none;\n"
"padding-bottom: 5px;"))
        self.clientOptionsTab.setObjectName(_fromUtf8("clientOptionsTab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.clientOptionsTab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 12, 0, 1, 3)
        self.generateButton = QtGui.QPushButton(self.clientOptionsTab)
        self.generateButton.setMinimumSize(QtCore.QSize(0, 50))
        self.generateButton.setStyleSheet(_fromUtf8("QPushButton#generateButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#generateButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/start.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.generateButton.setIcon(icon)
        self.generateButton.setIconSize(QtCore.QSize(32, 32))
        self.generateButton.setObjectName(_fromUtf8("generateButton"))
        self.gridLayout_2.addWidget(self.generateButton, 13, 0, 1, 3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.clientAdressLine = QtGui.QLineEdit(self.clientOptionsTab)
        self.clientAdressLine.setStyleSheet(_fromUtf8("QLineEdit#clientAdressLine {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QLineEdit#clientAdressLine:pressed {\n"
"            border: 1px ridge #c9f5f7;\n"
"            }"))
        self.clientAdressLine.setObjectName(_fromUtf8("clientAdressLine"))
        self.horizontalLayout.addWidget(self.clientAdressLine)
        self.clientPortLabel = QtGui.QLabel(self.clientOptionsTab)
        self.clientPortLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.clientPortLabel.setObjectName(_fromUtf8("clientPortLabel"))
        self.horizontalLayout.addWidget(self.clientPortLabel)
        self.clientPortLine = QtGui.QLineEdit(self.clientOptionsTab)
        self.clientPortLine.setMaximumSize(QtCore.QSize(70, 16777215))
        self.clientPortLine.setStyleSheet(_fromUtf8("QLineEdit#clientPortLine {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QLineEdit#clientPortLine:pressed {\n"
"            border: 1px ridge #c9f5f7;\n"
"            }"))
        self.clientPortLine.setObjectName(_fromUtf8("clientPortLine"))
        self.horizontalLayout.addWidget(self.clientPortLine)
        self.checkConnectionButton = QtGui.QPushButton(self.clientOptionsTab)
        self.checkConnectionButton.setMinimumSize(QtCore.QSize(0, 22))
        self.checkConnectionButton.setMaximumSize(QtCore.QSize(16777215, 22))
        self.checkConnectionButton.setStyleSheet(_fromUtf8("QPushButton#checkConnectionButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#checkConnectionButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.checkConnectionButton.setObjectName(_fromUtf8("checkConnectionButton"))
        self.horizontalLayout.addWidget(self.checkConnectionButton)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 1, 1, 2)
        self.workingDirLabel = QtGui.QLabel(self.clientOptionsTab)
        self.workingDirLabel.setObjectName(_fromUtf8("workingDirLabel"))
        self.gridLayout_2.addWidget(self.workingDirLabel, 4, 0, 1, 1)
        self.line = QtGui.QFrame(self.clientOptionsTab)
        self.line.setStyleSheet(_fromUtf8("border: 1px ridge;\n"
"            border-color: #2c3e50;"))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 7, 0, 1, 3)
        self.usbSpredingCheck = QtGui.QCheckBox(self.clientOptionsTab)
        self.usbSpredingCheck.setObjectName(_fromUtf8("usbSpredingCheck"))
        self.gridLayout_2.addWidget(self.usbSpredingCheck, 8, 1, 1, 1)
        self.line_2 = QtGui.QFrame(self.clientOptionsTab)
        self.line_2.setStyleSheet(_fromUtf8(""))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_2.addWidget(self.line_2, 9, 0, 1, 3)
        self.autostartCheck = QtGui.QCheckBox(self.clientOptionsTab)
        self.autostartCheck.setObjectName(_fromUtf8("autostartCheck"))
        self.gridLayout_2.addWidget(self.autostartCheck, 8, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.currentUserLabel = QtGui.QLabel(self.clientOptionsTab)
        self.currentUserLabel.setStyleSheet(_fromUtf8("padding-top: 4px;"))
        self.currentUserLabel.setObjectName(_fromUtf8("currentUserLabel"))
        self.horizontalLayout_3.addWidget(self.currentUserLabel)
        self.workingDirLine = QtGui.QLineEdit(self.clientOptionsTab)
        self.workingDirLine.setStyleSheet(_fromUtf8("QLineEdit#workingDirLine {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QLineEdit#workingDirLine:pressed {\n"
"            border: 1px ridge #c9f5f7;\n"
"            }"))
        self.workingDirLine.setObjectName(_fromUtf8("workingDirLine"))
        self.horizontalLayout_3.addWidget(self.workingDirLine)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 4, 1, 1, 2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.clientFileNameLine = QtGui.QLineEdit(self.clientOptionsTab)
        self.clientFileNameLine.setStyleSheet(_fromUtf8("QLineEdit#clientFileNameLine {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QLineEdit#clientFileNameLine:pressed {\n"
"            border: 1px ridge #c9f5f7;\n"
"            }"))
        self.clientFileNameLine.setObjectName(_fromUtf8("clientFileNameLine"))
        self.horizontalLayout_4.addWidget(self.clientFileNameLine)
        self.generateRandomNameButton = QtGui.QPushButton(self.clientOptionsTab)
        self.generateRandomNameButton.setMaximumSize(QtCore.QSize(22, 22))
        self.generateRandomNameButton.setStyleSheet(_fromUtf8("QPushButton#generateRandomNameButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#generateRandomNameButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.generateRandomNameButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.generateRandomNameButton.setIcon(icon1)
        self.generateRandomNameButton.setObjectName(_fromUtf8("generateRandomNameButton"))
        self.horizontalLayout_4.addWidget(self.generateRandomNameButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 3, 1, 1, 2)
        self.connectionTimeoutLine = QtGui.QLineEdit(self.clientOptionsTab)
        self.connectionTimeoutLine.setStyleSheet(_fromUtf8("QLineEdit#connectionTimeoutLine {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QLineEdit#connectionTimeoutLine:pressed {\n"
"            border: 1px ridge #c9f5f7;\n"
"            }"))
        self.connectionTimeoutLine.setObjectName(_fromUtf8("connectionTimeoutLine"))
        self.gridLayout_2.addWidget(self.connectionTimeoutLine, 2, 1, 1, 2)
        self.clientAddressLabel = QtGui.QLabel(self.clientOptionsTab)
        self.clientAddressLabel.setObjectName(_fromUtf8("clientAddressLabel"))
        self.gridLayout_2.addWidget(self.clientAddressLabel, 0, 0, 1, 1)
        self.fileNameLabel = QtGui.QLabel(self.clientOptionsTab)
        self.fileNameLabel.setObjectName(_fromUtf8("fileNameLabel"))
        self.gridLayout_2.addWidget(self.fileNameLabel, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.serverPasswordLine = QtGui.QLineEdit(self.clientOptionsTab)
        self.serverPasswordLine.setStyleSheet(_fromUtf8("QLineEdit#serverPasswordLine {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QLineEdit#serverPasswordLine:pressed {\n"
"            border: 1px ridge #c9f5f7;\n"
"            }"))
        self.serverPasswordLine.setEchoMode(QtGui.QLineEdit.Password)
        self.serverPasswordLine.setObjectName(_fromUtf8("serverPasswordLine"))
        self.horizontalLayout_2.addWidget(self.serverPasswordLine)
        self.showPasswordButton = QtGui.QPushButton(self.clientOptionsTab)
        self.showPasswordButton.setMaximumSize(QtCore.QSize(22, 22))
        self.showPasswordButton.setStyleSheet(_fromUtf8("QPushButton#showPasswordButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#showPasswordButton:checked {\n"
"            border-color: #27ae60;\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.showPasswordButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/unhide.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.showPasswordButton.setIcon(icon2)
        self.showPasswordButton.setIconSize(QtCore.QSize(18, 18))
        self.showPasswordButton.setCheckable(True)
        self.showPasswordButton.setObjectName(_fromUtf8("showPasswordButton"))
        self.horizontalLayout_2.addWidget(self.showPasswordButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 1, 1, 2)
        self.connectionTimeoutLabel = QtGui.QLabel(self.clientOptionsTab)
        self.connectionTimeoutLabel.setObjectName(_fromUtf8("connectionTimeoutLabel"))
        self.gridLayout_2.addWidget(self.connectionTimeoutLabel, 2, 0, 1, 1)
        self.serverPasswordLabel = QtGui.QLabel(self.clientOptionsTab)
        self.serverPasswordLabel.setObjectName(_fromUtf8("serverPasswordLabel"))
        self.gridLayout_2.addWidget(self.serverPasswordLabel, 1, 0, 1, 1)
        self.FakeGroup = QtGui.QGroupBox(self.clientOptionsTab)
        self.FakeGroup.setStyleSheet(_fromUtf8("padding-top: 15px;\n"
"border: 1px ridge;\n"
"border-color: #2c3e50;"))
        self.FakeGroup.setCheckable(True)
        self.FakeGroup.setObjectName(_fromUtf8("FakeGroup"))
        self.gridLayout_3 = QtGui.QGridLayout(self.FakeGroup)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.fakeFileExtensionLabel = QtGui.QLabel(self.FakeGroup)
        self.fakeFileExtensionLabel.setStyleSheet(_fromUtf8("padding: px;\n"
"border: none;"))
        self.fakeFileExtensionLabel.setObjectName(_fromUtf8("fakeFileExtensionLabel"))
        self.horizontalLayout_5.addWidget(self.fakeFileExtensionLabel)
        self.fakeFileExtension = QtGui.QLineEdit(self.FakeGroup)
        self.fakeFileExtension.setStyleSheet(_fromUtf8("QLineEdit#fakeFileExtension {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QLineEdit#fakeFileExtension:pressed {\n"
"            border: 1px ridge #c9f5f7;\n"
"            }"))
        self.fakeFileExtension.setObjectName(_fromUtf8("fakeFileExtension"))
        self.horizontalLayout_5.addWidget(self.fakeFileExtension)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.FakeGroup, 10, 0, 1, 3)
        self.pluginsGroup = QtGui.QGroupBox(self.clientOptionsTab)
        self.pluginsGroup.setStyleSheet(_fromUtf8("padding-top: 15px;\n"
"border: 1px ridge;\n"
"border-color: #2c3e50;"))
        self.pluginsGroup.setObjectName(_fromUtf8("pluginsGroup"))
        self.gridLayout_4 = QtGui.QGridLayout(self.pluginsGroup)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.remoteAudioCheck = QtGui.QCheckBox(self.pluginsGroup)
        self.remoteAudioCheck.setStyleSheet(_fromUtf8("border: none;\n"
"padding-top: 1;"))
        self.remoteAudioCheck.setObjectName(_fromUtf8("remoteAudioCheck"))
        self.gridLayout_4.addWidget(self.remoteAudioCheck, 0, 0, 1, 1)
        self.remoteWebcamCheck = QtGui.QCheckBox(self.pluginsGroup)
        self.remoteWebcamCheck.setStyleSheet(_fromUtf8("border: none;\n"
"padding-top: 1;"))
        self.remoteWebcamCheck.setObjectName(_fromUtf8("remoteWebcamCheck"))
        self.gridLayout_4.addWidget(self.remoteWebcamCheck, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.pluginsGroup, 11, 0, 1, 3)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/settings.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.clientOptionsTab, icon3, _fromUtf8(""))
        self.sourceEditorTab = QtGui.QWidget()
        self.sourceEditorTab.setGeometry(QtCore.QRect(0, 0, 737, 435))
        self.sourceEditorTab.setObjectName(_fromUtf8("sourceEditorTab"))
        self.gridLayout_5 = QtGui.QGridLayout(self.sourceEditorTab)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.idleLayout = QtGui.QVBoxLayout()
        self.idleLayout.setObjectName(_fromUtf8("idleLayout"))
        self.buttonsLayout = QtGui.QHBoxLayout()
        self.buttonsLayout.setObjectName(_fromUtf8("buttonsLayout"))
        self.obfuscateButton = QtGui.QPushButton(self.sourceEditorTab)
        self.obfuscateButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.obfuscateButton.setStyleSheet(_fromUtf8("QPushButton#obfuscateButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 5px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#obfuscateButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/shuffle.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.obfuscateButton.setIcon(icon4)
        self.obfuscateButton.setObjectName(_fromUtf8("obfuscateButton"))
        self.buttonsLayout.addWidget(self.obfuscateButton)
        self.saveButton = QtGui.QPushButton(self.sourceEditorTab)
        self.saveButton.setStyleSheet(_fromUtf8("QPushButton#saveButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 5px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#saveButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/save_as.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveButton.setIcon(icon5)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.buttonsLayout.addWidget(self.saveButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.buttonsLayout.addItem(spacerItem1)
        self.idleLayout.addLayout(self.buttonsLayout)
        self.gridLayout_5.addLayout(self.idleLayout, 0, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.backToOptionsButton = QtGui.QPushButton(self.sourceEditorTab)
        self.backToOptionsButton.setMinimumSize(QtCore.QSize(0, 50))
        self.backToOptionsButton.setStyleSheet(_fromUtf8("QPushButton#backToOptionsButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#backToOptionsButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/back.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backToOptionsButton.setIcon(icon6)
        self.backToOptionsButton.setIconSize(QtCore.QSize(32, 32))
        self.backToOptionsButton.setObjectName(_fromUtf8("backToOptionsButton"))
        self.horizontalLayout_6.addWidget(self.backToOptionsButton)
        self.nextToAssemblyButton = QtGui.QPushButton(self.sourceEditorTab)
        self.nextToAssemblyButton.setMinimumSize(QtCore.QSize(0, 50))
        self.nextToAssemblyButton.setStyleSheet(_fromUtf8("QPushButton#nextToAssemblyButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#nextToAssemblyButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.nextToAssemblyButton.setIcon(icon)
        self.nextToAssemblyButton.setIconSize(QtCore.QSize(32, 32))
        self.nextToAssemblyButton.setObjectName(_fromUtf8("nextToAssemblyButton"))
        self.horizontalLayout_6.addWidget(self.nextToAssemblyButton)
        self.gridLayout_5.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/python.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.sourceEditorTab, icon7, _fromUtf8(""))
        self.executablesVersion = QtGui.QWidget()
        self.executablesVersion.setGeometry(QtCore.QRect(0, 0, 737, 435))
        self.executablesVersion.setObjectName(_fromUtf8("executablesVersion"))
        self.toolBox.addItem(self.executablesVersion, _fromUtf8(""))
        self.sourceEditor = QtGui.QWidget()
        self.sourceEditor.setGeometry(QtCore.QRect(0, 0, 737, 435))
        self.sourceEditor.setObjectName(_fromUtf8("sourceEditor"))
        self.toolBox.addItem(self.sourceEditor, _fromUtf8(""))
        self.gridLayout.addWidget(self.toolBox, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(10)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Client Builder (PyInstaller)", None))
        self.generateButton.setText(_translate("Form", "Generate Code", None))
        self.clientAdressLine.setText(_translate("Form", "192.168.1.2", None))
        self.clientPortLabel.setText(_translate("Form", "Port:", None))
        self.clientPortLine.setText(_translate("Form", "4434", None))
        self.checkConnectionButton.setText(_translate("Form", "Check Connection", None))
        self.workingDirLabel.setText(_translate("Form", "Working Dir:", None))
        self.usbSpredingCheck.setText(_translate("Form", "Enable Usb Spreading", None))
        self.autostartCheck.setText(_translate("Form", "Enable Autostart", None))
        self.currentUserLabel.setText(_translate("Form", "/%CurrentUser%/", None))
        self.workingDirLine.setText(_translate("Form", "Moderat", None))
        self.clientFileNameLine.setText(_translate("Form", "Morderat_server", None))
        self.connectionTimeoutLine.setText(_translate("Form", "5", None))
        self.clientAddressLabel.setText(_translate("Form", "Connetion Address:", None))
        self.fileNameLabel.setText(_translate("Form", "Client File Name:", None))
        self.serverPasswordLine.setText(_translate("Form", "Moderat123", None))
        self.connectionTimeoutLabel.setText(_translate("Form", "Connection Timeout (seconds):", None))
        self.serverPasswordLabel.setText(_translate("Form", "Client Password (default: Moderat123):", None))
        self.FakeGroup.setTitle(_translate("Form", "Show Fake File On First Run", None))
        self.fakeFileExtensionLabel.setText(_translate("Form", "Fake File Extension:", None))
        self.fakeFileExtension.setPlaceholderText(_translate("Form", "examples: doc, docx, xls, jpeg", None))
        self.pluginsGroup.setTitle(_translate("Form", "Plugins", None))
        self.remoteAudioCheck.setText(_translate("Form", "Remote Microphone", None))
        self.remoteWebcamCheck.setText(_translate("Form", "Remote Webcam", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.clientOptionsTab), _translate("Form", "Client Options", None))
        self.obfuscateButton.setText(_translate("Form", "Obfuscate", None))
        self.saveButton.setText(_translate("Form", "Save", None))
        self.backToOptionsButton.setText(_translate("Form", "Back To Client Options", None))
        self.nextToAssemblyButton.setText(_translate("Form", "Next To Assembly Editor", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.sourceEditorTab), _translate("Form", "Source Editor - Obfuscator", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.executablesVersion), _translate("Form", "Assembly Information", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.sourceEditor), _translate("Form", "Source Editor - Obfuscator", None))

import res_rc
