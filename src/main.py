import customtkinter as ctk
from tkinter.ttk import Notebook
import asyncio
from tkinter import Entry, Text, WORD, END, filedialog as fd
from hugchat import hugchat
from hugchat.login import Login
import json
import os
from datetime import datetime
from openai import OpenAI


folder_name = 'storage'

file_path: str = os.path.join(folder_name, 'log.json')

#Lectura de Open AI
file_path_Chat_GPT_API = os.path.join(folder_name, 'log_OpenAPI.json')


def capture_log_openAPI(openAPI):
    open_api = {'OpenAPI': openAPI}
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    with open(file_path, 'w') as file:
        json.dump(open_api, file)


def read_log_OpenAI():
    if not os.path.exists(file_path_Chat_GPT_API):
        create_window_log()
    else:
        try:
            with open(file_path_Chat_GPT_API, 'r') as log:
                log_data_openAPI = json.load(log)
                return log_data_openAPI['OpenAPI']
        except json.decoder.JSONDecodeError:
            create_window_log()


#Lectura hugchat
def capture_log_hug(us, passwd):
    data = {'us': us, 'passwd': passwd}
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    with open(file_path, 'w') as file:
        json.dump(data, file)


def read_log_hug():
    if not os.path.exists(file_path):
        create_window_log()
    else:
        try:
            with open(file_path, 'r') as log:
                log_data = json.load(log)
                return log_data['us'], log_data['passwd']
        except json.decoder.JSONDecodeError:
            create_window_log()

#importacion Chat GPT
def import_ChatGPT(openAPI):
    client = OpenAI(openAPI)
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"},
            {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
            {"role": "user", "content": "Where was it played?"}
        ]
    )
    return response


#importacion HugChat
def import_chat_bot_hug(email, passwd):
    EMAIL = email
    PASSWD = passwd
    cookie_path_dir = folder_name
    sign = Login(EMAIL, PASSWD)
    cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    return chatbot


def generate_response_hug(text, email, passwd):
    chatbot = import_chat_bot_hug(email=email, passwd=passwd)
    query_result = chatbot.chat(text)
    return query_result


async def import_text_response_hug(text):
    email, passwd = read_log_hug()
    return generate_response_hug(text=text, email=email, passwd=passwd)


def check_directory(directory):
    if os.path.isdir(directory):
        for filename in os.listdir(directory):
            if filename.endswith(".json"):
                return True
    return False


def check_file_true():
    print("The directory exists and contains a JSON file.")


def check_file_false():
    print("The directory does not exist or does not contain a JSON file.")


def check_file_log():
    directory = os.path.dirname(file_path)  # Get directory path from file path
    if check_directory(directory):
        check_file_true()
        return True
    else:
        check_file_false()
        create_window_log()
        return False


async def import_chat(text):
    email, passwd = read_log_hug()
    chatbot = import_chat_bot_hug(email=email, passwd=passwd)
    response = chatbot.chat(text=text)
    return response


def import_frame(master):
    class MyFrame(ctk.CTkFrame):
        def __init__(self, master=master, **kwargs):
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

            self.export_button = ctk.CTkButton(self, text="Export to Markdown", command=self.export_to_markdown,
                                               fg_color="#FF9800",
                                               text_color="black")
            self.export_button.grid(row=3, column=1, padx=20, pady=10, sticky='ew')

            self.my_entry.bind('<Return>', lambda event: self.master.after(0, self.print_response_layout))

        def create_text_response_init(self):
            response_update = self.my_entry.get()
            response_init = asyncio.run(self.proceso(entrada=response_update))
            return response_init

        def export_to_markdown(self):
            if file_path:
                text_to_export = self.response_text.get("1.0", END)
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(text_to_export)

        def print_response_layout(self):
            response = self.create_text_response_init()
            self.my_entry.delete(0, END)
            self.response_text.config(state="normal")
            self.response_text.insert(END, response)
            self.response_text.config(state="disabled")

        @staticmethod
        async def proceso(entrada):
            if check_file_log():
                response = await import_chat(text=entrada)
                return response

    return MyFrame(master)


class MyFrameTabs:
    def __init__(self, master, **kwargs):
        self.notebook = Notebook(master, **kwargs)
        master.grid_columnconfigure(1, weight=1)
        master.grid_rowconfigure(0, weight=1)

        self.generic_note = import_frame(master=master)

        self.notebook.add(self.generic_note, text="Notes")
        self.notebook.grid(row=0, column=1, sticky='nsew', rowspan=5, columnspan=50)

    def get_current_text_widget(self):
        return self.notebook.winfo_children()[self.notebook.index(self.notebook.select())]


class InputUs(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label_us = ctk.CTkLabel(self, text="Us:", width=150)
        self.label_us.grid(row=0, column=0)

        self.entry_new_us = ctk.CTkEntry(self, width=300)
        self.entry_new_us.grid(row=0, column=1)


class InputPasswd(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label_passwd = ctk.CTkLabel(self, text="Password:", width=150)
        self.label_passwd.grid(row=0, column=0)

        self.entry_new_passwd = ctk.CTkEntry(self, show="*", width=300)
        self.entry_new_passwd.grid(row=0, column=1)


class ButtonLog(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs, fg_color="#FF9800", text_color="black")
        self.button_action = ctk.CTkButton(self, width=20)


class App_login_hug(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Logging")
        self.geometry("500x150")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.input_us = InputUs(master=self)
        self.input_passwd = InputPasswd(master=self)

        def logging():
            new_us = self.input_us.entry_new_us.get()
            new_passwd = self.input_passwd.entry_new_passwd.get()
            capture_log_hug(us=new_us, passwd=new_passwd)
            self.destroy()
            read_log_hug()

        self.log_button = ButtonLog(master=self, text="Logg In", command=logging)

        self.input_us.grid(row=0)
        self.input_passwd.grid(row=1)
        self.log_button.grid(row=2)


def create_window_log():
    if not os.path.exists(file_path):
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
    open(file_path, 'w').close()
    app = App_login_hug()
    app.mainloop()


class MyLogButton(ctk.CTkButton):
    def __init__(self, master, **kwargs):  
        super().__init__(master, **kwargs)  
        self.configure(text="Log", width=30, command=create_window_log)


class OptionsFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)  
        self.my_log_button = MyLogButton(master=self, fg_color="#FF9800", text_color="black")
        self.my_log_button.grid(row=30, column=0, padx=5, pady=5)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("IA Notebook")
        self.geometry("400x545")

        self.grid_rowconfigure(1, weight=1)

        self.options_frame = OptionsFrame(master=self)
        self.options_frame.grid(row=0, column=0, sticky="nesw", rowspan="33")
        self.my_frame = MyFrameTabs(master=self)


def app_window_init():
    app = App()
    app.mainloop()


if __name__ == '__main__':
    app_window_init()
