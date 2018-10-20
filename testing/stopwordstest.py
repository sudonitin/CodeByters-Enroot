import nltk
import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet, stopwords


para="Hello world! Where are you? I am fine. Good night. Today's Headlines are"
para1="At least 60 people celebrating Dussehra were killed after a train ran over hundreds standing on a railway track in Amritsar on Friday evening. As Ravan's effigy - located very close to the tracks at Jaura Phatak - was lit and fireworks went off, a section of the crowd retreated towards the tracks, where a large number of people were already standing to watch the celebrations. The people who were hit could not see or hear the train due to the exploding crackers. An angry crowd shouted slogans against local legislator Navjot Kaur Sidhu, who was present as chief guest during the event. Chief Minister Amarinder Singh has ordered an inquiry into the accident."
para2=""
words=[]

matches=re.findall(r'[a-zA-Z0-9\']+', para1)
for match in matches:
    words.append(match.lower())
print(words)

sw=stopwords.words('english')
i=0
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
cleanWords=words

wordSynonyms=[]
for matchedWords in cleanWords:
    for syn in wordnet.synsets(matchedWords):
        for lemma in syn.lemmas():
            wordSynonyms.append(lemma.name().lower())

wordSynonyms.sort()
wordSynonyms2=[]
#remove duplicates from synonyms
for d in wordSynonyms:
    if d not in wordSynonyms2:
        wordSynonyms2.append(d)

print(wordSynonyms2)
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
    

