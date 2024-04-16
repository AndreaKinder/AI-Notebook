from hugchat import hugchat
from hugchat.login import Login
from logs.create_log import read_log
import logs.directory_guide


def import_chat_bot(email, passwd):
    EMAIL = email
    PASSWD = passwd
    cookie_path_dir = logs.directory_guide.data_directory_folder()
    sign = Login(EMAIL, PASSWD)
    cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    return chatbot


def generate_response(text, email, passwd):
    chatbot = import_chat_bot(email=email, passwd=passwd)
    query_result = chatbot.chat(text)
    return query_result


async def import_text_response(text):
    email, passwd = read_log()
    return generate_response(text=text, email=email, passwd=passwd)

