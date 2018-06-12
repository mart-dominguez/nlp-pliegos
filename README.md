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
