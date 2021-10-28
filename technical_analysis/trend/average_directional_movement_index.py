import technical_analysis as ta

def ADX(high, low, close, limit, opt_ATR_params={'ma_function':ta.EMA, 'alpha':1.071421}):
    # get adx from dmi
    _, _, adx = ta.DMI(high, low, close, limit, opt_ATR_params)
    return adx