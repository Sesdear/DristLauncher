import json
import os
import shutil
import sys
import zipfile
from colorama import init
from colorama import Fore, Back, Style

from main_window import Window
from PyQt6.QtWidgets import QApplication
import requests
init()

print(Back.YELLOW + "Download icons status: in progress", Style.RESET_ALL)
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
print(Back.GREEN + "Download Icons status: Done", Style.RESET_ALL)

try:
    print(Back.YELLOW + "Delete Temp Icons files status: in progress", Style.RESET_ALL)
    folder_path = 'icons'
    file_path = destination
    os.remove(file_path)
    shutil.rmtree(folder_path)
    print(Back.GREEN + "Delete Temp files status: Done", Style.RESET_ALL)
except Exception as e:
    print(Back.RED + f"Error while deleting temp files: {e}", Style.RESET_ALL)
#_______________________________________________________________
# Создание папок

folder_path_event_create = "minecraft_event"

if not os.path.exists(folder_path_event_create):
    os.makedirs(folder_path_event_create)
    print(Back.GREEN + "Path \"minecraft_event\" Create", Style.RESET_ALL)

folder_path_dristpunk_create = "minecraft_dristpunk"

if not os.path.exists(folder_path_dristpunk_create):
    os.makedirs(folder_path_dristpunk_create)
    print(Back.GREEN + "Path \"minecraft_dristpunk\" Create", Style.RESET_ALL)

folder_path_data_create = "data"

if not os.path.exists(folder_path_data_create):
    os.makedirs(folder_path_data_create)
    print(Back.GREEN + "Path \"Data\" Create", Style.RESET_ALL)
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
    print(Back.GREEN + "Event file create: info.json", Style.RESET_ALL)

# Dristpunk info.json create
json_file_path_dristpunk = os.path.join(folder_path_dristpunk, 'info.json')
if not os.path.exists(json_file_path_dristpunk):
    with open(json_file_path_dristpunk, 'w') as f:
        json.dump({"version": 0}, f, indent=4)
    print(Back.GREEN + "Dristpunk file create: info.json", Style.RESET_ALL)

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
    print(Back.GREEN + "Data file create: nickname.json", Style.RESET_ALL)

# config.json create
json_file_path_nickname = os.path.join(folder_path_data, 'config.json')
if not os.path.exists(json_file_path_nickname):
    with open(json_file_path_nickname, 'w') as f:
        json.dump({"ram": 2048}, f, indent=4)
    print(Back.GREEN + "Data file create: config.json")

json_file_path_nickname = os.path.join(folder_path_data, 'options.json')
if not os.path.exists(json_file_path_nickname):
    with open(json_file_path_nickname, 'w') as f:
        json.dump({
    "username": "None",
    "uuid": "None"
    }, f, indent=4)
    print(Back.GREEN + "Data file create: options.json", Style.RESET_ALL)

#_______________________________________________________________
print("Start DristLauncher", Style.RESET_ALL)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())