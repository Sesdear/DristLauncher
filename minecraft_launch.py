import os
import shutil
import subprocess
import json
import minecraft_launcher_lib
import requests
from bs4 import BeautifulSoup
import random

def start_minecraft_event():
    print("\n Start Launch Minecraft")
    minecraft_directory = 'minecraft_event/'

    url = "https://chocolate-elenore-53.tiiny.site/"
    response = requests.get(url)

    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    version_minecraft = soup.find('p', class_='event_minecraft_version')
    version_minecraft_on_website = version_minecraft.get_text()

    version_loader = soup.find('p', class_='event_loader_version')
    version_loader_on_website = version_loader.get_text()

    mods_loader_version = soup.find('p', class_='modsLoader_event_version')
    mods_loader_version_on_website = mods_loader_version.get_text()

    print(version_minecraft)
    print(version_loader_on_website)
    print(mods_loader_version_on_website)

    file_path = 'data/nickname.json'

    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            data1 = json.load(f)
        print("Nickname.json найден")

        print("Options 1")
        options = {
            "username": data1["User-info"][0]["username"],
            "uuid": data1["User-info"][0]["UUID"],
            "token": "",
            "jvmArguments": [],
            "executablePath": os.path.realpath(shutil.which("java")), # The path to the java executable
            "gameDirectory": ""
            # "executablePath" : executablePath
        }
        print("Options 2")
    else:
        print("Файл 'data/nickname.json' не найден.")
        return  # Выйти из функции, так как нет необходимых данных для запуска Minecraft


    # __________________________________
    file_path2 = 'data/config.json'
    print('Minecraft data path')

    if os.path.exists(file_path2):
        with open(file_path2, 'r') as config:
            ram_config = json.load(config)
        max_ram = ram_config["ram"]
        print('Minecraft pick ram')
    else:
        print("Файл 'data/config.json' не найден.")
        return

    print('\n\nCheck Errors\n')

    print('\nFix Minecraft\n')
    print("Download forge")

    current_max = 0

    def set_status(status: str):
        print(status)

    def set_progress(progress: int):
        if current_max != 0:
            print(f"{progress}/{current_max}")

    def set_max(new_max: int):
        global current_max
        current_max = new_max

    minecraft_directory = 'minecraft_event/'

    callback = {
        "setStatus": set_status,
        "setProgress": set_progress,
        "setMax": set_max
    }


    destination_folder = 'minecraft_event/'
    forge_version = minecraft_launcher_lib.forge.find_forge_version(f"{version_minecraft_on_website}")
    print(forge_version)
    minecraft_launcher_lib.forge.install_forge_version(forge_version, destination_folder, callback=callback)
    # __________________________________

    print(f"Fix {random.randrange(1, 100)} Errors")

    options["jvmArguments"] = [f"-Xmx{max_ram}m", f"-Xms256m"]
    options["gameDirectory"] = "minecraft_event/"
    print('Minecraft jvmArgs applyed')

    # Получение команды для запуска Minecraft
    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(
        f"{version_minecraft_on_website}-{mods_loader_version_on_website}-{version_loader_on_website}",
        minecraft_directory, options)
    print(f'Minecraft command OK: {minecraft_command}')


    try:
        # Запуск Minecraft
        subprocess.Popen(minecraft_command)
    except Exception as e:
        print(f"Ошибка при запуске Minecraft: {e}")


def start_minecraft_dristpunk():
    print("\n Start Launch Minecraft")
    minecraft_directory = 'minecraft_dristpunk/'

    url = "https://chocolate-elenore-53.tiiny.site/"
    response = requests.get(url)

    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    version_minecraft = soup.find('p', class_='dristpunk_minecraft_version')
    version_minecraft_on_website = version_minecraft.get_text()

    version_loader = soup.find('p', class_='dristpunk_loader_version')
    version_loader_on_website = version_loader.get_text()

    mods_loader_version = soup.find('p', class_='modsLoader_dristpunk_version')
    mods_loader_version_on_website = mods_loader_version.get_text()

    print(version_minecraft)
    print(version_loader_on_website)
    print(mods_loader_version_on_website)

    file_path = 'data/nickname.json'

    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            data1 = json.load(f)
        print("Nickname.json найден")

        print("Options 1")
        options = {
            "username": data1["User-info"][0]["username"],
            "uuid": data1["User-info"][0]["UUID"],
            "token": "",
            "jvmArguments": [],
            "executablePath": os.path.realpath(shutil.which("java")), # The path to the java executable
            "gameDirectory": ""
            # "executablePath" : executablePath
        }
        print("Options 2")
    else:
        print("Файл 'data/nickname.json' не найден.")
        return  # Выйти из функции, так как нет необходимых данных для запуска Minecraft


    # __________________________________
    file_path2 = 'data/config.json'
    print('Minecraft data path')

    if os.path.exists(file_path2):
        with open(file_path2, 'r') as config:
            ram_config = json.load(config)
        max_ram = ram_config["ram"]
        print('Minecraft pick ram')
    else:
        print("Файл 'data/config.json' не найден.")
        return

    print('\n\nCheck Errors\n')

    print('\nFix Minecraft\n')
    print("Download forge")

    current_max = 0

    def set_status(status: str):
        print(status)

    def set_progress(progress: int):
        if current_max != 0:
            print(f"{progress}/{current_max}")

    def set_max(new_max: int):
        global current_max
        current_max = new_max

    minecraft_directory = 'minecraft_dristpunk/'

    callback = {
        "setStatus": set_status,
        "setProgress": set_progress,
        "setMax": set_max
    }


    destination_folder = 'minecraft_dristpunk/'
    forge_version = minecraft_launcher_lib.forge.find_forge_version(f"{version_minecraft_on_website}")
    print(forge_version)
    minecraft_launcher_lib.forge.install_forge_version(forge_version, destination_folder, callback=callback)
    # __________________________________

    print(f"Fix {random.randrange(1, 100)} Errors")

    options["jvmArguments"] = [f"-Xmx{max_ram}m", f"-Xms256m"]
    options["gameDirectory"] = "minecraft_dristpunk/"
    print('Minecraft jvmArgs applyed')

    # Получение команды для запуска Minecraft
    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(
        f"{version_minecraft_on_website}-{mods_loader_version_on_website}-{version_loader_on_website}",
        minecraft_directory, options)
    print(f'Minecraft command OK: {minecraft_command}')


    try:
        # Запуск Minecraft
        subprocess.Popen(minecraft_command)
    except Exception as e:
        print(f"Ошибка при запуске Minecraft: {e}")



