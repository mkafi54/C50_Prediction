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
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Jenis Kelamin : ")
        self.update()
        self.label.move(10, 50)

        self.jkel = QtWidgets.QComboBox(self)
        self.update()
        self.jkel.addItem("-Pilih Jenis Kelamin-")
        self.jkel.addItem('laki-laki')
        self.jkel.addItem('perempuan')
        self.jkel.move(90, 40)
        self.jkel.setObjectName("jkel")
        self.layout().addWidget(self.jkel)
        self.jk = ""

        # ===================================================Atribut 2
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Rentang Usia : ")
        self.update()
        self.label.move(10, 85)

        self.usia = QtWidgets.QComboBox(self)
        self.update()
        self.usia.addItem("-Pilih Rentang Usia-")
        self.usia.addItem('12-16')
        self.usia.addItem("17-25")
        self.usia.addItem("26-35")
        self.usia.addItem("36-45")
        self.usia.addItem("56-65")
        self.usia.move(90, 75)
        self.layout().addWidget(self.usia)
        self.us = ""
        # ===================================================Atribut 3
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Status Kawin : ")
        self.update()
        self.label.move(10, 120)

        self.kwn = QtWidgets.QComboBox(self)
        self.update()
        self.kwn.addItem("-Pilih Status Kawin-")
        self.kwn.addItem('kawin')
        self.kwn.addItem("Belum Kawin")
        self.kwn.move(90, 110)
        self.layout().addWidget(self.kwn)
        self.kw = ""

        # ===================================================Atribut 5
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Partisipasi Sekolah : ")
        self.update()
        self.label.move(270, 50)

        self.sklh = QtWidgets.QComboBox(self)
        self.update()
        self.sklh.addItem("-Pilih Partisipasi Sekolah-")
        self.sklh.addItem('tidak/belum pernah sekolah')
        self.sklh.addItem("masih sekolah")
        self.sklh.addItem("tidak bersekolah lagi")
        self.sklh.move(380, 40)
        self.layout().addWidget(self.sklh)
        self.kw = ""

        # ===================================================Atribut 6
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Jenjang Pendidikan : ")
        self.update()
        self.label.move(270, 85)

        self.pndd = QtWidgets.QComboBox(self)
        self.update()
        self.pndd.addItem("-Pilih Jenjang Pendidikan-")
        self.pndd.addItem('SD/SDLB')
        self.pndd.addItem("paket A")
        self.pndd.addItem("M.ibdtidaiyah")
        self.pndd.addItem("SMP/SMPLB")
        self.pndd.addItem("paket B")
        self.pndd.addItem("M.tsanawiyah")
        self.pndd.addItem("M.SMA/SMK/SMALB")
        self.pndd.addItem("paket C")
        self.pndd.addItem("M.Alliyah")
        self.pndd.addItem("perguruan tinggi")
        self.pndd.move(380, 75)
        self.layout().addWidget(self.pndd)
        self.pn = ""

        # ===================================================Atribut 7
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Ijazah Terakhir : ")
        self.update()
        self.label.move(270, 120)

        self.ijz = QtWidgets.QComboBox(self)
        self.update()
        self.ijz.addItem("-Pilih Ijazah Terakhir-")
        self.ijz.addItem('tidak punya ijazah')
        self.ijz.addItem("SD/sederajat")
        self.ijz.addItem("SMP/sederajat")
        self.ijz.addItem("SMA/sederajat")
        self.ijz.addItem("D1/D2/D3")
        self.ijz.addItem("D4/S1")
        self.ijz.addItem("S2/S3")
        self.ijz.move(380, 110)
        self.layout().addWidget(self.ijz)
        self.ij = ""

    def initUI(self):
        # ===========================================================Judul
        self.label = QtWidgets.QLabel(self)
        self.label.setText("PREDIKSI PENGANGGURAN")
        self.update()
        self.label.move(180, 10)

        # ============================================================Button
        # act=backend.b1Act()
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Simpan")
        # self.b1.clicked.connect(self.clicked)
        self.b1.clicked.connect(self.submit)
        self.b1.move(200, 260)

    def clicked(self):
        self.label.setText("button pressed")
        self.update()

    def submit(self):
        # import main
        self.jk = str(self.jkel.currentText())
        self.sk = str(self.sklh.currentText())
        self.us = str(self.usia.currentText())
        self.ij = str(self.ijz.currentText())
        self.kw = str(self.kwn.currentText())
        self.pn = str(self.pndd.currentText())
        self.model.testPrint()
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