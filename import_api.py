from hugchat import hugchat
from hugchat.login import Login
from hugchat.message import Message
from log import capture_log

mail, passwd = capture_log()

EMAIL = mail
PASSWD = mail
cookie_path_dir = "./cookies/"
sign = Login(EMAIL, PASSWD)
cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)

# Create your ChatBot
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"


def response(text):
    query_result: Message = chatbot.chat(text)
    print(query_result)
    return query_result
