# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
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
        Form.resize(400, 207)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/settings.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setWindowOpacity(1.0)
        Form.setStyleSheet(_fromUtf8("background-color: #2c3e50;\n"
"color: #c9f5f7;"))
        self.gridLayout_2 = QtGui.QGridLayout(Form)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.settingsTab = QtGui.QTabWidget(Form)
        self.settingsTab.setStyleSheet(_fromUtf8("QTabBar::tab {\n"
"padding: 5px;\n"
"margin-left: 2px;\n"
"border: 1px ridge;\n"
"border-color: #2c3e50;\n"
"background-color: #34495e;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"background-color: #2c3e50;\n"
"border-bottom: none;\n"
"}\n"
"\n"
"QTabBar::pane {\n"
"background-color: #fff;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"color: rgb(246, 246, 244);\n"
"margin: 0px,1px,1px,1px;\n"
"border: 1px ridge;\n"
"border-color: #2c3e50;\n"
"border-top: none;\n"
"background-color: #fff;\n"
"background-position: center;\n"
"}"))
        self.settingsTab.setTabPosition(QtGui.QTabWidget.North)
        self.settingsTab.setMovable(True)
        self.settingsTab.setObjectName(_fromUtf8("settingsTab"))
        self.connectionTab = QtGui.QWidget()
        self.connectionTab.setObjectName(_fromUtf8("connectionTab"))
        self.gridLayout = QtGui.QGridLayout(self.connectionTab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.ipAddressLabel = QtGui.QLabel(self.connectionTab)
        self.ipAddressLabel.setMinimumSize(QtCore.QSize(150, 0))
        self.ipAddressLabel.setObjectName(_fromUtf8("ipAddressLabel"))
        self.horizontalLayout.addWidget(self.ipAddressLabel)
        self.ipAddressLine = QtGui.QLineEdit(self.connectionTab)
        self.ipAddressLine.setStyleSheet(_fromUtf8("background-color: #34495e; \n"
"border: none;\n"
"border: 1px ridge;\n"
"border-color: #2c3e50;"))
        self.ipAddressLine.setObjectName(_fromUtf8("ipAddressLine"))
        self.horizontalLayout.addWidget(self.ipAddressLine)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.portLabel = QtGui.QLabel(self.connectionTab)
        self.portLabel.setMinimumSize(QtCore.QSize(150, 0))
        self.portLabel.setObjectName(_fromUtf8("portLabel"))
        self.horizontalLayout_2.addWidget(self.portLabel)
        self.portLine = QtGui.QLineEdit(self.connectionTab)
        self.portLine.setStyleSheet(_fromUtf8("background-color: #34495e; \n"
"border: none;\n"
"border: 1px ridge;\n"
"border-color: #2c3e50;"))
        self.portLine.setObjectName(_fromUtf8("portLine"))
        self.horizontalLayout_2.addWidget(self.portLine)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.maxConnectionsLabel = QtGui.QLabel(self.connectionTab)
        self.maxConnectionsLabel.setMinimumSize(QtCore.QSize(150, 0))
        self.maxConnectionsLabel.setObjectName(_fromUtf8("maxConnectionsLabel"))
        self.horizontalLayout_4.addWidget(self.maxConnectionsLabel)
        self.maxConnectionsLine = QtGui.QLineEdit(self.connectionTab)
        self.maxConnectionsLine.setStyleSheet(_fromUtf8("background-color: #34495e; \n"
"border: none;\n"
"border: 1px ridge;\n"
"border-color: #2c3e50;"))
        self.maxConnectionsLine.setObjectName(_fromUtf8("maxConnectionsLine"))
        self.horizontalLayout_4.addWidget(self.maxConnectionsLine)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.timeoutLabel = QtGui.QLabel(self.connectionTab)
        self.timeoutLabel.setMinimumSize(QtCore.QSize(150, 0))
        self.timeoutLabel.setObjectName(_fromUtf8("timeoutLabel"))
        self.horizontalLayout_3.addWidget(self.timeoutLabel)
        self.timeoutLine = QtGui.QLineEdit(self.connectionTab)
        self.timeoutLine.setStyleSheet(_fromUtf8("background-color: #34495e; \n"
"border: none;\n"
"border: 1px ridge;\n"
"border-color: #2c3e50;"))
        self.timeoutLine.setObjectName(_fromUtf8("timeoutLine"))
        self.horizontalLayout_3.addWidget(self.timeoutLine)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.settingsTab.addTab(self.connectionTab, _fromUtf8(""))
        self.interfaceTab = QtGui.QWidget()
        self.interfaceTab.setObjectName(_fromUtf8("interfaceTab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.interfaceTab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.languageLabel = QtGui.QLabel(self.interfaceTab)
        self.languageLabel.setMinimumSize(QtCore.QSize(150, 0))
        self.languageLabel.setMaximumSize(QtCore.QSize(150, 16777215))
        self.languageLabel.setObjectName(_fromUtf8("languageLabel"))
        self.horizontalLayout_5.addWidget(self.languageLabel)
        self.languageCombo = QtGui.QComboBox(self.interfaceTab)
        self.languageCombo.setStyleSheet(_fromUtf8("border: 1px ridge;\n"
"border-color: #2c3e50;\n"
"height: 20px;\n"
"font-size: 12px;\n"
"background-color: #34495e;"))
        self.languageCombo.setObjectName(_fromUtf8("languageCombo"))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.languageCombo)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 1, 0, 1, 1)
        self.settingsTab.addTab(self.interfaceTab, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.settingsTab, 0, 1, 1, 1)
        self.saveButton = QtGui.QPushButton(Form)
        self.saveButton.setMinimumSize(QtCore.QSize(0, 30))
        self.saveButton.setStyleSheet(_fromUtf8("QPushButton#saveButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            border-left: none;\n"
"            }\n"
"\n"
"QPushButton#saveButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.gridLayout_2.addWidget(self.saveButton, 1, 0, 1, 2)

        self.retranslateUi(Form)
        self.settingsTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "ModeRat Settings", None))
        self.ipAddressLabel.setText(_translate("Form", "Ip Address:", None))
        self.portLabel.setText(_translate("Form", "Port:", None))
        self.maxConnectionsLabel.setText(_translate("Form", "Maximum Connections:", None))
        self.timeoutLabel.setText(_translate("Form", "Connection Timeout:", None))
        self.settingsTab.setTabText(self.settingsTab.indexOf(self.connectionTab), _translate("Form", "Connection Settings", None))
        self.languageLabel.setText(_translate("Form", "Language: ", None))
        self.languageCombo.setItemText(0, _translate("Form", "english", None))
        self.languageCombo.setItemText(1, _translate("Form", "georgian", None))
        self.settingsTab.setTabText(self.settingsTab.indexOf(self.interfaceTab), _translate("Form", "Interface", None))
        self.saveButton.setText(_translate("Form", "Save", None))
