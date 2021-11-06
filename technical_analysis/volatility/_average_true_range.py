import technical_analysis as ta
import numpy as np

def ATR(high, low, close, limit, moving_average_func=ta.EMA, alpha=2):
    # get true range
    tr = ta.TRANGE(high, low, close)
    atr = ta.MA(tr, limit, moving_average_func, {'alpha':alpha})

    return atr