import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import *


class imagen(QMainWindow):
    def __init__(self):
        super(imagen, self).__init__()
        img = uic.loadUi(r"login_ok2.ui", self)
        img.boton_change.clicked.connect(self.change_image)
        
        img.show()
        
    def change_image(self):
        self.nombre_materia.setText("Matemáticas")
        self.nombre_materia.setStyleSheet("color: white; font: 16pt;")
        pixmap = QPixmap(r"Assets\nacho.png")
        self.foto.setPixmap(pixmap)

app = QApplication(sys.argv)
UIWindow = imagen()
app.exec_()