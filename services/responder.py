import email, imghdr
from os.path import basename
from .request_handle import RequestHandle
from services.html_generator import HTML_Generator
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def build_email_content(mail_from,mail_to,subject,content,data,format="HTML"):    
    mail = MIMEMultipart()
    mail["From"] = mail_from
    mail["To"] = mail_to
    mail["Subject"] = subject
    mail.attach(MIMEText(content, 'html'))
    if(data):
        f = data
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
            part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
            mail.attach(part)
    return mail

class Responder:
    def __init__(self):
        pass
    def respond(self,host_mail,mail):
        from_mail = 'email.labdev@gmail.com'
        rh = RequestHandle()
        req_handle = rh.parse_request(mail)
        content = {
            'html': '',
            'data': None
        }
        # print(req_handle)
        if("function" in req_handle):
            func = req_handle['function']
            if(req_handle['params'] != None and len(req_handle['params']) >= 1):
                content = func(req_handle['params'])
            else:
                content = func()
        # print(content['html'])
        mail_mesage = build_email_content(
            from_mail,
            mail['sender'],
            req_handle['command'],
            HTML_Generator.html_mail(req_handle['msg'],content['html']),
            content['data']
        )
        host_mail.send_mail(from_mail,mail['sender'],mail_mesage)
        # print(req_handle)