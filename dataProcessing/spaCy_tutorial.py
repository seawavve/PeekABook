import spacy
from spacy import displacy
nlp=spacy.load('en_core_web_sm')
doc = nlp("JSJbaby is the super team with professor Park")
displacy.render(doc, style="dep",jupyter=True,options={'distance':90})

displacy.render(doc,style='ent',jupyter=True,options={'distance':90})
