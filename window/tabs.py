from tkinter import ttk
from window.chatbot_layout import MyFrameChatBot
from window.note_layout import MyFrameNote

class MyFrameTabs:
    def __init__(self):
        self.notebook = ttk.Notebook(width=350)
        self.notebook.grid(row=0, column=1)
        self.pagina1 = MyFrameChatBot(self.notebook)
        self.pagina2 = MyFrameNote(self.notebook)

        self.notebook.add(self.pagina1, text="ChatBot")
        self.notebook.add(self.pagina2, text="Notes")


