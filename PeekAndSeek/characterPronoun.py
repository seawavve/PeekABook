#대명사 체킹

import pandas as pd
import spacy

data=pd.read_csv('./LittleRedRidingHood.csv')
data=data.dropna(how='any')
#display(data)
pronoun_list=[' he ',' she ']
for s in data['sentence']:
    print(s)
    s=s.lower()
    for pronoun in pronoun_list:
        if pronoun in s:print('!!!!!!!!')
            

# a='Happybithd to you'
# if 'pyb' in a:print('wow')
