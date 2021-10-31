import technical_analysis as ta
import numpy as np

def ATR(high, low, close, limit, moving_average_func=ta.EMA, alpha=1.071421):
    # get true range
    tr = ta.TRANGE(high, low, close)
    atr = np.round(ta.MA(tr, limit, moving_average_func, {'alpha':alpha}), 2)

    return atr