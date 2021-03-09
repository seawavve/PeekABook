from textblob import TextBlob

f = open("./Cinderella_data.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
    print(TextBlob(line).sentiment)
    #print('*')
f.close()
