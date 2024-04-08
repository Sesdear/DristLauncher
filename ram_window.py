import sys

from PyQt6.QtWidgets import QApplication, QFrame
from ram_gui import Ui_RamFrame

class Ram_Window(QFrame):
    def __init__(self):
        super().__init__()

        self.ui = Ui_RamFrame()
        self.ui.setupUi(self)
        self.show()











