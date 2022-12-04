from junior_functions.junior_error_check.network_error import *

from junior_functions.junior_fundamental_ops.communication import *
from googleapiclient.discovery import build
from nltk.corpus import stopwords
from urllib.request import Request
import requests
import cv2 as cv
from win32api import GetSystemMetrics
from numpy import argmax

screenresolution = [GetSystemMetrics(1), GetSystemMetrics(0)]
api_key = "AIzaSyD-2jLJ_54dq-e5Uum3H4bTwaxnKNJJPvE"
cx = "005781771271595608202:2tmzzdy9vag"
Q_stop_words = ['search', 'for', 'find', 'out', 'about', 'look', 'into']
stop_words = stopwords.words('english')
stop_words = stop_words + ['images', 'display', 'show', 'pictures', 'get']

if network_status() == True:
    service = build("customsearch", "v1", developerKey = api_key)

    def google_search(search_term, **kwargs):
        print("[INFO] Searching Google for results")
        res = service.cse().list(q=search_term, cx = cx, **kwargs).execute()
        return res['items']
else:
    None

def QandA(text):
    if network_status() == True:
        keywords = [e for e in text.split() if e not in Q_stop_words]
        search_term = ' '.join(keywords)
        print("[INFO] Search term: " + search_term)
        results = google_search(search_term + ' site:en.wikipedia.org', num = 1)
        print("[INFO] Results acquired")
        snippet = results[0]['snippet'].replace('\n', '').replace('...', '').replace('....', '').split('.')[0]
        print("[INFO] Snippet: \n" + snippet)
        print("[INFO] Reading snippet")
        speak(snippet)
    else:
        print("[INFO] Network Unavailable")

def img_search(text):
    if network_status() == True:
        keywords = [e for e in text.split() if e not in stop_words]
        search_term = ' '.join(keywords)
        print("[INFO] Search term: " + search_term)
        results = google_search(search_term, num = 10, searchType = 'image')
        print("[INFO] Acquiring images")
        speak('acquiring images sir')
        snippet = []
        for i in range(10):
            try:
                url = results[i]['link']
                print(url)
                snippet.append(results[i]['snippet'].split()[0] + str(i) + '.jpg')
                print(snippet[i])
                f = open('C:/Users/noxx.inc/desktop/cache/q_and_a/' + snippet[i], 'wb')
                f.write(requests.get(url).content)
                f.close()
            except:
                continue

        print("[INFO] Obtained images")
        speak('these are the relevant images sir')
        print("[INFO] Displaying images")
        for i in range(10):
            try:
                image1 = cv.imread('C:/Users/noxx.inc/desktop/cache/q_and_a/' + snippet[i])
                imageresolution = [image1.shape[1] + 250, image1.shape[0] + 250]
                resolution = screenresolution[argmax(imageresolution)] / max(imageresolution)
                img = cv.resize(image1, (0, 0), fx = resolution, fy = resolution) if image1.shape[0] > screenresolution[0] or image1.shape[0] > screenresolution[0] else image1
                cv.imshow(snippet[i], img)
                k = cv.waitKey(0)
                if k == ord('q'): break
            except:
                continue

        cv.destroyAllWindows()
    else:
        print("[INFO] Network Unavailable")
