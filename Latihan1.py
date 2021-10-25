import numpy as np
import pandas as pd
import xlrd

df_can = pd.read_excel('https://github.com/ardhiraka/PFDS_sources/blob/master/Canada.xlsx?raw=true',
                        sheet_name='Canada by Citizenship',
                        skiprows = range(20),
                        skipfooter = 2)

#print(df_can.head())
#print(df_can.tail())
df_can.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis = 1, inplace=True)
#Mengganti nama kolom
df_can.rename(columns={'OdName' : 'Country', 'AreaName' : 'Continent', 'RegName' : 'Region'}, inplace=True)
print(df_can.columns)