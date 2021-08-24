from textblob import TextBlob

f = open("./Cinderella_data.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
    #print(TextBlob(line).sentiment)
    print(TextBlob(line).sentiment.polarity)
f.close()


#프레임워크로 |문장|라벨(전체 polarity의 평균에서 크면 1 작으면 0)| 구현
print('******')
f = open("./HanselandGretel_data.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
    print(TextBlob(line).sentiment.polarity)
    #print('*')
f.close()

print('******')
f = open("./LittleRedRidingHood_data.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
    print(TextBlob(line).sentiment.polarity)
    #print('*')
f.close()
