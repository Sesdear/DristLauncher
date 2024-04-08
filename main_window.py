import sys
import json

from PyQt6.QtWidgets import QApplication, QFrame
from gui import Ui_Frame

from scripts.eventButton_script import eventButton_click
from scripts.dristpunckButton_script import dristButton_click
from scripts.folderButton_sctipt import folder_open
from ram_window import Ram_Window
from scripts.download_event_forge import download_forge_installer as EFI
from scripts.download_dristpunk_forge import download_forge_installer as DFI

class Window(QFrame):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.show()

        self.ram_window = None


        self.ui.Dristpunk_Button.clicked.connect(self.dristpuck_click)
        self.ui.Folder_Button.clicked.connect(self.folder_click)
        self.ui.Event_Button.clicked.connect(self.event_click)
        self.ui.RamButton.clicked.connect(self.ram_window_open)
        self.ui.ApplyNicknameButton.clicked.connect(self.setNickname)

    def event_click(self):
        eventButton_click()
        EFI()

    def dristpuck_click(self):
        dristButton_click()
        DFI()

    def folder_click(self):
        folder_open()

    def ram_window_open(self):
        # Открытие окна с регулировкой памяти
        self.ram_window = None
        if self.ram_window is None:
            self.ram_window = Ram_Window()
            self.ram_window.show()

    def setNickname(self):
        # Сохранение никнейма
        nickname = self.ui.nicknameEdit.text()
        dict = {"nickname": nickname}
        with open("data/nickname.json", "w") as file:
            json.dump(dict, file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Window()
    sys.exit(app.exec())