import pandas as pd
import numpy as np
df = pd.read_csv('Heart.csv')
#Menghitung CI menggunakan library 'statsmodels'
#import statsmodels.api as sm
#print(df)

#Construct a CI for the female population proportion has heart disease
#Mengganti 1 dan 0 dengan pria dan wanita di kolom Sex1
df['Sex1'] = df.sex.replace({1 : "Male", 0 : "Female"})
#Menggunakan kolom 'Target'
dx = df[["target", "Sex1"]].dropna()
#Menunjukkan jumlah pria dan wanita yang menderita penyakit jantung 
#dan yang tidak menderita penyakit jantung
pd.crosstab(dx.target, dx.Sex1)
print(pd.crosstab(dx.target, dx.Sex1))

#Hitung proporsi penduduk wanita yang menderita penyakit jantung
p_fm = 226 / (86+226)
print(p_fm)

#Hitung jumlah populasi wanita 
n = 86 + 226
print(n)

#Hitung Standard Error
se_female = np.sqrt(p_fm * (1 - p_fm) / n)
print(se_female)

#Membuat CI 
z_score = 1.96
lcb = p_fm - z_score * se_female #Lower limit of the CI
ucb = p_fm + z_score * se_female #upper limit of the CI
print(lcb, ucb)

#sm.stats.proportion_confint( n * p_fm, n)
#print(sm.stats.proportion_confint( n * p_fm, n))

#Mendapatkan Mean, Standard Deviation, dan Population Size dari populasi Pria dan Wanita
#df.groupby("Sex1").agg({"cho1" : [np.mean, np.std, np.size]})
mean_fe = 261.45
sd =64.4
n = 312
z = 1.96

#Calculate the standard error uisng the formula for the standard error of the mean
se = sd / np.sqrt(n)
print(se)


#Construct the CI --> untuk mean cholosterol pada populasi wanita
lcb = mean_fe - z * se #Lower limit of the CI
ucb = mean_fe + z * se #Upper Limit of the CI
print(lcb, ucb)