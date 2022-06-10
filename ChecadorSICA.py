# import pruebaDB as DB
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys, urllib.request, json, time
from PyQt5.QtCore import QTimer, QTime, QDate, QDateTime, Qt


class principal(QMainWindow):
    def __init__(self):
        super(principal, self).__init__()
        index = uic.loadUi(r"C:\Users\Nacho Andrade\Documents\Nuevo SICA\SICA_2_pruebas\login.ui", self)
        index.Number_1.clicked.connect(lambda: self.IngresoNumeros('1'))
        index.Number_2.clicked.connect(lambda: self.IngresoNumeros('2'))
        index.Number_3.clicked.connect(lambda: self.IngresoNumeros('3'))
        index.Number_4.clicked.connect(lambda: self.IngresoNumeros('4'))
        index.Number_5.clicked.connect(lambda: self.IngresoNumeros('5'))
        index.Number_6.clicked.connect(lambda: self.IngresoNumeros('6'))
        index.Number_7.clicked.connect(lambda: self.IngresoNumeros('7'))
        index.Number_8.clicked.connect(lambda: self.IngresoNumeros('8'))
        index.Number_9.clicked.connect(lambda: self.IngresoNumeros('9'))
        index.Number_0.clicked.connect(lambda: self.IngresoNumeros('0'))
        index.borrar.clicked.connect(self.borrar_ID)
        index.Aceptar.clicked.connect(self.Login)
        index.setWindowTitle("Sistema de Control de Asistencias (SICA)")

        self.barra_progreso.setStyleSheet('QProgressBar{background:transparent;border-radius: 0px}')
        self.timer_reloj = QTimer(self)
        self.timer = QTimer(self)

        self.timer_reloj.timeout.connect(lambda: self.displayTime(self.reloj))
        self.timer_reloj.start()
        index.show()


    def displayTime(self, fecha):
        currentTime = QDateTime.currentDateTime()
        displayText = currentTime.toString(Qt.DefaultLocaleLongDate)
        displayText = displayText.capitalize()
        fecha.setAlignment(Qt.AlignCenter)
        fecha.setText(displayText)


    def IngresoNumeros(self, valor):
        self.increment = 0
        ingreso = self.ID.text()
        ingreso += valor
        self.ID.setText(ingreso)
        self.pauseResume()

    def borrar_ID(self):
        self.increment = 0
        id = self.ID.text()
        newId = id[:-1]
        self.ID.setText(newId)
        self.mensaje.setAlignment(Qt.AlignCenter)
        self.mensaje.setStyleSheet("color: white; font-size:16pt; ")
        self.mensaje.setText("ESPERANDO CÓDIGO")
        self.ID.setStyleSheet("QLineEdit {border: None; font: 18pt; border-radius: 5px;}")
        tam = len(id)
        self.pauseResume()

    def resumeOperation(self):
        if self.increment >= 100:
            self.timer.stop()
            self.barra_progreso.setValue(0)
            self.ID.setText('')
            self.mensaje.setAlignment(Qt.AlignCenter)
            self.mensaje.setStyleSheet("color: white; font-size:16pt; ")
            self.mensaje.setText("ESPERANDO CÓDIGO")
            self.ID.setStyleSheet("QLineEdit {border: None; font: 18pt; border-radius: 5px;}")
            self.barra_progreso.setStyleSheet('QProgressBar{background:transparent;border-radius: 0px}')
        else:
            self.increment += 1
            self.barra_progreso.setValue(self.increment)

    def pauseResume(self):
        self.barra_progreso.setStyleSheet('QProgressBar{background:white;border-radius: 0px}')
        if self.timer.isActive():
            self.barra_progreso.setValue(0)
            self.timer.stop()
            self.timer.start(100)

        else:
            self.timer.timeout.connect(self.resumeOperation)
            self.timer.start(100)


    def Login(self):

        codigoBuscado = self.ID.text()
        if codigoBuscado == "":
            pass
        else:
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

                self.timer_reloj.stop()
                self.timer.stop()


                entrar = uic.loadUi(r"C:\Users\Nacho Andrade\Documents\Nuevo SICA\SICA_2_pruebas\Login_ok2.ui", self)
                nombre = (d['name'])
                materia = (d['email'])
                entrar.nombre.setText(f"Usuario: {nombre} registrado correctamente")
                entrar.nombre_materia.setText(materia)
                self.nombre.setAlignment(Qt.AlignCenter)
                self.nombre.setStyleSheet("color: white; font-size:20pt; font-weight: bold; ")
                self.nombre_materia.setAlignment(Qt.AlignCenter)
                self.nombre_materia.setStyleSheet("color: white; font-size:16pt; background-color: qlineargradient(spread:pad, x1:0.506, y1:0.284, x2:0.483, y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 55));")
                entrar.setWindowTitle("Sistema de Control de Asistencias (SICA)")

                self.timer_reloj = QTimer(self)
                self.timer_reloj.timeout.connect(lambda: self.displayTime(self.reloj_2))
                self.timer_reloj.start()
                entrar.show()

            else:
                self.ID.setStyleSheet("QLineEdit {border: 2px solid red; font: 18pt; border-radius: 5px;}")
                self.mensaje.setAlignment(Qt.AlignCenter)
                self.mensaje.setStyleSheet("color: red; font-size:16pt")
                self.mensaje.setText("¡CÓDIGO NO ENCONTRADO!")




app = QApplication(sys.argv)
UIWindow = principal()
app.exec_()