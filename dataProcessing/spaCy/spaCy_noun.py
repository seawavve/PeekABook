import pandas as pd
data=pd.read_csv('./Cinderella.csv')
data

import spacy
from spacy import displacy
nlp=spacy.load('en_core_web_sm')
contents=data['Cinderella']
str_format = "{:>25}"*4

for content in contents:
    nouns=[]
    if type(content)==float:continue
    doc = nlp(content)
    #displacy.render(doc, style="dep",jupyter=True,options={'distance':90})
    #displacy.render(doc,style='ent',jupyter=True,options={'distance':90})
    #for token in doc:
    #    print(token.text, token.pos_, token.tag_, token.ent_type_) 
    for chunk in doc.noun_chunks:
        nouns.append(chunk.text)
        #print(str_format.format(chunk.text, chunk.root.text, chunk.root.dep_, chunk.root.head.text))
    print(nouns)

#문장을 단순화 하면 명사를 뽑는 정확도가 더 높아지지 않을까?

#이 단어들로 word 유사도를 찍어서 cluster로 만들면 사람과 사물을 확실히 구분할 수 있지 않을까?
doc = nlp('time girl Cinderella she stepsisters who they dress chores')
for t1 in doc:
    for t2 in doc:
        print(t1,t2,':',t1.similarity(t2))
