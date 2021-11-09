import technical_analysis as ta

def RMA(close, limit):
    alpha = 1/limit
    return ta.EMA(close, limit, alpha)