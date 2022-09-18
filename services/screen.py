import io,time, base64, numpy as np, cv2,pyautogui
from PIL import ImageGrab
from .html_generator import HTML_Generator
from datetime import datetime
class Screen:
    def __init__(self):
        pass
    def __screen_shot(self):
        img = ImageGrab.grab()
        img_bytes = io.BytesIO()
        now = datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
        filename = 'screenshot_'+str(now)+'.png'
        img.save(filename)
        return filename
    def __screen_record(self,elapse_time):
        now = datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
        filename = 'record_'+str(now)+'.webm'
        SCREEN_SIZE = tuple(pyautogui.size())
        fourcc = cv2.VideoWriter_fourcc(*'VP80')
        fps = 12.0
        out = cv2.VideoWriter(filename, fourcc, fps, (SCREEN_SIZE))
        record_seconds = elapse_time
        for i in range(int(record_seconds * fps)):
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            out.write(frame)
            if cv2.waitKey(1) == ord("q"):
                break
        cv2.destroyAllWindows()
        # record = open(filename,"rb").read()
        # record_base64 = base64.b64encode(record).decode('utf-8')
        return filename
    def get_screen_shot(self):
        image_base64 = self.__screen_shot()
        html = HTML_Generator.html_msg(
            "Chụp màn hình thành công",True,True)
        return {
            'html': html,
            'data': image_base64
        }
    def get_screen_recorder(self,params):
        video_base64 = self.__screen_record(int(params[0]))
        html = HTML_Generator.html_msg(
            "Quay màn hình thành công",True,True)
        return {
            'html': html,
            'data': video_base64
        }