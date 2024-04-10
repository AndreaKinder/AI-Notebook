import customtkinter
from import_api import response
import tracemalloc
import asyncio

tracemalloc.start()

pregunta = ""


async def question():
    pregunta_pendiente = entry.get()
    print(pregunta_pendiente)
    return pregunta_pendiente


async def respuesta():
    respuesta_pendiente = await response(text=await question())
    print(respuesta_pendiente)
    return respuesta_pendiente


async def resolucion():
    await question()
    await respuesta()


def start_asyncio_loop():
    loop = asyncio.get_event_loop()
    if not loop.is_running():
        asyncio.ensure_future(resolucion())
        loop.run_forever()


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("600x440")

entry = customtkinter.CTkEntry(app, width=500, textvariable=pregunta, placeholder_text="CTkEntry")
entry.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)

# Bind the Return key to a function that starts the asyncio loop
entry.bind("<Return>", lambda event: start_asyncio_loop())

app.mainloop()

