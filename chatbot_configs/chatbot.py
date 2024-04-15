from chatbot_configs.import_api import import_chat_bot
from logs.create_log import read_log


def generate_response_chat_bot(text, email, passwd, context=None):
    chatbot = import_chat_bot(email=email, passwd=passwd)
    query_result, new_context = chatbot.chat(text, context=context)
    return query_result, new_context


async def import_chat_response(text, context=None):
    email, passwd = read_log()
    response, new_context = generate_response_chat_bot(text=text, email=email, passwd=passwd, context=context)
    return response, new_context
