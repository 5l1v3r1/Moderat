from ui.builder import Ui_Form as builderUi
from PyQt4.QtGui import *


class Builder(QWidget, builderUi):

    def __init__(self, args):
        QWidget.__init__(self)
        self.setupUi(self)