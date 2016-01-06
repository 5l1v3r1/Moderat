from PyQt4.QtGui import *
from PyQt4.QtCore import *

import pyaudio
import socket
import os
from libs.modechat import get, send

class mainPopup(QWidget, ):

    def __init__(self, args):
        QWidget.__init__(self)

        self.sock = args['sock']
        self.socket = args['socket']
        self.ipAddress = args['ipAddress']
        self.icon = args['icon']

        self.setWindowTitle('Audio Streaming from - %s - Socket #%s' % (self.ipAddress, self.socket))
        self.setWindowIcon(QIcon(self.icon))

        print 'aq'

        data = get(self.sock, 'startChildSocket audioStreaming', 'socket')
        print data
        if data == 'audioStreaming':
            data = get(self.sock, 'startAudio', 'startAudio')
            print data
            if data == 'audioStreamingStarted':
                self.stream_sock, self.connection = self.server.accept()
                if self.stream_sock:
                    print 'connection accepted'