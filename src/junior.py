# Introducing Question and Answer feature: extraction from a large corpus of wikipedia wiki.
# Compartmentalizing conversation

print("[INFO] Initializing")

print("[INFO] Importing fundamental funtionalities")
from junior_functions.junior_fundamental_ops.query import *
from junior_functions.junior_fundamental_ops.communication import *
from junior_functions.junior_fundamental_ops.basics import *
from junior_functions.junior_fundamental_ops.email import *
from junior_functions.junior_fundamental_ops.media import *

print("[INFO] Importing advanced funtionalities")
from junior_functions.junior_advanced_ops.conversation import *
from junior_functions.junior_advanced_ops.q_and_a import *
from junior_functions.junior_advanced_ops.recorder import *
from junior_functions.junior_advanced_ops.recogniser import *

while True:
    text = listen()
    print("[INFO] STT: " + text)
    func = function(text)
    print("[INFO] Performing function: " + func)
    locals()[func](text)
