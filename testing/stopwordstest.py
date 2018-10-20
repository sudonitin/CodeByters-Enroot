import nltk
import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet, stopwords


para=""
words=[]

matches=re.findall(r'[a-zA-Z0-9\']+', "Hello world! Where are you? I am fine. Good night. Today's Headlines are")
for match in matches:
    words.append(match.lower())
print(words)

sw=stopwords.words('english')
cleanWords=[]

i=0
l=len(words)
count=0
while i<len(words):
    j=0    
    while j<len(sw):
        try:
            if words[i]==sw[j]:
                words.pop(i)
                i=i-1                
        except:
            break
        j=j+1
    i=i+1    
print(words)
"""
maxwordlen=len(words)
maxswlen=len(sw)

for i in range(0, maxwordlen):
    for j in range(0, maxswlen):
        if(words[i]==sw[j]):
            words.pop(i)
            maxwordlen=maxwordlen-1
"""
                      
#recognise stop words
#stopwords.words('english')
#stopwords are words that are most commonly used 
#words like 'the', 'is', 'a', 'before', 'after' etc. This makes it easy
#for search engines to index pages.    
    

