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
        Form.resize(400, 326)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/mprocesses.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setWindowOpacity(1.0)
        Form.setStyleSheet(_fromUtf8("background-color: #2c3e50;\n"
"color: #bdc3c7;"))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.processesLabel = QtGui.QLabel(Form)
        self.processesLabel.setObjectName(_fromUtf8("processesLabel"))
        self.gridLayout.addWidget(self.processesLabel, 2, 1, 1, 1)
        self.processesCountLabel = QtGui.QLabel(Form)
        self.processesCountLabel.setObjectName(_fromUtf8("processesCountLabel"))
        self.gridLayout.addWidget(self.processesCountLabel, 2, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.processesTable = QtGui.QTableWidget(Form)
        self.processesTable.setFocusPolicy(QtCore.Qt.NoFocus)
        self.processesTable.setStyleSheet(_fromUtf8("QHeaderView::section {\n"
"    background-color: #34495e;\n"
"    padding: 2px;\n"
"    color: #bdc3c7;\n"
"    font: 75 8pt \"MS Shell Dlg 2\";\n"
"    border: 1px ridge;\n"
"    border-right: none;\n"
"    border-color: #2c3e50;\n"
"}\n"
"\n"
"QTableWidget#processesTable {\n"
"    background-position: center;\n"
"    border: 1px ridge;\n"
"    padding: 5px;\n"
"    color: #ecf0f1;\n"
"    border-color: #2c3e50;\n"
"    font: 8pt \"MS Shell Dlg 2\";\n"
"    background-color: #34495e;\n"
"}\n"
"\n"
"QTableWidget#processesTable:item:selected {\n"
"background-color: #2c3e50;\n"
"color: #ecf0f1;\n"
"}"))
        self.processesTable.setDragDropOverwriteMode(False)
        self.processesTable.setAlternatingRowColors(False)
        self.processesTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.processesTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.processesTable.setShowGrid(False)
        self.processesTable.setObjectName(_fromUtf8("processesTable"))
        self.processesTable.setColumnCount(2)
        self.processesTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.processesTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.processesTable.setHorizontalHeaderItem(1, item)
        self.processesTable.horizontalHeader().setStretchLastSection(True)
        self.processesTable.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.processesTable, 1, 0, 1, 3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.getProcessesButton = QtGui.QPushButton(Form)
        self.getProcessesButton.setMinimumSize(QtCore.QSize(32, 32))
        self.getProcessesButton.setMaximumSize(QtCore.QSize(32, 32))
        self.getProcessesButton.setStyleSheet(_fromUtf8("QPushButton#getProcessesButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            border-right: none\n"
"            }\n"
"\n"
"QPushButton#getProcessesButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.getProcessesButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/update.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.getProcessesButton.setIcon(icon1)
        self.getProcessesButton.setIconSize(QtCore.QSize(18, 18))
        self.getProcessesButton.setObjectName(_fromUtf8("getProcessesButton"))
        self.horizontalLayout.addWidget(self.getProcessesButton)
        self.terminateProcessButton = QtGui.QPushButton(Form)
        self.terminateProcessButton.setMinimumSize(QtCore.QSize(32, 32))
        self.terminateProcessButton.setMaximumSize(QtCore.QSize(32, 32))
        self.terminateProcessButton.setStyleSheet(_fromUtf8("QPushButton#terminateProcessButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            border-left: none\n"
"            }\n"
"\n"
"QPushButton#terminateProcessButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.terminateProcessButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/terminate.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.terminateProcessButton.setIcon(icon2)
        self.terminateProcessButton.setIconSize(QtCore.QSize(18, 18))
        self.terminateProcessButton.setCheckable(False)
        self.terminateProcessButton.setObjectName(_fromUtf8("terminateProcessButton"))
        self.horizontalLayout.addWidget(self.terminateProcessButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/always_top.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.alwaysTopButton.setIcon(icon3)
        self.alwaysTopButton.setIconSize(QtCore.QSize(18, 18))
        self.alwaysTopButton.setCheckable(True)
        self.alwaysTopButton.setObjectName(_fromUtf8("alwaysTopButton"))
        self.horizontalLayout.addWidget(self.alwaysTopButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.processesLabel.setText(_translate("Form", "Processes:", None))
        self.processesCountLabel.setText(_translate("Form", "0", None))
        item = self.processesTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "PID", None))
        item = self.processesTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Filename", None))
        self.getProcessesButton.setToolTip(_translate("Form", "Save", None))
        self.terminateProcessButton.setToolTip(_translate("Form", "Smilies Detection", None))
        self.alwaysTopButton.setToolTip(_translate("Form", "Always Top", None))

