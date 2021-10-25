import math
import statistics 
import numpy as np
import scipy.stats
import pandas as pd

#List Python 
x = [8.0, 1, 2.5, 4, 28.0]
x_with_nan = [8.0, 1, 2.5, math.nan, 4, 28.0]
y, y_with_nan = np.array(x), np.array(x_with_nan)
z, z_with_nan = pd.Series(x), pd.Series(x_with_nan)

mean_ = sum(x) / len(x)
print(mean_)

mean = statistics.mean(x_with_nan)
print(mean)

#Menggunakan NumPy 
mean1 = np.mean(y)
print(mean1)

#mean() merupakan sebuah fungsi, kita dapat menggunakan method.mean()
mean2 = y.mean()
print(mean2)

#print(np.mean(y_with_nan) #fungsi mean dari numpy
#print(y_with_nan.mean()) #Method.mean()

#Mengabaikan nilai nan, menggunakan np.nanmean()
#print(np.nanmean(y_with_nan))

#pd.Series mempunya method.mean()
mean3 = z.mean()
print(mean3)