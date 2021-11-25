from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
# from main import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets
import model



class MyWindow(QMainWindow):
    def __init__(self, model):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 500, 300)
        self.setWindowTitle("Decision tree c5.0")
        self.initUI()
        self.model = model

        # ===================================================Atribut 1


    def initUI(self):
        self.centralwidget = QtWidgets.QWidget(QMainWindow)
        self.tabWidget = QtWidgets.QtabWidget(self.centralWidget)
        # ===========================================================Judul
        self.label = QtWidgets.QLabel(self)
        self.label.setText("PREDIKSI PENGANGGURAN")
        self.update()
        self.label.move(180, 10)

        # ============================================================Button
        # act=backend.b1Act()
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Mulai Klasifikasi")
        # self.b1.clicked.connect(self.clicked)
        self.b1.clicked.connect(self.submit)
        self.b1.move(200, 260)

    def clicked(self):
        self.label.setText("button pressed")
        self.update()

    def submit(self):
        # import main
        # self.jk = str(self.jkel.currentText())
        # self.sk = str(self.sklh.currentText())
        # self.us = str(self.usia.currentText())
        # self.ij = str(self.ijz.currentText())
        # self.kw = str(self.kwn.currentText())
        # self.pn = str(self.pndd.currentText())
        # self.model.testPrint()
        self.model.c5()


    def update(self):
        self.label.adjustSize()

    def show_popup(self):
        jk = str(self.jkel.currentText())
        pop = QMessageBox()
        pop.setWindowTitle("judul Popup")
        pop.setText(jk)
        self.update()

        x = pop.exec_()


# def window():
#     app = QApplication(sys.argv)
#     wind = MyWindow()
#     wind.show()
#     sys.exit(app.exec_())
#
# window()