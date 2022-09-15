import io, base64, numpy as np, cv2,pyautogui
from PIL import ImageGrab
from .html_generator import HTML_Generator

class Screen:
    def __init__(self,elapse_time):
        self.elapse_time = elapse_time
        pass
    def __screen_shot(self):
        img = ImageGrab.grab()
        img_bytes = io.BytesIO()
        img.save(img_bytes, format="PNG")
        encoded_string = base64.b64encode(img_bytes.getvalue()).decode('utf-8')
        return encoded_string
    def __screen_record(self):
        SCREEN_SIZE = tuple(pyautogui.size())
        fourcc = cv2.VideoWriter_fourcc(*'VP80')
        fps = 12.0
        out = cv2.VideoWriter("record.webm", fourcc, fps, (SCREEN_SIZE))
        record_seconds = self.elapse_time
        for i in range(int(record_seconds * fps)):
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            out.write(frame)
            if cv2.waitKey(1) == ord("q"):
                break
        cv2.destroyAllWindows()
        record = open('record.webm',"rb").read()
        record_base64 = base64.b64encode(record).decode('utf-8')
        return record_base64
    def get_screen_shot(self):
        image_base64 = self.__screen_shot()
        html = HTML_Generator.html_msg(
            "Chụp màn hình thành công",True,True)
        return {
            'html': html,
            'data': image_base64
        }
    def get_screen_recorder(self):
        video_base64 = self.__screen_record()
        html = HTML_Generator.html_msg(
            "Quay màn hình thành công",True,True)
        return {
            'html': html,
            'data': video_base64
        }