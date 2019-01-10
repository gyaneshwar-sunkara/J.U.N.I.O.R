# First working version of junior.
# Follows a symantic definition for syntactic codex.

print("[INFO] Initializing")

print("[INFO] Importing funtionalities")
from junior_functions.junior_fundamental_ops.basics import *
from junior_functions.junior_fundamental_ops.communication import *
from junior_functions.junior_fundamental_ops.email import *
from junior_functions.junior_fundamental_ops.media import *

Greeting = ["good", "morning", "junior"]
Greetings = ["Hello sir, what is the plan for today",
             "Hi sir, what are you up to."]
_Greetings = ["See you next time sir",
              "Have a good time sir",
              "Later sir"]
_text = ["write","note", "text", "filename"]
_music = ["some", "music"]
_movie = ["movie", "video"]
email = ["read", "emails", "email", "check"]
_search = ["search", "look", "go"]
_web = ["youtube.com", "gogoanime.sh",
        "https://www.youtube.com/results?search_query=",
        "https://www.google.com/search?q="]

while True:
    text = listen()
    print("[INFO] STT: " + text)
    cache = text.lower().strip().split()
    if Greeting[0] in cache or Greeting[1] in cache or Greeting[2] in cache: speak(Greetings[np.random.randint(len(Greetings))])
    if cache[0] in ["thank", "quit"]: speak(_Greetings[np.random.randint(len(_Greetings))]);break
    if cache[0] in _text:
        write(cache[1])
    if cache[0] == "play" or cache[0] == "listen":
        if (_music[0] in cache or _music[1] in cache):
            path = music()
            file, performer, album = file_details(path)
            speak("playing, " + file + " from " + album + ", by " + performer + " sir")
            play(path)
        if (_movie[0] in cache or _movie[1] in cache):
            path = movie()
            file, folder, title = file_details(path)
            speak("playing,"+ title + "sir")
            play(path)
    if (email[0] in cache or email[3] in cache) and (email[1] in cache or email[2] in cache):
        print("[INFO] Gathering emails")
        speak("gathering emails sir.")
        _email = emails()
        speak("reading emails sir.")
        for i in range(5):
            speak("from "+_email[0][i]+ ".")
            _email[1][i] = _email[1][i].replace('&#39;','\'')
            speak(_email[1][i])

        print("[INFO] Completed reading")
        speak("that's it for now sir")

print("[INFO] Aborting")
