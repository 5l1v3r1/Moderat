# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'get_text_ui.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(412, 120)
        Dialog.setMinimumSize(QtCore.QSize(412, 120))
        Dialog.setMaximumSize(QtCore.QSize(412, 120))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(_fromUtf8("background-color: #2c3e50;\n"
"color: #c9f5f7;"))
        self.gridLayout_3 = QtGui.QGridLayout(Dialog)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.okButton = QtGui.QPushButton(Dialog)
        self.okButton.setStyleSheet(_fromUtf8("QPushButton#okButton {\n"
"            background-color: #27ae60;\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 10px;\n"
"            margin: 0px;\n"
"            }\n"
"\n"
"QPushButton#okButton:pressed {\n"
"            background-color: #2ecc71;\n"
"            }"))
        self.okButton.setIconSize(QtCore.QSize(20, 20))
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.gridLayout_3.addWidget(self.okButton, 2, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)
        self.textGroup = QtGui.QGroupBox(Dialog)
        self.textGroup.setStyleSheet(_fromUtf8("background-color: #34495e;\n"
"border: 1px solid #2c3e50;\n"
"padding-top: 7px;"))
        self.textGroup.setObjectName(_fromUtf8("textGroup"))
        self.gridLayout = QtGui.QGridLayout(self.textGroup)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.addTextButton = QtGui.QPushButton(self.textGroup)
        self.addTextButton.setMaximumSize(QtCore.QSize(16777215, 28))
        self.addTextButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.addTextButton.setStyleSheet(_fromUtf8("background-color: #455F7A;\n"
"padding: 5px;\n"
"border-right: none;"))
        self.addTextButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/set_alias.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addTextButton.setIcon(icon1)
        self.addTextButton.setIconSize(QtCore.QSize(20, 20))
        self.addTextButton.setObjectName(_fromUtf8("addTextButton"))
        self.horizontalLayout_2.addWidget(self.addTextButton)
        self.textLine = QtGui.QLineEdit(self.textGroup)
        self.textLine.setStyleSheet(_fromUtf8("background-color: #455F7A;\n"
"padding: 5px;\n"
"border-left: none;"))
        self.textLine.setObjectName(_fromUtf8("textLine"))
        self.horizontalLayout_2.addWidget(self.textLine)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.textGroup, 0, 0, 1, 2)
        self.cancelButton = QtGui.QPushButton(Dialog)
        self.cancelButton.setStyleSheet(_fromUtf8("QPushButton#cancelButton {\n"
"            background-color: #e74c3c;\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 10px;\n"
"            margin: 0px;\n"
"            }\n"
"\n"
"QPushButton#cancelButton:pressed {\n"
"            background-color: #c0392b;\n"
"            }"))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.gridLayout_3.addWidget(self.cancelButton, 2, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.textLine, self.okButton)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Get Text", None))
        self.okButton.setText(_translate("Dialog", "Ok", None))
        self.textGroup.setTitle(_translate("Dialog", "Get Text Title", None))
        self.textLine.setPlaceholderText(_translate("Dialog", "Placeholdertext", None))
        self.cancelButton.setText(_translate("Dialog", "Cancel", None))

