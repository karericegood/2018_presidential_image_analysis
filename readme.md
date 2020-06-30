선형대수학 프로젝트 보고서

201811025 김성주

**1. 서론**

현대사회는 선거를 기반으로 대표를 선발하곤 한다. 그리고 선거는 보통 투표를 통해 이루어진다. 본 조는 2017년 19대 대통령 선거와 관련된 기사 중 두 후보자(문재인, 안철수), 특정 시기(후보자 토론회)를 기준으로 분류한 뒤, 이를 자연어 학습을 통해 분석하고자 했다.

**2. 본론** 

1) 분석 과정

(1) 한글 전처리

한글은 영어와 다르게 다양한 조사가 붙는다. 이는 우리가 자연어 학습을 하는 과정을 방해하곤 한다. 따라서 전처리 과정으로 한글 문장을 조사 등을 제외하는 과정이 필요하다. 본 조는 Konlpy를 통해 이를 정제하였다.

(2) gensim 학습

전처리가 끝난 텍스트를 워드파일로 저장한 후, 이를 다시 gensim으로 학습시켰다. 이때 4/3-4/7, 4/8-4/12, 4/13-4/17, 4/18-4/22, 4/23-4/27, 4/28~5/3 총 6개의 기간을 학습했다. 이때 10차원

(SIZE), 최소빈도(MIN_COUNT) 1에 창(WINDOW)을 5로 구성했고, 반복(ECHO)을 100회 시행했다.

(3) 데이터 분석

지지율과 관련된 단어의 등장 빈도를 분석한 결과, 가장 많이 등장하면서도 상반된 단어 둘을 선별하였다.(본 연구에서는 ‘상승’과 ‘하락’이었다.) ‘상승’의 경우 model.wv[‘상승’]+model.wv[‘지지율’]-model.wv[‘하락’]으로 상승과 지지율의 합벡터 주변에 있으나, 하락과 다른 단어들을 표현하는 새로운 벡터(NEW상승)를 만들었다. ‘하락’의 경우도 마찬가지다.(NEW하락) 그리고 이들과 내적한 값이 가장 높은 단어 30개를 선별해, 이 단어들과 ‘문재인’, 그리고 ‘안철수’와의 평균을 냈다. 그리고 이 둘의 값의 차를 구했다.(즉 본 연구에서는 ‘NEW상승’과 ‘NEW하락’의 내적 값의 차를 구했다.)

2) 분석 결과

전체적으로 문재인 후보와 안철수 후보의 결과가 기존 안철수 지지율 그래프가 증감하는 모습과 유사한 경향성을 가졌음을 확인할 수 있었다. 이는 두 후보가 같은 데이터를 사용했고, 문재인과 안철수의 내적 값이 항상 .7~.8 사이였기 때문이라 추측할 수 있다.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/aca61533-0285-4260-a445-10c90ea4e34c/_2020-06-30__5.19.49.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/aca61533-0285-4260-a445-10c90ea4e34c/_2020-06-30__5.19.49.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/17f274dc-9328-41f5-9613-bc5182ef67f6/_2020-06-30__5.20.07.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/17f274dc-9328-41f5-9613-bc5182ef67f6/_2020-06-30__5.20.07.png)


