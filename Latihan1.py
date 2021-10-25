import numpy as np
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/ardhiraka/PFDS_sources/master/property_data.csv')

#print(df.head(10)) #akan nge print 10 baris awal

#hanya keluar kolom ST_NUM
print(df['ST_NUM']) 
#dapat melihat / mengkonfirmasi Missing Values
df['ST_NUM'].isnull()

#Melihat Missing Values Pada Number of Bedrooms
df['NUM_BEDROOMS']
print(df['NUM_BEDROOMS'].isnull)

#Melihat Unexpected Missing Values
print(df['OWN_OCCUPIED'])
print(df['OWN_OCCUPIED'].isnull)
