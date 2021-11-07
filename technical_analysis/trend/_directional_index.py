import technical_analysis as ta
from technical_analysis._utils.convert_datatype import convert_numpy, convert_to_numpy

def FIND_DI(high, low, close, limit, direction_type='PLUS'):
    # validate data
    high, original_datatype = convert_to_numpy(high)
    low, _ = convert_to_numpy(low)
    close, _ = convert_to_numpy(close)

    # find directional movement
    find_dm = ta.FIND_DM(high, low, direction_type)
    
    smoothed_find_dm = ta.SMMA(find_dm, limit)
    average_true_range = ta.ATR(high, low, close, limit)

    find_di = 100 * smoothed_find_dm/average_true_range

    return convert_numpy(find_di, original_datatype)

def PLUS_DI(high, low, close, limit):
    return FIND_DI(high, low, close, limit, 'PLUS')

def MINUS_DI(high, low, close, limit):
    return FIND_DI(high, low, close, limit, 'MINUS')
