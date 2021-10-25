import math
import statistics 
import numpy as np
import scipy.stats
import pandas as pd

x = [8.0, 1, 2.5, 4, 28.0]
n = len(x)
x_with_nan = [8.0, 1, 2.5, math.nan, 4, 28.0]
y, y_with_nan = np.array(x), np.array(x_with_nan)
z, z_with_nan = pd.Series(x), pd.Series(x_with_nan)

mean_ = sum(x) / n
var_ = sum((item - mean_)**2 for item in x ) / (n-1)
std_ = var_ ** 0.5

skew_ = (sum((item - mean_)**3 for item in x)* n / ((n - 1) * (n - 2) * std_**3))
#print(skew_)

y, y_with_nan = np.array(x), np.array(x_with_nan)
print(scipy.stats.skew(y, bias=False))
print(scipy.stats.skew(y_with_nan, bias=False))

z, z_with_nan = pd.Series(x), pd.Series(x_with_nan)
print(z.skew())
