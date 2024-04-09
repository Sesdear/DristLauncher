import json
import os
import subprocess

# Функция для поиска исполняемого файла Java
def find_java_executable():
    try:
        result = subprocess.run(["where", "java"], capture_output=True, text=True, check=True)
        output = result.stdout.strip()
        java_path = output.split("\n")[0]
        return java_path
    except subprocess.CalledProcessError:
        print("Исполняемый файл Java не найден.")
        return None

# Функция для запуска Minecraft
def launch_minecraft(username, max_memory):
    java_path = find_java_executable()
    if not java_path:
        print("Java не установлена или ее исполняемый файл не найден.")
        return

    minecraft_jar_path = os.path.abspath("versions/1.18.2/1.18.2.jar")
    print(minecraft_jar_path)

    memory_option = f"-Xmx{max_memory}M"

    subprocess.Popen([java_path, memory_option, "-jar", minecraft_jar_path, "--username", username])

config_path = "../data/config.json"
nickname_path = "../data/nickname.json"

try:
    with open(config_path, 'r') as f:
        max_mem = json.load(f)
    with open(nickname_path, 'r') as f:
        nickname = json.load(f)

    max_memory = max_mem["ram"]
    username = nickname["nickname"]

    # Запускаем Minecraft
    launch_minecraft(username, max_memory)

except FileNotFoundError:
    print("Файл конфигурации или файла с никнеймом не найден.")
except json.JSONDecodeError:
    print("Ошибка декодирования JSON в файле конфигурации или файла с никнеймом.")
