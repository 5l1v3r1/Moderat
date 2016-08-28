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
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setStyleSheet(_fromUtf8("background-color: #34495e;\n"
"padding: -3px;\n"
"border: none;\n"
"margin-left: 1px;\n"
"margin-right: 1px;"))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.onlineGroup = QtGui.QGroupBox(self.groupBox)
        self.onlineGroup.setStyleSheet(_fromUtf8("background-color: #34495e;\n"
"border: none;"))
        self.onlineGroup.setTitle(_fromUtf8(""))
        self.onlineGroup.setObjectName(_fromUtf8("onlineGroup"))
        self.gridLayout_6 = QtGui.QGridLayout(self.onlineGroup)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.addFileButton = QtGui.QPushButton(self.onlineGroup)
        self.addFileButton.setMinimumSize(QtCore.QSize(0, 0))
        self.addFileButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.addFileButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.addFileButton.setStyleSheet(_fromUtf8("QPushButton#addFileButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 5px;\n"
"            }\n"
"\n"
"QPushButton#addFileButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.addFileButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/add_file.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addFileButton.setIcon(icon1)
        self.addFileButton.setIconSize(QtCore.QSize(18, 18))
        self.addFileButton.setCheckable(False)
        self.addFileButton.setObjectName(_fromUtf8("addFileButton"))
        self.horizontalLayout_6.addWidget(self.addFileButton)
        self.addFolderButton = QtGui.QPushButton(self.onlineGroup)
        self.addFolderButton.setMinimumSize(QtCore.QSize(0, 0))
        self.addFolderButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.addFolderButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.addFolderButton.setStyleSheet(_fromUtf8("QPushButton#addFolderButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 5px;\n"
"            }\n"
"\n"
"QPushButton#addFolderButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.addFolderButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/add_folder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addFolderButton.setIcon(icon2)
        self.addFolderButton.setIconSize(QtCore.QSize(18, 18))
        self.addFolderButton.setCheckable(False)
        self.addFolderButton.setChecked(False)
        self.addFolderButton.setObjectName(_fromUtf8("addFolderButton"))
        self.horizontalLayout_6.addWidget(self.addFolderButton)
        self.line_3 = QtGui.QFrame(self.onlineGroup)
        self.line_3.setStyleSheet(_fromUtf8("border: 1px ridge #2c3e50;"))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.horizontalLayout_6.addWidget(self.line_3)
        self.line_4 = QtGui.QFrame(self.onlineGroup)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.horizontalLayout_6.addWidget(self.line_4)
        self.renameButton = QtGui.QPushButton(self.onlineGroup)
        self.renameButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.renameButton.setStyleSheet(_fromUtf8("QPushButton#renameButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 5px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#renameButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.renameButton.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/set_alias.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.renameButton.setIcon(icon3)
        self.renameButton.setIconSize(QtCore.QSize(18, 18))
        self.renameButton.setObjectName(_fromUtf8("renameButton"))
        self.horizontalLayout_6.addWidget(self.renameButton)
        self.hiddenButton = QtGui.QPushButton(self.onlineGroup)
        self.hiddenButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.hiddenButton.setStyleSheet(_fromUtf8("QPushButton#hiddenButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 5px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#hiddenButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.hiddenButton.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/eye.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hiddenButton.setIcon(icon4)
        self.hiddenButton.setIconSize(QtCore.QSize(18, 18))
        self.hiddenButton.setObjectName(_fromUtf8("hiddenButton"))
        self.horizontalLayout_6.addWidget(self.hiddenButton)
        self.removeButton = QtGui.QPushButton(self.onlineGroup)
        self.removeButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.removeButton.setStyleSheet(_fromUtf8("QPushButton#removeButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 5px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#removeButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.removeButton.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/trash.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeButton.setIcon(icon5)
        self.removeButton.setIconSize(QtCore.QSize(18, 18))
        self.removeButton.setObjectName(_fromUtf8("removeButton"))
        self.horizontalLayout_6.addWidget(self.removeButton)
        self.line_2 = QtGui.QFrame(self.onlineGroup)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout_6.addWidget(self.line_2)
        self.line_5 = QtGui.QFrame(self.onlineGroup)
        self.line_5.setStyleSheet(_fromUtf8("border: 1px ridge #2c3e50;"))
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.horizontalLayout_6.addWidget(self.line_5)
        self.line = QtGui.QFrame(self.onlineGroup)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_6.addWidget(self.line)
        self.downloadButton = QtGui.QPushButton(self.onlineGroup)
        self.downloadButton.setStyleSheet(_fromUtf8("QPushButton#downloadButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 5px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#downloadButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.downloadButton.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/down.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.downloadButton.setIcon(icon6)
        self.downloadButton.setObjectName(_fromUtf8("downloadButton"))
        self.horizontalLayout_6.addWidget(self.downloadButton)
        self.uploadButton = QtGui.QPushButton(self.onlineGroup)
        self.uploadButton.setStyleSheet(_fromUtf8("QPushButton#uploadButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 5px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#uploadButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.uploadButton.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/up.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uploadButton.setIcon(icon7)
        self.uploadButton.setObjectName(_fromUtf8("uploadButton"))
        self.horizontalLayout_6.addWidget(self.uploadButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.gridLayout_6.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.onlineGroup, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.explorerDrivesDrop = QtGui.QComboBox(self.groupBox)
        self.explorerDrivesDrop.setMinimumSize(QtCore.QSize(50, 0))
        self.explorerDrivesDrop.setMaximumSize(QtCore.QSize(50, 32))
        self.explorerDrivesDrop.setBaseSize(QtCore.QSize(0, 0))
        self.explorerDrivesDrop.setStyleSheet(_fromUtf8("background: #2c3e50;\n"
"border: none;\n"
"border: 1px ridge;\n"
"border-color: #2c3e50;\n"
"padding: 3px;"))
        self.explorerDrivesDrop.setObjectName(_fromUtf8("explorerDrivesDrop"))
        self.horizontalLayout_2.addWidget(self.explorerDrivesDrop)
        self.explorerPathEntry = QtGui.QLineEdit(self.groupBox)
        self.explorerPathEntry.setMinimumSize(QtCore.QSize(0, 28))
        self.explorerPathEntry.setStyleSheet(_fromUtf8("background: #2c3e50;\n"
"border: none;\n"
"border: 1px ridge;\n"
"border-color: #2c3e50;\n"
"padding: 3px;"))
        self.explorerPathEntry.setText(_fromUtf8(""))
        self.explorerPathEntry.setObjectName(_fromUtf8("explorerPathEntry"))
        self.horizontalLayout_2.addWidget(self.explorerPathEntry)
        self.upButton = QtGui.QPushButton(self.groupBox)
        self.upButton.setMinimumSize(QtCore.QSize(0, 28))
        self.upButton.setMaximumSize(QtCore.QSize(500, 28))
        self.upButton.setStyleSheet(_fromUtf8("QPushButton#upButton {\n"
"            border: none;\n"
"            border-radius: none;\n"
"            padding: 5px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#upButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.upButton.setText(_fromUtf8(""))
        self.upButton.setIcon(icon7)
        self.upButton.setIconSize(QtCore.QSize(18, 18))
        self.upButton.setObjectName(_fromUtf8("upButton"))
        self.horizontalLayout_2.addWidget(self.upButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.explorerTable = QtGui.QTableWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.explorerTable.sizePolicy().hasHeightForWidth())
        self.explorerTable.setSizePolicy(sizePolicy)
        self.explorerTable.setFocusPolicy(QtCore.Qt.NoFocus)
        self.explorerTable.setAcceptDrops(True)
        self.explorerTable.setStyleSheet(_fromUtf8("QHeaderView::section {\n"
"background-color: #2c3e50;\n"
"padding: 2px;\n"
"color: #cff7f8;\n"
"font: 75 10px \"MS Shell Dlg 2\";\n"
"border: 1px solid;\n"
"border-top: none;\n"
"border-bottom: none;\n"
"border-color: #34495e;\n"
"}\n"
"\n"
"QTableWidget#explorerTable {\n"
"background-position: center;\n"
"border:  none;\n"
"padding: 5px;\n"
"margin-left: 1px;\n"
"margin-right: 1px;\n"
"color: #cff7f8;\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"background-color: #34495e;\n"
"\n"
"background-image: url(assets/bg.png);\n"
"background-repeat: no-repeat;\n"
"}\n"
"\n"
"QTableWidget#explorerTable:item:selected {\n"
"background-color: #2c3e50;\n"
"color: #cff7f8;\n"
"}"))
        self.explorerTable.setFrameShape(QtGui.QFrame.StyledPanel)
        self.explorerTable.setFrameShadow(QtGui.QFrame.Plain)
        self.explorerTable.setLineWidth(1)
        self.explorerTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.explorerTable.setProperty("showDropIndicator", False)
        self.explorerTable.setDragDropOverwriteMode(False)
        self.explorerTable.setAlternatingRowColors(False)
        self.explorerTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.explorerTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.explorerTable.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.explorerTable.setShowGrid(False)
        self.explorerTable.setGridStyle(QtCore.Qt.DotLine)
        self.explorerTable.setWordWrap(False)
        self.explorerTable.setCornerButtonEnabled(True)
        self.explorerTable.setObjectName(_fromUtf8("explorerTable"))
        self.explorerTable.setColumnCount(4)
        self.explorerTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.explorerTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.explorerTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.explorerTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.explorerTable.setHorizontalHeaderItem(3, item)
        self.explorerTable.horizontalHeader().setVisible(True)
        self.explorerTable.horizontalHeader().setCascadingSectionResizes(True)
        self.explorerTable.horizontalHeader().setDefaultSectionSize(50)
        self.explorerTable.horizontalHeader().setHighlightSections(True)
        self.explorerTable.horizontalHeader().setSortIndicatorShown(False)
        self.explorerTable.horizontalHeader().setStretchLastSection(True)
        self.explorerTable.verticalHeader().setVisible(False)
        self.explorerTable.verticalHeader().setCascadingSectionResizes(False)
        self.verticalLayout.addWidget(self.explorerTable)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.fileLabel = QtGui.QLabel(Form)
        self.fileLabel.setMaximumSize(QtCore.QSize(16777215, 15))
        self.fileLabel.setStyleSheet(_fromUtf8("color: #ecf0f1;"))
        self.fileLabel.setObjectName(_fromUtf8("fileLabel"))
        self.horizontalLayout_5.addWidget(self.fileLabel)
        self.dirLabel = QtGui.QLabel(Form)
        self.dirLabel.setMaximumSize(QtCore.QSize(16777215, 15))
        self.dirLabel.setStyleSheet(_fromUtf8("color: #e67e22;"))
        self.dirLabel.setObjectName(_fromUtf8("dirLabel"))
        self.horizontalLayout_5.addWidget(self.dirLabel)
        self.hfileLabel = QtGui.QLabel(Form)
        self.hfileLabel.setMaximumSize(QtCore.QSize(16777215, 15))
        self.hfileLabel.setStyleSheet(_fromUtf8("color: #9b59b6;"))
        self.hfileLabel.setObjectName(_fromUtf8("hfileLabel"))
        self.horizontalLayout_5.addWidget(self.hfileLabel)
        self.hdirLabel = QtGui.QLabel(Form)
        self.hdirLabel.setMaximumSize(QtCore.QSize(16777215, 15))
        self.hdirLabel.setStyleSheet(_fromUtf8("color: #3498db;"))
        self.hdirLabel.setObjectName(_fromUtf8("hdirLabel"))
        self.horizontalLayout_5.addWidget(self.hdirLabel)
        self.selectedLabel = QtGui.QLabel(Form)
        self.selectedLabel.setStyleSheet(_fromUtf8("color: #f1c40f;"))
        self.selectedLabel.setObjectName(_fromUtf8("selectedLabel"))
        self.horizontalLayout_5.addWidget(self.selectedLabel)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.dirfilesLabel = QtGui.QLabel(Form)
        self.dirfilesLabel.setObjectName(_fromUtf8("dirfilesLabel"))
        self.horizontalLayout_5.addWidget(self.dirfilesLabel)
        self.dirfilesCountLabel = QtGui.QLabel(Form)
        self.dirfilesCountLabel.setObjectName(_fromUtf8("dirfilesCountLabel"))
        self.horizontalLayout_5.addWidget(self.dirfilesCountLabel)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.explorerTable.setSortingEnabled(False)
        item = self.explorerTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Type", None))
        item = self.explorerTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Name", None))
        item = self.explorerTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Date Modified", None))
        item = self.explorerTable.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Size", None))
        self.fileLabel.setText(_translate("Form", "File", None))
        self.dirLabel.setText(_translate("Form", "Directory", None))
        self.hfileLabel.setText(_translate("Form", "Hidden File", None))
        self.hdirLabel.setText(_translate("Form", "Hidden Directory", None))
        self.selectedLabel.setText(_translate("Form", "Selected", None))
        self.dirfilesLabel.setText(_translate("Form", "Directories / Files:", None))
        self.dirfilesCountLabel.setText(_translate("Form", "0", None))
