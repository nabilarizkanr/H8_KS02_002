import numpy as np
import pandas as pd
mv = ['na', 'n/a', '--']
df = pd.read_csv('https://raw.githubusercontent.com/ardhiraka/PFDS_sources/master/property_data.csv',na_values=mv)

#Replacing
df['ST_NUM'].fillna(125,inplace=True)
df.loc[2, 'ST_NUM']=125
median = df['NUM_BEDROOMS'].median()
df['NUM_BEDROOMS'].fillna(median, inplace=True)
print(df.head(9))