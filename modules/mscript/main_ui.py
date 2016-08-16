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
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/script.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setWindowOpacity(1.0)
        Form.setStyleSheet(_fromUtf8("QWidget {\n"
"background-color: #2c3e50;\n"
"color: #bdc3c7;\n"
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
        self.scriptTab = QtGui.QTabWidget(Form)
        self.scriptTab.setStyleSheet(_fromUtf8(" QTabBar::tab {\n"
"  padding: 10px;\n"
"  padding-left: 15px;\n"
"  margin-left: 9px;\n"
"  width: 80%;\n"
"  border: 1px ridge;\n"
"  border-color: #2c3e50;\n"
" }\n"
"\n"
" QTabBar::tab:selected {\n"
"   background: #34495e;\n"
" }\n"
"\n"
" QTabBar::pane {\n"
"   background-color: #2c3e50;\n"
" }\n"
"\n"
"QTabWidget::pane {\n"
"    color: rgb(246, 246, 244);\n"
"    margin: 0px,1px,1px,1px;\n"
"    border: 1px ridge;\n"
"    border-color: #0F2D40;\n"
"    background-color: #194759;\n"
"    background-position: center;\n"
"    border: none;\n"
"      }"))
        self.scriptTab.setObjectName(_fromUtf8("scriptTab"))
        self.pythonTab = QtGui.QWidget()
        self.pythonTab.setObjectName(_fromUtf8("pythonTab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.pythonTab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.runButton = QtGui.QPushButton(self.pythonTab)
        self.runButton.setMinimumSize(QtCore.QSize(28, 28))
        self.runButton.setMaximumSize(QtCore.QSize(28, 28))
        self.runButton.setStyleSheet(_fromUtf8("QPushButton#runButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            border-bottom: none;\n"
"            border-right: none;\n"
"            }\n"
"\n"
"QPushButton#runButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.runButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/start.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.runButton.setIcon(icon1)
        self.runButton.setIconSize(QtCore.QSize(18, 18))
        self.runButton.setObjectName(_fromUtf8("runButton"))
        self.verticalLayout.addWidget(self.runButton)
        self.fromFileButton = QtGui.QPushButton(self.pythonTab)
        self.fromFileButton.setMinimumSize(QtCore.QSize(28, 28))
        self.fromFileButton.setMaximumSize(QtCore.QSize(28, 28))
        self.fromFileButton.setStyleSheet(_fromUtf8("QPushButton#fromFileButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            border-top: none;\n"
"            border-bottom: none;\n"
"            border-right: none;\n"
"            }\n"
"\n"
"QPushButton#fromFileButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.fromFileButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fromFileButton.setIcon(icon2)
        self.fromFileButton.setIconSize(QtCore.QSize(18, 18))
        self.fromFileButton.setObjectName(_fromUtf8("fromFileButton"))
        self.verticalLayout.addWidget(self.fromFileButton)
        self.closeOutputButton = QtGui.QPushButton(self.pythonTab)
        self.closeOutputButton.setMinimumSize(QtCore.QSize(28, 28))
        self.closeOutputButton.setMaximumSize(QtCore.QSize(28, 28))
        self.closeOutputButton.setStyleSheet(_fromUtf8("QPushButton#closeOutputButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            border-top: none;\n"
"            border-bottom: none;\n"
"            border-right: none;\n"
"            }\n"
"\n"
"QPushButton#closeOutputButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.closeOutputButton.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/bottom.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeOutputButton.setIcon(icon3)
        self.closeOutputButton.setIconSize(QtCore.QSize(18, 18))
        self.closeOutputButton.setObjectName(_fromUtf8("closeOutputButton"))
        self.verticalLayout.addWidget(self.closeOutputButton)
        self.clearButton = QtGui.QPushButton(self.pythonTab)
        self.clearButton.setMinimumSize(QtCore.QSize(28, 28))
        self.clearButton.setMaximumSize(QtCore.QSize(28, 28))
        self.clearButton.setStyleSheet(_fromUtf8("QPushButton#clearButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            border-top: none;\n"
"            border-right: none;\n"
"            }\n"
"\n"
"QPushButton#clearButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.clearButton.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/remove.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearButton.setIcon(icon4)
        self.clearButton.setIconSize(QtCore.QSize(18, 18))
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.verticalLayout.addWidget(self.clearButton)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.splitter = QtGui.QSplitter(self.pythonTab)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.horizontalLayout_2.addWidget(self.splitter)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/python.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.scriptTab.addTab(self.pythonTab, icon5, _fromUtf8(""))
        self.gridLayout.addWidget(self.scriptTab, 0, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.showOutputButton = QtGui.QPushButton(Form)
        self.showOutputButton.setMinimumSize(QtCore.QSize(80, 0))
        self.showOutputButton.setStyleSheet(_fromUtf8("padding: 5px;\n"
"background: #34495e;\n"
"border: 1px ridge;\n"
"border-right: none;\n"
"border-color: #2c3e50;\n"
"border-bottom: none;"))
        self.showOutputButton.setObjectName(_fromUtf8("showOutputButton"))
        self.horizontalLayout.addWidget(self.showOutputButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.outputText = QtGui.QTextEdit(Form)
        self.outputText.setStyleSheet(_fromUtf8("background-color: #131E25;\n"
"padding: 5px;\n"
"color: #bdc3c7;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border: 1px ridge;\n"
"border-color: #2c3e50;"))
        self.outputText.setReadOnly(True)
        self.outputText.setObjectName(_fromUtf8("outputText"))
        self.verticalLayout_2.addWidget(self.outputText)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.retranslateUi(Form)
        self.scriptTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Remote Scripting", None))
        self.scriptTab.setTabText(self.scriptTab.indexOf(self.pythonTab), _translate("Form", "Python", None))
        self.showOutputButton.setText(_translate("Form", "Output", None))

