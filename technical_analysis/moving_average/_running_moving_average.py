import technical_analysis as ta
# running/rolling moving average is also known as smoothed moving average
def RMA(close, limit):
    alpha = 1/limit
    return ta.EMA(close, limit, alpha)

def SMMA(close, limit):
    return RMA(close, limit)