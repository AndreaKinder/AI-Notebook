import json
import os

folder_name = 'data'
file_path = os.path.join(folder_name, 'log.json')


def capture_log(us, paswd):
    data = {'us': us, 'paswd': paswd}
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    with open(file_path, 'w') as file:
        json.dump(data, file)

def read_log():
    obj_log=object
    with open(file_path, 'r') as log:
        log_data = json.dump(fp=obj_log, log)
        print(log_data)

read_log()
