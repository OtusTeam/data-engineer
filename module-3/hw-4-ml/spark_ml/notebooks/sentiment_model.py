from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
import re
import nltk
from nltk.stem.porter import PorterStemmer

def preprocessor(text):
    cleaned = re.sub("[^a-zA-Z]", " ", text)
    return cleaned

def tokenizer(text):
    tokens = [t for t in nltk.word_tokenize(text) if len(t)>3]
    stems = []
    for item in tokens:
        stems.append(PorterStemmer().stem(item))
    return stems


vectorizer = TfidfVectorizer(preprocessor=preprocessor,tokenizer=tokenizer)


pipeline = Pipeline([
    ('tfidf', vectorizer),
    ('clf', RandomForestClassifier()),
])


parameters = {
    'tfidf__max_df': (0.5, 0.75, 1.0),
    'clf__n_estimators': (40,60,100),
    'clf__max_depth': (5,8)
}

