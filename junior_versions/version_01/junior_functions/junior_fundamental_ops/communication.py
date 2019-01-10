import speech_recognition as sr

import pyttsx3

def listen():
    sample_rate = 44100
    chunk_size = 1024
    device_id = 1

    r = sr.Recognizer()

    with sr.Microphone(device_index = device_id,sample_rate = sample_rate, chunk_size = chunk_size) as source:
        while True:
            r.adjust_for_ambient_noise(source)
            print("[INFO] Listening")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                return text
            except sr.UnknownValueError:
                print("[INFO] No audio found")
            except sr.RequestError:
                print("[INFO] Can't connect to Goole")  # verified

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait();
    engine.stop()  # verified
