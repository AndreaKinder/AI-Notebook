import asyncio
import tkinter as tk
import customtkinter as ctk
from logs.check_log import check_file_for_generate_response_chatbot


class PromptEntry(ctk.CTkEntry):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(width=300)


class MyFrameChatBot(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.label = ctk.CTkLabel(self, text="")
        self.label.grid(row=20, padx=100, pady=230)
        self.my_entry = PromptEntry(master=self, width=290)
        self.my_entry.grid(row=21, padx=10, pady=1)
        self.my_entry.bind('<Return>', self.print_response_layout)
        self.response_widgets = []
        self.context = None

    def print_response_layout(self, event: object = None) -> object: #TODO Add text dialog form
        response, self.context = self.create_text_response_init()
        my_response_entry = tk.Text(master=self, height=2, width=35, padx=5, pady=5)
        my_response_entry.insert(tk.END, response)
        my_response_entry.configure(state='disabled')
        self.response_widgets.append(my_response_entry)
        for i, widget in enumerate(self.response_widgets):
            assert isinstance(widget, object)
            widget.grid(row=20 - i, column=0, padx=9, pady=1)
            self.grid_rowconfigure(21 - i, weight=1)
        self.my_entry.delete(0, tk.END)

    def create_text_response_init(self):
        response_update = self.my_entry.get()
        response_init, new_context = run_asyncio_coroutine(check_file_for_generate_response_chatbot(
            text=response_update,
            context=self.context)
        )
        return response_init, new_context


async def proceso(entrada):
    response = await check_file_for_generate_response_chatbot(text=entrada)
    return response


def run_asyncio_coroutine(coroutine):
    loop = asyncio.new_event_loop()
    result = loop.run_until_complete(coroutine)
    loop.close()
    return result
