from tkinter import Entry, Text, WORD, END
from turtle import fd

import customtkinter as ctk
from chatbot_configs.translator_import import check_text


class MyFrameTranslate(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=2)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=1)

        self.my_entry = Entry(self)
        self.my_entry.grid(row=1, column=1, padx=40, pady=2, ipady=10, sticky='ew')

        self.response_text = Text(self, wrap=WORD, height=25, width=35)
        self.response_text.grid(row=2, column=1, padx=20, pady=5, sticky='ew')
        self.response_text.config(state="disabled")
        self.my_entry.bind('<Return>', lambda event: print_response_layout(self))



        def create_text_response_init(self):
            response_update = self.my_entry.get()
            response_init:str = check_text(text=response_update)
            return response_init

        def print_response_layout(self):
            self.response_text.config(state="normal")
            self.response_text.delete('1.0', END)
            response = create_text_response_init(self)
            self.my_entry.delete(0, END)
            self.response_text.insert(END, response)
            self.response_text.config(state="disabled")

