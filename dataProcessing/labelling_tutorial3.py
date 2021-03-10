from textblob import TextBlob
import pandas as pd

def labelling(book):
    total_posNeg=0
    df = pd.DataFrame(columns=('sentence','posNeg','bi_posNeg'))
    print(book)
    f = open("./"+ book +"_data.txt", 'r')
    lines = f.readlines()
    for line in lines:
        df=df.append({'sentence':line,'posNeg':TextBlob(line).sentiment.polarity},ignore_index=True)
        total_posNeg+=TextBlob(line).sentiment.polarity
    #print(df)
    print('total 긍부정값:',total_posNeg)
    average_posNeg=total_posNeg/len(df)
    print('average 긍부정값:',total_posNeg/len(df))
    f.close()
    binary_labelling(df,average_posNeg)

def binary_labelling(df,average_posNeg):

    for i in range(len(df)):
        if df.iloc[i,1]>average_posNeg:
            df.iloc[i,2]=1
        else:
            df.iloc[i,2]=0
    print(df)




def main():
    books=['Cinderella','HanselandGretel','LittleRedRidingHood']
    for book in books:
        labelling(book)
    return 0

if __name__ == "__main__":
	main()
