from hugchat import hugchat
from hugchat.login import Login
from check_log import check_file_log
from create_log import read_log
from logg_window import crate_wondow_log


def import_chat_bot(mail, passwd):
    EMAIL = mail
    PASSWD = passwd
    cookie_path_dir = "./cookies/"
    sign = Login(EMAIL, PASSWD)
    cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    return chatbot


def response(text, mail, passwd):
    chatbot = import_chat_bot(mail=mail, passwd=passwd)
    query_result = chatbot.chat(text)
    print(query_result)
    return query_result


def import_log_api(text):
    checking_file = check_file_log()
    if checking_file:
        mail, passwd = read_log()
        response(text=text, mail=mail, passwd=passwd)
    else:
        crate_wondow_log()
