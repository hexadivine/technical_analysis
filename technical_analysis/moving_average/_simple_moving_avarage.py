from technical_analysis._utils.convert_datatype import convert_numpy, convert_to_numpy
import numpy as np
from math import nan

def SMA(data, limit):
    total_data = len(data)
    if (limit == 1):
        return data
    if (limit > total_data):
        return convert_numpy(np.full(total_data, np.nan), str(type(data))) 

    data, original_datatype = convert_to_numpy(data)

    count_nan = 0
    while (count_nan < total_data and np.isnan(data[count_nan])):
        count_nan+=1

    if (count_nan > 0):
        data[count_nan:] = SMA(data[count_nan:], limit)
        return data

    continues_sum = np.cumsum(data, dtype='float')
    continues_sum[limit:] = continues_sum[limit:] - continues_sum[:-limit]
    moving_avarage = continues_sum[limit-1:]/limit
    
    moving_avarage = np.concatenate([(limit-1)*[nan], moving_avarage])

    return convert_numpy(moving_avarage, to=original_datatype)