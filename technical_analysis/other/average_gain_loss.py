from numpy import nan
import technical_analysis as ta
from technical_analysis._utils.convert_datatype import convert_numpy, convert_to_numpy
import numpy as np

# needs fix
def AVG_GAIN(data, length):
    data, original_datatype = convert_to_numpy(data)
    # print(data)
    data[1:] = data[1:] - data[:-1]
    # data[1:] = data[1:]*100/data[:-1] - 100
    # print(data)
    data[0] = nan

    for i in range(1, len(data)):
        if (data[i] < 0):
            data[i] = 0


    avg_gain = np.zeros_like(data)
    avg_gain[1:] = ta.RMA(data[1:], length)
    avg_gain[0] = nan

    # print(avg_gain)
    return convert_numpy(avg_gain, original_datatype)

def AVG_LOSS(data, length):
    data, original_datatype = convert_to_numpy(data)

    data[1:] = data[1:] - data[:-1]
    # data[1:] = data[1:]*100/data[:-1] - 100
    data[0] = nan

    for i in range(1, len(data)):
        if (data[i] >= 0):
            data[i] = 0
        else:
            data[i] = abs(data[i])

    avg_loss = np.zeros_like(data)
    avg_loss[1:] = ta.RMA(data[1:], length)
    avg_loss[0] = nan
    # print(avg_loss)

    return convert_numpy(avg_loss, original_datatype)