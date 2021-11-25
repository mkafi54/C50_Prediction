import pandas as pd
import string
from collections import OrderedDict
import pandas as pd
import rpy2.robjects as ro
from rpy2.robjects import DataFrame
from rpy2.robjects.packages import importr
from rpy2 import robjects

class testView():
    file = "penduduknew.csv"

    df = pd.read_csv(file, sep=";", header=0)
    print(df)