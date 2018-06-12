import nltk
from nltk.corpus import cess_esp as cess
from nltk import word_tokenize
from nltk import sent_tokenize
from docx import Document
#from io import StringIO
#nltk.data.load('tokenizers/punkt/spanish.pickle') 

text = ""
f = open('PLIEGO_EJEMPLO.docx', 'rb')
document = Document(f)
for i in document.paragraphs:
    text +=i.text
f.close()

print(text[:45])

# obtengo los tokens
tokens = word_tokenize(text)
print(type(tokens))
print(len(tokens))
print(tokens[:10])

words = tokens[:10]
tagged_words = nltk.corpus.cess_esp.pos_tag(words)
pos_tag
nouns = []
for (word, tag) in tagged_words:
    print(word+' '+tag)
