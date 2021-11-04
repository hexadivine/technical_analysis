from technical_analysis._utils.convert_datatype import convert_numpy, convert_to_numpy
import technical_analysis as ta
import numpy as np

def SMMA(data, limit):
    data, original_datatype = convert_to_numpy(data)
    data_len = len(data)
    if (limit > data_len or limit <= 0):
        raise ValueError("Invalid Limit Set")

    start=0
    while (start < data_len and np.isnan(data[start])):
        start+=1

    sum=0
    for index in range(start, start+limit-1):
        sum += data[index]
        data[index] = np.nan
    
    sma = (sum+data[start+limit-1])/limit
    smma = sma/limit
    
    for index in range(start+limit-1, data_len-1):
        old_data_val = data[index]
        data[index] = smma
        smma = (smma*limit - smma + old_data_val)/limit

    data[data_len-1] = smma

    return convert_numpy(data, to=original_datatype)