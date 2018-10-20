import re
"""
d matches a digit
"""

p=re.compile('\d+')
#print(p.match('hello93'))
#m=p.match('23hello 34')
#print(m.group())
s=p.search('23 helllo 34')
print(s.group()) #search stops after matching


#use this instead of word_tokenise
matches=re.findall(r'[a-zA-Z0-9]+', "Mr. Hello world! Where are you? I am fine. Good night. Today's Headlines are")
for match in matches:
    print(match.lower())






"""
inpt="aaaaabbbbcccc"
word="Hello this word has spaces"
print(inpt.strip('a'))
print(word.strip('this'))

wordls=word.split()
for i in range(0, len(wordls)):
    print(wordls[i])
"""
