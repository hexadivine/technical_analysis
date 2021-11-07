import technical_analysis as ta
import numpy as np

def ATR(high, low, close, limit):
    # get true range
    tr = ta.TRANGE(high, low, close)
    atr = ta.SMA(tr, limit)

    return atr