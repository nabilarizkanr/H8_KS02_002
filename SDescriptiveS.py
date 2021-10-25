import math
import statistics 
import numpy as np
import scipy.stats
import pandas as pd

x = [-5.0, -1.1, 0.1, 2.0, 8.0, 12.8, 21.0, 25.8, 41.0]
y = np.array(x)
y_with_nan = np.insert(y, 2, np.nan)
z, z_with_nan = pd.Series(y), pd.Series(y_with_nan)
#Mendapatkan Descriptive Statistics dengan cepat
result = scipy.stats.describe(y, ddof=1, bias=False)
print(result)

#Mengakses nilai tertentu dengan dot notation
print(result.nobs)
print(result.minmax[0])
print(result.minmax[1])
print(result.mean)
print(result.variance)
print(result.skewness)
print(result.kurtosis)

#Pandas
result = z.describe()
print(result)

#Jika ingin berisi persentil lain, akses setiap item result dengan labelnya 
print(result['mean'])
print(result['std'])
print(result['min'])
print(result['max'])
print(result['25%'])
print(result['50%'])
print(result['75%'])