"""
1. remove stop words
2. make list of synonyms of user input
3. get all non stop words from website if exists
and compare with synonym list of user side

4. also create antonym list
"""

import nltk
import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet
#nltk.download() download has been complete
#sentence="This is any delimeter, by default it is space."
#tokens=nt.word_tokenize(sentence)
#print(sent_tokenize(sentence))
#for i in range(0, len(tokens)):
#    print(tokens[i])
#sent="Hello world! Where are you? I am fine. Good night. Today's Headlines are"
#p=re.compile('[a-z]')

"""
print(sent_tokenize(sent))
print(word_tokenize(sent)) 
print(sent.split())

#convert to lower character
lowerWords=word_tokenize(sent)
for i in range(0, len(lowerWords)):
    lowerWords[i]=lowerWords[i].lower()

#to remove punctuation marks
newWords=[]
for i in range(0, len(lowerWords)):
    s=re.search(r'[a-z0-9\']+', lowerWords[i])
    if s:
        newWords.append(lowerWords[i])
"""


sent="Hello world! Where are you? I am fine. Good night. Today's Headlines are"
words=[]
matches=re.findall(r'[a-zA-Z0-9\']+', "Hello world! Where are you? I am fine. Good night. Today's Headlines are")
for match in matches:
    print(match.lower())
    words.append(match.lower())

#this is to collect sysnonyms
wordSynonyms=[]
for syn in wordnet.synsets('Computer'):
    for lemma in syn.lemmas():
        wordSynonyms.append(lemma.name())
print(wordSynonyms)        



"""
problem with split is that it takes continous letters aas words
so 'when?' is also considered a word(inlcuding '?') and not only when
"""
