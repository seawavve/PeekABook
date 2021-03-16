
import pandas as pd

def find_characters(data):
    characters=[]

    for content in contents:
        if type(content)==float:continue
        doc = nlp(content)

        for ent in doc.ents:
            if (ent.label_=='ORG') or (ent.label_=='PERSON'):
                #print(ent.text) 
                if ent.text not in characters:characters.append(ent.text) 
            #print(ent.text, ent.label_)
        #displacy.render(doc,style='ent',jupyter=True,options={'distance':90})
    return characters



data=pd.read_csv('./LittleRedRidingHood.csv')
data=data.dropna(how='any')
print(find_characters(data))
