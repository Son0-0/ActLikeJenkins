# ActLikeJenkins

![alj](https://user-images.githubusercontent.com/81317358/183281262-ae215fdd-7dc6-4a8e-b681-8d6a1a8c1a4a.jpg)

## Description
- Github Repository에 업데이트가 일어나면 자동으로 배포
  - 메인 코드 Flask로 작성
  - Node.js로 작성한 백엔드 코드에서만 테스트 및 작동 확인
  - 업데이트 트래킹 원하는 브랜치 설정가능
- pm2 start app.js -o out.log 명령어로 실행시 작성된 log 모니터링
  - [ERROR]/${err_position}/${err_name}/${err_message} 형식으로 에러메시지 작성
  - err_monitor/monitor.py 실행후 node 서버 에러 발생시 슬랙 웹훅으로 전송

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

3. 에러 로그 모니터를 위한 err_monitor/monitor.py 파일 실행
```python3 err_monitor/monitor.py``` or ```python err_monitor/monitor.py```
  - 서버 내 백그라운드 실행하고 싶은 경우
  ```nohup err_monitor/monitor.py &``` or ```nohup err_monitor/monitor.py &```

## Slack Webhook Message
<img width="731" alt="스크린샷 2022-08-07 오전 2 09 32" src="https://user-images.githubusercontent.com/81317358/183259276-b23dc08b-3098-4dda-93a2-89acc3410dd0.png">

<img width="726" alt="스크린샷 2022-08-07 오후 5 01 01" src="https://user-images.githubusercontent.com/81317358/183281333-53a36ad5-98cf-45dc-bb99-ef6074245525.png">
