import requests
from bs4 import BeautifulSoup
import json


def download_forge_installer():
    source_url = "https://chocolate-elenore-53.tiiny.site/"
    response = requests.get(source_url)
    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'html.parser')

    # Получаем версии Forge и Minecraft с веб-страницы
    version_forge = soup.find('p', class_='event_forge_version').get_text()
    version_minecraft = soup.find('p', class_='event_minecraft_version').get_text()

    # Читаем версии из файла info.json
    with open('minecraft_event/info.json', 'r') as f:
        data = json.load(f)
        saved_forge_version = data.get('forge_version')
        saved_minecraft_version = data.get('minecraft_version')

    # Проверяем, совпадают ли версии
    if version_forge == saved_forge_version and version_minecraft == saved_minecraft_version:
        pass
    else:
        # Загружаем новый инсталлер Forge и обновляем версии в info.json
        download_url = f"https://maven.minecraftforge.net/net/minecraftforge/forge/{version_minecraft}-{version_forge}/forge-{version_minecraft}-{version_forge}-installer.jar"
        response = requests.get(download_url)
        with open('minecraft_event/forge-installer.jar', 'wb') as file:
            file.write(response.content)

        # Обновляем версии в info.json
        with open('minecraft_event/info.json', 'w') as f:
            json.dump({'minecraft_version': version_minecraft, 'forge_version': version_forge}, f)
