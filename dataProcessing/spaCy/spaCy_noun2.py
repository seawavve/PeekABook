import pandas as pd
data=pd.read_csv('./Cinderella.csv')
data

import spacy
from spacy import displacy
nlp=spacy.load('en_core_web_sm')
contents=data['sentence']
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
    total=0
    for t2 in doc:
        #print(t1,t2,':',t1.similarity(t2))
        total+=float(str(t1.similarity(t2)))
    print(t1,total)

# time 1.4338764440000002
# girl 2.7071105060000002
# Cinderella 2.272461083
# she 1.9354007040000003
# stepsisters 1.967431927
# who 1.2574595547
# they 2.236996789
# dress 1.8283941267
# chores 2.115779127
# 결론: 다 비슷비슷하게 나와서 spacy자체 벡터를 사용하진 말아야겠다
