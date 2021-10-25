import math
import statistics 
import numpy as np
from numpy.lib.function_base import cov
import scipy.stats
import pandas as pd

x = list(range(-10, 11))
y = [0, 2, 2, 2, 2, 3, 3, 6, 7, 4, 7, 6, 6, 9, 4, 5, 5, 10, 11, 12, 14]
x_ , y_ = np.array(x), np.array(y)
x__, y__ = pd.Series(x_), pd.Series(y_)

#Covariance
n = len(x)
mean_x, mean_y = sum(x) /n, sum(y) / n
cov_xy = (sum((x[k] - mean_x) * (y[k] - mean_y) for k in range(n))
            / (n - 1))
#print(cov_xy)

#NumPy memiliki fungsi cov(), yang mengembalikan covariance matrix
cov_matrix = np.cov(x_, y_)
print(cov_matrix)

#Mewakili covariance aktual antara x dan y
cov_xy = cov_matrix[0,1]
print(cov_xy)
cov_xy = cov_matrix[1,0]
print(cov_xy)

#Series Pandas memiliki metode .cov()
cov_xy = x__.cov(y__)
print(cov_xy)
cov_xy = y__.cov(x__)
print(cov_xy)

var_x = sum((item - mean_x) ** 2 for item in x) / (n-1)
var_y = sum((item - mean_y)**2 for item in y) / (n - 1)
std_x, std_y = var_x ** 0.5, var_y ** 0.5
r = cov_xy / (std_x * std_y)
print(r)


#menghitung the p-value
r, p = scipy.stats.pearsonr(x_,y_)
print(r)
print(p)

corr_matrix = np.corrcoef(x_, y_)
print(corr_matrix)

r = corr_matrix[0,1]
print(r)
r = corr_matrix[1,0]
print(r)

print(scipy.stats.lineregress(x_,y_))

result = scipy.stats.linregress(x_,y_)
r = result.rvalue
print(r)

r = x__.corr(y__)
print(r)
r = y__.corr(x__)
print(r)