from collections import OrderedDict
import pandas as pd
import rpy2.robjects as ro
from rpy2.robjects import DataFrame
from rpy2.robjects.packages import importr
from rpy2 import robjects

from Predict import Predict
from layout import *

C50 = importr('C50')
C5_0 = robjects.r('C5.0')
stats = importr('stats')
base = importr("base")


class Model():

    def __init__(self):
        self.prd = None
        self.lst = []
        self.df = None
        self.predData = None
        self.df = None
        self.predict = None
        self.data = None
        self.dataPred = None
        self.result = None
        self.model = None
        self.dataPredd = None
        self.C50 = importr('C50')
        self.C5_0 = robjects.r('C5.0')
        self.stats = importr('stats')
        self.base = importr("base")

        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.layoutNew = Ui_MainWindow(self, self.predict)
        self.layoutNew.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

    m = "worked"

    def importPredict(self):
        atrib = ['jenis_kelamin',
                 'rentang_usia',
                 'status_kawin',
                 'partisipasi_sekolah',
                 'jenjang_pendidikan',
                 'ijazah_tertinggi']
        predname = self.layoutNew.filepred
        print(predname)
        self.predData = pd.read_csv('PrediksiData.csv', sep=";", header=0, names=atrib)
        print(' data Prediksi : '+self.predData)

        return self.predData

    def getData(self):
        return self.importPredict()

    def prediks(self):
        print('masuk predict')
        # dp = self.importPredict()
        print('asign data')
        self.df = pd.DataFrame(self.predData)
        print('asign data')
        print(self.df)
        c = 0
        idx = len(self.df.index)
        # print(len(df.index))
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
            # print("class predict")

            predictModel = self.Classify()
            predRes = str(robjects.r.predict(predictModel, self.dataPred))
            res = predRes.split(' ')[1]
            partres = res.partition("\n")
            resFinal = partres[0]
            self.lst.append(resFinal)
        print('keluar looping')
        print(self.lst)

    def geter(self):
        return self.predict()

    def exportPredict(self):

        # p = self.geter()
        self.df['Prediksi'] = self.lst
        print(self.df)
        self.df.to_excel(r'D:\kuliah\TA2\export hasil\df.xlsx')
        print('data berhasil di export')


    def Classify(self):
        # print("Data Prediksi : ")
        # self.Predict.predict()
        atribute = ['jenis_kelamin',
                    'rentang_usia',
                    'status_kawin',
                    'partisipasi_sekolah',
                    'jenjang_pendidikan',
                    'ijazah_tertinggi',
                    'menganggur']

        file = self.layoutNew.fnames
        self.data = pd.read_csv(file, sep=";", header=0, names=atribute)
        # print("in Model : "+file)
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

        # # test1 = ([self.view.jk], [self.view.us], [self.view.kw], [self.view.sk], [self.view.pn], [self.view.ij])
        # # =========================================================================================================================== Data Prediksi
        # test = (['laki laki'], ['17-25'], ['belum kawin'], ['tidak bersekolah lagi'], ['SMA/SMK/SMALB'], ['SMA/sederajat'])
        # rtest = list(map(ro.StrVector, test))
        # q = OrderedDict(zip(map(str, range(len(rtest))), rtest))
        # datatest = DataFrame(q)

        # print(self.layoutNew.spinBox.value)
        valSplit = '0.'+self.layoutNew.strval
        # print(valSplit)
        # print(type(valSplit))
        flsplit = float(valSplit)
        # print(flsplit)
        # print(type(flsplit))
        model = C50.C5_0(vard, y, trials=1, rules=False , control=C50.C5_0Control(noGlobalPruning=True, bands=0, sample=flsplit, earlyStopping=True, seed=9999))
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
