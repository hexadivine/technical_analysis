import numpy as np
import pandas as pd

class SMA():
    def __init__(self, data, limit):
        self.__sma = []
        self.__data_type = None

        if (str(type(data)) == "<class 'numpy.ndarray'>"):
            self.__data_type = 'numpy'
        elif (str(type(data)) == "<class 'pandas.core.series.Series'>"):
            self.__data_type = 'pandas'
        elif (str(type(data)) == "<class 'list'>"):
            self.__data_type = 'list'
        else:
            raise ValueError
    
        self.__sma = self.__calculate_sma(np.array(data), limit)

    def __calculate_sma(self, data, limit):
        if (limit > len(data)):
            return np.full(len(data), float("nan"))

        continues_sum = np.cumsum(data, dtype='float')
        continues_sum[limit:] = continues_sum[limit:] - continues_sum[:-limit]
        moving_avarage = continues_sum[limit-1:]/limit
        
        moving_avarage = np.concatenate([(limit-1)*[float("nan")], moving_avarage])
        return np.round(moving_avarage,2)

    def get_sma(self):
        if (self.__data_type == 'numpy'):
            return self.__sma
        elif (self.__data_type == 'pandas'):
            return pd.Series(self.__sma)
        elif (self.__data_type == 'list'):
            return list(self.__sma)
        else:
            raise ValueError

def sma(data, limit=14):
    technical_analysis = SMA(data, limit)
    return technical_analysis.get_sma()