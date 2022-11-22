# NLPChatbot

댓글데이터 기반 NLP 프로젝트
- 학습데이터 소개
<img width="881" alt="image" src="https://user-images.githubusercontent.com/73158757/203312149-22e7b956-6eb4-4e5a-91b9-8168489dedda.png">

-사용한 학습 모델
<img width="784" alt="image" src="https://user-images.githubusercontent.com/73158757/203312295-965bbbbc-935d-4459-b692-0e96959ea1c9.png">

- 데이터확인 및 전처리
긍정댓글 : 1 , 부정댓글 : 0 으로 라벨링


- 데이터셋 나누기/중복제거 
<img width="272" alt="image" src="https://user-images.githubusercontent.com/73158757/203313297-a19d7165-3478-4bba-a151-705b5d2eb816.png">

- Train/Test 데이터 Tokenizing
<img width="168" alt="image" src="https://user-images.githubusercontent.com/73158757/203313446-0ef9852e-5a7c-4118-bf6f-21d890bbe3e4.png">

- 인터넷 댓글 데이터셋 다운로드 후 데이터 전처리 후 모델학습 진행
<모델평가지표 -> 성능 비교 위해 2개의 모델 학습> 
<img width="830" alt="image" src="https://user-images.githubusercontent.com/73158757/203311960-642452bd-eda5-4bd9-b761-5aaff72825b2.png">


- 로컬 뿐만아니라 외부접속 허용 위해 ngrok 서버 사용하여 flask 웹 서비스 구축 (처리속도 해결 위해 코랩서버 사용하여 구현)
<img width="908" alt="image" src="https://user-images.githubusercontent.com/73158757/203311704-6489b0ac-a0cd-42a5-b441-ff3867f4b41a.png">


pycharm, ngrok, colab 
