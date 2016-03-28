# coding=utf-8

import os
from languages import __all__

server_payload = '''

# CLIENTS TABLE HEADER
self.serversTable.horizontalHeaderItem(0).setText(%s) #
self.serversTable.horizontalHeaderItem(1).setText(%s)
self.serversTable.horizontalHeaderItem(2).setText(%s)
self.serversTable.horizontalHeaderItem(3).setText(%s)
self.serversTable.horizontalHeaderItem(5).setText(%s)
self.serversTable.horizontalHeaderItem(6).setText(%s)
self.serversTable.horizontalHeaderItem(7).setText(%s)
self.serversTable.horizontalHeaderItem(8).setText(%s)

'''


def load_languages():
    return __all__

class ChooseLanguage:

    def __init__(self, lang):
        pass
