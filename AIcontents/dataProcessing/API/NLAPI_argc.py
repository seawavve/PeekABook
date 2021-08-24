"""Demonstrates how to make a simple call to the Natural Language API."""

import argparse
import pandas as pd

from google.cloud import language_v1

def print_result(annotations, title):
    df = pd.DataFrame(columns=('sentence','score', 'magnitude'))

    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude

    for index, sentence in enumerate(annotations.sentences):
        sentence_score = sentence.sentiment.score
        sentence_magnitude = sentence.sentiment.magnitude

        df = df.append({'sentence': sentence.text.content, 'score': sentence_score, 'magnitude': sentence_magnitude}, ignore_index = True)

        #print(sentence.text.content)
        #print("Sentence {} has a sentiment score of {}".format(index, sentence_score))

    print("Overall Sentiment: score of {} with magnitude of {}".format(score, magnitude))

    #df = df.append(score, magnitude)
    df.to_csv('./' + title + '.csv', header = True, index = True)
    
    return 0

def analyze(book_title):
    """Run a sentiment analysis request on text within a passed filename."""
    #print(book_title)
    title = book_title.split('.')[0]
    client = language_v1.LanguageServiceClient()

    with open(book_title, "r", encoding='utf-8') as book:
        # Instantiates a plain text document.
        content = book.read().replace('\n', '')
    
    document = language_v1.Document(content = content, type_=language_v1.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(request = {'document': document})

    # Print the results
    print_result(annotations, title)

if __name__ == "__main__":
    """f = open("./Pinocchio.txt", 'r')
    book = f.readlines()
    book = "".join(book)
    analyze(book)
    """
    parser = argparse.ArgumentParser(
        description = __doc__, formatter_class = argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "book_title",
        help = "The title of the book you'd like to analyze.",
    )
    args = parser.parse_args()

    analyze(args.book_title)
