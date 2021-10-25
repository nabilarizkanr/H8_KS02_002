import pandas as pd
import numpy as np
from scipy.stats.morestats import anderson
import statsmodels.api as sm

#Pearson's Correlation Test
from scipy.stats import pearsonr
data1 = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869]
data2 = [0.353, 3.517, 0.125, -7.545, -0.555, -1.536, 3.350, -1.578, -3.537, -1.579]
stat, p = pearsonr(data1, data2)
print('stat = %.3f, p = %.3f' % (stat,p))
if p > 0.05 :
    print('Probably Independent')
else :
    print('Probably Dependent')

#Spearman's Rank Correlation Test
from scipy.stats import spearmanr
data1 = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869]
data2 = [0.353, 3.517, 0.125, -7.545, -0.555, -1.536, 3.350, -1.578, -3.537, -1.579]
stat, p = spearmanr(data1, data2)
print('stat = %.3f, p = %.3f' % (stat, p))
if p > 0.05 :
    print('Probably Independent')
else :
    print('Probably Dependent')

#Kendall's Rank Correlation
from scipy.stats import kendalltau
data1 = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869]
data2 = [0.353, 3.517, 0.125, -7.545, -0.555, -1.536, 3.350, -1.578, -3.537, -1.579]
stat, p = kendalltau(data1, data2)
print('stat = %.3f, p = %.3f' % (stat,p))
if p > 0.05 :
    print('Probably Independent')
else :
    print('Probably Dependent')

#Chi-Squared Test
from scipy.stats import chi2_contingency
table = [[10, 20, 30], [6, 9, 17]]
stat, p, dof, expected = chi2_contingency(table)
print('stat = %.3f, p = %.3f' % (stat, p))
if p > 0.05 :
    print('Probably Independent')
else :
    print('Probably Dependent')

#Augmented Dickey-Fuller Unit Root Test
from statsmodels.tsa.stattools import adfuller
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
stat, p, lags, obs, crit, t = adfuller(data)
print('stat = %.3f, p = %.3f' % (stat, p))
if p > 0.05 :
    print('Probably not Stationary')
else :
    print('Probably Stationary')

#Kwiatkowski-Phillips-Schmidt-Shin
from statsmodels.tsa.stattools import kpss
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
stat, p, lags, crit = kpss(data)
print('stat = %.3f, p = %.3f' % (stat, p))
if p > 0.05 :
    print('Probably not Stationary')
else :
    print('Probably Stationary')