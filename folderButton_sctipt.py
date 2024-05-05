import os
import subprocess


def folder_open():
    # Открывает директорию кода
    current_directory = os.getcwd()
    subprocess.Popen(r'explorer "{}"'.format(current_directory))
