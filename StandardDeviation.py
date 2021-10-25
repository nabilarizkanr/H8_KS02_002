import math
import statistics 
import numpy as np
import scipy.stats
import pandas as pd

x = [8.0, 1, 2.5, 4, 28.0]
n = len(x)
mean_ = sum(x) / n
var_ = sum((item - mean_)**2 for item in x) / (n-1)
std_ = var_ ** 0.5
#print(std_)

#menggunakan statistics.stdev()
std_ = statistics.stdev(x)
#print(std_)

#menggunakan NumPy -> fungsi std() dan method.std()
print(np.std(x, ddof=1))
print(x.std(ddof=1))

#Objek pd.Series memiliki method.std()
z.std(ddof=1)
