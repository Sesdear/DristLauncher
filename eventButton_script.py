from bs4 import BeautifulSoup
from download_event_req import download_and_update_mods, minecraft_download_event
import requests
import json
from minecraft_launch import start_minecraft_event

def eventButton_click():
    # URL для проверки версии сборки
    url = "https://chocolate-elenore-53.tiiny.site/"

    try:
        # Попытка выполнить GET-запрос к веб-сайту
        response = requests.get(url)
        response.raise_for_status()  # Проверка статуса ответа
        print("\nRead Website status: in progress")

        # Парсинг HTML-документа для получения версии сборки
        soup = BeautifulSoup(response.text, 'html.parser')
        version_element = soup.find('p', class_='event_version')
        version_on_website = version_element.get_text()
        print("Read Website status: Done")

        print("\nRead ver on client status: in progress")
        with open('minecraft_event/info.json', 'r', encoding='utf-8') as f:
            data1 = json.load(f)
        version_on_client = data1["version"]
        print('Read ver on client status: Done')

        print('Version from info.json on client:', version_on_client)
        print('Version on website:', version_on_website)
        # Проверка соответствия версий сборок

        if version_on_website != version_on_client:
            print("Ver on web != ver on client")
            # Обновление / загрузка ресурсов
            print("\nMods download status: in progress")
            download_and_update_mods()
            print("Mods download status: Done")

            print("\nMinecraft download status: in progress")
            minecraft_download_event()
            print("Minecraft download: Done")
            # Обновление версии в локальном JSON-файле
            data1["version"] = version_on_website
            with open('minecraft_event/info.json', 'w', encoding='utf-8') as f:
                json.dump(data1, f, ensure_ascii=False, indent=4)

            print(4)
        # Отладочный вывод
        print("\n \n Start Check Minecraft Download")
        start_minecraft_event()

    except requests.exceptions.RequestException as e:
        # Обработка исключения при ошибке запроса
        print('Error during request:', e)
    except Exception as e:
        # Обработка других исключений
        print('Error:', e)

# Вызов функции при нажатии на кнопку
