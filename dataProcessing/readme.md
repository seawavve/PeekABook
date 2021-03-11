# Dataprocessing
  
<img src="https://github.com/seawavve/PeekABook/blob/main/dataProcessing/labelling.png" width="500" >  
  
  + 감정 Labelling  
textblob 라이브러리를 사용하여 긍부정지수를 판단했습니다.  
한 문서의 average 감정지수를 파악하려 이를 토대로 0(부정)과 1(긍정)으로 라벨링했습니다.  
  
  + 대화 상대 파악  
 spaCy 형태소분석기를 사용하여 명사를 추출했습니다.  
 NLTK 형태소분석기로 명사를 다시 한 번 추출하여 두 개의 성능을 비교해볼 예정입니다.  
 사람과 사물의 판단은 워드 벡터로 판단하기로 했습니다.  
