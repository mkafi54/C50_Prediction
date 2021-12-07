import sys
from collections import OrderedDict

import pandas as pd
from rpy2.robjects import DataFrame
from rpy2.robjects.packages import importr
import rpy2.robjects as ro

from model import *
from layout import *


class Predict():

    def __init__(self):
        self.model = None
        self.dataPred = None

        # app = QtWidgets.QApplication(sys.argv)
        # MainWindow = QtWidgets.QMainWindow()
        self.layoutNew = Ui_MainWindow(self, self.model)
        # self.layoutNew.setupUi(MainWindow)
        # MainWindow.show()
        # sys.exit(app.exec_())
        # self.model = model(self)


    def predict(self):
        atrib = ['jenis_kelamin',
                 'rentang_usia',
                 'status_kawin',
                 'partisipasi_sekolah',
                 'jenjang_pendidikan',
                 'ijazah_tertinggi']

        predData = pd.read_csv('PrediksiData.csv', sep=";", header=0, names=atrib)

        df = pd.DataFrame(predData)
        c = 0
        print(len(df.index))
        # print(str(df.iloc[c, c]))
        # print(type(str(df.iloc[c].T)))

        Test = ([str(df.iloc[c, 0])], [str(df.iloc[c, 1])],
                [str(df.iloc[c, 2])], [str(df.iloc[c, 3])],
                [str(df.iloc[c, 4])], [str(df.iloc[c, 5])])

        rTest = list(map(ro.StrVector, Test))
        q = OrderedDict(zip(map(str, range(len(rTest))), rTest))
        self.dataPred = DataFrame(q)
        print("class predict")
        # print(Test)
        # predictData = self.predct()
        # print(self.dataPred)
        predictModel = self.model.Classify()
        # print(robjects.r.predict(predictModel, self.dataPred))
        # print(type(str(robjects.r.predict(predictModel, self.dataPred))))
        predRes = str(robjects.r.predict(predictModel, self.dataPred))
        res = predRes.split(' ')[1]
        partres = res.partition("\n")
        resFinal = partres[0]
        print("\n\n\n"+resFinal)

        return self.dataPred




