from junior_functions.junior_fundamental_ops.communication import *

from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file

def emails(text = None):
    print("[INFO] Gathering emails")
    speak("gathering emails sir.")
    store = file.Storage(r'C:\cygwin64\home\PC\Junior\token.json')
    creds = store.get()
    service = build('gmail', 'v1', http=creds.authorize(Http()))
    msg_ids = service.users().messages().list(userId='me').execute()
    thread_ids = []
    for i in range(10):
        thread_ids.append((i, msg_ids['messages'][i]['id']))
    print("[INFO] Thread_ids obtained")
    messages = []
    for i in range(10):
        messages.append(service.users().messages().get(userId='me', id=thread_ids[i][1]).execute())
    print("[INFO] Messages obtained")
    sender = []
    subjects = []
    for i in range(10):
        for msg in messages[i]['payload']['headers']:
            if msg['name'] == 'From': sender.append(msg['value'].split('<')[0])
            if msg['name'] == 'Subject': subjects.append(msg['value'])
    speak("reading emails sir.")
    for i in range(5):
        speak("from " + sender[i] + ".")
        subjects[i] = subjects[i].replace('&#39;','\'')
        speak(subjects[i])
    print("[INFO] Completed reading")
    speak("that's it for now sir")  # verified

def send_email():
    return None
