import pyaudio
import os
from junior_functions.junior_fundamental_ops.communication import *


def photo_capture(text = None):
    speak("identification sir")
    identity = listen()
    os.system("py C:/cygwin64/home/PC/FaceRecogniser/capture.py " + identity)

def audio_recorder(text = None):
    return None

def video_recorder(text = None):
    return None
