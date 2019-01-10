from junior_functions.junior_fundamental_ops.communication import *

def write(file):
    speak("starting recording sir")
    print("[INFO] Started recording")
    text = listen()
    file_handler = open("C:/Users/noxx.inc/desktop/cache/" + file + ".txt", "w+")
    file_handler.write(text)
    file_handler.close()
    print("[INFO] Saved file as " + file + ".txt")
    speak('saved file as ' + file + ', in cache sir')  # verified
