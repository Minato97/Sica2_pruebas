from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Label")

        self.setGeometry(0, 0, 400, 300)

        self.label_1 = QLabel("Normal Label", self)

        self.label_1.move(100, 100)

        self.label_1.setStyleSheet("border: 1px solid black;")

        self.label_2 = QLabel("Hidden Label", self)

        self.label_2.move(100, 150)

        self.label_2.setStyleSheet("border: 1px solid black;")

        self.label_2.setHidden(False)

        self.show()


App = QApplication(sys.argv)

window = Window()

sys.exit(App.exec())