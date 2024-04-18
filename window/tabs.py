from tkinter.ttk import Notebook
from layouts.note_layout import MyFrameNote
from layouts.layout_code import MyFrameCode
from layouts.layout_translate import MyFrameTranslate


class MyFrameTabs:
    def __init__(self, master, **kwargs):
        # Asegurarse de que el notebook se pueda colocar correctamente en el master
        self.notebook = Notebook(master, **kwargs)
        master.grid_columnconfigure(1, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Inicializar las pestañas con el notebook como su master
        self.generic_note = MyFrameNote(self.notebook)
        self.consult_code = MyFrameCode(self.notebook)
        self.translate = MyFrameTranslate(self.notebook)

        # Añadir las pestañas al notebook
        self.notebook.add(self.generic_note, text="Notes")
        self.notebook.add(self.consult_code, text="Code")
        self.notebook.add(self.translate, text="Translate")
        self.notebook.grid(row=0, column=1, sticky='nsew', rowspan=5, columnspan=50)

    def get_current_text_widget(self):
        return self.notebook.winfo_children()[self.notebook.index(self.notebook.select())]
