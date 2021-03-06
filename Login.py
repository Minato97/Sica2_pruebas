# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1108, 958)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        font.setUnderline(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.500136, x2:1, y2:0.466, stop:0 rgba(1, 33, 116, 255), stop:1 rgba(9, 92, 184, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 5, 5, 5)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 50))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.500136, x2:1, y2:0.466, stop:0 rgba(48, 48, 48, 255), stop:1 rgba(101, 101, 101, 255));")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times new Roman")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;\n"
"font: family \"Times new Roman\";")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times new Roman")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white;\n"
"font: family \"Times new Roman\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 8))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 10))
        self.frame_2.setStyleSheet("background-color: rgb(172, 26, 45);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout.addWidget(self.frame_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.cuadroAbajo = QtWidgets.QFrame(self.centralwidget)
        self.cuadroAbajo.setStyleSheet("background: none;")
        self.cuadroAbajo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cuadroAbajo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cuadroAbajo.setObjectName("cuadroAbajo")
        self.label_3 = QtWidgets.QLabel(self.cuadroAbajo)
        self.label_3.setGeometry(QtCore.QRect(280, 40, 180, 180))
        self.label_3.setMinimumSize(QtCore.QSize(180, 180))
        self.label_3.setMaximumSize(QtCore.QSize(180, 180))
        self.label_3.setStyleSheet("border-image: url(:/cct/biometrics.jpg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.cuadroAbajo)
        self.pushButton_2.setGeometry(QtCore.QRect(660, 20, 80, 50))
        self.pushButton_2.setMinimumSize(QtCore.QSize(80, 50))
        self.pushButton_2.setMaximumSize(QtCore.QSize(100, 70))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("border: none;\n"
"background-color: rgb(204, 204, 204);\n"
"border-radius: 3px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.cuadroAbajo)
        self.pushButton_3.setGeometry(QtCore.QRect(480, 80, 80, 50))
        self.pushButton_3.setMinimumSize(QtCore.QSize(80, 50))
        self.pushButton_3.setMaximumSize(QtCore.QSize(100, 70))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("border: none;\n"
"background-color: rgb(204, 204, 204);\n"
"border-radius: 3px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.cuadroAbajo)
        self.pushButton_4.setGeometry(QtCore.QRect(570, 80, 80, 50))
        self.pushButton_4.setMinimumSize(QtCore.QSize(80, 50))
        self.pushButton_4.setMaximumSize(QtCore.QSize(100, 70))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("border: none;\n"
"background-color: rgb(204, 204, 204);\n"
"border-radius: 3px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.cuadroAbajo)
        self.pushButton_5.setGeometry(QtCore.QRect(660, 80, 80, 50))
        self.pushButton_5.setMinimumSize(QtCore.QSize(80, 50))
        self.pushButton_5.setMaximumSize(QtCore.QSize(100, 70))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("border: none;\n"
"background-color: rgb(204, 204, 204);\n"
"border-radius: 3px;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.cuadroAbajo)
        self.pushButton_6.setGeometry(QtCore.QRect(480, 140, 80, 50))
        self.pushButton_6.setMinimumSize(QtCore.QSize(80, 50))
        self.pushButton_6.setMaximumSize(QtCore.QSize(100, 70))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("border: none;\n"
"background-color: rgb(204, 204, 204);\n"
"border-radius: 3px;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.cuadroAbajo)
        self.pushButton_7.setGeometry(QtCore.QRect(570, 140, 80, 50))
        self.pushButton_7.setMinimumSize(QtCore.QSize(80, 50))
        self.pushButton_7.setMaximumSize(QtCore.QSize(100, 70))
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet("border: none;\n"
"background-color: rgb(204, 204, 204);\n"
"border-radius: 3px;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.cuadroAbajo)
        self.pushButton_8.setGeometry(QtCore.QRect(660, 140, 80, 50))
        self.pushButton_8.setMinimumSize(QtCore.QSize(80, 50))
        self.pushButton_8.setMaximumSize(QtCore.QSize(100, 70))
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet("border: none;\n"
"background-color: rgb(204, 204, 204);\n"
"border-radius: 3px;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.cuadroAbajo)
        self.pushButton_9.setGeometry(QtCore.QRect(480, 200, 80, 50))
        self.pushButton_9.setMinimumSize(QtCore.QSize(80, 50))
        self.pushButton_9.setMaximumSize(QtCore.QSize(100, 70))
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet("border: none;\n"
"background-color: rgb(204, 204, 204);\n"
"border-radius: 3px;")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_11 = QtWidgets.QPushButton(self.cuadroAbajo)
        self.pushButton_11.setGeometry(QtCore.QRect(570, 260, 170, 50))
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet("border: none;\n"
"background-color: rgb(204, 204, 204);\n"
"border-radius: 3px;")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_10 = QtWidgets.QPushButton(self.cuadroAbajo)
        self.pushButton_10.setGeometry(QtCore.QRect(570, 200, 80, 50))
        self.pushButton_10.setMinimumSize(QtCore.QSize(80, 50))
        self.pushButton_10.setMaximumSize(QtCore.QSize(100, 70))
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet("border: none;\n"
"background-color: rgb(204, 204, 204);\n"
"border-radius: 3px;")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_12 = QtWidgets.QPushButton(self.cuadroAbajo)
        self.pushButton_12.setGeometry(QtCore.QRect(660, 200, 80, 50))
        self.pushButton_12.setMinimumSize(QtCore.QSize(80, 50))
        self.pushButton_12.setMaximumSize(QtCore.QSize(100, 70))
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet("border: none;\n"
"background-color: rgb(204, 204, 204);\n"
"border-radius: 3px;")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.cuadroAbajo)
        self.pushButton_13.setGeometry(QtCore.QRect(480, 260, 80, 50))
        self.pushButton_13.setMinimumSize(QtCore.QSize(80, 50))
        self.pushButton_13.setMaximumSize(QtCore.QSize(100, 70))
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_13.setStyleSheet("border: none;\n"
"background-color: rgb(204, 204, 204);\n"
"border-radius: 3px;")
        self.pushButton_13.setObjectName("pushButton_13")
        self.lineEdit = QtWidgets.QLineEdit(self.cuadroAbajo)
        self.lineEdit.setGeometry(QtCore.QRect(480, 20, 171, 51))
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"font: 18pt;\n"
"border-radius: 5px;\n"
"}\n"
"QLineEdit:focus {\n"
"border: 2px solid green;\n"
"}")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.cuadroAbajo)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setStyleSheet("background: none;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(420, 90, 221, 51))
        self.label_4.setStyleSheet("background: none;\n"
"color: white;\n"
"")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setGeometry(QtCore.QRect(420, 150, 221, 31))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background: none;\n"
"border: none;\n"
"color: white;")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_4.setStyleSheet("background: none;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setGeometry(QtCore.QRect(450, 10, 171, 100))
        self.label_5.setMinimumSize(QtCore.QSize(0, 100))
        self.label_5.setStyleSheet("border-image: url(:/cct/footer.png);\n"
"background: none;\n"
"")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.frame_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(self.lineEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Sistema de Control de Asistencias</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Jueves 29 de Abril de 2022</p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Borrar"))
        self.pushButton_3.setText(_translate("MainWindow", "1"))
        self.pushButton_4.setText(_translate("MainWindow", "2"))
        self.pushButton_5.setText(_translate("MainWindow", "3"))
        self.pushButton_6.setText(_translate("MainWindow", "4"))
        self.pushButton_7.setText(_translate("MainWindow", "5"))
        self.pushButton_8.setText(_translate("MainWindow", "6"))
        self.pushButton_9.setText(_translate("MainWindow", "7"))
        self.pushButton_11.setText(_translate("MainWindow", "Acerptar"))
        self.pushButton_10.setText(_translate("MainWindow", "8"))
        self.pushButton_12.setText(_translate("MainWindow", "9"))
        self.pushButton_13.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Esperando c??digo</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Click aqu?? para consultar horarios y/o faltas"))
# import udgLogo_rc
