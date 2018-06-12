from __future__ import print_function
import nltk
import spaghetti as sgt
from nltk.corpus import cess_esp as cess
from nltk import word_tokenize
from nltk import sent_tokenize
from docx import Document

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


# Default Spaghetti tagger.
print (sgt.pos_tag(words), end="\n\n")

spa_tagger = sgt.CESSTagger()
# POS tagger trained on unigrams of CESS corpus.
spa_unigram_tagger = spa_tagger.uni
print (spa_unigram_tagger.tag(words))

# POS tagger traned on bigrams of CESS corpus.
spa_bigram_tagger = spa_tagger.bi
print (spa_bigram_tagger.tag(words))

spamwe_tagger = sgt.CESSTagger(use_mwe=True) # Recognizes Multi-Word Expressions as one token.
# POS tagger trained on unigrams that includes MWEs from the CESS.
spamwe_unigram_tagger = spamwe_tagger.uni
print (spamwe_unigram_tagger.tag(words))

# POS tagger trained on bigrams that includes MWEs from the CESS.
spamwe_bigram_tagger = spamwe_tagger.bi
print (spamwe_unigram_tagger.tag(words))