from collections import OrderedDict
import pandas as pd
import rpy2.robjects as ro
from rpy2.robjects import DataFrame
from rpy2.robjects.packages import importr
from rpy2 import robjects

from predict import Predict
from layout import *

C50 = importr('C50')
C5_0 = robjects.r('C5.0')
stats = importr('stats')
base = importr("base")


class Model():

    def __init__(self):

        self.predict = None
        self.data = None
        self.flsplit = None
        self.y = None
        self.vard = None
        self.prunVal = None
        self.result = None
        self.prdd = None
        self.C50 = importr('C50')
        self.C5_0 = robjects.r('C5.0')
        self.stats = importr('stats')
        self.base = importr("base")
        self.rob = robjects

        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.layoutNew = Ui_MainWindow(self)
        self.layoutNew.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

    def valSplit(self,layoutNew):
        valsplit = '0.'+layoutNew
        return valsplit

    def importClass(self):
        atribute = ['jenis_kelamin',
                    'rentang_usia',
                    'status_kawin',
                    'partisipasi_sekolah',
                    'jenjang_pendidikan',
                    'ijazah_tertinggi',
                    'menganggur']

        file = self.layoutNew.fnames
        self.Data = pd.read_csv(file, sep=";", header=0, names=atribute)
        return self.Data

    def prunValue(self):
        toggle = (self.layoutNew.prunVal)
        if toggle is True:
            prunVal = False
        else:
            prunVal = True
        return prunVal

    def Classify(self):
        global prunVal
        self.data = self.importClass()
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
        # # test1 = ([self.view.jk], [self.view.us], [self.view.kw], [self.view.sk], [self.view.pn], [self.view.ij])
        # # =========================================================================================================================== Data Prediksi
        # test = (['laki laki'], ['17-25'], ['belum kawin'], ['tidak bersekolah lagi'], ['SMA/SMK/SMALB'], ['SMA/sederajat'])
        # rtest = list(map(ro.StrVector, test))
        # q = OrderedDict(zip(map(str, range(len(rtest))), rtest))
        # datatest = DataFrame(q)
        valSplit = self.valSplit(self.layoutNew.strval)
        self.flsplit = float(valSplit)
        toggle = (self.layoutNew.prunVal)
        if toggle is True:
            prunVal = False
        else:
            prunVal = True
        print("pruning value : ",prunVal)
        model = C50.C5_0(vard, y, trials=1, rules=False, control=C50.C5_0Control(noGlobalPruning=prunVal, bands=2, sample=self.flsplit,
                                                                                  earlyStopping=True, seed=9999))

        # self.results = str(base.summay(model))
        str(base.summary(model))
        conf = str(base.summary(model)).partition("Evaluation")
        con = str(base.summary(model)).splitlines()
        # print(con)
        # print("THIS    : ",con[36:58])

        prin = conf[2]
        e = prin.partition("\t5\n\n\n")
        f = e[0]
        g = f.partition("\n\n\nEvaluation")
        print(g)
        print("Evaluation",g[0])
        # self.result = str(base.summary(model))
        self.result = str("Evaluation" + g[0])

        return self.flsplit,prunVal,vard,y

    def predic(self):
        print("works")
        spltVal,prnVal,dVar,vy = self.Classify()
        prd = C50.C5_0(dVar, vy, trials=1, rules=False ,control=C50.C5_0Control(noGlobalPruning=prnVal, bands=0, sample=spltVal ,earlyStopping=True, seed=9999))

        print(base.summary(prd))
        confd = str(base.summary(prd)).partition("test data")
        prind = confd[2]
        print(prind, '\n')
        print(len(confd))
        self.prdd = str("Evaluation on test data"+prind)
