import psutil
from PyQt6.QtWidgets import QApplication, QFrame
from PyQt6.QtCore import Qt
from ram_gui import Ui_RamFrame
import json


class Ram_Window(QFrame):
    def __init__(self):
        super().__init__()

        self.ui = Ui_RamFrame()
        self.ui.setupUi(self)
        self.show()

        self.ui.pushButton.clicked.connect(self.save_click)
        self.ui.RamSlider.valueChanged.connect(self.slider_changed)
        self.ui.RamEditLine.editingFinished.connect(self.edit_line_changed)  # Соединение сигнала editingFinished
        self.set_values()

    def set_values(self):
        # Выставление значений на QSlider и в QEditLine
        with open('data/config.json', 'r') as json_file:
            data = json.load(json_file)
        max_memory_mb = self.get_max_memory()
        self.ui.RamSlider.setMinimum(0)
        self.ui.RamSlider.setMaximum(int(max_memory_mb))
        self.ui.RamSlider.setValue(data["ram"])
        self.ui.RamEditLine.setText(str(data["ram"]))

    def get_max_memory(self):
        # Получение макс МБ озу
        virtual_memory = psutil.virtual_memory()
        max_memory_mb = virtual_memory.total / (1024 ** 2)
        return max_memory_mb

    def save_click(self):
        # Сохранение значения из QSlider и QEditLine
        select_ram = self.ui.RamSlider.value()
        self.ui.RamEditLine.setText(str(select_ram))
        with open('data/config.json', 'r') as json_file:
            data = json.load(json_file)
        data["ram"] = select_ram
        with open('data/config.json', 'w') as json_file:
            json.dump(data, json_file)

    def slider_changed(self, value):
        # Обновление значения QEditLine при изменении положения слайдера
        self.ui.RamEditLine.setText(str(value))

    def edit_line_changed(self):
        # Обновление значения QSlider при изменении значения в QEditLine
        value = int(self.ui.RamEditLine.text())
        self.ui.RamSlider.setValue(value)


if __name__ == "__main__":
    app = QApplication([])
    ram_window = Ram_Window()
    app.exec()
