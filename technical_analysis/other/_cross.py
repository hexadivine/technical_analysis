"""
Return boolean array when crossesover or crossesunder
"""
import numpy as np

# Check whether crossover_data crosses stable_data over or not.
def CROSSOVER(crossover_data, stable_data):
    data_len = len(crossover_data)

    result = np.full(data_len, False)
    crossed_over = False    # This flag is used in condition to toggle False value from result array, when it crossesover for the first time.

    for i in range(data_len):
        if (crossover_data[i] > stable_data[i] and not crossed_over):
            result[i] = True    # Set True when crosses over for the first time
            crossed_over = True
        elif (crossover_data[i] < stable_data[i] and crossed_over):
            crossed_over = False
    
    return result

# Check whether crossunder_data crosses stable_data below or not
def CROSSUNDER(crossunder_data, stable_data):
    data_len = len(crossunder_data)

    result = np.full(data_len, False)
    crossed_under = False       # This flag is used in condition to toggle False value from result array, when it crossesunder for the first time.

    for i in range(data_len):
        if (crossunder_data[i] < stable_data[i] and not crossed_under):
            result[i] = True    # Set True when crosses under for the first time
            crossed_under = True
        elif (crossunder_data[i] > stable_data[i] and crossed_under):
            crossed_under = False 
    
    return result
    
# check both crossover(1) and crossunder(-1) [else 0]
def CROSS(crossover_data, stable_data):
    data_len = len(crossover_data)
    cross = np.zeros_like(crossover_data)

    crossed_over = False
    for i in range(data_len):
        if (crossover_data[i] > stable_data[i] and not crossed_over):
            crossed_over = True
            cross[i] = crossover_data[i]
        elif (crossover_data[i] < stable_data[i] and crossed_over):
            crossed_over = False
            cross[i] = -crossover_data[i]

    return cross