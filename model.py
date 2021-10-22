from collections import OrderedDict
import pandas as pd
import rpy2.robjects as ro
from rpy2.robjects import DataFrame
from rpy2.robjects.packages import importr
from rpy2 import robjects
from view import *

C50 = importr('C50')
C5_0 = robjects.r('C5.0')
stats = importr('stats')
base = importr("base")

class Model():

    def __init__(self):

        self.data = None
        self.C50 = importr('C50')
        self.C5_0 = robjects.r('C5.0')
        self.stats = importr('stats')
        self.base = importr("base")
        app = QApplication(sys.argv)
        self.view = MyWindow(self)
        self.view.show()
        sys.exit(app.exec_())


# ==================================================== Target Variable
#
# ==================================================== Data Uji
#     def testing(self):
#         test = ([self.view.jk], [self.view.us], [self.view.kw], [self.view.sk], [self.view.pn], [self.view.ij])
#         rtest = list(map(ro.StrVector, test))
#         q = OrderedDict(zip(map(str, range(len(rtest))), rtest))
#         datatest = DataFrame(q)
#         return datatest
#
#     # def c50(self):
#     #     m = Model()
#     #     model = C50.C5_0(m.train(), m.attr())
#     #     print(base.summary(model))
#     #     return model
#
#     def testPrint(self):
#         # m = Model()
#         print(self.testing())

    # m = model()
    def c5(self):
        print("Data Prediksi : ")
        atribute = ['jenis_kelamin',
                    'rentang_usia',
                    'status_kawin',
                    'partisipasi_sekolah',
                    'jenjang_pendidikan',
                    'ijazah_tertinggi',
                    'menganggur']

        self.data = pd.read_csv('penduduknew.csv', sep=";", header=0, names=atribute)

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
        #=========================================================================================================================== Data Prediksi
        test = (['laki laki'], ['17-25'], ['belum kawin'],['tidak bersekolah lagi'], ['SMA/SMK/SMALB'], ['SMA/sederajat'])
        rtest = list(map(ro.StrVector, test))
        q = OrderedDict(zip(map(str, range(len(rtest))), rtest))
        datatest = DataFrame(q)

        model = C50.C5_0(vard, y, control = C50.C5_0Control(sample = 0.3))
        # C50.C5_0Control(sample = 0.3)

        print(test)

        print(base.summary(model))

        print(robjects.r.predict(model, datatest))
# c = ("hello")

# base.plot(model)


