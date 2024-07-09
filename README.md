# 메일을 보내는 기능 구현(gmail)
참조 : https://developers.google.com/gmail/api/quickstart/python?hl=ko

1. 프로그램 준비
    1) 파이썬 설치
        - [파이썬 설치하는 법](https://wikidocs.net/8)
    2) pip 패키지 관리도구 설치

2. Google API 준비
    1) Google Cloud 프로젝트 생성
        - https://developers.google.com/workspace/guides/create-project?hl=ko
    2) Gmail API 사용 설정
        - https://console.cloud.google.com/flows/enableapi?apiid=gmail.googleapis.com&hl=ko
    3) OAuth 동의 화면 구성
        - https://console.cloud.google.com/apis/credentials/consent?hl=ko
    4) 사용자 인증 정보 생성(OAuth 클라이언트 ID - 데스크톱 앱)
        - https://console.cloud.google.com/apis/credentials?hl=ko
    5) JSON 파일 저장(credentials.json)

3. 라이브러리 설치
    1) google-api-python-client
    2) google-auth-httplib2
    3) google-auth-oauthlib
    * pip install '라이브러리명'

4. 구조
    1) 최초 메일 전송 시 credentials.json으로 본인 확인
    2) 본인 확인이 완료 시 token.json이 생성
    3) token.json을 통한 메일 발송
    * 리눅스 서버와 같이 본인 확인이 안될 경우 credentials.json과 token.json을 넣는방식으로 진행