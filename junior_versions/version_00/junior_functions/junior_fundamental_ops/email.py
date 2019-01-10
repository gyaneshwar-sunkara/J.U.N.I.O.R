from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file

def emails():
    store = file.Storage(r'C:\cygwin64\home\PC\Junior\token.json')
    creds = store.get()
    service = build('gmail', 'v1', http=creds.authorize(Http()))
    msg_ids = service.users().messages().list(userId='me').execute()
    thread_ids = []
    for i in range(10):
        thread_ids.append((i, msg_ids['messages'][i]['id']))

    print("[INFO] Thread_ids obtained")
    threads = []
    for i in range(10):
        threads.append(service.users().threads().get(userId='me', id=thread_ids[i][1]).execute())

    print("[INFO] Messages obtained")
    froms = []
    subjects = []
    for i in range(10):
        for msg in threads[i]['messages'][0]['payload']['headers']:
            if msg['name'] == 'From': froms.append(msg['value'].split('<')[0])
            if msg['name'] == 'Subject': subjects.append(msg['value'])
    return [froms, subjects]  # verified

def send_email():
    return None
