import technical_analysis as ta
from technical_analysis._utils.convert_datatype import convert_numpy, convert_to_numpy

def MACD(close, fast_ema_period=12, slow_ema_period=26, signal_ema_period=9):
    close, original_datatype = convert_to_numpy(close)

    if (slow_ema_period < fast_ema_period):
        temp_swap = slow_ema_period
        slow_ema_period = fast_ema_period
        fast_ema_period = temp_swap

    fast_ema = ta.EMA(close, fast_ema_period, alpha=2/(fast_ema_period + 1)) 
    slow_ema = ta.EMA(close, slow_ema_period, alpha=2/(slow_ema_period + 1)) 

    macd_line = fast_ema - slow_ema
    signal_line = ta.EMA(macd_line, signal_ema_period, alpha=2/(signal_ema_period + 1))
    macd_histogram = macd_line - signal_line

    return convert_numpy(macd_line, original_datatype), convert_numpy(signal_line, original_datatype), convert_numpy(macd_histogram, original_datatype)