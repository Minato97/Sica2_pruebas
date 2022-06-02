# import pruebaDB as DB
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys, urllib.request, json, time
from PyQt5.QtCore import QTimer, QTime, QDate, QDateTime, Qt

timer = QTimer()


class principal(QMainWindow):
    def __init__(self):
        super(principal, self).__init__()
        index = uic.loadUi(r"C:\Users\Nacho Andrade\Documents\Nuevo SICA\SICA_2_pruebas\login.ui", self)
        index.Number_1.clicked.connect(self.IngresoNumeros_1)
        index.Number_2.clicked.connect(self.IngresoNumeros_2)
        index.Number_3.clicked.connect(self.IngresoNumeros_3)
        index.Number_4.clicked.connect(self.IngresoNumeros_4)
        index.Number_5.clicked.connect(self.IngresoNumeros_5)
        index.Number_6.clicked.connect(self.IngresoNumeros_6)
        index.Number_7.clicked.connect(self.IngresoNumeros_7)
        index.Number_8.clicked.connect(self.IngresoNumeros_8)
        index.Number_9.clicked.connect(self.IngresoNumeros_9)
        index.Number_0.clicked.connect(self.IngresoNumeros_0)
        index.borrar.clicked.connect(self.borrar_ID)
        index.Aceptar.clicked.connect(self.Login)


        global timer
        timer.timeout.connect(self.displayTime)
        timer.start()
        index.show()


    def displayTime(self):
        currentTime = QDateTime.currentDateTime()
        displayText = currentTime.toString(Qt.DefaultLocaleLongDate)
        displayText = displayText.capitalize()
        self.reloj.setAlignment(Qt.AlignCenter)
        self.reloj.setText(displayText)

    def IngresoNumeros_1(self):
        ingreso = self.ID.text()
        ingreso += '1'
        self.ID.setText(ingreso)

    def IngresoNumeros_2(self):
        ingreso = self.ID.text()
        ingreso += '2'
        self.ID.setText(ingreso)

    def IngresoNumeros_3(self):
        ingreso = self.ID.text()
        ingreso += '3'
        self.ID.setText(ingreso)

    def IngresoNumeros_4(self):
        ingreso = self.ID.text()
        ingreso += '4'
        self.ID.setText(ingreso)

    def IngresoNumeros_5(self):
        ingreso = self.ID.text()
        ingreso += '5'
        self.ID.setText(ingreso)

    def IngresoNumeros_6(self):
        ingreso = self.ID.text()
        ingreso += '6'
        self.ID.setText(ingreso)

    def IngresoNumeros_7(self):
        ingreso = self.ID.text()
        ingreso += '7'
        self.ID.setText(ingreso)

    def IngresoNumeros_8(self):
        ingreso = self.ID.text()
        ingreso += '8'
        self.ID.setText(ingreso)

    def IngresoNumeros_9(self):
        ingreso = self.ID.text()
        ingreso += '9'
        self.ID.setText(ingreso)

    def IngresoNumeros_0(self):
        ingreso = self.ID.text()
        ingreso += '0'
        self.ID.setText(ingreso)

    def borrar_ID(self):
        self.ID.setText("")
        self.mensaje.setAlignment(Qt.AlignCenter)
        self.mensaje.setStyleSheet("color: white; font-size:16pt; ")
        self.mensaje.setText("Esperendo Código")
        self.ID.setStyleSheet("QLineEdit {border: None; font: 18pt; border-radius: 5px;}")

    def Login(self):
        global timer
        codigoBuscado = self.ID.text()
        codigoBuscado= int(codigoBuscado)

        print(codigoBuscado)
        print(type(codigoBuscado))

        url = "http://148.202.89.12:90/api/user"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        for d in data:
            if d['id'] == codigoBuscado:

                print(d['id'])
                print(type(d['id']))

                entrar = uic.loadUi(r"C:\Users\Nacho Andrade\Documents\Nuevo SICA\SICA_2_pruebas\Frame_login.ui", self)
                nombre = (d['name'])
                print(nombre)
                entrar.nombres.setText(nombre)
                entrar.show()
                timer.stop()
            else:
                self.ID.setStyleSheet("QLineEdit {border: 2px solid red; font: 18pt; border-radius: 5px;}")
                self.mensaje.setAlignment(Qt.AlignCenter)
                self.mensaje.setStyleSheet("color: red; font-size:16pt; ")
                self.mensaje.setText("Código no encontrado")


    
app = QApplication(sys.argv)
UIWindow = principal()
app.exec_()