import email, imaplib, smtplib
from threading import Thread

SERVER_IMAP = 'imap.gmail.com'
SERVER_SMTP = 'smtp.gmail.com'

class MailService:
    def __init__(self):
        self.username = None
        self.password = None
        self.imap = imaplib.IMAP4_SSL(SERVER_IMAP)
        self.smtp = smtplib.SMTP(SERVER_SMTP, port=587)
    def login(self,username,password):
        try:
            self.username = username
            self.password = password
            self.imap.login(username,password)
            print("Connecting mail service: Success!\n")
            return 1
        except Exception as e:
            print("Connecting mail service: Failure!\n")
            print(e) 
            return 0
    def read_mail(self,category="primary",box="inbox"):
        print("box",box)
        mail = self.imap
        mail.select(box)
        print("Receing mail...")
        # status,data = mail.search(None, '(SUBJECT "[G8RC]")') // Không lọc được 
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
                    if(mail_subject.startswith('[G8RC]')):
                        mails_request.append({'sender':mail_from,'subject':mail_subject})
        print("Receing mail: Completed!")
        return mails_request
    def send_mail(self,mail):
        smtp = self.smtp
        smtp.ehlo()
        smtp.starttls()
        smtp.login(self.username, self.password)
        smtp.sendmail(mail)
        smtp.quit()
    def close(self):
        mail = self.imap
        try:
            mail.logout()
            print("Disconnect mail service: Success!\n")
            return 1
        except Exception as e:
            print("Disconnect mail service: Failure!\n")
            print(e) 
            return 0

