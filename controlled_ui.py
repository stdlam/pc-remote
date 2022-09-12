from tkinter import  Canvas, Button, PhotoImage


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
            bg = "#FFFFFF",
            height = 600,
            width = 1000,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.place(x = 0, y = 0)
        self.image_image_1 = PhotoImage(
            file=abs_path("image_1.png"))
        self.image_1 = self.create_image(
            500.0,
            300.0,
            image=self.image_image_1
        )
        
        self.image_image_2 = PhotoImage(
            file=abs_path("image_2.png"))
        self.image_2 = self.create_image(
            466.0,
            323.0,
            image=self.image_image_2
        )

        self.btn_run = Button(self,
            text='Run',
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("Run clicked"),
            relief="flat"
        )
        self.btn_run.place(
            #x=727.0,
            #y=72.0,
            x=727.0,
            y=20.0,
            width=120.0,
            height=120.0
        )
        
        self.btn_exit = Button(self,
            text='Exit',
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("Exit clicked"),
            relief="flat"
        )
        self.btn_exit.place(
            #x=552.0,
            #y=251.0,
            x=552.0,
            y=20.0,
            width=120.0,
            height=120.0
        )

