import numpy as np

import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer

stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

non_stop_words = ['what', 'is', 'how', 'to', 'who', 'are', 'of', 'get', 'me', 'give', 'yourself']
my_stop_words = [e for e in nltk.corpus.stopwords.words('english') if e not in non_stop_words]

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words=set(my_stop_words))

def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]


conversation = {
'limit': "limited functionalities, can't process",
'greeting': 'hey, junior, hello, morning, greetings',
'intro': 'describe yourself, tell about yourself, how do you work',
'chat': 'how are you',
'QandA': 'takes requests as questions and provides answers',
'gratification': 'thank you, quit, shutdown, later'
}

functionalities = {
'write': "write a text, letter",
'music': "play music, listen to songs",
'movie': "play movie, watch film's",
'emails': "read email's, check if i have any email",
'QandA': 'look for , find out about, what\'s, search for, what is, how to make create, who is are, on google',
'img_search': 'display give, get me, show images of, pictures of, pics',
'photo_capture': "take a , capture him , on camera snap a , remember him her",
'recogniser' : "face faceial recognition turn on"
}


def function(text):
    score = []
    for i in {**conversation, **functionalities}.items():
        score.append(cosine_sim(text, i[1]))
    return list({**conversation, **functionalities}.keys())[np.argmax(score)]  # verified
