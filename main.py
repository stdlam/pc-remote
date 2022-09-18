import sys, os.path, winshell, win32com.client, ctypes, time
from threading import Thread

from services.thread_targets import check_mail_thread
from services.maill_service import MailService
from services.html_generator import HTML_Generator
from services.request_handle import RequestHandle
from services.keylogger import KeyLogger
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QMessageBox,
    QSystemTrayIcon,
    QMenu
)
from PyQt6.QtGui import QIcon
ms = None
isConnected = False

USERNAME = 'email.labdev@gmail.com'
PASSWORD = 'twptcpnnaekacqwn'

class Server(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.tcpServer = None
        self.start = False

    def initUI(self):
        user32 = ctypes.windll.user32

        desktop_width = user32.GetSystemMetrics(0)
        desktop_height = user32.GetSystemMetrics(1)

        width = int(desktop_width * 0.15)
        height = int(desktop_height * 0.107)

        self.resize(width, height)

        self.setWindowTitle('Server')

        layout = QVBoxLayout()

        self.open_button = QPushButton("Run", self)
        self.open_button.clicked.connect(self.run_server)
        create_shorcut_button = QPushButton("Create shortcut", self)
        create_shorcut_button.clicked.connect(self.generator_shorcut)
        exit_button = QPushButton("Exit", self)
        exit_button.clicked.connect(exit)

        layout.addStretch()
        layout.addWidget(self.open_button)
        layout.addWidget(create_shorcut_button)
        layout.addWidget(exit_button)
        layout.addStretch()

        self.setLayout(layout)

        self.show()
    def showApp(self):
        self.show()
    def run_server(self):
        global isConnected
        if(isConnected == False):
            onRun()
            self.open_button.setText('Stop')
            # self.hide()
        else:
            ms.close()
            self.open_button.setText('Run')
            isConnected = False
    def generator_shorcut(self):
        create_shortcut(
            os.path.join(get_startup_path(), 'ServerRemote.lnk'), # Startup path
            "python", # Runner
            os.path.abspath('main.py'), # Argument
            os.getcwd(), # wDir
            os.path.abspath('icon.ico') # Icon path
        )
        pass

def exit():
    global isConnected
    isConnected = ms.close()
    Thread
    sys.exit()

def get_startup_path():
    startupPath = winshell.startup()
    return startupPath
def create_shortcut(path,runner,argument,wDir,icon):
    shell = win32com.client.Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    print(r''+runner +" "+ argument)
    shortcut.Targetpath =  r'D:\Study\MMT\pc-remote\main.py -python'
    shortcut.WorkingDirectory = r''+wDir
    shortcut.IconLocation = r''+icon
    shortcut.save()
def connect_mail_service():
    while True:
        try:
            ms.login(USERNAME,PASSWORD)
            return 1
        except:
            pass
def scan_maill():
    while isConnected:
        print('SCANNING...')
        mails_request = ms.read_mail()
        print(mails_request)
        time.sleep(8)
def onRun():
    global isConnected
    isConnected = connect_mail_service()
    Thread(target=check_mail_thread,args=(ms,8,)).start()

def onStop():
    global isConnected
    isConnected = ms.close()
    pass
def main():
    global ms
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(os.path.abspath('icon.ico')))
    ex = Server()
    ms = MailService()
    # Tray Icon 
    trayIcon =  QSystemTrayIcon(QIcon(os.path.abspath('icon.ico')), parent=app)
    trayIcon.setToolTip('Server remote')
    trayIcon.show()
    # Menu Tray Icon 
    menu = QMenu()
    openAction = menu.addAction('Open')
    openAction.triggered.connect(ex.showApp)
    exitAction = menu.addAction('Exit')
    exitAction.triggered.connect(exit)
    # Tạo tray icon
    trayIcon.setContextMenu(menu)

    #Lấy whitelist
    # rh = RequestHandle()
    # print(rh.parse_request({'sender':'hoaikhaqn1996@gmail.com','subject':'[G8RC] SYSTEM shutdown'}))

    # Lấy địa chỉ Mac
    # mac = Mac()
    # print(HTML_Generator.html_mail("Lấy địa chỉ Mac",mac.get_mac()['html']))

    # Lấy nội dung gõ phím (keylogger)
    # keylog = KeyLogger()
    # print(HTML_Generator.html_mail("Lấy nội dung gõ phím",keylog.get_key_log([5])['html']))

    # Chụp màn hình
    # screen = Screen()
    # screen_shot_mail = screen.get_screen_shot()
    # print(HTML_Generator.html_mail("Chụp ảnh màn hình",screen_shot_mail['html']))

    # Quay màn hình
    # screen = Screen(10)
    # screen_record_mail = screen.get_screen_recorder()
    # print(HTML_Generator.html_mail("Quay ảnh màn hình",screen_record_mail['html']))

    # Gửi danh sách lệnh
    # h = Help()
    # print(HTML_Generator.html_mail("Lấy danh sách lệnh",h.show_help()['html']))

    # Lấy danh sách ứng dụng
    # app_running = AppRunning()
    # HTML_RESPONSE =  HTML_Generator.html_mail("Lấy danh sách ứng dụng đang chạy",app_running.get_apps()['html'])
    # Đóng ứng dụng bằng ID
    # app_id = 17456
    # HTML_RESPONSE = HTML_Generator.html_mail("Đóng ứng dụng có ID "+str(app_id),app_running.close_app(app_id)['html'])

    # Lấy danh sách tiến trình
    # process = Process()
    # HTML_RESPONSE = HTML_Generator.html_mail("Lấy danh sách tiến trình đang chạy",process.get_processes()['html'])
    # Đóng tiến trình bằng ID
    # pro_id = 17456
    # HTML_RESPONSE = HTML_Generator.html_mail("Đóng tiến trình có ID "+str(pro_id),process.close_process(pro_id)['html'])

    # Shutdown
    # pc = PC()
    # print(HTML_Generator.html_mail("Shutting down ", pc.shutdown()['html']))

    # Restart
    # pc = PC()
    # print(HTML_Generator.html_mail("Restarting ", pc.restart()['html']))

    # if(HTML_RESPONSE): print(HTML_RESPONSE)

    sys.exit(app.exec())
if __name__ == '__main__':
    main()