from technical_analysis._utils.convert_datatype import convert_numpy, convert_to_numpy
import numpy as np

def TRANGE(high, low, close):
    # validate data
    high, high_type = convert_to_numpy(high)
    low, _ = convert_to_numpy(low)
    close, _ = convert_to_numpy(close)

    # step1 - (Current High - Current Low)
    high_low_difference = abs(high-low)
    high_low_difference[0] = np.nan

    # step2 -  Absolute value of (Current High - Previous Close)
    high_prevclose_difference = np.zeros_like(high, dtype='float')
    high_prevclose_difference[0] = np.nan
    high_prevclose_difference[1:] = abs(high[1:] - close[:-1])

    # step3 - Absolute value of (Current Low - Previous Close)
    low_prevclose_difference = np.zeros_like(low, dtype='float')
    low_prevclose_difference[0] = np.nan
    low_prevclose_difference[1:] = abs(low[1:] - close[:-1])

    # True Range = Maximum values of (step1, step2, step3)
    true_range = np.zeros_like(close, dtype='float')
    true_range_length = len(true_range)
    for index in range(true_range_length):
        true_range[index] = max(high_low_difference[index], high_prevclose_difference[index], low_prevclose_difference[index])

    return convert_numpy(true_range, to=high_type)
