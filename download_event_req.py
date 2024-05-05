import os
import requests
import zipfile
import shutil

from colorama import Back, Style
from colorama import init
init()

def download_and_update_mods():
    print("\n")
    print("\n")
    source_folder = 'minecraft_event/mods/Drist_Sources-Event_Data/'
    destination_folder = 'minecraft_event/mods'

    print(Back.YELLOW + f"Download mods from Github status: in progress (files path: {destination_folder}", Style.RESET_ALL)

    repo_url = 'https://codeload.github.com/Sesdear/Drist_Sources/zip/refs/heads/Event_Data'
    destination_folder_parent = 'minecraft_event/'

    if not os.path.exists(destination_folder_parent):
        os.makedirs(destination_folder_parent)
    destination = os.path.join(destination_folder_parent, 'mods.zip')

    response = requests.get(repo_url, stream=True)

    with open(destination, 'wb') as f:
        f.write(response.content)

    extracted_folder_path = os.path.join(destination_folder_parent, 'mods')
    with zipfile.ZipFile(destination, 'r') as zip_ref:
        zip_ref.extractall(extracted_folder_path)

    for filename in os.listdir(source_folder):
        source_file_path = os.path.join(source_folder, filename)
        destination_file_path = os.path.join(destination_folder, filename)
        print(f"Moving {source_file_path} to {destination_file_path}")
        shutil.move(source_file_path, destination_file_path)
    print(Back.GREEN + "Download mods from github status: Done", Style.RESET_ALL)
    try:
        print(Back.YELLOW + "Delete Temp mods files status: in progress", Style.RESET_ALL)
        folder_path = source_folder
        file_path = destination
        os.remove(file_path)
        shutil.rmtree(folder_path)
        print(Back.GREEN + "Delete Temp files status: Done", Style.RESET_ALL)
    except Exception as e:
        print(f"Error while deleting temp files: {e}", Style.RESET_ALL)
    print("\n")
    print("\n")

def minecraft_download_event():
    print("\n")
    print("\n")
    source_folder = 'minecraft_event/Drist_Sources-Event_Minecraft/'
    destination_folder = 'minecraft_event/'

    print(Back.YELLOW + f"Download minecraft from github status: in progress (files path: {destination_folder}", Style.RESET_ALL)

    repo_url = 'https://codeload.github.com/Sesdear/Drist_Sources/zip/refs/heads/Event_Minecraft'
    destination_folder_parent = 'minecraft_event/'

    if not os.path.exists(destination_folder_parent):
        os.makedirs(destination_folder_parent)

    print("\n")
    print(Back.YELLOW + "Download minecraft.zip status: in progress", Style.RESET_ALL)
    destination = os.path.join(destination_folder_parent, 'minecraft.zip')
    response = requests.get(repo_url, stream=True)
    print(Back.GREEN + "Download minecraft.zip status: Done")
    print("\n")

    with open(destination, 'wb') as f:
        f.write(response.content)

    extracted_folder_path = destination_folder_parent
    with zipfile.ZipFile(destination, 'r') as zip_ref:
        zip_ref.extractall(extracted_folder_path)

    for filename in os.listdir(source_folder):
        source_file_path = os.path.join(source_folder, filename)
        destination_file_path = os.path.join(destination_folder, filename)
        print(f"Moving {source_file_path} to {destination_file_path}")
        shutil.move(source_file_path, destination_file_path)
    print(Back.GREEN + "Download minecraft from github status: Done", Style.RESET_ALL)

    print("\n")
    try:
        print(Back.YELLOW + "Delete Temp minecraft files status: in progress", Style.RESET_ALL)
        folder_path = source_folder
        file_path = destination
        os.remove(file_path)
        shutil.rmtree(folder_path)
        print(Back.GREEN + "Delete Temp files status: Done", Style.RESET_ALL)
    except Exception as e:
        print(f"Error while deleting temp files: {e}")
    print("\n")
    print("\n")

