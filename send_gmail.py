from __future__ import print_function

import base64
from email.message import EmailMessage
import os
import mimetypes
from google.auth.transport.requests import Request

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# SCOPES 변경시 token.json 삭제 후 다시 생성 필요.
# SCOPES 종류(https://developers.google.com/gmail/api/auth/scopes?hl=ko 참조)
# 아래 예시는 메일 읽기와 메일 보내기 기능
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.send']

def mail_auth_check():
    creds = None

    # token.json파일이 있을 경우
    if os.path.exists('token.json'):
        print('token exists!')
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        print('creds')

    # 인증이 안됬을 경우 인증 진행 후 token.json 생성
    if not creds or not creds.valid:
        print('not valid')
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # 다음 실행을 위한 token.json 생성
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
            
    return creds

def gmail_send_message(to: str, title: str, content: str):    

    print('to', to, 'title', title, 'content', content)

    # 메일 인증 확인
    cred = mail_auth_check()

    # 메일 발송
    print('now try')
    try:
        service = build('gmail', 'v1', credentials=cred)
        message = EmailMessage()
        message.set_content(content)

        message['To'] = to
        message['From'] = 'chunie9702@gmail.com'
        message['Subject'] = title

        # 첨부파일이 있을 경우
        attachment_filename = "photo.jpg"
        # guessing the MIME type
        type_subtype, _ = mimetypes.guess_type(attachment_filename)
        maintype, subtype = type_subtype.split("/")

        with open(attachment_filename, "rb") as fp:
            attachment_data = fp.read()
        message.add_attachment(attachment_data, maintype, subtype)

        # 메세지 인코딩
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()) \
            .decode()

        create_message = {
            'raw': encoded_message
        }

        # pylint: disable=E1101
        send_message = (service.users().messages().send(userId="me", body=create_message).execute())
        
        print(f'send_message id: {send_message["id"]}')

    except HttpError as error:
        print(F'An error occurred: {error}')
        send_message = None
        return False
    return True


if __name__ == '__main__':
    gmail_send_message("chunie9702@gmail.com", "test", "content")
