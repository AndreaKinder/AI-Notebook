import asyncio
import tkinter as tk
import customtkinter as ctk
from logs.check_log import check_file_for_generate_response



class PromptEntry(ctk.CTkEntry):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(width=300)


class MyFrameNote(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid()

        self.my_entry = tk.Entry(self, width=30)
        self.my_entry.grid(row=1, padx=10, pady=1)

        self.response_text = tk.Text(self, wrap=tk.WORD, height=25, width=37)
        self.response_text.grid(row=0, column=0, padx=30, pady=20)
        self.response_text.config(state="disabled")

        self.my_entry.bind('<Return>', lambda eveny: print_response_layout(self))

        def create_text_response_init(self):
            response_update = self.my_entry.get()
            response_init = run_asyncio_coroutine(proceso(entrada=response_update))
            return response_init

        def print_response_layout(self):
            response = create_text_response_init(self)
            self.my_entry.delete(0, tk.END)
            self.response_text.config(state="normal")
            self.response_text.insert(tk.END, response)
            self.response_text.config(state="disabled")

@staticmethod
async def proceso(entrada):
    response = await check_file_for_generate_response(text=entrada)
    return response

@staticmethod
def run_asyncio_coroutine(coroutine):
   loop = asyncio.new_event_loop()
   result = loop.run_until_complete(coroutine)
   loop.close()
   return result