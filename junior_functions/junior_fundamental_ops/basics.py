from junior_functions.junior_fundamental_ops.communication import *

def write(text = None):
    speak("what should be the file name sir")
    file = 'default'
    file = listen()
    speak("starting recording sir")
    print("[INFO] Started recording")
    text_to_write = listen()
    file_handler = open("C:/Users/noxx.inc/desktop/cache/" + file + ".txt", "w+")
    file_handler.write(text_to_write)
    file_handler.close()
    print("[INFO] Saved file as " + file + ".txt")
    speak('saved file as ' + file + ', in cache sir')  # verified
