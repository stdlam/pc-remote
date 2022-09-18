import psutil
from .html_generator import HTML_Generator
class Process:
    def __init__(self):
        pass
    def __process_df(self):
        list_process = []
        for proc in psutil.process_iter(['pid', 'name']):
            list_process.append([proc.info['pid'],proc.info['name']])
        # print(list_process)
        return {
            'type': 'single',
            'columns': ['PID','Name'],
            'data': list_process
        }
    def get_processes(self):
        html = HTML_Generator.html_table(self.__process_df())
        return {
            'html': html,
            'data': None
        }

    def __closing(self,params):
        try:
            p = psutil.Process(params[0])
            p.kill()
            return 1
        except:
            return 0

    def close_process(self,id):
        status = self.__closing(id)
        msg = ""
        if(status):
            msg = "Đóng tiến trình thành công"
        else: 
            msg = "Đóng tiến trình thất bại"
        html = HTML_Generator.html_msg(msg,status,True)
        return {
            'html': html,
            'data': None
        }