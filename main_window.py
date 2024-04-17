# main.py
import sys
import json
import threading

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QFrame
from gui import Ui_Frame
from colorama import init
from colorama import Fore, Back, Style

from eventButton_script import eventButton_click
from folderButton_sctipt import folder_open
from ram_window import Ram_Window
from generate_cracked_uuid import generate_cracked_uid
from dristpunckButton_script import dristpunkButton_click

from download_event_req import download_and_update_mods as Event_Upadte_Mods
from download_event_req import minecraft_download_event as Event_Update_Minecraft

from download_dristpunck_req import download_and_update_mods as Dristpunk_Update_Mods
from download_dristpunck_req import minecraft_download_dristpunk as Dristpunk_Upadte_Minecraft
init()



class Window(QFrame):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Frame()
        self.ui.setupUi(self)

        ###########################################
        #### Custom title bar
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.ram_window = None
        self.old_pos = None

        self.ui.widget_2.mousePressEvent = self.mouse_press_event
        self.ui.widget_2.mouseMoveEvent = self.mouse_move_event
        self.ui.widget_2.mouseReleaseEvent = self.mouse_release_event

        self.ui.closeButton.clicked.connect(self.close)
        self.ui.minButton.clicked.connect(self.showMinimized)

        ###########################################
        #### Connect buttons
        print(Back.YELLOW + "Button load status: in progress", Style.RESET_ALL)
        self.ui.Dristpunk_Button.clicked.connect(dristpunkButton_click)
        self.ui.Folder_Button.clicked.connect(folder_open)
        self.ui.Event_Button.clicked.connect(eventButton_click)
        self.ui.RamButton.clicked.connect(self.ram_window_open)
        self.ui.ApplyNicknameButton.clicked.connect(self.setNickname)

        self.ui.UpdateModsEvent_Button.clicked.connect(self.updateModsEvent_thread)
        self.ui.UpdateAllEvent_Button.clicked.connect(self.upadteAllEvent_thread)

        self.ui.UpdateModsDristpunk_Button.clicked.connect(self.updateModsDristpunk_thread)
        self.ui.UpdateAllDristpunk_Button.clicked.connect(self.upadteAllDristpunk_thread)

        print(Back.GREEN + "Button load status: Done", Style.RESET_ALL)

        print(Back.MAGENTA + "setText from nickname.json in nicknameEdit", Style.RESET_ALL)
        with open ('data/nickname.json', 'r') as f:
            nickname_value = json.load(f)
        self.ui.nicknameEdit.setText(nickname_value["User-info"][0]["username"])

    ###########################################
    #### Functions

    def eventButton_thread(self):
        def start_minecraft():
            eventButton_click()
        start_event_thread = threading.Thread(target=start_minecraft)
        start_event_thread.start()
    def updateModsEvent_thread(self):
        def update_mods():
            Event_Upadte_Mods()
        up_event_thread = threading.Thread(target=update_mods)
        up_event_thread.start()
    def updateModsDristpunk_thread(self):
        def update_mods():
            Dristpunk_Update_Mods()
        up_dristpunk_thread = threading.Thread(target=update_mods)
        up_dristpunk_thread.start()
    def upadteAllEvent_thread(self):
        # Define a function to update Event mods and Minecraft
        def update_all():
            Event_Upadte_Mods()
            Event_Update_Minecraft()

        # Create a thread to execute the update function
        upA_event_thread = threading.Thread(target=update_all)
        upA_event_thread.start()
    def upadteAllDristpunk_thread(self):
        # Define a function to update Dristpunk mods and Minecraft
        def update_all():
            Dristpunk_Update_Mods()
            Dristpunk_Upadte_Minecraft()

        # Create a thread to execute the update function
        upA_dristpunk_thread = threading.Thread(target=update_all)
        upA_dristpunk_thread.start()
    def ram_window_open(self):
        print(Back.BLUE + "Open ram_window", Style.RESET_ALL)
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

        print("\n")
        print(Back.YELLOW + "Generate UUID status: in progress", Style.RESET_ALL)

        generate_cracked_uid()

        print(Back.GREEN + "Generate UUID status: Done", Style.RESET_ALL)
        print("\n")

    def mouse_press_event(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.old_pos = event.globalPosition()

    def mouse_move_event(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton and self.old_pos:
            delta = event.globalPosition() - self.old_pos
            self.move(int(self.x() + delta.x()), int(self.y() + delta.y()))

            self.old_pos = event.globalPosition()

    def mouse_release_event(self, event):
        self.old_pos = None





'''if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())'''
