import tkinter as tk
import controlled_ui as main

window = tk.Tk()
window.title("Controled PC")

window.geometry("1000x600")
window.configure(bg = "#FFFFFF")
window.resizable(False, False)

def on_run_clicked():
    return

def on_exit_clicked():
    return

ui = main.Main_UI(window)
# on click callback
ui.btn_exit.config(command=on_exit_clicked())
ui.btn_run.config(command=on_run_clicked())

window.mainloop()

