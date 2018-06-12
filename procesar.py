from nltk import word_tokenize
from nltk import sent_tokenize
import io
from PyPDF2 import PdfFileReader

with open("pliego-ejemplo02.pdf",'rb') as f:
    if f:
        ipdf = PdfFileReader(f)
        print("DocumentInformation : "+str(ipdf.documentInfo.producer))
        print("Number of pages:-"+str(ipdf.numPages))
        for page in ipdf.pages: 
           print(page.extractText().encode('utf-8'));
            #print(page.extractText().encode('ascii', 'ignore'))
            #
#            print("nueva pagina")
#        textpdf = [ for p in ipdf.pages]
#        mifile = io.open("test.txt", 'w', encoding='utf8') #open("test.txt","w")
#        for item in textpdf:
#            mifile.write(item)
#        mifile.close()


'''archivo = "test.txt"
f1 = io.open(archivo, 'rU', encoding='utf-8')
#file1 = open(archivo,"r")
text = f1.read()
print(text[:45])

# obtengo los tokens
tokens = word_tokenize(text)
print(type(tokens))
print(len(tokens))
print(tokens[:10])

oraciones = sent_tokenize(text)
print(len(oraciones))
print(oraciones[:2])
'''