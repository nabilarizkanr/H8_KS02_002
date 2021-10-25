import numpy as np
import pandas as pd
import datetime

from pandas.core.arrays import string_

date_rng = pd.date_range(start='1/01/2020', end='1/08/2020', freq='H')
#print(date_rng)

df= pd.DataFrame(date_rng, columns=['date'])
df['Data'] = np.random.randint(0,100,size=(len(date_rng)))
#Konversi indeks data frame menjadi datetime index 
df['datetime'] = pd.to_datetime(df['date'])
df=df.set_index('datetime')
df.drop(['date'], axis=1, inplace=True)
print(df.head())

