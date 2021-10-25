import pandas as pd
import numpy as np
import statsmodels.api as sm
import scipy.stats.distributions as dist
df = pd.read_csv('Heart.csv')

#print(df.head())
#The Population proportion of Ireland having heart disease is 42%. Are more people suffering from heart disease in the US?
#define the null hypothesis and alternative hypothesis
#null hypothesis = population proportion yang menderita penyakit jantung di AS kurang dari atau sama dengan 42%
#Ho = p0 = 0.42 #null hypothesis
#Ha = p > 0.42 #alternative hypothesis

#Assume the dataset above is a representative sample from
#the population of the US
#Calculate the population proportion of the US having heart disease
p_us = len(df[df['target'] == '1']) / len(df)

#calculate the Test Statistic :
se = np.sqrt(0.42 * (1 - 0.42) / len(df))

#Best Estimates 
be = p_us

#hypothesized estimate
he = 0.42
test_stat = (be - he) / se

#Calculate the p - value
pvalue = 2 * dist.norm.cdf(-np.abs(test_stat))

#Infer the conclusion from the p - value