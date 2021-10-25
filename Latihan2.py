import numpy as np
import pandas as pd
mv = ['na', 'n/a', '--']
df = pd.read_csv('https://raw.githubusercontent.com/ardhiraka/PFDS_sources/master/property_data.csv',na_values=mv)

cnt = 0
for row in df['OWN_OCCUPIED'] :
    try:
        int(row) #Mengubah row menjadi int 
        df.loc[cnt, 'OWN_OCCUPIED']=np.nan
    except ValueError:
        pass
    cnt+=1

print(df.head(9))

#Summarizing Missing Values
print(df.isnull().sum()) #total missing values 
print(df.isnull().values.any()) #apakah kita memiliki nilai yang hilang sama sekali?
print(df.isnull().sum().sum()) #total missing values