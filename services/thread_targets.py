import  time
from .request_handle import RequestHandle
from .responder import Responder
from threading import Thread

def scan_maill(ms):
    print('SCANNING...')
    mails_request = ms.read_mail()
    for mail_req in mails_request:
        re = Responder()
        re.respond(ms,mail_req)
    print("DONE")

def check_mail_thread(host_mail,timeout):
    while True:
        print('SCANNING...')
        scan_maill(host_mail)
        time.sleep(timeout)
