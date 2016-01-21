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
        Form.resize(400, 330)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/mkeylogger.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setWindowOpacity(1.0)
        Form.setStyleSheet(_fromUtf8("background-color: #0F2D40;\n"
"color: #2ecc71;"))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.alwaysTopButton = QtGui.QPushButton(Form)
        self.alwaysTopButton.setMinimumSize(QtCore.QSize(0, 24))
        self.alwaysTopButton.setStyleSheet(_fromUtf8("QPushButton#alwaysTopButton {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            padding-right: 3px;\n"
"            color: white;\n"
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/always_top.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.alwaysTopButton.setIcon(icon1)
        self.alwaysTopButton.setCheckable(True)
        self.alwaysTopButton.setObjectName(_fromUtf8("alwaysTopButton"))
        self.gridLayout.addWidget(self.alwaysTopButton, 0, 3, 1, 1)
        self.stopKeyloggingButton = QtGui.QPushButton(Form)
        self.stopKeyloggingButton.setMinimumSize(QtCore.QSize(53, 24))
        self.stopKeyloggingButton.setStyleSheet(_fromUtf8("QPushButton#stopKeyloggingButton {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            padding-right: 5px;\n"
"            color: white;\n"
"            text-decoration: none;\n"
"            background-color: #225E75\n"
"            }\n"
"\n"
"QPushButton#stopKeyloggingButton:checked {\n"
"            background: #194759;\n"
"            color: grey;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            background-color:#1B4C5E;\n"
"            }"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopKeyloggingButton.setIcon(icon2)
        self.stopKeyloggingButton.setCheckable(False)
        self.stopKeyloggingButton.setChecked(False)
        self.stopKeyloggingButton.setObjectName(_fromUtf8("stopKeyloggingButton"))
        self.gridLayout.addWidget(self.stopKeyloggingButton, 0, 1, 1, 1)
        self.startKeyloggingButton = QtGui.QPushButton(Form)
        self.startKeyloggingButton.setMinimumSize(QtCore.QSize(53, 24))
        self.startKeyloggingButton.setStyleSheet(_fromUtf8("QPushButton#startKeyloggingButton {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            padding-right: 5px;\n"
"            color: white;\n"
"            text-decoration: none;\n"
"            background-color: #225E75\n"
"            }\n"
"\n"
"QPushButton#startKeyloggingButton:checked {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            color: grey;\n"
"            border-color: #0F2D40;\n"
"            background-color:#1B4C5E;\n"
"            }"))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/play.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startKeyloggingButton.setIcon(icon3)
        self.startKeyloggingButton.setIconSize(QtCore.QSize(18, 18))
        self.startKeyloggingButton.setCheckable(False)
        self.startKeyloggingButton.setObjectName(_fromUtf8("startKeyloggingButton"))
        self.gridLayout.addWidget(self.startKeyloggingButton, 0, 0, 1, 1)
        self.keystokesText = QtGui.QTextEdit(Form)
        self.keystokesText.setStyleSheet(_fromUtf8("background-position: center;\n"
"border: 1px outset;\n"
"border-color: #0F2D40;\n"
"border-radius: 2px;\n"
"color: rgb(178, 197, 214);\n"
"background-color: #081621;\n"
"font: 75 9pt \"MS Shell Dlg 2\";"))
        self.keystokesText.setDocumentTitle(_fromUtf8(""))
        self.keystokesText.setUndoRedoEnabled(False)
        self.keystokesText.setReadOnly(True)
        self.keystokesText.setObjectName(_fromUtf8("keystokesText"))
        self.gridLayout.addWidget(self.keystokesText, 1, 0, 1, 4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.stopKeyloggingButton.setText(_translate("Form", "Stop", None))
        self.startKeyloggingButton.setText(_translate("Form", "Start", None))
        self.keystokesText.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))

