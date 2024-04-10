import os
import shutil
import subprocess
import json
import time
import minecraft_launcher_lib

minecraft_directory = 'minecraft_event/'

def start_minecraft():
    with open('data/nickname.json', 'r') as f:
        data = json.load(f)
    options = {
        "username": data["User-info"][0]["username"],
        "uuid": data["User-info"][0]["UUID"],
        "token": "",
        "jvmArguments": [],
        "executablePath": os.path.realpath(shutil.which("java"))  # The path to the java executable
        # "executablePath" : executablePath
    }

    # Получение команды для запуска Minecraft
    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command("1.18.2-forge-40.2.18", minecraft_directory, options)

    try:
        # Запуск Minecraft
        subprocess.Popen(minecraft_command)
    except Exception as e:
        print(f"Ошибка при запуске Minecraft: {e}")

start_minecraft()
