from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from PyQt5.QtCore import QTimer, QTime, QDate, QDateTime, Qt
import ChecadorSICA as ch


def IngresoNumeros(self, valor):
    self.camera.start()
    self.increment = 0
    ingreso = self.ID.text()
    ingreso += valor
    self.ID.setText(ingreso)
    self.pauseResume()


def borrar_ID(self):
    # self.increment = 0
    id = self.ID.text()
    newId = id[:-1]
    self.ID.setText(newId)
    self.mensaje.setAlignment(Qt.AlignCenter)
    self.mensaje.setStyleSheet("color: white; font-size:16pt; ")
    self.mensaje.setText("ESPERANDO CÓDIGO")
    self.ID.setStyleSheet("QLineEdit {border: None; font: 18pt; border-radius: 5px;}")
    tam = len(id)
    # self.pauseResume()

def displayTime(self, fecha):
    currentTime = QDateTime.currentDateTime()
    displayText = currentTime.toString(Qt.DefaultLocaleLongDate)
    displayText = displayText.capitalize()
    fecha.setAlignment(Qt.AlignCenter)
    fecha.setText(displayText)

def resumeOperation(self):
    if self.increment >= 100:
        self.camera.stop()
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

    def select_camera(self, i):
        self.available_cameras = QCameraInfo.availableCameras()
        # getting the selected camera
        self.camera = QCamera(lambda: ch.available_cameras(self,[i]))

        # setting view finder to the camera
        self.camera.setViewfinder(self.visor)

        # setting capture mode to the camera
        self.camera.setCaptureMode(QCamera.CaptureStillImage)

        # creating a QCameraImageCapture object
        self.capture = QCameraImageCapture(self.camera)
        # getting current camera name
        self.current_camera_name = self.available_cameras[i].description()

        # initial save sequence
        self.save_seq = 0
