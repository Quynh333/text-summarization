import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import re

def split_sentences(text):
    sentences = re.split(r'(?<=[.!?]) +', text)
    return sentences

def score_sentences(sentences):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(sentences)
    scores = np.sum(tfidf_matrix.toarray(), axis=1)
    return scores

def summarize(text, ratio=0.25):
    sentences = split_sentences(text)
    
    if len(sentences) <= 1:
        return text

    scores = score_sentences(sentences)
    num_sentences = max(1, int(len(sentences) * ratio))

    ranked_sentences = np.argsort(scores)[-num_sentences:]
    ranked_sentences = sorted(ranked_sentences)

    summary = " ".join([sentences[i] for i in ranked_sentences])
    return summary