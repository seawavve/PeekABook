#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
file=pd.read_csv('./hand_labelled/Alice-in-Wonderland.csv')
file.set_axis(['sentence','emo'], 
                    axis='columns', inplace=True)
data=file
data.sort_values(by=['emo'], axis=0,inplace=True)
data.reset_index(inplace=True,drop=True)
display(file)
data_info(file)

file2=pd.read_csv('./hand_labelled/Androvles and the lion.csv')
file2.set_axis(['sentence','emo'], 
                    axis='columns', inplace=True)
#display(file2)
data_info(file2)

file3=pd.read_csv('./hand_labelled/Beauty and the Beast.csv')
file3.set_axis(['sentence','emo'], 
                    axis='columns', inplace=True)
data_info(file3)

file4=pd.read_csv('./hand_labelled/Cinderella.csv')
file4.set_axis(['sentence','emo'], 
                    axis='columns', inplace=True)
data_info(file4)

file5=pd.read_csv('./hand_labelled/Hansel-and-Gretel.csv')
file5.set_axis(['sentence','emo'], 
                    axis='columns', inplace=True)
data_info(file5)

file6=pd.read_csv('./hand_labelled/harrypotter1.csv')
file6.set_axis(['sentence','emo'], 
                    axis='columns', inplace=True)
data_info(file6)

file7=pd.read_csv('./hand_labelled/Little-Red-Riding-Hood.csv')
file7.set_axis(['sentence','emo'], 
                    axis='columns', inplace=True)
data_info(file7)

file8=pd.read_csv('./hand_labelled/Snow White.csv')
file8.set_axis(['sentence','emo'], 
                    axis='columns', inplace=True)
data_info(file8)

file9=pd.read_csv('./hand_labelled/The Fox and the Crow.csv')
file9.set_axis(['sentence','emo'], 
                    axis='columns', inplace=True)
data_info(file9)

file10=pd.read_csv('./hand_labelled/The Gingerbread Man.csv')
file10.set_axis(['sentence','emo'], 
                    axis='columns', inplace=True)
data_info(file10)

file11=pd.read_csv('./hand_labelled/The Grasshopper and the Ants.csv')
file11.set_axis(['sentence','emo'], 
                    axis='columns', inplace=True)
data_info(file11)

file12=pd.read_csv('./hand_labelled/The North Wind and the Sun.csv')
file12.set_axis(['sentence','emo'], 
                    axis='columns', inplace=True)
data_info(file12)

file13=pd.read_csv('./hand_labelled/The Rat and the Elephant.csv')
file13.set_axis(['sentence','emo'], 
                    axis='columns', inplace=True)
data_info(file13)

file14=pd.read_csv('./hand_labelled/The-Arabian-Nights.csv')
file14.set_axis(['sentence','emo'], 
                    axis='columns', inplace=True)
data_info(file14)

data= pd.concat([file2,file3,file4,file5,file6,file7,file8,file9,file10,file11,file12,file13],axis=0)
data.sort_values(by=['emo'], axis=0,inplace=True)
data.reset_index(inplace=True,drop=True)
display(data)


# In[26]:


def data_info(data):
    emoName=['중립','행복','분노','사랑','슬픔','두려움','호의','놀람','걱정']
    emoSize=[]
    print('\n')
    for j in range(5): #감정개수
        count=0
        for i in range(len(data)):
            if data.iloc[i,1]==j:
                count+=1
        print(emoName[j],'의 갯수:',count)
        emoSize.append(count)
        if j==0:nuetral_size=count
    print(emoSize)
    return emoSize

data_info(data)


# In[24]:


#중립갯수 분노*4개로 맞추기
#dataframe 중립 문장들 중에 랜덤으로 250개 뽑아서
#새로 저장하기

import random
import numpy as np

def get_random_Nuetral(data,nuetral_size):
    size=300
    #nuetral_data=pd.DataFrame(columns=['sentence','emo'])
    np.random.seed(0)
    random_list=np.random.randint(nuetral_size,size=size)
    #print(random_list)
    for i in range(size):
        f = open('./final_data/0/'+str(i)+".txt", 'w')
        f.write(str(data.iloc[random_list[i],0]))
        f.close()
    
    
nuetral_size=data_info(data)
get_random_Nuetral(data,nuetral_size[0])


# In[25]:



def get_text(data,emo):
    for i in range(len(data)):
        if data.iloc[i,1]==emo:
            text=str(data.iloc[i,0])
            f = open('./final_data/'+str(emo)+'/'+str(i)+".txt", 'w')
            f.write(text)
            f.close()
    

def main():
    for emo in range(1,5):
        get_text(data,emo)
    return 0

if __name__=='__main__':
    main()


# In[ ]:





# In[ ]:


# Test뽑기
# The-Arabian-Nights.csv


# In[31]:


file14=pd.read_csv('./hand_labelled/The-Arabian-Nights.csv')
file14.set_axis(['sentence','emo'], 
                    axis='columns', inplace=True)
data_info(file14)
data=file14


# In[32]:


import random
import numpy as np

def get_test_random_Nuetral(data,nuetral_size):
    size=40
    np.random.seed(0)
    random_list=np.random.randint(nuetral_size,size=size)
    #print(random_list)
    for i in range(size):
        f = open('./Arabian_test_data/0/'+str(i)+".txt", 'w')
        f.write(str(data.iloc[random_list[i],0]))
        f.close()
    
    
nuetral_size=data_info(data)
get_test_random_Nuetral(data,nuetral_size[0])

def get_text(data,emo):
    for i in range(len(data)):
        if data.iloc[i,1]==emo:
            text=str(data.iloc[i,0])
            f = open('./Arabian_test_data/'+str(emo)+'/'+str(i)+".txt", 'w')
            f.write(text)
            f.close()
    

def main():
    for emo in range(1,5):
        get_text(data,emo)
    return 0

if __name__=='__main__':
    main()


# In[ ]:





# In[ ]:




