# main.py
import sys
import json

from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import QApplication, QFrame
from gui import Ui_Frame

from eventButton_script import eventButton_click
from folderButton_sctipt import folder_open
from ram_window import Ram_Window
from generate_cracked_uuid import generate_cracked_uid
from dristpunckButton_script import dristpunkButton_click


class Window(QFrame):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.show()

        self.ram_window = None


        print("\nButton laod status: in progress")
        self.ui.Dristpunk_Button.clicked.connect(dristpunkButton_click)
        self.ui.Folder_Button.clicked.connect(folder_open)
        self.ui.Event_Button.clicked.connect(eventButton_click)
        self.ui.RamButton.clicked.connect(self.ram_window_open)
        self.ui.ApplyNicknameButton.clicked.connect(self.setNickname)
        print("Button load status: Done")

        print("setText from nickname.json in nicknameEdit")
        with open ('data/nickname.json', 'r') as f:
            nickname_value = json.load(f)
        self.ui.nicknameEdit.setText(nickname_value["User-info"][0]["username"])\

    def ram_window_open(self):
        print("Open ram_window")
        self.ram_window = None
        if self.ram_window is None:
            self.ram_window = Ram_Window()
            self.ram_window.show()

    def setNickname(self):
        nickname = self.ui.nicknameEdit.text()
        with open("data/nickname.json") as file:
            data2 = json.load(file)
        data2["User-info"][0]["username"] = str(nickname)

        with open('data/nickname.json', 'w') as jis_set:
            json.dump(data2, jis_set, indent=4)

        with open("data/options.json") as f:
            data = json.load(f)
        data["username"] = str(nickname)

        with open('data/options.json', 'w') as js_set:
            json.dump(data, js_set, indent=4)

        print("\nGenerate UUID status: in progress")

        generate_cracked_uid()

        print("Generate UUID status: Done")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Window()
    sys.exit(app.exec())
