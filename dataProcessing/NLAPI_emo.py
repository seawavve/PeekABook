from google.cloud import language_v1
import pandas as pd

def sample_analyze_sentiment(text_content, df):
    client = language_v1.LanguageServiceClient()

    type_ = language_v1.Document.Type.PLAIN_TEXT
    language = "en"
    document = {"content": text_content, "type_": type_, "language": language}

    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})
    # Get sentiment for all sentences in the document
    for sentence in response.sentences:
        df = df.append({'sentence':sentence.text.content,'score': sentence.sentiment.score, 'magnitude': sentence.sentiment.magnitude}, ignore_index=True)
        #print(u"Sentence text: {}".format(sentence.text.content))
        #print(u"Sentence sentiment score: {}".format(sentence.sentiment.score))
        #print(u"Sentence sentiment magnitude: {}".format(sentence.sentiment.magnitude))
    return df

f = open("./LittleRedRidingHood.txt", 'r')
df = pd.DataFrame(columns=('sentence','score', 'magnitude'))
lines = f.readlines()
for line in lines:
    if len(line)<2:continue
    line=line.replace('\n','')
    df = sample_analyze_sentiment(line, df)
df.to_csv('./' + 'LittleRedRidingHood_API' + '.csv', header=True, index=True)