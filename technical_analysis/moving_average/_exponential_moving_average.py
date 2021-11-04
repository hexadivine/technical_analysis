import numpy as np
from technical_analysis._utils.convert_datatype import convert_to_numpy, convert_numpy
import technical_analysis as ta


def EMA(data, limit, alpha=2):
    total_data = len(data)
    # validate data
    data, original_datatype = convert_to_numpy(data)
    if (limit > len(data)):
        return convert_numpy(np.full(total_data, np.nan), str(type(data))) 

    # count nan values in data
    total_nan=0
    while (total_nan < total_data and np.isnan(data[total_nan])):
        total_nan+=1
    
    # ignore nan values if exists and find ema
    if (total_nan>0):
        data[total_nan:] = EMA(data[total_nan:], limit, alpha)
        return data

    # weigh formula
    weight = alpha/(limit+1)

    # find first ema (ema(1)=sma(data, limit))
    ema = np.zeros_like(data)
    ema[:limit] = ta.SMA(data[:limit], limit)

    # find 2nd ema to nth (n=length of data) [ema(today) = (data(today) - ema(yesterday))*weight + ema(yesterday)]
    data_len = len(data)
    for i in range(limit, data_len):
        ema[i] = (data[i] - ema[i-1])*weight + ema[i-1]

    return convert_numpy(ema, original_datatype)