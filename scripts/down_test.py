'''
import os
import requests
import zipfile
import shutil

def download_and_update_minecraft():
    # Подключение к репозиторию
    source_folder = '../minecraft_event/Drist_Sources-Event_Minecraft/'
    destination_folder = '../minecraft_event/'

    repo_url = 'https://codeload.github.com/Sesdear/Drist_Sources/zip/refs/heads/Event_Minecraft'
    destination_folder_parent = '../minecraft_event/'

    if not os.path.exists(destination_folder_parent):
        os.makedirs(destination_folder_parent)

    destination = os.path.join(destination_folder_parent, 'minecraft.zip')

    response = requests.get(repo_url, stream=True)

    with open(destination, 'wb') as f:
        f.write(response.content)

    extracted_folder_path = os.path.join(destination_folder_parent, '.')
    with zipfile.ZipFile(destination, 'r') as zip_ref:
        zip_ref.extractall(extracted_folder_path)

    if os.path.exists(source_folder):  # Check if source folder exists
        for filename in os.listdir(source_folder):
            source_file_path = os.path.join(source_folder, filename)
            destination_file_path = os.path.join(destination_folder, filename)
            shutil.move(source_file_path, destination_file_path)

        folder_path = source_folder
        file_path = destination
        os.remove(file_path)
        shutil.rmtree(folder_path)
    else:
        print(f"Source folder '{source_folder}' does not exist.")'''