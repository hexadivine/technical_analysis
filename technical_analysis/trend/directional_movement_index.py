from technical_analysis._utils.convert_datatype import convert_numpy, convert_to_numpy
import technical_analysis as ta
import numpy as np

def DMI(high, low, close, limit, opt_ATR_params={'ma_function':ta.EMA, 'alpha':1.071421}):
    # validate data
    high, original_datatype = convert_to_numpy(high)
    low, _ = convert_to_numpy(low)

    if (False in high > low):
        raise ValueError("Some High values are smaller than Low values")

    # get positive and negative directional movement
    pos_dm, neg_dm  = ta.DM(high, low)

    # smoothed with the help of exponential moving average
    smoothed_pos_dm = ta.EMA(pos_dm, limit, 1.071421)
    smoothed_neg_dm = ta.EMA(neg_dm, limit, 1.071421)

    # get Average true range
    average_true_range = ta.ATR(high, low, close, limit, opt_ATR_params['ma_function'], opt_ATR_params['alpha'])

    # used the formula to get positive and negative directional index
    pos_di = 100*smoothed_pos_dm/average_true_range
    neg_di = 100*smoothed_neg_dm/average_true_range
    
    # calculate dx
    dx = abs(pos_di - neg_di)/abs(pos_di + neg_di)

    # get average directional movement index using ema on dx
    adx = 100*ta.EMA(dx, limit,1.071421)

    return np.round(convert_numpy(pos_di, to=original_datatype),2), np.round(convert_numpy(neg_di, to=original_datatype),2), np.round(convert_numpy(adx, to=original_datatype),2)

