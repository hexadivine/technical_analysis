"""

ma_cross function will compair two simple moving avarages and 
will buy if fast ma crossess slow ma over and sells if fast ma crossess slow ma below
    
ma_limit2's default value is 1 this give feature to comapair ma with closing price. 
If closing price crosses ma over then buy else sell.

"""

import technical_analysis as ta
from technical_analysis._utils.convert_datatype import convert_numpy, convert_to_numpy

def MA_CROSS(data, ma_limit1, ma_limit2=1, slow_ma_func=None, fast_ma_func=None):
    data, original_datatype = convert_to_numpy(data)
    if (slow_ma_func == None):
        slow_ma_func = ta.SMA
    if (fast_ma_func == None):
        fast_ma_func = ta.SMA

    # if only ma_limit1 is passed then ma will be compaired with the close.
    if (ma_limit2 == 1):
        slow_ma_limit = ma_limit1
        fast_ma_limit = ma_limit2
    # if both args are passed...
    else:
        # ...it will check for slow ma limit and fast ma limit smaller will be slow ma limit and vice versa
        if (ma_limit1<ma_limit2):
            slow_ma_limit = ma_limit2
            fast_ma_limit = ma_limit1
        else:
            slow_ma_limit = ma_limit1
            fast_ma_limit = ma_limit2
        
    # get the moving averages
    slow_ma = slow_ma_func(data, slow_ma_limit)
    fast_ma = fast_ma_func(data, fast_ma_limit) 

    cross = ta.CROSS(fast_ma, slow_ma)

    return convert_numpy(cross, original_datatype)