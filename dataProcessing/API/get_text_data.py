#!/usr/bin/env python
# coding: utf-8

# In[2]:


#csv파일을 읽어와서 긍정,부정,중립 폴더에 한 문장씩 집어넣는 python3파일입니다.
import pandas as pd
data=pd.read_csv('./Junglebook_labelled.csv')
display(data)


# In[9]:


def get_pos_text(s,i):
    f = open('./Pos/'+str(i)+".txt", 'w')
    f.write(s)
    f.close()
    
def get_neg_text(s,i):
    f = open('./Neg/'+str(i)+".txt", 'w')
    f.write(s)
    f.close()

def get_mod_text(s,i):
    f = open('./Mod/'+str(i)+".txt", 'w')
    f.write(s)
    f.close()
    
def main():
    for i in range(len(data)): #len(data)
        if data.loc[i,'label']==2:get_pos_text(data.loc[i,'sentence'],i)
        elif data.loc[i,'label']==1:get_mod_text(data.loc[i,'sentence'],i)
        else: get_neg_text(data.loc[i,'sentence'],i)
    return 0

if __name__=='__main__':
    main()


# In[ ]:




