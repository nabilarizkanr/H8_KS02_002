import matplotlib.pyplot as plt
from IPython.display import Math, Latex
from IPython.core.display import Image
from scipy.stats import bernoulli
import seaborn as sns 
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
da = pd.read_csv('nhanes_2015_2016.csv')

#print(da.head())

females = da[da["RIAGENDR"] == 2]
male = da[da["RIAGENDR"] == 1]

n1 = len(females)
mu1 = females["BMXBMI"].mean()
sd1 = females["BMXBMI"].std()

print(n1, mu1, sd1)

n2 = len(male)
mu2 = male["BMXBMI"].mean()
sd2 = male["BMXBMI"].std()

print(n2, mu2, sd2)

print(sm.stats.ztest(females["BMXBMI"].dropna(),
male["BMXBMI"].dropna(), alternative = 'two-sided'))

#Conclusion of The Hypothesis Test
#P-Value (6.59e-10) sangat kecil = reject the Null Hypothesis

#Histogram
plt.figure(figsize = (7,4))
plt.title("Female BMI Histogram", fontsize = 16)
plt.hist(females["BMXBMI"].dropna(), edgecolor = 'k', color = 'pink', bins = 25)
plt.show()

plt.figure(figsize = (7,4))
plt.title("Male BMI Histogram", fontsize = 16)
plt.hist(male["BMXBMI"].dropna(), edgecolor = 'k', color = 'blue', bins = 25)
plt.show()