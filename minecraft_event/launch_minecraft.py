import json
import os
import subprocess

# Function to find the Java executable
def find_java_executable():
    try:
        result = subprocess.run(["where", "java"], capture_output=True, text=True, check=True)
        output = result.stdout.strip()
        java_path = output.split("\n")[0]
        return java_path
    except subprocess.CalledProcessError:
        print("Java executable not found.")
        return None

# Function to launch Minecraft
def launch_minecraft(username, max_memory):
    java_path = find_java_executable()
    if not java_path:
        return

    minecraft_jar_path = "versions/1.18.2/1.18.2.jar"
    memory_option = f"-Xmx{max_memory}M"

    subprocess.Popen([java_path, memory_option, "-jar", minecraft_jar_path, "--username", username])


config_path = "../data/config.json"
nickname_path = "../data/nickname.json"

with open(config_path, 'r') as f:
    max_mem = json.load(f)
with open(nickname_path, 'r') as f:
    nickname = json.load(f)

max_memory = max_mem["ram"]
username = nickname["nickname"]

# Launch Minecraft
launch_minecraft(username, max_memory)