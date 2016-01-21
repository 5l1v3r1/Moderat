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
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/mexplorer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(_fromUtf8("QWidget {background-color: #0F2D40;\n"
"color: #2ecc71;}\n"
"\n"
" QScrollBar:vertical {\n"
"     border: 1px outset;\n"
"     border-color: #0F2D40;\n"
"     background: #194759;\n"
"     width: 10px;\n"
"     margin: 22px 0 22px 0;\n"
" }\n"
" QScrollBar::handle:vertical {\n"
"     background: #2ecc71;\n"
"     min-height: 20px;\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: 1px outset;\n"
"     border-color: #0F2D40;\n"
"     background: #32CC99;\n"
"     height: 16px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:vertical {\n"
"     border: 1px outset;\n"
"     border-color: #0F2D40;\n"
"     background: #32CC99;\n"
"     height: 16px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     border: 1px outset;\n"
"     border-color: #0F2D40;\n"
"     border-radius: 2px;\n"
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
"     background: #194759;\n"
"     height: 10px;\n"
"     margin: 0px 40px 0 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #2ecc71;\n"
"    min-width: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    border: 1px outset;\n"
"    border-color: #0F2D40;\n"
"    background: #32CC99;\n"
"    width: 16px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: 1px outset;\n"
"    border-color: #0F2D40;\n"
"    background: #32CC99;\n"
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
"    background: pink;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}"))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.fileLabel = QtGui.QLabel(Form)
        self.fileLabel.setMaximumSize(QtCore.QSize(16777215, 15))
        self.fileLabel.setStyleSheet(_fromUtf8("color: rgb(155, 89, 182);"))
        self.fileLabel.setObjectName(_fromUtf8("fileLabel"))
        self.horizontalLayout_5.addWidget(self.fileLabel)
        self.dirLabel = QtGui.QLabel(Form)
        self.dirLabel.setMaximumSize(QtCore.QSize(16777215, 15))
        self.dirLabel.setStyleSheet(_fromUtf8("color: rgb(0, 255, 255);"))
        self.dirLabel.setObjectName(_fromUtf8("dirLabel"))
        self.horizontalLayout_5.addWidget(self.dirLabel)
        self.hfileLabel = QtGui.QLabel(Form)
        self.hfileLabel.setMaximumSize(QtCore.QSize(16777215, 15))
        self.hfileLabel.setStyleSheet(_fromUtf8("color: rgb(235, 235, 235);"))
        self.hfileLabel.setObjectName(_fromUtf8("hfileLabel"))
        self.horizontalLayout_5.addWidget(self.hfileLabel)
        self.hdirLabel = QtGui.QLabel(Form)
        self.hdirLabel.setMaximumSize(QtCore.QSize(16777215, 15))
        self.hdirLabel.setStyleSheet(_fromUtf8("color: rgb(201, 101, 101);"))
        self.hdirLabel.setObjectName(_fromUtf8("hdirLabel"))
        self.horizontalLayout_5.addWidget(self.hdirLabel)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 3)
        self.splitter = QtGui.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lexplorerDrivesDrop = QtGui.QComboBox(self.layoutWidget)
        self.lexplorerDrivesDrop.setMinimumSize(QtCore.QSize(50, 32))
        self.lexplorerDrivesDrop.setMaximumSize(QtCore.QSize(50, 32))
        self.lexplorerDrivesDrop.setBaseSize(QtCore.QSize(0, 0))
        self.lexplorerDrivesDrop.setStyleSheet(_fromUtf8("border: 1px ridge;\n"
"border-color: #0F2D40;\n"
"border-radius: none;\n"
"height: 15px;\n"
"font-size: 12px;\n"
"background-color: #081621;\n"
"padding-left: 5px;"))
        self.lexplorerDrivesDrop.setObjectName(_fromUtf8("lexplorerDrivesDrop"))
        self.horizontalLayout.addWidget(self.lexplorerDrivesDrop)
        self.lrefreshButton = QtGui.QPushButton(self.layoutWidget)
        self.lrefreshButton.setMinimumSize(QtCore.QSize(32, 32))
        self.lrefreshButton.setMaximumSize(QtCore.QSize(32, 32))
        self.lrefreshButton.setStyleSheet(_fromUtf8("QPushButton#lrefreshButton {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            text-decoration: none;\n"
"            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #194759, stop:1 #225E75);\n"
"            }\n"
"\n"
"QPushButton#lrefreshButton:pressed {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #112F3B, stop:1 #1B4C5E);\n"
"            }"))
        self.lrefreshButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lrefreshButton.setIcon(icon1)
        self.lrefreshButton.setObjectName(_fromUtf8("lrefreshButton"))
        self.horizontalLayout.addWidget(self.lrefreshButton)
        self.lupButton = QtGui.QPushButton(self.layoutWidget)
        self.lupButton.setMinimumSize(QtCore.QSize(32, 32))
        self.lupButton.setMaximumSize(QtCore.QSize(32, 32))
        self.lupButton.setStyleSheet(_fromUtf8("QPushButton#lupButton {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            text-decoration: none;\n"
"            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #194759, stop:1 #225E75);\n"
"            }\n"
"\n"
"QPushButton#lupButton:pressed {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #112F3B, stop:1 #1B4C5E);\n"
"            }"))
        self.lupButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/up.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lupButton.setIcon(icon2)
        self.lupButton.setObjectName(_fromUtf8("lupButton"))
        self.horizontalLayout.addWidget(self.lupButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.uploadButton = QtGui.QPushButton(self.layoutWidget)
        self.uploadButton.setMinimumSize(QtCore.QSize(80, 32))
        self.uploadButton.setMaximumSize(QtCore.QSize(80, 32))
        self.uploadButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.uploadButton.setStyleSheet(_fromUtf8("QPushButton#uploadButton {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            padding-right: 5px;\n"
"            color: white;\n"
"            text-decoration: none;\n"
"            background-color: #225E75\n"
"            }\n"
"\n"
"QPushButton#uploadButton:pressed {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #112F3B, stop:1 #1B4C5E);\n"
"            }"))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/upload.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uploadButton.setIcon(icon3)
        self.uploadButton.setObjectName(_fromUtf8("uploadButton"))
        self.horizontalLayout.addWidget(self.uploadButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.localLabel = QtGui.QLabel(self.layoutWidget)
        self.localLabel.setObjectName(_fromUtf8("localLabel"))
        self.horizontalLayout_4.addWidget(self.localLabel)
        self.lexplorerPathEntry = QtGui.QLineEdit(self.layoutWidget)
        self.lexplorerPathEntry.setMinimumSize(QtCore.QSize(0, 28))
        self.lexplorerPathEntry.setStyleSheet(_fromUtf8("border: 1px ridge;\n"
"border-color: #0F2D40;\n"
"border-radius: none;\n"
"height: 15px;\n"
"font-size: 12px;\n"
"background-color: #081621;\n"
"padding-left: 5px;"))
        self.lexplorerPathEntry.setText(_fromUtf8(""))
        self.lexplorerPathEntry.setObjectName(_fromUtf8("lexplorerPathEntry"))
        self.horizontalLayout_4.addWidget(self.lexplorerPathEntry)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.lexplorerTable = QtGui.QTableWidget(self.layoutWidget)
        self.lexplorerTable.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lexplorerTable.setStyleSheet(_fromUtf8("QHeaderView::section {\n"
"    background-color: #194759;\n"
"    color: white;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QTableWidget#lexplorerTable {\n"
"    background-position: center;\n"
"    border: 1px outset;\n"
"    border-color: #0F2D40;\n"
"    border-radius: 2px;\n"
"    background-color: #081621;\n"
"}\n"
"\n"
"QTableWidget#lexplorerTable:item:selected {\n"
"background-color: #194759;\n"
"height: 50px;\n"
"color: #2ecc71;\n"
"border: none;\n"
"}"))
        self.lexplorerTable.setFrameShape(QtGui.QFrame.StyledPanel)
        self.lexplorerTable.setFrameShadow(QtGui.QFrame.Plain)
        self.lexplorerTable.setLineWidth(1)
        self.lexplorerTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.lexplorerTable.setProperty("showDropIndicator", False)
        self.lexplorerTable.setDragDropOverwriteMode(False)
        self.lexplorerTable.setAlternatingRowColors(False)
        self.lexplorerTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.lexplorerTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.lexplorerTable.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.lexplorerTable.setShowGrid(False)
        self.lexplorerTable.setGridStyle(QtCore.Qt.DotLine)
        self.lexplorerTable.setWordWrap(False)
        self.lexplorerTable.setCornerButtonEnabled(True)
        self.lexplorerTable.setObjectName(_fromUtf8("lexplorerTable"))
        self.lexplorerTable.setColumnCount(4)
        self.lexplorerTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.lexplorerTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.lexplorerTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.lexplorerTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.lexplorerTable.setHorizontalHeaderItem(3, item)
        self.lexplorerTable.horizontalHeader().setVisible(True)
        self.lexplorerTable.horizontalHeader().setCascadingSectionResizes(True)
        self.lexplorerTable.horizontalHeader().setDefaultSectionSize(50)
        self.lexplorerTable.horizontalHeader().setHighlightSections(True)
        self.lexplorerTable.horizontalHeader().setSortIndicatorShown(False)
        self.lexplorerTable.horizontalHeader().setStretchLastSection(True)
        self.lexplorerTable.verticalHeader().setVisible(False)
        self.lexplorerTable.verticalHeader().setCascadingSectionResizes(False)
        self.verticalLayout_2.addWidget(self.lexplorerTable)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.downloadButton = QtGui.QPushButton(self.layoutWidget1)
        self.downloadButton.setMinimumSize(QtCore.QSize(80, 32))
        self.downloadButton.setMaximumSize(QtCore.QSize(80, 32))
        self.downloadButton.setStyleSheet(_fromUtf8("QPushButton#downloadButton {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            color: white;\n"
"            padding-left: 5px;\n"
"            text-decoration: none;\n"
"            background-color: #225E75;\n"
"            }\n"
"\n"
"QPushButton#downloadButton:pressed {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #112F3B, stop:1 #1B4C5E);\n"
"            }"))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/download.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.downloadButton.setIcon(icon4)
        self.downloadButton.setObjectName(_fromUtf8("downloadButton"))
        self.horizontalLayout_2.addWidget(self.downloadButton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.rexplorerDrivesDrop = QtGui.QComboBox(self.layoutWidget1)
        self.rexplorerDrivesDrop.setMinimumSize(QtCore.QSize(50, 32))
        self.rexplorerDrivesDrop.setMaximumSize(QtCore.QSize(50, 32))
        self.rexplorerDrivesDrop.setBaseSize(QtCore.QSize(0, 0))
        self.rexplorerDrivesDrop.setStyleSheet(_fromUtf8("border: 1px ridge;\n"
"border-color: #0F2D40;\n"
"border-radius: none;\n"
"height: 15px;\n"
"font-size: 12px;\n"
"background-color: #081621;\n"
"padding-left: 5px;"))
        self.rexplorerDrivesDrop.setObjectName(_fromUtf8("rexplorerDrivesDrop"))
        self.horizontalLayout_2.addWidget(self.rexplorerDrivesDrop)
        self.rrefreshButton = QtGui.QPushButton(self.layoutWidget1)
        self.rrefreshButton.setMinimumSize(QtCore.QSize(32, 32))
        self.rrefreshButton.setMaximumSize(QtCore.QSize(32, 32))
        self.rrefreshButton.setStyleSheet(_fromUtf8("QPushButton#rrefreshButton {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            text-decoration: none;\n"
"            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #194759, stop:1 #225E75);\n"
"            }\n"
"\n"
"QPushButton#rrefreshButton:pressed {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #112F3B, stop:1 #1B4C5E);\n"
"            }"))
        self.rrefreshButton.setText(_fromUtf8(""))
        self.rrefreshButton.setIcon(icon1)
        self.rrefreshButton.setObjectName(_fromUtf8("rrefreshButton"))
        self.horizontalLayout_2.addWidget(self.rrefreshButton)
        self.rupButton = QtGui.QPushButton(self.layoutWidget1)
        self.rupButton.setMinimumSize(QtCore.QSize(32, 32))
        self.rupButton.setMaximumSize(QtCore.QSize(32, 32))
        self.rupButton.setStyleSheet(_fromUtf8("QPushButton#rupButton {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            text-decoration: none;\n"
"            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #194759, stop:1 #225E75);\n"
"            }\n"
"\n"
"QPushButton#rupButton:pressed {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #112F3B, stop:1 #1B4C5E);\n"
"            }"))
        self.rupButton.setText(_fromUtf8(""))
        self.rupButton.setIcon(icon2)
        self.rupButton.setObjectName(_fromUtf8("rupButton"))
        self.horizontalLayout_2.addWidget(self.rupButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.remoteLabel = QtGui.QLabel(self.layoutWidget1)
        self.remoteLabel.setObjectName(_fromUtf8("remoteLabel"))
        self.horizontalLayout_3.addWidget(self.remoteLabel)
        self.rexplorerPathEntry = QtGui.QLineEdit(self.layoutWidget1)
        self.rexplorerPathEntry.setMinimumSize(QtCore.QSize(0, 28))
        self.rexplorerPathEntry.setStyleSheet(_fromUtf8("border: 1px ridge;\n"
"border-color: #0F2D40;\n"
"border-radius: none;\n"
"height: 15px;\n"
"font-size: 12px;\n"
"background-color: #081621;\n"
"padding-left: 5px;"))
        self.rexplorerPathEntry.setText(_fromUtf8(""))
        self.rexplorerPathEntry.setObjectName(_fromUtf8("rexplorerPathEntry"))
        self.horizontalLayout_3.addWidget(self.rexplorerPathEntry)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.rexplorerTable = QtGui.QTableWidget(self.layoutWidget1)
        self.rexplorerTable.setFocusPolicy(QtCore.Qt.NoFocus)
        self.rexplorerTable.setStyleSheet(_fromUtf8("QHeaderView::section {\n"
"    background-color: #194759;\n"
"    color: white;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QTableWidget#rexplorerTable {\n"
"    background-position: center;\n"
"    border: 1px outset;\n"
"    border-color: #0F2D40;\n"
"    border-radius: 2px;\n"
"    background-color: #081621;\n"
"}\n"
"\n"
"QTableWidget#rexplorerTable:item:selected {\n"
"background-color: #194759;\n"
"height: 50px;\n"
"color: #2ecc71;\n"
"border: none;\n"
"}"))
        self.rexplorerTable.setFrameShape(QtGui.QFrame.StyledPanel)
        self.rexplorerTable.setFrameShadow(QtGui.QFrame.Plain)
        self.rexplorerTable.setLineWidth(1)
        self.rexplorerTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.rexplorerTable.setProperty("showDropIndicator", False)
        self.rexplorerTable.setDragDropOverwriteMode(False)
        self.rexplorerTable.setAlternatingRowColors(False)
        self.rexplorerTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.rexplorerTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.rexplorerTable.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.rexplorerTable.setShowGrid(False)
        self.rexplorerTable.setGridStyle(QtCore.Qt.DotLine)
        self.rexplorerTable.setWordWrap(False)
        self.rexplorerTable.setCornerButtonEnabled(True)
        self.rexplorerTable.setObjectName(_fromUtf8("rexplorerTable"))
        self.rexplorerTable.setColumnCount(4)
        self.rexplorerTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.rexplorerTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.rexplorerTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.rexplorerTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.rexplorerTable.setHorizontalHeaderItem(3, item)
        self.rexplorerTable.horizontalHeader().setVisible(True)
        self.rexplorerTable.horizontalHeader().setCascadingSectionResizes(True)
        self.rexplorerTable.horizontalHeader().setDefaultSectionSize(50)
        self.rexplorerTable.horizontalHeader().setHighlightSections(True)
        self.rexplorerTable.horizontalHeader().setSortIndicatorShown(False)
        self.rexplorerTable.horizontalHeader().setStretchLastSection(True)
        self.rexplorerTable.verticalHeader().setVisible(False)
        self.rexplorerTable.verticalHeader().setCascadingSectionResizes(False)
        self.verticalLayout.addWidget(self.rexplorerTable)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 3)
        self.progressBar = QtGui.QProgressBar(Form)
        self.progressBar.setStyleSheet(_fromUtf8("QProgressBar:horizontal {\n"
"border: 1px solid #2ecc71;\n"
"border-radius: 3px;\n"
"background: #081621;\n"
"padding: 1px;\n"
"text-align: top;\n"
"margin-right: 4ex;\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"background: #194759;\n"
"margin-right: 1px;\n"
"width: 5px;\n"
"}"))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout.addWidget(self.progressBar, 3, 1, 1, 1)
        self.cancelButton = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelButton.sizePolicy().hasHeightForWidth())
        self.cancelButton.setSizePolicy(sizePolicy)
        self.cancelButton.setMinimumSize(QtCore.QSize(70, 25))
        self.cancelButton.setStyleSheet(_fromUtf8("QPushButton#cancelButton {\n"
"            background: #194759;\n"
"            border: 1px solid #2ecc71;\n"
"            color: white;\n"
"            background-color: #194759;\n"
"            }\n"
"\n"
"QPushButton#cancelButton:pressed {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #112F3B, stop:1 #1B4C5E);\n"
"            }"))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.gridLayout.addWidget(self.cancelButton, 3, 2, 1, 1)
        self.statusLabel = QtGui.QLabel(Form)
        self.statusLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setObjectName(_fromUtf8("statusLabel"))
        self.gridLayout.addWidget(self.statusLabel, 2, 1, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.fileLabel.setText(_translate("Form", "File", None))
        self.dirLabel.setText(_translate("Form", "Directory", None))
        self.hfileLabel.setText(_translate("Form", "Hidden File", None))
        self.hdirLabel.setText(_translate("Form", "Hidden Directory", None))
        self.uploadButton.setText(_translate("Form", "upload", None))
        self.localLabel.setText(_translate("Form", "LOCAL:\\", None))
        self.lexplorerTable.setSortingEnabled(False)
        item = self.lexplorerTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Type", None))
        item = self.lexplorerTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Name", None))
        item = self.lexplorerTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Date Modified", None))
        item = self.lexplorerTable.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Size", None))
        self.downloadButton.setText(_translate("Form", "download", None))
        self.remoteLabel.setText(_translate("Form", "REMOTE:\\", None))
        self.rexplorerTable.setSortingEnabled(False)
        item = self.rexplorerTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Type", None))
        item = self.rexplorerTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Name", None))
        item = self.rexplorerTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Date Modified", None))
        item = self.rexplorerTable.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Size", None))
        self.progressBar.setFormat(_translate("Form", "%p%", None))
        self.cancelButton.setText(_translate("Form", "Cancel", None))
        self.statusLabel.setText(_translate("Form", "Status", None))