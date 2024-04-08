import os
import requests
import zipfile
import shutil

def download_and_update_mods():
    #Подключение к репозиторию
    repo_url = 'https://codeload.github.com/Sesdear/Drist_Sources/zip/refs/heads/Dristpunk_Data'
    destination_folder = 'minecraft_dristpunk/'

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    destination = os.path.join(destination_folder, 'mods.zip')

    response = requests.get(repo_url, stream=True)

    with open(destination, 'wb') as f:
        f.write(response.content)

    extracted_folder_path = os.path.join(destination_folder, 'mods')
    with zipfile.ZipFile(destination, 'r') as zip_ref:
        zip_ref.extractall(extracted_folder_path)

    #____________________________________________________________


    source_folder = os.path.join(extracted_folder_path, 'Drist_Sources-Dristpunk_Data')
    destination_folder_2 = 'minecraft_dristpunk/mods'

    for filename in os.listdir(source_folder):
        source_file_path = os.path.join(source_folder, filename)
        destination_file_path = os.path.join(destination_folder_2, filename)
        shutil.move(source_file_path, destination_file_path)

    folder_path = source_folder
    file_path = destination
    os.remove(file_path)
    shutil.rmtree(folder_path)
