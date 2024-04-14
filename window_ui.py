import customtkinter as ctk
from logg_window import crate_wondow_log
from import_api import import_log_api


class MyLogButton(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(text="Log", width=30, command=crate_wondow_log)


class PromptEntry(ctk.CTkEntry):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(width=300)


class MyFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.label = ctk.CTkLabel(self, text="")
        self.label.grid(padx=100, pady=230)
        self.my_entry = PromptEntry(master=self, width=290)
        self.my_entry.grid(padx=10, pady=1)
        self.my_entry.bind('<Return>', lambda event: text_response_init())
        def text_response_init():
            update_question = self.my_entry.get()
            import_log_api(text=update_question)



class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Chat Bot")
        self.geometry("400x600")
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(2, weight=2)

        self.my_frame = MyFrame(master=self)
        self.my_frame.grid(row=2, column=1, padx=10, pady=10)

        self.my_log_button = MyLogButton(master=self)
        self.my_log_button.grid(row=2, column=0, padx=5, pady=5)


app = App()
app.mainloop()


