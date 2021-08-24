from textblob import TextBlob
import pandas as pd
import spacy


def labelling(book):
    total_posNeg=0
    df = pd.DataFrame(columns=('sentence','posNeg','posNeg3'))
    print(book)
    f = open("./"+ book +".txt", 'r')
    lines = f.readlines()
    for line in lines:
        if len(line)<2:continue
        line=line.replace('\n','')
#         tokens=tokenize_sentence(line)
#         print(tokens)
        df=df.append({'sentence':line,'posNeg':TextBlob(line).sentiment.polarity},ignore_index=True)
        total_posNeg+=TextBlob(line).sentiment.polarity
    #print(df)
    print('total posNeg:',total_posNeg)
    average_posNeg=total_posNeg/len(df)
    print('average posNeg:',total_posNeg/len(df))
    f.close()
    three_labelling(df,average_posNeg,book)

def three_labelling(df,average_posNeg,book):

    for i in range(len(df)):
        if (df.iloc[i,1]>=0) and (df.iloc[i,1]<0.15):
            df.iloc[i,2]=1
        elif (df.iloc[i,1]>=0.15):
            df.iloc[i,2]=2
        else:
            df.iloc[i,2]=0
    df=df.dropna(how='any')
    df.to_csv('./' + book + '.csv', header=True, index=True)
    display(df)

def tokenize_sentence(sentence):
    tokens=[]
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(sentence)
    for token in doc:
        tokens.append(token.text)
    return tokens

def main():
    books=['Peterpan']
    
    for book in books:
        labelling(book)
    return 0

if __name__ == "__main__":
	main()
