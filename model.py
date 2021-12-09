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
        self.lst = []
        self.predData = None
        self.df = None
        self.predict = None
        self.data = None
        self.dataPred = None
        self.result = None
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


    def importPredict(self):
        atrib = ['jenis_kelamin',
                 'rentang_usia',
                 'status_kawin',
                 'partisipasi_sekolah',
                 'jenjang_pendidikan',
                 'ijazah_tertinggi']
        predname = self.layoutNew.filepred
        print(predname)
        self.predData = pd.read_csv(predname, sep=";", header=0, names=atrib)
        print(' data Prediksi : '+self.predData)

    def prediks(self):
        print('masuk predict')
        print('asign data')
        self.df = pd.DataFrame(self.predData)
        print('asign data')
        print(self.df)
        idx = len(self.df.index)
        self.lst=[]
        # ===========================================================================PREDICT LOOPING
        print('masuk looping')
        for c in range(idx):
            Test = ([str(self.df.iloc[c, 0])], [str(self.df.iloc[c, 1])],
                    [str(self.df.iloc[c, 2])], [str(self.df.iloc[c, 3])],
                    [str(self.df.iloc[c, 4])], [str(self.df.iloc[c, 5])])

            rTest = list(map(ro.StrVector, Test))
            q = OrderedDict(zip(map(str, range(len(rTest))), rTest))
            self.dataPred = DataFrame(q)
            predictModel = self.Classify()
            predRes = str(robjects.r.predict(predictModel, self.dataPred))
            res = predRes.split(' ')[1]
            partres = res.partition("\n")
            resFinal = partres[0]
            self.lst.append(resFinal)
        print('keluar looping')
        print(self.lst)

    def exportPredict(self):
        self.df['Prediksi'] = self.lst
        print(self.df)
        self.df.to_excel(r'D:\kuliah\TA2\export hasil\df.xlsx')
        print('data berhasil di export')

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

    def Classify(self):
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

        # print(self.layoutNew.spinBox.value)

        valSplit = self.valSplit(self.layoutNew.strval)
        self.flsplit = float(valSplit)
        # print(flsplit)
        # print(type(flsplit))
        model = C50.C5_0(vard, y, trials=1, rules=False , control=C50.C5_0Control(noGlobalPruning=True, bands=0, sample=self.flsplit, earlyStopping=True, seed=9999))
        # C50.C5_0Control(sample = 0.3)

        # print(self.dataPred)
        # print(type(self.dataPred))
        # print(datatest)
        # print(type(datatest))
        # self.results = str(base.summay(model))
        self.result = str(base.summary(model))
        # print(str(base.summary(model)))
        # print(type(str(base.summary(model))))
        return model







# base.plot(model)
