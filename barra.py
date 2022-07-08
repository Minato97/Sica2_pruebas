
from PyQt5.QtCore import QTimer, QTime, QDate, QDateTime, Qt


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
