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
        Form.setStyleSheet(_fromUtf8("background-color: #2c3e50;\n"
"color: #c9f5f7;"))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.screenshotButton = QtGui.QPushButton(Form)
        self.screenshotButton.setMinimumSize(QtCore.QSize(0, 28))
        self.screenshotButton.setMaximumSize(QtCore.QSize(16777215, 28))
        self.screenshotButton.setStyleSheet(_fromUtf8("QPushButton#screenshotButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 5px;\n"
"            background-color: #2c3e50;\n"
"            }\n"
"\n"
"QPushButton#screenshotButton:pressed {\n"
"            background-color: #34495e;\n"
"            }"))
        self.screenshotButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/desktop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.screenshotButton.setIcon(icon1)
        self.screenshotButton.setObjectName(_fromUtf8("screenshotButton"))
        self.horizontalLayout.addWidget(self.screenshotButton)
        self.saveButton = QtGui.QPushButton(Form)
        self.saveButton.setMinimumSize(QtCore.QSize(0, 28))
        self.saveButton.setMaximumSize(QtCore.QSize(16777215, 28))
        self.saveButton.setStyleSheet(_fromUtf8("QPushButton#saveButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 5px;\n"
"            background-color: #2c3e50;\n"
"            }\n"
"\n"
"QPushButton#saveButton:pressed {\n"
"            background-color: #34495e;\n"
"            }"))
        self.saveButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/save_as.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveButton.setIcon(icon2)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.horizontalLayout.addWidget(self.saveButton)
        self.clearButton = QtGui.QPushButton(Form)
        self.clearButton.setMinimumSize(QtCore.QSize(0, 28))
        self.clearButton.setMaximumSize(QtCore.QSize(16777215, 28))
        self.clearButton.setStyleSheet(_fromUtf8("QPushButton#clearButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 5px;\n"
"            background-color: #2c3e50;\n"
"            }\n"
"\n"
"QPushButton#clearButton:pressed {\n"
"            background-color: #34495e;\n"
"            }"))
        self.clearButton.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/trash.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearButton.setIcon(icon3)
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.horizontalLayout.addWidget(self.clearButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.alwaysTopButton = QtGui.QPushButton(Form)
        self.alwaysTopButton.setMinimumSize(QtCore.QSize(0, 24))
        self.alwaysTopButton.setStyleSheet(_fromUtf8("QPushButton#alwaysTopButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 5px;\n"
"            background-color: #2c3e50;\n"
"            }\n"
"\n"
"QPushButton#alwaysTopButton:checked {\n"
"            border: 1px ridge #c792ea;\n"
"            }"))
        self.alwaysTopButton.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/pin.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.alwaysTopButton.setIcon(icon4)
        self.alwaysTopButton.setCheckable(True)
        self.alwaysTopButton.setObjectName(_fromUtf8("alwaysTopButton"))
        self.horizontalLayout_2.addWidget(self.alwaysTopButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.screenshotLabel = QtGui.QLabel(Form)
        self.screenshotLabel.setStyleSheet(_fromUtf8("background-color: #34495e;\n"
"color: #455e54;"))
        self.screenshotLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.screenshotLabel.setObjectName(_fromUtf8("screenshotLabel"))
        self.gridLayout.addWidget(self.screenshotLabel, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Remote Desktop Preview", None))
        self.screenshotLabel.setText(_translate("Form", "Desktop Preview", None))
