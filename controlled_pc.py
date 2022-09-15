from ctypes import sizeof
import tkinter as tk
import controlled_ui as main
import os
import pathlib
import tempfile
import subprocess
from tkinter import END, ttk
from tkinter import messagebox

def get_whitelist():
    emails = []
    try:
        with open("whitelist.txt", "r") as credentials:
            for line in credentials:

                mail = line.split(",")
                emails.append(mail[0])
            return emails
    except FileNotFoundError:
        return []

class WhiteList(tk.Tk):
    
    def __init__(self):
        
        top = tk.Tk()  

        top.resizable(0, 0)

        top.title("White List")

        top.geometry("400x500")  
  
        lbl = tk.Label(top, text = "A list of email")  
  
        listbox = tk.Listbox(top) 

        def load_list():
            try: 
                if listbox.size() > 0:
                    listbox.delete(0, END)
                with open("whitelist.txt", "r") as credentials:
                    index = 0
                    for line in credentials:

                        mail = line.split(",")
                        listbox.insert(index, mail[0])
                        
                        index += 1
                return
            except FileNotFoundError:
                return

        load_list()

        #this button will delete the selected item from the list   
  
        btn_add = tk.Button(top, text = "add")
        btn_add.config(command=lambda: EmailDetail(""))
        btn_edit = tk.Button(top, text = "edit")
        btn_edit.config(command=lambda: EmailDetail(listbox.get(listbox.curselection()[0])))
        btn_delete = tk.Button(top, text = "delete")
        btn_delete.config(command=lambda: delete(listbox.get(listbox.curselection()[0])))
        btn_reload = tk.Button(top, text = "reload")
        btn_reload.config(command=lambda: load_list())
        
        def delete(selected_email):
            try:
                credentials = open("whitelist.txt", "r")
                old_list = []
                for line in credentials:
                    mail = line.split(",")[0]
                    old_list.append(mail)
                credentials.close()

                writer = open("whitelist.txt", "w")
                for item in old_list:
                    if item != selected_email:
                        writer.write(f"{item},\n")
                writer.close()
                listbox.delete(tk.ANCHOR)
                return
            except FileNotFoundError:
                return
  
        lbl.pack()  
        listbox.pack()  
        btn_delete.pack() 
        btn_add.pack() 
        btn_edit.pack()
        btn_reload.pack()
        top.mainloop()  


class EmailDetail(tk.Tk):

    def __init__(self, email):

        tk.Tk.__init__(self, email)

        main_frame = tk.Frame(self, bg="#3F6BAA", height=150, width=250)
        # pack_propagate prevents the window resizing to match the widgets
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")

        self.geometry("250x150")
        self.resizable(0, 0)

        isAdd = len(email) == 0
        if isAdd == True:
            self.title("Add")
        else:
            self.title("Edit")

        text_styles = {"font": ("Verdana", 10),
                       "background": "#3F6BAA",
                       "foreground": "#E1FFFF"}

        email_var = tk.StringVar()
        label_user = tk.Label(main_frame, text_styles, text="Email:")
        label_user.grid(row=1, column=0)
        email_var.set(email)
        entry_user = ttk.Entry(main_frame, width=20, textvariable=email_var)
        entry_user.grid(row=1, column=1)
        entry_user.insert(0, email)

        button = ttk.Button(main_frame, text="Save", command=lambda: save())
        button.grid(row=4, column=1)

        def save():
            # Creates a text file with the Username and password
            curemail = entry_user.get()
            if curemail == email: 
                EmailDetail.destroy(self)
                return
            
            validation = validate_user(curemail)
            if not validation:
                messagebox.showerror("Information", "This email already exists")
            else:
                if len(curemail) > 0:
                    if isAdd:
                        if get_whitelist().count(curemail) > 0:
                            messagebox.showinfo("Information", "This email was existed.")
                        else:
                            credentials = open("whitelist.txt", "a")
                            credentials.write(f"{curemail},\n")
                            credentials.close()
                    else:
                        try:
                            credentials = open("whitelist.txt", "r")
                            old_list = []
                            for line in credentials:
                                line = line.split(",")
                                old_list.append(line[0])
                            credentials.close()
                            
                            writer = open("whitelist.txt", "w")
                            for item in old_list:
                                if item == email:
                                    writer.write(f"{curemail},\n")
                                else:
                                    writer.write(f"{item},\n")
                            writer.close()
                            
                        except FileNotFoundError:
                            return
                    messagebox.showinfo("Information", "This email have been stored.")
                    EmailDetail.destroy(self)

                else:
                    messagebox.showerror("Information", "Email must not empty!")

        def validate_user(email):
            # Checks the text file for a username/password combination.
            try:
                with open("whitelist.txt", "r") as credentials:
                    for line in credentials:
                        line = line.split(",")
                        if line[0] == email:
                            return False
                return True
            except FileNotFoundError:
                return True


window = tk.Tk()
window.title("Controled PC")

window.geometry("1000x600")
window.configure(bg = "#FFFFFF")
window.resizable(False, False)

def create_shortcut(shortcut_path, target, arguments='', working_dir=''):
    shortcut_path = pathlib.Path(shortcut_path)
    shortcut_path.parent.mkdir(parents=True, exist_ok=True)

    def escape_path(path):
        return str(path).replace('\\', '/')

    def escape_str(str_):
        return str(str_).replace('\\', '\\\\').replace('"', '\\"')

    shortcut_path = escape_path(shortcut_path)
    target = escape_path(target)
    working_dir = escape_path(working_dir)
    arguments = escape_str(arguments)

    js_content = f'''
        var sh = WScript.CreateObject("WScript.Shell");
        var shortcut = sh.CreateShortcut("{shortcut_path}");
        shortcut.TargetPath = "{target}";
        shortcut.Arguments = "{arguments}";
        shortcut.WorkingDirectory = "{working_dir}";
        shortcut.Save();'''

    fd, path = tempfile.mkstemp('.js')
    try:
        with os.fdopen(fd, 'w') as f:
            f.write(js_content)
        subprocess.run([R'wscript.exe', path])
    finally:
        os.unlink(path)

ui = main.Main_UI(window)
chk_var = tk.IntVar()

def on_run_clicked():
    return

def on_exit_clicked():
    return

def on_whitelist_click():
    WhiteList()

def on_stop_click():
    return

def on_autostart_checked():
    print("on_autostart_checked " + str(chk_var.get()))
    if (chk_var.get() == 1):
        ui.btn_run["state"] = "disable"
    else: 
        ui.btn_run["state"] = "active"
    return



# on click callback
ui.btn_exit.config(command=lambda: on_exit_clicked())
ui.btn_run.config(command=lambda: on_run_clicked())
ui.btn_whitelist.config(command=lambda: on_whitelist_click())
ui.btn_stop.config(command=lambda: on_whitelist_click())
ui.ckb_autostart.config(command=lambda: on_autostart_checked(), variable=chk_var)



window.mainloop()


