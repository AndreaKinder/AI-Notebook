import tkinter as tk
import customtkinter as ctk
from chatbot_configs.translator_import import check_text


class MyFrameTranslate(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid()

        self.my_entry = tk.Entry(self, width=30)
        self.my_entry.grid(row=0, column=0, padx=10, pady=30, ipady=10)

        self.response_text = tk.Text(self, wrap=tk.WORD, height=20, width=37)
        self.response_text.grid(row=1, column=0, padx=30, pady=15)
        self.response_text.config(state="disabled")

        self.my_entry.bind('<Return>', lambda event: print_response_layout(self))

        def create_text_response_init(self):
            response_update = self.my_entry.get()
            response_init:str = check_text(text=response_update)
            return response_init

        def print_response_layout(self):
            self.response_text.config(state="normal")
            self.response_text.delete('1.0', tk.END)
            response = create_text_response_init(self)
            self.my_entry.delete(0, tk.END)
            self.response_text.insert(tk.END, response)
            self.response_text.config(state="disabled")


#TODO Add Export Text