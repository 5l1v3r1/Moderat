# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_ui.ui'
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
        Dialog.resize(395, 132)
        Dialog.setMinimumSize(QtCore.QSize(0, 0))
        Dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.addUsernameButton = QtGui.QPushButton(Dialog)
        self.addUsernameButton.setMinimumSize(QtCore.QSize(0, 34))
        self.addUsernameButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.addUsernameButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.addUsernameButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/add_moderator.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addUsernameButton.setIcon(icon1)
        self.addUsernameButton.setIconSize(QtCore.QSize(20, 20))
        self.addUsernameButton.setObjectName(_fromUtf8("addUsernameButton"))
        self.horizontalLayout_2.addWidget(self.addUsernameButton)
        self.usernameLine = QtGui.QLineEdit(Dialog)
        self.usernameLine.setMinimumSize(QtCore.QSize(0, 34))
        self.usernameLine.setObjectName(_fromUtf8("usernameLine"))
        self.horizontalLayout_2.addWidget(self.usernameLine)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.addPasswordButton = QtGui.QPushButton(Dialog)
        self.addPasswordButton.setMinimumSize(QtCore.QSize(0, 34))
        self.addPasswordButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.addPasswordButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.addPasswordButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/password.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addPasswordButton.setIcon(icon2)
        self.addPasswordButton.setIconSize(QtCore.QSize(20, 20))
        self.addPasswordButton.setObjectName(_fromUtf8("addPasswordButton"))
        self.horizontalLayout_3.addWidget(self.addPasswordButton)
        self.passwordLine = QtGui.QLineEdit(Dialog)
        self.passwordLine.setMinimumSize(QtCore.QSize(0, 34))
        self.passwordLine.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordLine.setObjectName(_fromUtf8("passwordLine"))
        self.horizontalLayout_3.addWidget(self.passwordLine)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.loginButton = QtGui.QPushButton(Dialog)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/locked.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loginButton.setIcon(icon3)
        self.loginButton.setIconSize(QtCore.QSize(20, 20))
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        self.verticalLayout.addWidget(self.loginButton)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "LogIn", None))
        self.usernameLine.setPlaceholderText(_translate("Dialog", "Username", None))
        self.passwordLine.setPlaceholderText(_translate("Dialog", "Password", None))
        self.loginButton.setText(_translate("Dialog", "Login", None))
