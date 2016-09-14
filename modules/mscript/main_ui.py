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
        Form.resize(766, 479)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setWindowOpacity(1.0)
        Form.setStyleSheet(_fromUtf8("QWidget {\n"
"background-color: #2c3e50;\n"
"color: #c9f5f7;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"     border: 1px outset;\n"
"     border-color: #0F2D40;\n"
"     width: 10px;\n"
"     margin: 22px 0 22px 0;\n"
" }\n"
" QScrollBar::handle:vertical {\n"
"     background: #95a5a6;\n"
"     min-height: 20px;\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: 1px outset;\n"
"     border-color: #0F2D40;\n"
"     background: #95a5a6;\n"
"     height: 16px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:vertical {\n"
"     border: 1px outset;\n"
"     border-color: #0F2D40;\n"
"     background: #95a5a6;\n"
"     height: 16px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     width: 3px;\n"
"     height: 3px;\n"
"     background: white;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar:horizontal {\n"
"border: 1px outset;\n"
"     border-color: #0F2D40;\n"
"     height: 10px;\n"
"     margin: 0px 40px 0 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #95a5a6;\n"
"    min-width: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    border: 1px outset;\n"
"    border-color: #0F2D40;\n"
"    background: #95a5a6;\n"
"    width: 16px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: 1px outset;\n"
"    border-color: #0F2D40;\n"
"    background: #95a5a6;\n"
"    width: 16px;\n"
"    subcontrol-position: top right;\n"
"    subcontrol-origin: margin;\n"
"    position: absolute;\n"
"    right: 20px;\n"
"}\n"
"\n"
"QScrollBar:left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}"))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setStyleSheet(_fromUtf8("background-color: #34495e;\n"
"border: 1px solid #2c3e50;\n"
"padding: -3px;"))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.runButton = QtGui.QPushButton(self.groupBox)
        self.runButton.setMinimumSize(QtCore.QSize(28, 28))
        self.runButton.setMaximumSize(QtCore.QSize(28, 28))
        self.runButton.setStyleSheet(_fromUtf8("QPushButton#runButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 5px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#runButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.runButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/run_script.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.runButton.setIcon(icon1)
        self.runButton.setIconSize(QtCore.QSize(24, 24))
        self.runButton.setObjectName(_fromUtf8("runButton"))
        self.horizontalLayout_3.addWidget(self.runButton)
        self.line = QtGui.QFrame(self.groupBox)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_3.addWidget(self.line)
        self.saveButton = QtGui.QPushButton(self.groupBox)
        self.saveButton.setStyleSheet(_fromUtf8("QPushButton#saveButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 5px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#saveButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.saveButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/save_as.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveButton.setIcon(icon2)
        self.saveButton.setIconSize(QtCore.QSize(20, 20))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.horizontalLayout_3.addWidget(self.saveButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pluginSearchLine = QtGui.QLineEdit(self.groupBox)
        self.pluginSearchLine.setStyleSheet(_fromUtf8("background-color: #455F7A;\n"
"padding: 5px;\n"
"border-right: none;"))
        self.pluginSearchLine.setObjectName(_fromUtf8("pluginSearchLine"))
        self.horizontalLayout_2.addWidget(self.pluginSearchLine)
        self.addPluginButton = QtGui.QPushButton(self.groupBox)
        self.addPluginButton.setMaximumSize(QtCore.QSize(16777215, 28))
        self.addPluginButton.setStyleSheet(_fromUtf8("background-color: #455F7A;\n"
"padding: 5px;\n"
"border-left: none;"))
        self.addPluginButton.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/add_plugin.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addPluginButton.setIcon(icon3)
        self.addPluginButton.setIconSize(QtCore.QSize(20, 20))
        self.addPluginButton.setObjectName(_fromUtf8("addPluginButton"))
        self.horizontalLayout_2.addWidget(self.addPluginButton)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.splitter_2 = QtGui.QSplitter(Form)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.layoutWidget = QtGui.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.idleLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.idleLayout.setSpacing(0)
        self.idleLayout.setObjectName(_fromUtf8("idleLayout"))
        self.gridLayout.addWidget(self.splitter_2, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Remote Scripting", None))

