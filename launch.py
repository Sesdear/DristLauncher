import json
import os
from main_window import Window
import sys
from PyQt6.QtWidgets import QApplication

#_______________________________________________________________
# Создание папок

folder_path_event_create = "minecraft_event"

if not os.path.exists(folder_path_event_create):
    os.makedirs(folder_path_event_create)

folder_path_dristpunk_create = "minecraft_dristpunk"

if not os.path.exists(folder_path_dristpunk_create):
    os.makedirs(folder_path_dristpunk_create)

folder_path_data_create = "data"

if not os.path.exists(folder_path_data_create):
    os.makedirs(folder_path_data_create)
#_______________________________________________________________
# Создание .json Файлов

folder_path_event = 'minecraft_event/'
folder_path_dristpunk = 'minecraft_dristpunk/'
folder_path_data = 'data/'

# Event info.json create
json_file_path_event = os.path.join(folder_path_event, 'info.json')
if not os.path.exists(json_file_path_event):
    with open(json_file_path_event, 'w') as f:
        json.dump({"version": 0, "minecraft_version": 0, "forge_version": 0}, f, indent=4)

# Dristpunk info.json create
json_file_path_dristpunk = os.path.join(folder_path_dristpunk, 'info.json')
if not os.path.exists(json_file_path_dristpunk):
    with open(json_file_path_dristpunk, 'w') as f:
        json.dump({"version": 0, "minecraft_version": 0, "forge_version": 0}, f, indent=4)

# nickname.json create
json_file_path_nickname = os.path.join(folder_path_data, 'nickname.json')
if not os.path.exists(json_file_path_nickname):
    with open(json_file_path_nickname, 'w') as f:
        json.dump({"nickname": "none"}, f, indent=4)

# config.json create
json_file_path_nickname = os.path.join(folder_path_data, 'config.json')
if not os.path.exists(json_file_path_nickname):
    with open(json_file_path_nickname, 'w') as f:
        json.dump({"ram": 2048}, f, indent=4)
#_______________________________________________________________
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Window()
    sys.exit(app.exec())