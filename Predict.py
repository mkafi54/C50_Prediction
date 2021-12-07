import sys
from collections import OrderedDict

import pandas as pd
from rpy2.robjects import DataFrame
from rpy2.robjects.packages import importr
import rpy2.robjects as ro

from layout import *


class Predict():

    def __init__(self):
        self.predData = None

        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.layoutNew = Ui_MainWindow(self, model)
        self.layoutNew.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())


    def predict(self):
        # atribute = ['jenis_kelamin',
        #             'rentang_usia',
        #             'status_kawin',
        #             'partisipasi_sekolah',
        #             'jenjang_pendidikan',
        #             'ijazah_tertinggi']
        #
        # file = self.layoutNew.predName
        # self.predData = pd.read_csv('DataPrediksi.csv', sep=";", header=0, names=atribute)
        # print("in Model : " + file)
        # test = (
        # [self.predData.jenis_kelamin], [self.predData.usia],
        # [self.predData.status_kawin], [self.predData.partisipasi_sekolah],
        # [self.predData.jenjang_pendidikan], [self.predData.ijazah_terakhir])
        #
        # rtest = list(map(ro.StrVector, test))
        # q = OrderedDict(zip(map(str, range(len(rtest))), rtest))
        # datatest = DataFrame(q)
        print("class predict")
        # print(datatest)




