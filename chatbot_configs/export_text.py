from window.tabs import MyFrameTabs
from layouts.layout_code import MyFrameCode
from layouts.layout_translate import MyFrameTranslate
from layouts.note_layout import MyFrameNote


def export_code_to_markdown(master):
    MyFrameCode(master=master).export_to_markdown_code()


def export_note_to_markdown(master):
    MyFrameNote(master=master).export_markdown_note()


def export_translate_to_markdown(master):
    MyFrameTranslate(master=master).export_to_markdown_translate()


def handle_export(master):
    tabs = MyFrameTabs(master=master)
    current_text_widget = tabs.get_current_text_widget()
    if current_text_widget == MyFrameCode:
        export_code_to_markdown(master)
    elif current_text_widget == MyFrameTranslate:
        export_translate_to_markdown(master)
    elif current_text_widget == MyFrameNote:
        export_note_to_markdown(master)
