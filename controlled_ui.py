from tkinter import  Canvas, Button, Checkbutton, PhotoImage


import os
import sys
def abs_path(file_name):
    file_name = 'assets/' + file_name
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, file_name)

class Main_UI(Canvas):
    def __init__(self, parent):
        Canvas.__init__(self, parent)
        self.configure(
            #window,
            bg = "#3F6BAA",
            height = 500,
            width = 400,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.place(x = 0, y = 0)
        
        self.btn_run = Button(self,
            text='Run',
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("Run clicked")
        )
        self.btn_run.place(
            #x=727.0,
            #y=72.0,
            rely=0.1, relx=0.40
        )
        self.ckb_autostart = Checkbutton(self, text='Auto Run', onvalue=1, offvalue=0)
        self.ckb_autostart.place(rely=0.1, relx=0.55)
        
        self.btn_exit = Button(self,
            text='Exit',
            command=lambda: print("Exit clicked"),
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.btn_exit.place(rely=0.4, relx=0.4)

        self.btn_whitelist = Button(self,
            text='White List',
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("White List clicked"),
            relief="flat"
        )
        self.btn_whitelist.place(rely=0.3, relx=0.36)

        self.btn_stop = Button(self,
            text='Stop',
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("Stop clicked"),
            relief="flat"
        )
        self.btn_stop.place(rely=0.2, relx=0.4)

        

