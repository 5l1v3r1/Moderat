from PyQt4.QtGui import *
from PyQt4.QtCore import *

import pyaudio
import socket
import threading
import time
import os

from main_ui import Ui_Form

from libs.modechat import get, send

class mainPopup(QWidget, Ui_Form):

    def __init__(self, args):
        QWidget.__init__(self)
        self.setupUi(self)

        self.sock = args['sock']
        self.socket = args['socket']
        self.ipAddress = args['ipAddress']

        self.setWindowTitle('Audio Streaming from - %s - Socket #%s' % (self.ipAddress, self.socket))

        self.recordButton.setDisabled(True)
        self.stopButton.setDisabled(True)

        self.listenButton.clicked.connect(self.startListen)
        self.stopButton.clicked.connect(self.stopListen)

    def stopListen(self):
        send(self.sock, 'stopAudio', 'stopaudio')
        try:
            self.audio.active = False
        except AttributeError:
            pass

        # Flush Buffer
        self.listenButton.setDisabled(True)
        self.recordButton.setDisabled(True)
        self.stopButton.setDisabled(True)

        self.sock.settimeout(1)
        try:
            l = self.sock.recv(1024)
            while l:
                l = self.sock.recv(1024)
        except socket.timeout:
            pass


        self.listenButton.setDisabled(False)
        self.recordButton.setDisabled(True)
        self.stopButton.setDisabled(True)

    def startListen(self):
        data = get(self.sock, 'startAudio', 'startaudio')
        if data == 'audioStarted':
            self.audio = listenAudio(self.sock)
            self.audio.start()
            self.listenButton.setDisabled(True)
            self.recordButton.setDisabled(False)
            self.stopButton.setDisabled(False)
        else:
            print data
            self.listenButton.setDisabled(False)
            self.recordButton.setDisabled(True)
            self.stopButton.setDisabled(True)

    def closeEvent(self, event):
        self.stopListen()

class listenAudio(threading.Thread):
    def __init__(self, sock):
        super(listenAudio, self).__init__()

        self.sock = sock
        self.active = True

        # Pyaudio Initialization
        self.chunk = 1024
        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(format = pyaudio.paInt16, channels = 1, rate = 10240, output = True)

    def run(self):
        while self.active:
            try:
                chunk = self.sock.recv(1024)
                self.stream.write(chunk)
            except socket.error:
                break
        self.stream.close()
        self.p.terminate()