import subprocess, os
from .html_generator import HTML_Generator
class AppRunning:
    def __init__(self):
        pass
    def __app_df(self):
        cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Description,Id'
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        remove_top = 0
        list_app = []
        for line in proc.stdout:
            if not line.decode()[0].isspace():
                remove_top = remove_top + 1
                if remove_top > 2:
                    list_app.append([line.decode().rstrip()[:20].replace(' ', ''),line.decode().rstrip()[20:].replace(' ', '')])
        return {
            'type': 'single',
            'columns': ['Name','ID'],
            'data': list_app
        }

    def get_apps(self):
        html = HTML_Generator.html_table(self.__app_df())
        return {
            'html': html,
            'data': None
        }

    def __closing(self,id):
        cmd = 'taskkill.exe /F /PID ' + str(id)
        try:
            a = os.system(cmd)
            if a == 0:
                return 1
            else:
                return 0
        except:
            return 0

    def close_app(self,params):
        status = self.__closing(params[0])
        msg = ""
        if(status):
            msg = "Đóng ứng dụng thành công"
        else: 
            msg = "Đóng ứng dụng thất bại"
        html = HTML_Generator.html_msg(msg,status,True)
        return {
            'html': html,
            'data': None
        }