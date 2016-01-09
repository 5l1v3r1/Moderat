from PyQt4.QtGui import *
from PyQt4.QtCore import *

import pyaudio
import socket
import threading
from array import array

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

        self.defaultInputDeviceNameLabel.setText(get(self.sock, 'getDefaultInputDeviceName', 'getname'))

        self.listenButton.clicked.connect(self.startListen)
        self.stopButton.clicked.connect(self.stopListen)

    def stopListen(self):
        send(self.sock, 'stopAudio', 'stopaudio')
        try:
            self.audio.active = False

            self.stopVolume()

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
        rate = self.rateDrop.currentText()
        data = get(self.sock, 'startAudio %s' % self.rate, 'startaudio')
        if data == 'audioStarted':
            self.audio = ListenAudio(self.sock, int(self.rate))
            self.audio.start()
            self.startVolume()
            self.listenButton.setDisabled(True)
            self.recordButton.setDisabled(False)
            self.stopButton.setDisabled(False)
        else:
            self.listenButton.setDisabled(False)
            self.recordButton.setDisabled(True)
            self.stopButton.setDisabled(True)

    def startVolume(self):
        # Create a QTimer
        self.timer = QTimer()
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.setVolume)
        self.timer.start(10)

    def stopVolume(self):
        self.timer.stop()

    def setVolume(self):
        try:
            self.volume = self.audio.volume
            self.volumeProgress.setValue(int(self.volume))
        except AttributeError:
            pass

    def closeEvent(self, event):
        self.stopListen()


class ListenAudio(threading.Thread):
    def __init__(self, sock, rate):
        super(ListenAudio, self).__init__()

        self.sock = sock
        self.active = True
        self.rate = rate
        self.volume = 0

        # Pyaudio Initialization
        self.chunk = 1024
        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(format=pyaudio.paInt16, channels=1, rate=self.rate, output=True)

    def run(self):
        while self.active:
            try:
                chunk = self.sock.recv(1024)
                sound_data = array('h', chunk)
                self.volume = max(sound_data)
                self.stream.write(chunk)
            except (socket.error, ValueError):
                break
        self.stream.close()
        self.p.terminate()
