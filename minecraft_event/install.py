import os
import subprocess

forge_installer_path = 'forge-installer.jar'

def install_forge(forge_installer_path):
    if not os.path.exists(forge_installer_path):
        print("Установщик Forge не найден.")
        return

    

    # Запускаем установку серверной части Forge
    subprocess.call(["java", "-jar", forge_installer_path, "--installClient"])

install_forge(forge_installer_path)
