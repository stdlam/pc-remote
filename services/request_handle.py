from operator import truediv
import os, re
from xmlrpc.client import Boolean
from .html_generator import HTML_Generator
from .help import Help
class RequestHandle:
    def __init__(self):
        pass
    def __read_whitelist(self):
        emails = []
        try:
            with open("whitelist.txt", "r") as credentials:
                for line in credentials:
                    mail = line.replace("\n", "").split(",")
                    emails.append({'email':mail[0],'role':int(mail[1])})
                credentials.close()
                return emails
        except FileNotFoundError:
            return []
    def parse_request(self,request):
        mail_req = None
        whiteList = self.__read_whitelist()
        # Check email
        isValid = False
        for mail in whiteList:
            if(request['sender'] == mail['email']): 
                isValid = True
                mail_req = mail
        if(isValid == False):
            return {'msg':"Email không hợp lệ",'command':request['subject']}
        # Check role
        isValid = False
        cmd_basic = ['MAC','APP','PROCESS','SCREEN','KEYLOGGER']
        cmd_advance = ['REGISTRY','EXPLORER','SYSTEM']
        group_cmd_request = request['subject'].split(" ")[1]
        if(
            (group_cmd_request in cmd_basic and mail_req['role'] == 0) 
            or
            (group_cmd_request in cmd_advance and mail_req['role'] == 1)
        ):
            isValid = True
        if(isValid == False):
            return {'msg':"Email không đủ quyền điều khiển câu lệnh",'command':request['subject']}
        # Check command    
        isValid = False
        cmd_req = request['subject'].replace("[G8RC] ", "")
        commands = Help.get_commands()
        for group_cmd in commands:
            for cmd in group_cmd[1]:
                if(cmd == cmd_req):
                    isValid = True
        if(isValid == False):
            return {'msg':"Cú pháp lệnh không hợp lệ",'command':request['subject']}

        # Command valid
        return {'msg':"Cú pháp lệnh hợp lệ",'command':request['subject']}

