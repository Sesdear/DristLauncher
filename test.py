import requests

username = ("GayThunder")
def get_player_uuid(username):
    try:
        # Отправляем GET запрос к Mojang API для получения UUID игрока
        response = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}")

        # Проверяем успешность запроса
        if response.status_code == 200:
            # Получаем JSON данные из ответа
            data = response.json()
            # Возвращаем UUID игрока
            return data["id"]
        else:
            print(f"Ошибка при получении UUID: {response.status_code}")
            return None
    except Exception as e:
        print(f"Ошибка: {e}")
        return None

get_player_uuid(username)


# Получаем UUID игрока
player_uuid = get_player_uuid(username)

if player_uuid:
    print(f"UUID игрока {username}: {player_uuid}")
else:
    print("Не удалось получить UUID игрока.")

