import requests
from bs4 import BeautifulSoup


def set_name_event():
    url = "https://chocolate-elenore-53.tiiny.site/"

    try:
        response = requests.get(url)
        response.raise_for_status()
        print("\nRead Website status: in progress")
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        event_name = soup.find('p', class_='event_name')

        event_name_on_website = event_name.get_text()



    except requests.exceptions.RequestException as e:
        print('Error during request:', e)
    except Exception as e:
        print('Error:', e)
    print(event_name_on_website)
    return event_name_on_website

def set_name_dristpunk():
    url = "https://chocolate-elenore-53.tiiny.site/"

    try:
        response = requests.get(url)
        response.raise_for_status()
        response.encoding = 'utf-8'
        print("\nRead Website status: in progress")
        soup = BeautifulSoup(response.text, 'html.parser')

        dristpunk_name = soup.find('p', class_='dristpunk_name')

        distpunk_name_on_website = dristpunk_name.get_text()

    except requests.exceptions.RequestException as e:
        print('Error during request:', e)
    except Exception as e:
        print('Error:', e)
    return distpunk_name_on_website