import email

def build_email_content(mail_from,mail_to,subject,content,format="HTML"):    
    mail = email.message.EmailMessage()
    mail.add_header("From", mail_from)
    mail.add_header("To", mail_to)
    mail.add_header("Subject", subject)
    mail.set_content(content.html)

