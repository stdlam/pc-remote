import email,imaplib
from threading import Thread

EMAIL = 'email.labdev@gmail.com'
PASSWORD = 'twptcpnnaekacqwn'
SERVER = 'imap.gmail.com'

class MailService:
    def __init__(self):
        self.mail = None
    def __open_connect(self):
        try:
            self.mail = imaplib.IMAP4_SSL(SERVER)
            self.mail.login(EMAIL, PASSWORD)
            print("Connecting mail service: Success!\n")
            return 1
        except Exception as e:
            print("Connecting mail service: Failure!\n")
            print(e) 
            return 0
    def login(self):
        return self.__open_connect()
    def read_mail(self,category="primary",box="inbox"):
        print("box",box)
        mail = self.mail
        mail.select(box)
        print("Receing mail...")
        status,data = mail.search(None, 'ALL')
        print(data)
        mail_ids= []
        for block in data:
            mail_ids += block.split()
        mails_request = []
        for id in mail_ids:
            status,data = mail.fetch(id, '(RFC822)')
            for response_part in data:
                if isinstance(response_part, tuple):
                    message = email.message_from_bytes(response_part[1])
                    mail_from = email.utils.parseaddr(message['from'])[1]
                    mail_subject = message['subject']
                    mails_request.append({'sender':mail_from,'subject':mail_subject})
        print("Receing mail: Completed!")
        return mails_request
    def close(self):
        mail = self.mail
        try:
            mail.logout()
            print("Disconnect mail service: Success!\n")
            return 1
        except Exception as e:
            print("Disconnect mail service: Failure!\n")
            print(e) 
            return 0

