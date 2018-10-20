import nltk
import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet, stopwords

class Generator:
    def __init__(self, para):
        self.para=para
           
    def keywordGenerator(self):
        words=[]
        matches=re.findall(r'[a-zA-Z0-9\']+',self.para)
        for match in matches:
            words.append(match.lower())

        sw=stopwords.words('english')
        i=0
        sw=stopwords.words('english')
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
        return cleanWords

    def synonymGenerator(self, cleanWords):
        wordSynonyms=[]
        for matchedWords in cleanWords: 
            for syn in wordnet.synsets(matchedWords):
                for lemma in syn.lemmas():
                    wordSynonyms.append(lemma.name().lower())
        
        wordSynonyms.sort()
        wordSynonyms2=[]

        for d in wordSynonyms:
            if d not in wordSynonyms2:
                wordSynonyms2.append(d)

        return wordSynonyms2

para1="At least 60 people celebrating Dussehra were killed after a train ran over hundreds standing on a railway track in Amritsar on Friday evening. As Ravan's effigy - located very close to the tracks at Jaura Phatak - was lit and fireworks went off, a section of the crowd retreated towards the tracks, where a large number of people were already standing to watch the celebrations. The people who were hit could not see or hear the train due to the exploding crackers. An angry crowd shouted slogans against local legislator Navjot Kaur Sidhu, who was present as chief guest during the event. Chief Minister Amarinder Singh has ordered an inquiry into the accident."
para2="Somewhere around 60 individuals observing Dussehra were killed after a prepare kept running more than hundreds remaining on a railroad track in Amritsar on Friday evening. As Ravan's likeness - found near the tracks at Jaura Phatak - was lit and firecrackers went off, a segment of the group withdrew towards the tracks, where a substantial number of individuals were at that point remaining to watch the festivals. The general population who were hit couldn't see or hear the prepare because of the detonating saltines. An irate group yelled trademarks against neighborhood lawmaker Navjot Kaur Sidhu, who was available as boss visitor amid the occasion. Boss Clergyman Amarinder Singh has requested an investigation into the mischance."
para3="The present government is calling it a natural disaster instead of setting an example. This is not a natural disaster; this is massacre. No FIR is being registered on victims’ statement. An inquiry should happen out of Punjab under a high court."
para4="Moments before 61 people watching a Ravan effigy burn were crushed under a train in Amritsar on Friday evening, an organizer of the Dussehra event had bragged to the chief guest, Congress leader and former lawmaker Navjot Kaur Sidhu, that the crowd there was so enthusiastic to see her that they would stand on the nearby railway tracks and not budge even if hundreds of trains pass by"

gen_1=Generator(para1)
gen_2=Generator(para2)
gen_3=Generator(para3)
gen_4=Generator(para4)

keyWords1=gen_1.keywordGenerator()
keyWords2=gen_2.keywordGenerator()
keyWords3=gen_3.keywordGenerator()
keyWords4=gen_4.keywordGenerator()

synonym1=gen_1.synonymGenerator(keyWords1)

"""
print(keyWords1)
print(keyWords2)
print(keyWords3)
print(keyWords4)
"""
print(synonym1)
