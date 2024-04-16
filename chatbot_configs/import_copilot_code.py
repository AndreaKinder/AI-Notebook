from chatbot_configs.import_api import import_chat_bot
from logs.create_log import read_log


async def import_chat_code(text):
    email, passwd = read_log()
    chatbot = import_chat_bot(email=email, passwd=passwd)
    assistant = chatbot.search_assistant(assistant_name='Coder: Code Writer/Completer/Explainer/Debugger')
    code_chat = chatbot.new_conversation(assistant=assistant, system_prompt=text ,switch_to=True)
    response = chatbot.chat(text=text, conversation=code_chat)
    return response


