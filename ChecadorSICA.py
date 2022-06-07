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
        index.setWindowTitle("Nacho el perreador")
        self.timer = QTimer(self)

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
        self.increment = 0
        ingreso = self.ID.text()
        ingreso += '1'
        self.ID.setText(ingreso)
        self.pauseResume()

    def IngresoNumeros_2(self):
        self.increment = 0
        ingreso = self.ID.text()
        ingreso += '2'
        self.ID.setText(ingreso)
        self.pauseResume()

    def IngresoNumeros_3(self):
        self.increment = 0
        ingreso = self.ID.text()
        ingreso += '3'
        self.ID.setText(ingreso)
        self.pauseResume()

    def IngresoNumeros_4(self):
        self.increment = 0
        ingreso = self.ID.text()
        ingreso += '4'
        self.ID.setText(ingreso)
        self.pauseResume()

    def IngresoNumeros_5(self):
        self.increment = 0
        ingreso = self.ID.text()
        ingreso += '5'
        self.ID.setText(ingreso)
        self.pauseResume()

    def IngresoNumeros_6(self):
        self.increment = 0
        ingreso = self.ID.text()
        ingreso += '6'
        self.ID.setText(ingreso)
        self.pauseResume()

    def IngresoNumeros_7(self):
        self.increment = 0
        ingreso = self.ID.text()
        ingreso += '7'
        self.ID.setText(ingreso)
        self.pauseResume()

    def IngresoNumeros_8(self):
        self.increment = 0
        ingreso = self.ID.text()
        ingreso += '8'
        self.ID.setText(ingreso)
        self.pauseResume()

    def IngresoNumeros_9(self):
        self.increment = 0
        ingreso = self.ID.text()
        ingreso += '9'
        self.ID.setText(ingreso)
        self.pauseResume()

    def IngresoNumeros_0(self):
        self.increment = 0
        ingreso = self.ID.text()
        ingreso += '0'
        self.ID.setText(ingreso)
        self.pauseResume()

    def borrar_ID(self):
        self.increment = 0
        id= self.ID.text()
        newId = id[:-1]
        self.ID.setText(newId)
        self.mensaje.setAlignment(Qt.AlignCenter)
        self.mensaje.setStyleSheet("color: white; font-size:16pt; ")
        self.mensaje.setText("ESPERANDO CÓDIGO")
        self.ID.setStyleSheet("QLineEdit {border: None; font: 18pt; border-radius: 5px;}")
        self.pauseResume()

    def resumeOperation(self):
        if self.increment >= 100:
            self.timer.stop()
            self.barra_progreso.setValue(0)
            self.ID.setText('')
        else:
            self.increment += 1
            self.barra_progreso.setValue(self.increment)

    def pauseResume(self):
        if self.timer.isActive():
            self.barra_progreso.setValue(0)
            self.timer.stop()
            self.timer.start(100)

        else:
            self.timer.timeout.connect(self.resumeOperation)
            self.timer.start(100)


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

                entrar = uic.loadUi(r"C:\Users\Nacho Andrade\Documents\Nuevo SICA\SICA_2_pruebas\Login_ok2.ui", self)
                nombre = (d['name'])
                materia = (d['email'])
                entrar.nombre.setText(f"Usuario: {nombre} registrado correctamente")
                entrar.nombre_materia.setText(materia)
                self.nombre.setAlignment(Qt.AlignCenter)
                self.nombre.setStyleSheet("color: white; font-size:20pt; font-weight: bold; ")
                self.nombre_materia.setAlignment(Qt.AlignCenter)
                self.nombre_materia.setStyleSheet("color: white; font-size:16pt; background-color: qlineargradient(spread:pad, x1:0.506, y1:0.284, x2:0.483, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 55));")
                entrar.show()
                timer.stop()
                self.timer.stop()
            else:
                self.ID.setStyleSheet("QLineEdit {border: 2px solid red; font: 18pt; border-radius: 5px;}")
                self.mensaje.setAlignment(Qt.AlignCenter)
                self.mensaje.setStyleSheet("color: red; font-size:16pt")
                self.mensaje.setText("¡CÓDIGO NO ENCONTRADO!")




app = QApplication(sys.argv)
UIWindow = principal()
app.exec_()