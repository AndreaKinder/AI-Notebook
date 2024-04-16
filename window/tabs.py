from tkinter import ttk
from layouts.note_layout import MyFrameNote
from layouts.layout_code import MyFrameCode
from layouts.layout_translate import MyFrameTranslate

#TODO Add Options export text notes
#TODO Add Historic Notes

class MyFrameTabs:
    def __init__(self):
        self.notebook = ttk.Notebook(width=350)
        self.notebook.grid(row=0, column=1)
        self.generic_note = MyFrameNote(self.notebook)
        self.consult_code = MyFrameCode(self.notebook)
        self.translate = MyFrameTranslate(self.notebook)

        self.notebook.add(self.generic_note, text="Notes")
        self.notebook.add(self.consult_code, text="Code")
        self.notebook.add(self.translate, text="Translate")
        # TODO Add Navegate Web

