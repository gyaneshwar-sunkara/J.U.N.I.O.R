import os
import numpy as np
import re, json

from junior_functions.junior_fundamental_ops.communication import *

def file_details(path):
    file = ''
    sub_folder = path.split('/')[-2].split('(')[0]
    folder = path.split('/')[-3]
    for i in path.split('/')[-1].split():
        i = i.lower()
        if re.search('[a-z]', i[0]):
            file = file + ' ' + i
            if i.endswith('.mp3') or i.endswith('.m4a'): file = file[:-4]
    return file, folder, sub_folder

def movie(text = None, path = "C:/Users/noxx.inc/videos/movies"):
    def find_file(path):
        folders = os.listdir(path)
        if 'desktop.ini' in file: file.remove('desktop.ini')
        folder = folders[np.random.randint(len(folders))]
        path = path + '/' + folder
        return path
    file = []
    while len(file) == 0:
        path = find_file(path)
        file = [file for file in os.listdir(path) if file.endswith('.mp4') or file.endswith('.mkv')]
    path = path + '/' + file[0]
    file, folder, title = file_details(path)
    speak("playing,"+ title + "sir")
    play(path)

def music(text = None, path = "C:/Users/noxx.inc/music"):
    def find_file(path):
        folders = os.listdir(path)
        if 'desktop.ini' in folders: folders.remove('desktop.ini')
        folder = folders[np.random.randint(len(folders))]
        path = path + '/' + folder
        return path
    file = []
    while len(file) == 0:
        path = find_file(path)
        file = [file for file in os.listdir(path) if file.endswith('.mp3') or file.endswith('.zpl') or file.endswith('m4a')]
    path = path + '/' + file[0]
    file, performer, album = file_details(path)
    speak("playing, " + file + " from " + album + ", by " + performer + " sir")
    play(path)

def play(path):
    file = json.dumps(path)
    os.system(file)  # verified

"""
BUG REPORT
results error if :
    file extension not as above specified.
    folder contains other files.
file_details() is useful for files other than .mp3(audio_player has mp3_meta() for .mp3 files)
"""
