import sys
from collections import OrderedDict

import pandas as pd
from rpy2.robjects import DataFrame
from rpy2.robjects.packages import importr
import rpy2.robjects as ro

# from model import Model
# from layout import *
# from layout import Ui_MainWindow
# from model import Model
from abc import abstractmethod


class Predict():

    @staticmethod
    def importPredict(namefile):
        atrib = ['jenis_kelamin',
                 'rentang_usia',
                 'status_kawin',
                 'partisipasi_sekolah',
                 'jenjang_pendidikan',
                 'ijazah_tertinggi']
        predname = namefile
        print(predname)
        predData = pd.read_csv(predname, sep=";", header=0, names=atrib)
        print(' data Prediksi : ' + predData)
        return predData

    @staticmethod
    def prediks(predData, Classify, robjects):
        print('masuk predict')
        print('asign data')
        df = pd.DataFrame(predData)
        print('asign data')
        print(df)
        idx = len(df.index)
        lst = []
        # ===========================================================================PREDICT LOOPING
        print('masuk looping')
        for c in range(idx):
            Test = ([str(df.iloc[c, 0])], [str(df.iloc[c, 1])],
                    [str(df.iloc[c, 2])], [str(df.iloc[c, 3])],
                    [str(df.iloc[c, 4])], [str(df.iloc[c, 5])])
            rTest = list(map(ro.StrVector, Test))
            q = OrderedDict(zip(map(str, range(len(rTest))), rTest))
            dataPred = DataFrame(q)
            predictModel = Classify
            predRes = str(robjects.r.predict(predictModel, dataPred))
            res = predRes.split(' ')[1]
            partres = res.partition("\n")
            resFinal = partres[0]
            lst.append(resFinal)
        print('keluar looping')
        print(lst)
        return df, lst

    @staticmethod
    def exportPredict(df, lst):
        # p = geter()
        df['Prediksi'] = lst
        print(df)
        df.to_excel(r'D:\kuliah\TA2\export hasil\df.xlsx')
        print('data berhasil di export')
