from technical_analysis._utils.convert_datatype import convert_to_numpy, convert_numpy
import technical_analysis as ta
import numpy as np

def ADX(high, low, close, limit):
    # validate data
    high, original_datatype = convert_to_numpy(high)
    low, _ = convert_to_numpy(low)
    close, _ = convert_to_numpy(close)

    # find di
    plus_di = ta.PLUS_DI(high, low, close, limit)
    minus_di = ta.MINUS_DI(high, low, close, limit)

    # calculate dx
    dx = abs(plus_di - minus_di)/abs(plus_di + minus_di)

    # get average directional movement index using 
    adx = 100*ta.RMA(dx, limit)

    return convert_numpy(adx, original_datatype)