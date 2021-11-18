from technical_analysis._utils.convert_datatype import convert_numpy, convert_to_numpy
import technical_analysis as ta

def DMI(high, low, close, limit=14):
    # validate data
    high, original_datatype = convert_to_numpy(high)
    low, _ = convert_to_numpy(low)
    close, _ = convert_to_numpy(close)

    if (False in high > low):
        raise ValueError("Some High values are smaller than Low values")

    # find di
    plus_di = ta.PLUS_DI(high, low, close, limit)
    minus_di = ta.MINUS_DI(high, low, close, limit)

    # find adx
    adx = ta.ADX(high, low, close, limit)

    return convert_numpy(plus_di, to=original_datatype), convert_numpy(minus_di, to=original_datatype), convert_numpy(adx, to=original_datatype)

