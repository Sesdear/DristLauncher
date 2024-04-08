import sys

from PyQt6.QtWidgets import QApplication, QFrame
from gui import Ui_Frame

from scripts.eventButton_script import eventButton_click
from scripts.dristpunckButton_script import dristButton_click
from scripts.folderButton_sctipt import folder_open
from ram_window import Ram_Window

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

    def event_click(self):
        eventButton_click()

    def dristpuck_click(self):
        dristButton_click()

    def folder_click(self):
        folder_open()

    def ram_window_open(self):
        self.ram_window = None
        if self.ram_window is None:
            self.ram_window = Ram_Window()
            self.ram_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Window()
    sys.exit(app.exec())