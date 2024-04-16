import customtkinter as ctk
from window.logg_window import create_window_log
from window.tabs import MyFrameTabs

#TODO Customize UI
#TODO Add botton change option note or chatbot

class ResponseLayout(ctk.CTkEntry):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(width=150)


class MyLogButton(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(text="Log", width=30, command=create_window_log)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("IA Notebook")
        self.geometry("400x545")
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(2, weight=2)
        self.configure(fg_color="#F8F8F8")

#TODO Add frame for options configure list
        self.my_log_button = MyLogButton(master=self)
        self.my_log_button.configure(fg_color="#A9A9A9")
        self.my_log_button.grid(row=0, column=0, padx=5, pady=5)
        self.my_frame_tabs = MyFrameTabs()

def app_window_init():
    app = App()
    app.mainloop()
