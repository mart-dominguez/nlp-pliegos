# nlp-pliegos
procesar pliegos

# herramientas
* python-docx : https://python-docx.readthedocs.io/en/latest/#what-it-can-do
* https://pandas.pydata.org
* http://www.numpy.org
* https://www.nltk.org/install.html
* https://pythonhosted.org/PyPDF2/


# Descargar modulos de nltk
## tokenizer
```python
$ python3
>>> import nltk
>>> nltk.download('punkt')
```
## wordnet
```python
>>> import nltk
>>> nltk.download('wordnet')
>>> nltk.download('omw')
>>> from nltk.corpus import wordnet as wn
>>> wn.synsets('bank')[0].lemma_names('spa')
```
Descargar corpus de wordnet en español.
https://stackoverflow.com/questions/26474731/missing-spanish-wordnet-from-nltk 

Unigram y bigram
https://stackoverflow.com/questions/14732465/nltk-tagging-spanish-words-using-a-corpus


https://stackoverflow.com/questions/14732465/nltk-tagging-spanish-words-using-a-corpus

Analisis https://pmoracho.github.io/blog/2017/01/04/NLTK-mi-tutorial/ 

https://www.safaribooksonline.com/library/view/hands-on-natural-language/9781789139495/a41f8ef1-1ef4-4967-8d13-3ab655d66f8f.xhtml
from Hands-On Natural Language Processing with Python 

https://www.nltk.org/book/ch05.html

https://nlp.stanford.edu/software/tagger.shtml

FORMATO https://nlp.stanford.edu/software/spanish-faq.shtml