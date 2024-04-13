import json
import os
import shutil
import sys
import zipfile

from main_window import Window
from PyQt6.QtWidgets import QApplication
import requests

repo_url = 'https://codeload.github.com/Sesdear/Drist_Sources/zip/refs/heads/Icons'
destination_folder_parent = '.'
source_folder = 'icons/Drist_Sources-Icons/'
destination_folder = '.'

destination = os.path.join(destination_folder_parent, 'icons.zip')
response = requests.get(repo_url, stream=True)
with open(destination, 'wb') as f:
    f.write(response.content)

extracted_folder_path = os.path.join(destination_folder_parent, 'icons')
with zipfile.ZipFile(destination, 'r') as zip_ref:
    zip_ref.extractall(extracted_folder_path)

for filename in os.listdir(source_folder):
    source_file_path = os.path.join(source_folder, filename)
    destination_file_path = os.path.join(destination_folder, filename)
    print(f"Moving {source_file_path} to {destination_file_path}")
    shutil.move(source_file_path, destination_file_path)
print("Download mods from github status: Done")

try:
    print("\nDelete Temp mods files status: in progress")
    folder_path = 'icons'
    file_path = destination
    os.remove(file_path)
    shutil.rmtree(folder_path)
    print("Delete Temp files status: Done")
except Exception as e:
    print(f"Error while deleting temp files: {e}")
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