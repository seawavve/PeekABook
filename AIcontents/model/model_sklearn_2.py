import pandas as pd
data=pd.read_csv('./Peterpan_emo3.csv')
data=data.dropna(how='any')
print(f'Dimensions: {data.shape}')
data

import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict, GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix, accuracy_score

nltk.download('wordnet')
nltk.download('stopwords')

#Partitioning data
X_train, X_test, y_train, y_test = train_test_split(data['sentence'], data['posNeg3'], test_size=0.3, random_state=123)
print(f'Train dimensions: {X_train.shape, y_train.shape}')
print(f'Test dimensions: {X_test.shape, y_test.shape}')
# Check out target distribution
print(y_train.value_counts())
print(y_test.value_counts())

# Xdata를 tfidfvectorizer를 사용하여 문장 특징을 추출

def preprocess_text(text):
    # Tokenise words while ignoring punctuation
    tokeniser = RegexpTokenizer(r'\w+')
    tokens = tokeniser.tokenize(text)
    
    # Lowercase and lemmatise 
    lemmatiser = WordNetLemmatizer()
    lemmas = [lemmatiser.lemmatize(token.lower(), pos='v') for token in tokens]
    
    # Remove stop words
    keywords= [lemma for lemma in lemmas if lemma not in stopwords.words('english')]
    return keywords

# Create an instance of TfidfVectorizer
vectoriser = TfidfVectorizer(analyzer=preprocess_text)   
# Fit to the data and transform to feature matrix
X_train_tfidf = vectoriser.fit_transform(X_train)
X_train_tfidf.shape



# SGD분류기를 이용한 5-fold 교차검증 모델

sgd_clf = SGDClassifier(random_state=123)
sgf_clf_scores = cross_val_score(sgd_clf, X_train_tfidf, y_train, cv=5)
print(sgf_clf_scores)
print("Accuracy: %0.2f (+/- %0.2f)" % (sgf_clf_scores.mean(), sgf_clf_scores.std() * 2))

sgf_clf_pred = cross_val_predict(sgd_clf, X_train_tfidf, y_train, cv=5)
print(confusion_matrix(y_train, sgf_clf_pred))

#하이퍼 파라미터를 순차적으로 적용하면서 최고 성능을 가지는 파라미터 조합을 찾을 수 있는 gridsearchCV(cross validation)
#cross-validation을 기반으로 최적 값을 찾아줌
#시간이 오래걸림

grid = {'fit_intercept': [True,False],
        'early_stopping': [True, False],
        'loss' : ['hinge', 'log', 'squared_hinge'],
        'penalty' : ['l2', 'l1', 'none']}
search = GridSearchCV(estimator=sgd_clf, param_grid=grid, cv=5)
search.fit(X_train_tfidf, y_train)
search.best_params_

search.best_score_



import numpy as np
np.transpose(pd.DataFrame(search.cv_results_))

grid_sgd_clf_scores = cross_val_score(search.best_estimator_, X_train_tfidf, y_train, cv=5)
print(grid_sgd_clf_scores)
print("Accuracy: %0.2f (+/- %0.2f)" % (grid_sgd_clf_scores.mean(), grid_sgd_clf_scores.std() * 2))

pipe = Pipeline([('vectoriser', vectoriser),
                 ('classifier', search.best_estimator_)])
pipe.fit(X_train, y_train)

y_test_pred = pipe.predict(X_test)
print("Accuracy: %0.2f" % (accuracy_score(y_test, y_test_pred)))
print(confusion_matrix(y_test, y_test_pred))

import joblib 
# 객체를 pickled binary file 형태로 저장한다 
file_name = 'gridsearchCV.pkl' 
joblib.dump(search, file_name) 
