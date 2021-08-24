import pandas as pd
import spacy


def find_characters(data):
    characters=[]
    nlp=spacy.load('en_core_web_sm')
    contents=data['sentence']

    for content in contents:
        if type(content)==float:continue
        doc = nlp(content)

        for ent in doc.ents:
            if (ent.label_=='ORG') or (ent.label_=='PERSON'):
                #print(ent.text) 
                if ent.text not in characters:characters.append(ent.text) 
            #print(ent.text, ent.label_)
        #displacy.render(doc,style='ent',jupyter=True,options={'distance':90})
    characters=filter_characters(characters)
    return characters

def filter_characters(characters):
    filter_words=["Poof",'Knock','Hyap','Boo'] #의성어,의태어 거르기
    for filter_word in filter_words:
        if filter_word in characters:
            characters.remove(filter_word)
        
    return characters

data=pd.read_csv('./LittleRedRidingHood.csv')
data=data.dropna(how='any')
print(find_characters(data))

data=None
data=pd.read_csv('./Cinderella.csv')
data=data.dropna(how='any')
print(find_characters(data))

data=None
data=pd.read_csv('./HanselandGretel.csv')
data=data.dropna(how='any')
print(find_characters(data))


#여기에 사람이 손으로 아빠,엄마, 등등 가족,사람이면 추가하기
#의성어 의태어 제거 -> 수기 or threshold로 거르기
