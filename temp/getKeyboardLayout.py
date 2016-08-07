import ctypes
from decimal import *

# 67699721 ENG
# -257227721 GEO
# -257752039 RUS

user32 = ctypes.windll.user32

foregroundWindow = user32.GetForegroundWindow()
tid = user32.GetWindowThreadProcessId(foregroundWindow, 0)
print user32.GetKeyboardLayout(tid)