import os
from chatbot_configs.import_api import import_text_response
from window.logg_window import create_window_log
import logs.directory_guide


file_path = logs.directory_guide.log_directory()


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




