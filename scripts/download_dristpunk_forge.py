import requests
from bs4 import BeautifulSoup
import json


def download_forge_installer():
    source_url = "https://chocolate-elenore-53.tiiny.site/"
    response = requests.get(source_url)
    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    #print("Step 1")

    # Получаем версии Forge и Minecraft с веб-страницы
    version_forge = soup.find('p', class_='dristpunk_forge_version').get_text()
    version_minecraft = soup.find('p', class_='dristpunk_minecraft_version').get_text()
    #print("Step 2: " + version_forge, ", ", version_minecraft)

    # Читаем версии из файла info.json
    with open('minecraft_dristpunk/info.json', 'r') as f:
        data = json.load(f)
        saved_forge_version = data.get('forge_version')
        saved_minecraft_version = data.get('minecraft_version')
    #print("Step 3: ", saved_forge_version, ", ", saved_minecraft_version)

    # Проверяем, совпадают ли версии
    if version_forge == saved_forge_version and version_minecraft == saved_minecraft_version:
        #print("Step 4")
        pass
    else:
        # Загружаем новый инсталлер Forge и обновляем версии в info.json
        #print("Step 5")
        download_url = f"https://maven.minecraftforge.net/net/minecraftforge/forge/{version_minecraft}-{version_forge}/forge-{version_minecraft}-{version_forge}-installer.jar"
        response = requests.get(download_url)
        #print(download_url)
        with open('minecraft_dristpunk/forge-installer.jar', 'wb') as file:
            file.write(response.content)

        # Обновляем версии в info.json
        with open('minecraft_dristpunk/info.json', 'w') as f:
            json.dump({'minecraft_version': version_minecraft, 'forge_version': version_forge}, f)
