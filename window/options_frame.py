import customtkinter as ctk
from window.logg_window import create_window_log
from chatbot_configs.export_text import handle_export


class MyLogButton(ctk.CTkButton):
    def __init__(self, master, **kwargs):  # Corrected to include master
        super().__init__(master, **kwargs)  # Now correctly passing master and **kwargs to super
        self.configure(text="Log", width=30, command=create_window_log)


class ExportButton(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(text="Exp", width=30, command=handle_export(master))


class OptionsFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)  # Corrected to include call to super().__init__
        self.configure(fg_color="#F8F8F8")
        self.export_button = ExportButton(master=self)
        self.my_log_button = MyLogButton(master=self)
        self.export_button.grid(row=29, column=0, padx=5, pady=5)
        self.my_log_button.grid(row=30, column=0, padx=5, pady=5)
