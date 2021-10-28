from technical_analysis._utils.convert_datatype import convert_numpy, convert_to_numpy
import numpy as np

def FIND_DM(high, low, dm_type='PLUS'):
    # validate data
    high, original_datatype = convert_to_numpy(high)
    low, _ = convert_to_numpy(low)

    if False in high > low:
        raise ValueError("low value is greater than high")

    # find up move and down move
    # upMove = (Today's High - Yesterday's High)
    up_move = np.zeros_like(high, dtype='float')
    up_move[0] = np.nan
    up_move[1:] = high[1:]-high[:-1]

    # downMove = (Yesterday's Low - Today's Low)
    down_move = np.zeros_like(low, dtype='float')
    down_move[0] = np.nan
    down_move[1:] = low[:-1]-low[1:]

    # finding dm 
    find_dm = np.zeros_like(high, dtype='float')
    find_dm[0] = np.nan

    find_dm_len = len(find_dm)
    for index in range(1, find_dm_len):
        # +dm = (if UpMove > DownMove and UpMove > 0, then +DM = UpMove, else +DM = 0)
        if (dm_type.lower() == 'plus'):
            if (up_move[index] > down_move[index] and up_move[index] > 0):
                find_dm[index] = up_move[index]
            else:
                find_dm[index] = 0
        # -dm = (if DownMove > UpMove and DownMove > 0, then -DM = DownMove, else -DM = 0)
        elif (dm_type.lower() == 'minus'):
            if (up_move[index] < down_move[index] and down_move[index] > 0):
                find_dm[index] = down_move[index]
            else:
                find_dm[index] = 0
  
    return convert_numpy(find_dm, to=original_datatype)

def PLUS_DM(high, low):
    return FIND_DM(high, low, 'PLUS')

def MINUS_DM(high, low):
    return FIND_DM(high, low, 'MINUS')