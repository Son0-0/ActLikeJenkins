# ActLikeJenkins

![actLikeJenkins](https://user-images.githubusercontent.com/81317358/183255704-893b2dcb-7eff-432c-9d7c-603c2a23fff9.jpg)

## Description
- Github Repository에 업데이트가 일어나면 자동으로 배포
  - 메인 코드 Flask로 작성
  - Node.js로 작성한 백엔드 코드에서만 테스트 및 작동 확인
  - 업데이트 트래킹 원하는 브랜치 설정가능

## Installation
1. 레포지토리 클론  
```git clone https://github.com/Son0-0/ActLikeJenkins.git```
2. 필요한 라이브러리 설치  
```pip install -r requirements.txt```

## Settings
1. PORT_NUM 설정 (기본 설정 5000)
2. Github Webhook 설정
  - 자신의 서버 url + :5000/update로 경로 설정
  - 파일 실행전 서버 포트 열기
3. WEBHOOK_URL 설정 (Slack)
4. Shell script 파일 수정
5. npm pm2 install (pm2 필수)

## How to run your ActLikeJenkins
1. app.py 파일 실행  
```python3 app.py``` or ```python app.py```  
  - 서버 내 백그라운드 실행하고 싶은 경우
  ```nohup python3 app.py &``` or ```nohup python app.py &```
2. PM2 모듈 설치 및 app.js 실행
```npm install pm2``` and ```pm2 start app.js```
