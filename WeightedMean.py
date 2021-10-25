import math
import statistics 
import numpy as np
import scipy.stats
import pandas as pd

#List Python 
x = [8.0, 1, 2.5, 4, 28.0]
w = [0.1, 0.2, 0.3, 0.25, 0.15]

#wmean = sum(w[i] * x[i] for i in range(len(x))) / sum(w)
#print(wmean)

#wmean = sum(x_ * w_ for (x_, w_) in zip(x, w)) / sum(w)
#print(wmean)

#Menggunakan np.average() untuk mendapatkan weighted mean dari array NumPy atau Series Pandas :
y, z, w = np.array(x), pd.Series(x), np.array(w)
wmean = np.average(y, weights = w)
print(wmean)

wmean = np.average(z, weights = w)
print(wmean)

#element-wise produc w* dengan np.sum() atau .sum()
wmean1 = (w * y ).sum() / w.sum()
print(wmean1)