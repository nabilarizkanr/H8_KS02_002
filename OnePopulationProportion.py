import matplotlib.pyplot as plt
from IPython.display import Math, Latex
from IPython.core.display import Image
from scipy.stats import bernoulli
import seaborn as sns 
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Use of proportions_ztest() from statsmodels

n = 1018
pnull = .52
phat = .56
#Mengembalikan dua nilai -z-statistic dan p-value
print(sm.stats.proportions_ztest(phat * n, n, pnull, alternative = 'larger'))

#Conclusion of the hypothesis test
#nilai p-value dari z-test cukup kecil oleh karena itu reject the Null Hypothesis

