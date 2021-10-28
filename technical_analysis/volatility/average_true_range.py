import technical_analysis as ta
import numpy as np

def ATR(high, low, close, limit, moving_average=ta.EMA, alpha_for_ema=1.071421):
    # get true range
    tr = ta.TRANGE(high, low, close)

    # special case for ema as it has alpha
    if (moving_average.__name__ == 'EMA'):
        return np.round(moving_average(tr, limit, alpha_for_ema), 2)

    return np.round(moving_average(tr, limit), 2)