#-*- coding: utf8 -*-

# about the tagger: http://nlp.stanford.edu/software/tagger.shtml 
# about the tagset: nlp.lsi.upc.edu/freeling/doc/tagsets/tagset-es.html
import nltk

from nltk.corpus import cess_esp as cess
from nltk import word_tokenize
from nltk import sent_tokenize
from docx import Document
from nltk import UnigramTagger as ut
from nltk import BigramTagger as bt
from nltk.tag import StanfordPOSTagger

# Read the corpus into a list, 
# each entry in the list is one sentence.
cess_sents = cess.tagged_sents()
# Train the unigram tagger
uni_tag = ut(cess_sents)

text = ""
f = open('PLIEGO_EJEMPLO.docx', 'rb')
document = Document(f)
for i in document.paragraphs:
    text +=i.text
f.close()
print("=========== PRIMEROS 45 ========")
print(text[:45])

# obtengo los tokens
tokens = word_tokenize(text)
words = tokens[:250]
print("=========== TOKENS 50  ========")
print(words)

"""archivo_salida = open("my_tokens.txt","w")
for word in tokens:
    print(word,file=archivo_salida)
"""
text = nltk.Text(tokens)
print(type(tokens))
print(len(tokens))
print(tokens[:10])

text.collocations()

stanford_dir = '/home/mdominguez/Documentos/devs/ml/stanford-postagger-full-2018-10-16/'
jarfile = stanford_dir + 'stanford-postagger.jar'
modelfile = stanford_dir + 'models/spanish.tagger'

spanish_postagger = StanfordPOSTagger(model_filename=modelfile, path_to_jar=jarfile, encoding='utf8')


tagged_words = spanish_postagger.tag(words)
print(tagged_words[:100])
