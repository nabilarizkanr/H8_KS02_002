import numpy as np
import pandas as pd
import xlrd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

df_can = pd.read_excel('https://github.com/ardhiraka/PFDS_sources/blob/master/Canada.xlsx?raw=true',
                        sheet_name='Canada by Citizenship',
                        skiprows = range(20),
                        skipfooter = 2)
#Membersihkan data 
df_can.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis = 1, inplace=True)
#Mengganti nama kolom
df_can.rename(columns={'OdName' : 'Country', 'AreaName' : 'Continent', 'RegName' : 'Region'}, inplace=True)
df_can.set_index('Country', inplace=True)
#Making all columns type string 
df_can.columns = list(map(str, df_can.columns))
#Adding total column 
df_can['Total'] = df_can.sum(axis = 1)
#Years that we will be using
years = list(map(str,range(1980,2014)))
df_tot = pd.DataFrame(df_can[years].sum(axis=0))
df_tot.index = map(float, df_tot.index)
df_tot.reset_index(inplace=True)
df_tot.columns= ['year', 'total']
#print(df_tot.head())
plt.figure(figsize=(15, 10))
sns.set(font_scale = 1.5)
#Change bg to white bg
#sns.set_style('ticks')
#Bg grid lines
sns.set_style('whitegrid')
ax = sns.regplot(x='year', y='total', data=df_tot, color='green', marker='+', scatter_kws={'s' : 200})
ax.set(xlabel = 'Year', ylabel = 'Total Immigration')
ax.set_title('Total Immigration to Canada From 1980 - 2013')
plt.show()