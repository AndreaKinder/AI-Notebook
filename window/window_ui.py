import customtkinter as ctk
from window.tabs import MyFrameTabs
from window.options_frame import OptionsFrame


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("IA Notebook")
        self.geometry("400x545")

        self.grid_rowconfigure(1, weight=1)
        self.configure(fg_color="#F8F8F8")

        # Inicialización y colocación de OptionsFrame con self como master
        self.options_frame = OptionsFrame(master=self)
        # Colocación de OptionsFrame en la ventana principal
        self.options_frame.grid(row=0, column=0, sticky="nesw", rowspan="33")
        self.my_frame = MyFrameTabs(master=self)



def app_window_init():
    app = App()
    app.mainloop()
