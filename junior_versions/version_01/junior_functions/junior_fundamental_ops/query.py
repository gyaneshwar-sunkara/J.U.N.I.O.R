import numpy as np

import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer

stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')

def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]


functionalities = {
#'converse': "hello junior, hey, are you there",
'limit': "limited functionalities, can't process",
'write': "write a text, letter",
'music': "play music, listen to songs",
'movie': "play movie, watch film's",
'emails': "read email's, check if i have any email"
}

def function(text):
    score = []
    for i in functionalities.items():
        score.append(cosine_sim(text, i[1]))

    return list(functionalities.keys())[np.argmax(score)]  #verified
