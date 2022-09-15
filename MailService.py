import imaplib as imap
import constants as c
import smtplib as smtp
import email
from email.header import decode_header
class MailService:
    def __init__(this):

        # connect to the IMAP server to retrieve email messages from a mail server.
        this.mail = imap.IMAP4_SSL(c.IMAP_SERVER)


    def loginMaiService(this, username, password):
        if this.mail.login(username, password)[0] == 'OK':
            return True
        return False

    def read_mail(this, category = "primary", box = c.MAILBOX[0]):
        this.mail.select(box)
        _, data = this.mail.search(None, 'UNSEEN')
        ids = data[0].split()

        if len(ids):
            first_mail_id = int(ids[0])
            latest_mail_id = int(ids[-1])
            print('first_email_id: ', first_mail_id)
            print('latest_email_id: ', latest_mail_id)
            email_content_list = []
        # for i in range(len(messages[0]), 0, -1):
            for i in range(latest_mail_id,first_mail_id - 1, -1):
                # fetch the email message by ID
                res, msg = this.mail.fetch(str(i), "(RFC822)")
                for response in msg:
                    if isinstance(response, tuple):
                        # parse a bytes email into a message object
                        msg = email.message_from_bytes(response[1])
                        # decode the email subject
                        subject, encoding = decode_header(msg["Subject"])[0]

                        if isinstance(subject, bytes):
                            # if it's a bytes, decode to str
                            if encoding:
                                subject = subject.decode(encoding)
                        # decode email sender
                        
                        sender, encoding = decode_header(msg.get("From"))[0]
                        # sender = email.utils.parseaddr(msg['from'])[1]
                        if isinstance(sender, bytes):
                            if encoding:
                                sender = sender.decode(encoding)
                        # print("Subject:", subject)
                        # print("From:", sender)
                        email_content_list.append({'sender':sender, 'subject':subject})
            return email_content_list
        else: 
            print("All email had been read!")        
            return[]