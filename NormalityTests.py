import pandas as pd
import numpy as np
from scipy.stats.morestats import anderson
import statsmodels.api as sm


#Shapiro-Wilk Test
from scipy.stats import shapiro
data = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869]
stat, p = shapiro(data)
print('stat = %.3f, p = %.3f' % (stat, p))
if p > 0.05 :
    print('Probably Gaussian')
else :
    print('Probably not Gaussian')

#D'Agostino's K^2 Test
from scipy.stats import normaltest
data = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869]
stat, p = normaltest(data)
print('stat = %.3f, p = %.3f' % (stat, p))
if p > 0.05 :
    print('Probably Gaussian')
else :
    print('Probably not Gaussian')


#Anderson-Darling Test
from scipy.stats import anderson
data = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869]
result = anderson(data)
print('stat = %.3f' % (result.statistic))
for i in range(len(result.critical_values)) :
    sl, cv = result.significance_level[i], result.critical_values[i]
    if result.statistic < cv :
        print('Probably Gaussian at the %.1f%% level' % (sl))
    else :
        print('Probably not Gaussian at the %.1%% level' % (sl))
