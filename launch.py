import json
import os
import sys
from main_window import Window
from PyQt6.QtWidgets import QApplication


with open('error_log.txt', 'w') as f:
    sys.stderr = f
sys.stderr = sys.__stderr__
#_______________________________________________________________
# Создание папок

folder_path_event_create = "minecraft_event"

if not os.path.exists(folder_path_event_create):
    os.makedirs(folder_path_event_create)
    print("Path \"minecraft_event\" Create")

folder_path_dristpunk_create = "minecraft_dristpunk"

if not os.path.exists(folder_path_dristpunk_create):
    os.makedirs(folder_path_dristpunk_create)
    print("Path \"minecraft_dristpunk\" Create")

folder_path_data_create = "data"

if not os.path.exists(folder_path_data_create):
    os.makedirs(folder_path_data_create)
    print("Path \"Data\" Create")
#_______________________________________________________________
# Создание .json Файлов

folder_path_event = 'minecraft_event/'
folder_path_dristpunk = 'minecraft_dristpunk/'
folder_path_data = 'data/'

# Event info.json create
json_file_path_event = os.path.join(folder_path_event, 'info.json')
if not os.path.exists(json_file_path_event):
    with open(json_file_path_event, 'w') as f:
        json.dump({"version": 0}, f, indent=4)
    print("Event file create: info.json")

# Dristpunk info.json create
json_file_path_dristpunk = os.path.join(folder_path_dristpunk, 'info.json')
if not os.path.exists(json_file_path_dristpunk):
    with open(json_file_path_dristpunk, 'w') as f:
        json.dump({"version": 0}, f, indent=4)
    print("Dristpunk file create: info.json")

# nickname.json create
json_file_path_nickname = os.path.join(folder_path_data, 'nickname.json')
if not os.path.exists(json_file_path_nickname):
    with open(json_file_path_nickname, 'w') as f:
        json.dump({
            "accessToken": None,
            "clientToken": None,
            "User-info": [{
                "username": "None",
                "AUTH_TYPE": "Offline Login",
                "UUID": "None"
            }]
        }, f, indent=4)
    print("Data file create: nickname.json")

# config.json create
json_file_path_nickname = os.path.join(folder_path_data, 'config.json')
if not os.path.exists(json_file_path_nickname):
    with open(json_file_path_nickname, 'w') as f:
        json.dump({"ram": 2048}, f, indent=4)
    print("Data file create: config.json")

json_file_path_nickname = os.path.join(folder_path_data, 'options.json')
if not os.path.exists(json_file_path_nickname):
    with open(json_file_path_nickname, 'w') as f:
        json.dump({
    "username": "None",
    "uuid": "None"
    }, f, indent=4)
    print("Data file create: options.json")

#_______________________________________________________________
print("Start DristLauncher")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Window()
    sys.exit(app.exec())