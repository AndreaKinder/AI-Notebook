from googletrans import Translator


translator = Translator(service_urls=[
    'translate.google.com',
    'translate.google.co.kr',
])


def translate_text(item, dest='en', src='es'):
    new_text:str = item
    print(new_text)
    try:
        a = translator.translate(text=new_text, dest=dest, src=src)
        translated_text = a.__dict__()["text"]
        return translated_text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None



def check_text(text):
    translated = translate_text(item=text)
    return translated


# TODO Function Detect lenguage
# TODO Function auto change traduction
