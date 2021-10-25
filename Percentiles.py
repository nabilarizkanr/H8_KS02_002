import math
import statistics 
import numpy as np
import scipy.stats
import pandas as pd

x = [-5.0, -1.1, 0.1, 2.0, 8.0, 12.8, 21.0, 25.8, 41.0]
#Membagi data menjadi beberapa interval
print(statistics.quantiles(x, n=2))
print(statistics.quantiles(x, n=4, method='inclusive'))

y = np.array(x)
#Menentukan persentil sampel
print(np.percentile(y, 5)) #Persentil ke 5
print(np.percentile(y, 95)) #Persentil ke 95
#Persentil merupakan NumPy 
print(np.percentile(y, [25, 50, 75])) #Persentil ke 25, 50, 75
print(np.median(y)) #Mengembalikan median

#Mengabaikan nilai nan, menggunakan NumPy
y_with_nan = np.insert(y, 2, np.nan)
print(y_with_nan)
print(np.nanpercentile(y_with_nan, [25, 50, 75]))

#Memberikan nilai-nilai kuantitatif 
print(np.quantile(y, 0.05))
print(np.quantile(y, 0.95))
print(np.quantile(y, [0.25, 0.5, 0.75]))
print(np.nanquantile(y_with_nan, [0.25, 0.5, 0.75]))

z, z_with_nan = pd.Series(y), pd.Series(y_with_nan)
print(z.quantile(0.05))
print(z.quantile(0.95))
print(z.quantile([0.25, 0.5, 0.75]))
print(z_with_nan.quantile([0.25, 0.5, 0.75]))