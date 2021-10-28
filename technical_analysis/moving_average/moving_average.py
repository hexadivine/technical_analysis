def MA(data, limit, ma_function, optional_params={}):
    if (ma_function.__name__ == 'EMA'):
        if (optional_params.get('alpha') == None):
            optional_params['alpha'] = 2
        return ma_function(data, limit, optional_params['alpha'])
    elif (ma_function.__name__ == 'SMA'):
        return ma_function(data, limit)
    elif (ma_function.__name__ == 'SMMA'):
        return ma_function(data, limit)
    else:
        raise ValueError("Invalid function name for moving average (currently supports SMA, SMMA, EMA)")
