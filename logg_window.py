import customtkinter as ctk


class InputUs(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label_us = ctk.CTkLabel(self, text="Usuario:", width=150)
        self.label_us.grid(row=0, column=0)

        self.entry_new_us = ctk.CTkEntry(self, width=300)
        self.entry_new_us.grid(row=0, column=1)


class InputPasswd(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label_passwd = ctk.CTkLabel(self, text="Contraseña:", width=150)
        self.label_passwd.grid(row=0, column=0)

        self.entry_new_passwd = ctk.CTkEntry(self, width=300)
        self.entry_new_passwd.grid(row=0, column=1)


class ButtonLog(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.button_action = ctk.CTkButton(self, width=20)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Loggin")
        self.geometry("500x150")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.log_button = ButtonLog(master=self, text="Logg In")
        self.input_us = InputUs(master=self)
        self.input_passwd = InputPasswd(master=self)

        self.input_us.grid(row=0)
        self.input_passwd.grid(row=1)
        self.log_button.grid(row=2)


def crate_wondow_log():
    app = App()
    app.mainloop()
