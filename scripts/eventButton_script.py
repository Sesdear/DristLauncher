from bs4 import BeautifulSoup
from scripts.download_event_mods import download_and_update_mods
import requests
import json



def eventButton_click():
    #Check Valid Modpack Version
    url = "https://chocolate-elenore-53.tiiny.site/"
    response = requests.get(url)


    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    version_element = soup.find('p', class_='event_version')
    version_on_website = version_element.get_text()

    with open('minecraft_event/info.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    version_on_client = data["version"]


    if version_on_website == version_on_client:
        pass
    else:
        #Update / download mods

        download_and_update_mods()
        #Write new version in json
        with open('minecraft_event/info.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        data["version"] = f"{version_on_website}"

        with open('minecraft_event/info.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


    #Debug code

    print('Version on client',version_on_client)
    print("Version on web", version_on_website)






