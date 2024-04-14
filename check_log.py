import os

folder_name = 'data'
file_path = os.path.join(folder_name, 'log.json')

def check_directory(directory):
    if os.path.isdir(directory):
        for filename in os.listdir(directory):
            if filename.endswith(".json"):
                return True
    return False


def funcion_si_existe():
    print("El directorio existe y contiene un archivo JSON.")


def funcion_si_no_existe():
    print("El directorio no existe o no contiene un archivo JSON.")





def check_file_log():
    directory = os.path.dirname(file_path)  # Get directory path from file path
    if check_directory(directory):
        funcion_si_existe()
        return True
    else:
        funcion_si_no_existe()
        return False
