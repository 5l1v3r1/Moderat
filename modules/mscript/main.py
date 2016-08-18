from PyQt4.QtGui import *
from PyQt4.QtCore import *

import main_ui
import idle

from libs.data_transfer import data_get
from libs.language import Translate

# Multi Lang
translate = Translate()
_ = lambda _word: translate.word(_word)


class mainPopup(QWidget, main_ui.Ui_Form):

    def __init__(self, args):
        QWidget.__init__(self)
        self.setupUi(self)

        self.sock = args['sock']
        self.client = args['client']
        self.session_id = args['session_id']
        self.plugins = args['plugins']

        self.setWindowTitle('Remote Scripting')

        # init idle with lines
        self.idle = idle.LineTextWidget()
        self.idleLayout.addWidget(self.idle)

        self.runButton.clicked.connect(self.run_script)
        self.fromFileButton.clicked.connect(self.from_file)
        self.clearButton.clicked.connect(self.clear_script)
        self.addPluginButton.clicked.connect(self.insert_plugin)
        self.pluginSearchLine.returnPressed.connect(self.insert_plugin)

        # Shortcuts
        self.connect(QShortcut(QKeySequence('Ctrl+Return'), self), SIGNAL('activated()'), self.run_script)
        self.connect(QShortcut(QKeySequence('Ctrl+P'), self.idle), SIGNAL('activated()'), self.insert_mprint)
        self.connect(QShortcut(QKeySequence('Ctrl+F'), self), SIGNAL('activated()'), self.set_search_focus)

        # Autocompleter
        completer = QCompleter(self.plugins.keys())
        completer.setCompletionMode(QCompleter.PopupCompletion)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.popup().setStyleSheet("background-color: #455F7A;\ncolor: #c9f5f7;")
        self.pluginSearchLine.setCompleter(completer)

    def run_script(self):
        script = self.idle.getTextEdit()
        output = data_get(self.sock, str(script), 'scriptingMode', session_id=self.session_id, to=self.client)
        self.idle.setHtml(output['payload'].replace('\n', '<br>'))

    def insert_plugin(self):
        plugin_name = str(self.pluginSearchLine.text())
        if self.plugins.has_key(plugin_name):
            self.idle.setText(self.plugins[plugin_name]['source'])
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
