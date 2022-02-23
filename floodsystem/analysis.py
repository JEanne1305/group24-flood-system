# Task 2F: given the water level time history, computes a least-squares fit of a polynomial
# Yuqing Xue (yx357)

import matplotlib
import numpy as np

def polyfit(dates, levels, p):
    # convert datetime object to float
    x = matplotlib.dates.date2num(dates)

    # using shifted x values, find coeffienct of best fit
    p_coeff = np.polyfit(x-x[0], levels, p)
    
    #convert coefficient into a polynomial that can be evaluated
    poly=np.poly1d(p_coeff)

