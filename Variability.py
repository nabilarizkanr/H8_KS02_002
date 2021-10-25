import math
import statistics 
import numpy as np
import scipy.stats
import pandas as pd

x = [8.0, 1, 2.5, 4, 28.0]
#Menghitung variance dengan python pure
n = len(x)
mean_ = sum(x) / n
var_ = sum((item - mean_)**2 for item in x) / (n-1)
#print(var_)

#dengan memanggil fungs statistics.variance()
var_ = statistics.variance(x)
#print(var_)

#dengan NumPy
var_ = np.var(x, ddof=1)
print(var_)