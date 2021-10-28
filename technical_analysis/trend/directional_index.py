import technical_analysis as ta
from technical_analysis._utils.convert_datatype import convert_numpy, convert_to_numpy

def FIND_DI(high, low, close, limit, direction_type='PLUS', moving_average_func=ta.EMA, alpha=1.071421):
    # validate data
    high, original_datatype = convert_to_numpy(high)
    low, _ = convert_to_numpy(low)
    close, _ = convert_to_numpy(close)

    # find directional movement
    find_dm = ta.FIND_DM(high, low, direction_type)
    
    smoothed_find_dm = ta.MA(find_dm, limit, moving_average_func, {'alpha': alpha})
    average_true_range = ta.ATR(high, low, close, limit, moving_average_func, alpha)

    find_di = 100 * smoothed_find_dm/average_true_range

    return convert_numpy(find_di, original_datatype)

def PLUS_DI(high, low, close, limit, moving_average_func=ta.EMA, alpha=1.071421):
    return FIND_DI(high, low, close, limit, 'PLUS', moving_average_func, alpha)

def MINUS_DI(high, low, close, limit, moving_average_func=ta.EMA, alpha=1.071421):
    return FIND_DI(high, low, close, limit, 'MINUS', moving_average_func, alpha)
