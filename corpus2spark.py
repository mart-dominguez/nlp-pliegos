#-*- coding: utf8 -*-

# about the tagger: http://nlp.stanford.edu/software/tagger.shtml 
# about the tagset: nlp.lsi.upc.edu/freeling/doc/tagsets/tagset-es.html
import nltk
import numpy as np
import matplotlib.pyplot as plt

from nltk.corpus import cess_esp as cess
from nltk import word_tokenize
from nltk import sent_tokenize
from docx import Document
from nltk import UnigramTagger as ut
from nltk import BigramTagger as bt
from nltk.tag import StanfordPOSTagger

from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


def sentence_features(st, ix):    
    d_ft = {}    
    d_ft['word'] = st[ix]
    d_ft['dist_from_first'] = ix - 0
    d_ft['dist_from_last'] = len(st) - ix
    d_ft['capitalized'] = st[ix][0].upper() == st[ix][0]
    d_ft['prefix1'] = st[ix][0]
    d_ft['prefix2'] = st[ix][:2]
    d_ft['prefix3'] = st[ix][:3]
    d_ft['suffix1'] = st[ix][-1]
    d_ft['suffix2'] = st[ix][-2:]
    d_ft['suffix3'] = st[ix][-3:]    
    d_ft['prev_word'] = '' if ix==0 else st[ix-1]    
    d_ft['next_word'] = '' if ix==(len(st)-1) else st[ix+1]    
    d_ft['numeric'] = st[ix].isdigit()    
    return d_ft

def get_untagged_sentence(tagged_sentence):
    [s,t] = zip(*tagged_sentence)
    return list(s)
    
def ext_ft(tg_sent):
    sent, tag = [], []
 
    for tg in tg_sent:
        for index in range(len(tg)):
            sent.append(sentence_features(get_untagged_sentence(tg), index))
            tag.append(tg[index][1])
 
    return sent, tag

# Read the corpus into a list, 
# each entry in the list is one sentence.
cess_sents = cess.tagged_sents()

corpus_file = open("corpus01.txt","w")
for word in cess_sents:
    print(word,file=corpus_file)

# Train the unigram tagger
uni_tag = ut(cess_sents)

X,y = ext_ft(cess_sents)

corpus_X_file = open("corpus_X.txt","w")
for word in X:
    print(word,file=corpus_X_file)


corpus_y_file = open("corpus_y.txt","w")
for word in y:
    print(word,file=corpus_y_file)