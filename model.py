import string
from collections import OrderedDict
import pandas as pd
import rpy2.robjects as ro
from rpy2.robjects import DataFrame
from rpy2.robjects.packages import importr
from rpy2 import robjects

import layoutNew
from view import *
from layoutNew import *

C50 = importr('C50')
C5_0 = robjects.r('C5.0')
stats = importr('stats')
base = importr("base")


class Model():

    def __init__(self):
        self.data = None
        self.result = None
        self.C50 = importr('C50')
        self.C5_0 = robjects.r('C5.0')
        self.stats = importr('stats')
        self.base = importr("base")

        # app = QtWidgets.QApplication(sys.argv)
        # self.view = MyWindow(self)
        # self.view.show()
        # sys.exit(app.exec_())

        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.layoutNew = Ui_MainWindow(self)
        self.layoutNew.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

    # def imp(self):
    #     print("Data Prediksi : ")
    #     atribute = ['jenis_kelamin',
    #                 'rentang_usia',
    #                 'status_kawin',
    #                 'partisipasi_sekolah',
    #                 'jenjang_pendidikan',
    #                 'ijazah_tertinggi',
    #                 'menganggur']
    #
    #     file = self.layoutNew.impFile()
    #     name = "penduduknew.csv"
    #     rname = r"{}".format(string)
    #     # name.encode('unicode_escape')
    #     self.data = pd.read_csv(name, sep=";", header=0)
    #     print(file)
    #     self.data = pd.read_csv(r'C:\Users\ACER\PycharmProjects\penduduknew.csv', sep=";", header=0, names=atribute)
    #     return self.data

    m = "worked"

    def c5(self):
        print("Data Prediksi : ")
        atribute = ['jenis_kelamin',
                    'rentang_usia',
                    'status_kawin',
                    'partisipasi_sekolah',
                    'jenjang_pendidikan',
                    'ijazah_tertinggi',
                    'menganggur']

        file = self.layoutNew.fnames
        self.data = pd.read_csv(file, sep=";", header=0, names=atribute)
        print("in Model : "+file)
        # self.data = pd.read_csv(r'C:\Users\ACER\PycharmProjects\penduduknew.csv', sep=";", header=0, names=atribute)
        valY = robjects.StrVector(self.data.menganggur)
        y = robjects.vectors.FactorVector(valY)

        atr = (self.data.jenis_kelamin,
               self.data.rentang_usia,
               self.data.status_kawin,
               self.data.partisipasi_sekolah,
               self.data.jenjang_pendidikan,
               self.data.ijazah_tertinggi)
        rattr = list(map(ro.StrVector, atr))
        d = OrderedDict(zip(map(str, range(len(rattr))), rattr))
        vard = DataFrame(d)

        # test1 = ([self.view.jk], [self.view.us], [self.view.kw], [self.view.sk], [self.view.pn], [self.view.ij])
        # =========================================================================================================================== Data Prediksi
        test = (
        ['laki laki'], ['17-25'], ['belum kawin'], ['tidak bersekolah lagi'], ['SMA/SMK/SMALB'], ['SMA/sederajat'])
        rtest = list(map(ro.StrVector, test))
        q = OrderedDict(zip(map(str, range(len(rtest))), rtest))
        datatest = DataFrame(q)

        # print(self.layoutNew.spinBox.value)
        valSplit = '0.'+self.layoutNew.strval
        print(valSplit)
        print(type(valSplit))
        flsplit = float(valSplit)
        print(flsplit)
        print(type(flsplit))
        model = C50.C5_0(vard, y, control=C50.C5_0Control(sample=flsplit))
        # C50.C5_0Control(sample = 0.3)

        print(test)
        # self.results = str(base.summay(model))
        self.result = str(base.summary(model))
        # print(str(base.summary(model)))
        print(type(str(base.summary(model))))

        print(robjects.r.predict(model, datatest))

    def test(self):
        print("works")
# c = ("hello")

# base.plot(model)
