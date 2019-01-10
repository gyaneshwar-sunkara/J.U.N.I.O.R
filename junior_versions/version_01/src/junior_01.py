# Improve in functionalities.
# Introducing NLP : No more if statements.

print("[INFO] Initializing")

print("[INFO] Importing funtionalities")
from junior_functions.junior_fundamental_ops.query import *
from junior_functions.junior_fundamental_ops.communication import *
from junior_functions.junior_fundamental_ops.basics import *
from junior_functions.junior_fundamental_ops.email import *
from junior_functions.junior_fundamental_ops.media import *

Greeting = ["good", "morning", "junior"]
Greetings = ["Hello sir, what is the plan for today",
             "Hi sir, what are you up to."]
_Greetings = ["See you next time sir",
              "Have a good time sir",
              "Later sir"]

while True:
    text = listen()
    print("[INFO] STT: " + text)
    cache = text.lower().strip().split()
    if Greeting[0] in cache or Greeting[1] in cache or Greeting[2] in cache: speak(Greetings[np.random.randint(len(Greetings))])
    elif cache[0] in ["thank", "quit"]: speak(_Greetings[np.random.randint(len(_Greetings))]);break
    else:
        func = function(text)
        locals()[func]()

print("[INFO] Aborting")
