import threading
import os
import requests
import zipfile
import shutil
import time

def download_and_update_mods():
    def download_and_update():
        # Ваша функция download_and_update_mods()
        source_folder = 'minecraft_dristpunk/mods/Drist_Sources-Dristpunk_Data/'
        destination_folder = 'minecraft_dristpunk/mods'

        print(f"\nDownload mods from Github status: in progress (files path: {destination_folder}")

        repo_url = 'https://codeload.github.com/Sesdear/Drist_Sources/zip/refs/heads/Dristpunk_Data'
        destination_folder_parent = 'minecraft_dristpunk/'

        if not os.path.exists(destination_folder_parent):
            os.makedirs(destination_folder_parent)
        print("Download mods")
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
        print("Download mods from github status: Done")
        try:
            print("\nDelete Temp mods files status: in progress")
            folder_path = source_folder
            file_path = destination
            os.remove(file_path)
            shutil.rmtree(folder_path)
            print("Delete Temp files status: Done")
        except Exception as e:
            print(f"Error while deleting temp files: {e}")

    # Создаем и запускаем поток для выполнения функции download_and_update()
    mods_thread = threading.Thread(target=download_and_update)
    mods_thread.start()
    mods_thread.join()
    time.sleep(5)

def minecraft_download_dristpunk():
    def minecraft_download():
        source_folder = 'minecraft_dristpunk/Drist_Sources-Dristpunk_Minecraft/'
        destination_folder = 'minecraft_dristpunk/'

        print(f"\nDownload minecraft from github status: in progress (files path: {destination_folder}")

        repo_url = 'https://codeload.github.com/Sesdear/Drist_Sources/zip/refs/heads/Dristpunk_Minecraft'
        destination_folder_parent = 'minecraft_dristpunk/'

        if not os.path.exists(destination_folder_parent):
            os.makedirs(destination_folder_parent)

        print("Download minecraft.zip status: in progress")
        destination = os.path.join(destination_folder_parent, 'minecraft.zip')
        response = requests.get(repo_url, stream=True)
        print("Download minecraft.zip status: Done")

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
        print("Download minecraft from github status: Done")
        try:
            print("\nDelete Temp minecraft files status: in progress")
            folder_path = source_folder
            file_path = destination
            os.remove(file_path)
            shutil.rmtree(folder_path)
            print("Delete Temp files status: Done")
        except Exception as e:
            print(f"Error while deleting temp files: {e}")

    # Создаем и запускаем поток для выполнения функции minecraft_download()
    minecraft_thread = threading.Thread(target=minecraft_download)
    minecraft_thread.start()
    minecraft_thread.join()
    time.sleep(10)
print("Both functions have finished executing.")
