import math
import statistics 
import numpy as np
from numpy.lib.function_base import cov
import scipy.stats
import pandas as pd

#Creating 2D NumPy array :
a = np.array([[1, 1, 1],
              [2, 3, 1],
              [4, 9, 2],
              [8, 27, 4],
              [16, 1, 1]])
print(np.mean(a))
print(a.mean())
print(np.median(a))
print(a.var(ddof=1))

print(np.mean(a, axis=0))
print(a.mean(axis=0))
print(np.mean(a, axis=1))
print(a.mean(axis=1))

print(np.median(a, axis=0))
print(np.median(a, axis=1))
print(a.var(axis=0, ddof=1))
print(a.var(axis=1, ddof=1))

#bekerja dengan fungsi statistik SciPy --> nilai default axis = 0
print(scipy.stats.gmean(a))
print(scipy.stats.gmean(a, axis=0))

#Jika axis = 1
print(scipy.stats.gmean(a, axis=1))

#Jika ingin statistik untuk seluruh dataset, maka axis=None
print(scipy.stats.gmean(a, axis=None))

#Mendapatkan nilai tertentu dari ringkasi dengan dot notation
result = scipy.stats.describe(a, axis=1, ddof=1, bias=False)
print(result.mean)

