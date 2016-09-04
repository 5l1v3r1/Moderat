from PyQt4.QtGui import *
from PyQt4.QtCore import *

import main_ui
import idle
import os

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
        self.plugins_dir = args['plugins_dir']

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
        self.output.setStyleSheet('''
        color: #c9f5f7;
        border: none;
        background-color: #34495e;
        background-image: url(assets/bg.png);
        background-repeat: no-repeat;
        background-position: center;
        padding: 5px;
        padding-top: 1px;''')
        self.splitter.addWidget(self.output)
        self.output.setHidden(True)

        self.runButton.clicked.connect(self.run_script)
        self.addPluginButton.clicked.connect(self.insert_plugin)
        self.saveButton.clicked.connect(self.save_plugin)
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

    def save_plugin(self):
        script_name, ok = QInputDialog.getText(self, _('SCRIPTING_PLUGIN_NAME'), _('SCRIPTING_PLUGIN_NAME'), QLineEdit.Normal)
        if ok:
            script_description, ok = QInputDialog.getText(self, _('SCRIPTING_PLUGIN_DESC'), _('SCRIPTING_PLUGIN_DESC'), QLineEdit.Normal)
            if ok:
                # Check if script_name exists
                if script_name in self.plugins.keys():
                    warn = QMessageBox(QMessageBox.Warning, _('SCRIPTING_PLUGIN_EXISTS'), _('SCRIPTING_PLUGIN_EXISTS'))
                    ans = warn.exec_()
                    return
                with open(os.path.join(self.plugins_dir, str(script_name)+'.py'), 'w') as plugin_file:
                    payload = 'plugin_name = r"""%s"""\n' % script_name
                    payload += 'plugin_description = r"""%s"""\n' % script_description
                    payload += 'r_source = r"""%s"""\n' % self.idle.getTextEdit()
                    payload += 'l_source = r"""%s"""\n' % self.lidle.getTextEdit()
                    plugin_file.write(payload)
                    warn = QMessageBox(QMessageBox.Warning, _('SCRIPTING_PLUGIN_SAVED'), _('SCRIPTING_PLUGIN_SAVED'))
                    ans = warn.exec_()

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
