import math
import statistics 
import numpy as np
import scipy.stats
import pandas as pd

x = [8.0, 1, 2.5, 4, 28.0]
n = len(x)
if n % 2:
    median_ = sorted(x)[round(0.5*(n-1))]
else:
    x_ord, index = sorted(x), round(0.5*n)
    median_ = 0.5 * (x_ord[index-1] + x_ord[index])

print(median_)
print(x)
print(statistics.median_low(x[:-1]))
print(statistics.median_high(x[:-1]))