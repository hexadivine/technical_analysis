import technical_analysis as ta
from technical_analysis._utils.convert_datatype import convert_numpy, convert_to_numpy
import numpy as np

# needs fix
def RSI(close, length=14):
    close, original_datatype = convert_to_numpy(close)

    avg_gain = ta.AVG_GAIN(close, length)
    avg_loss = ta.AVG_LOSS(close, length)

    rsi = np.zeros_like(close)

    for i in range(len(close)):
        if (avg_gain[i] == 0):
            rsi[i] = 0
        elif (avg_loss[i] == 0):
            rsi[i] = 100
        else:
            rs = avg_gain[i]/avg_loss[i]
            rsi[i] = 100 - 100/(1+rs)

    return convert_numpy(rsi, original_datatype)
