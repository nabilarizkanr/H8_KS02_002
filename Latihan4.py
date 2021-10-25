import numpy as np
import pandas as pd
import xlrd
import matplotlib as mpl
import matplotlib.pyplot as plt

df_can = pd.read_excel('https://github.com/ardhiraka/PFDS_sources/blob/master/Canada.xlsx?raw=true',
                        sheet_name='Canada by Citizenship',
                        skiprows = range(20),
                        skipfooter = 2)

df_can.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis = 1, inplace=True)
#Mengganti nama kolom
df_can.rename(columns={'OdName' : 'Country', 'AreaName' : 'Continent', 'RegName' : 'Region'}, inplace=True)
#Adding total column 
df_can['Total'] = df_can.sum(axis = 1)
years = list(map(str, range(1980, 2014)))
df_can.set_index('Country', inplace=True)

df_can.sort_values(by="Total", axis=0, ascending=False, inplace=True)
df_top5 = df_can.head(5)
#df_top5 = df_top5[range(1980, 2013)].transpose()
top1 = df_top5.loc[[df_top5.columns],range(1980,2013)]
print(df_top5)