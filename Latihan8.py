import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

opsd_daily = pd.read_csv('https://raw.githubusercontent.com/ardhiraka/PFDS_sources/master/opsd_germany_daily.csv', index_col=0, parse_dates=True)
#opsd_daily = opsd_daily.set_index('Date')
#print(opsd_daily.head(3))
#print(opsd_daily.index)
opsd_daily['Year'] = opsd_daily.index.year
opsd_daily['Month'] = opsd_daily.index.month
opsd_daily['Weekday'] = opsd_daily.index.weekday
#print(opsd_daily.head())
#print(opsd_daily.loc['2017-08-10']) #Memilih data untuk satu hari
#print(opsd_daily.loc['2014-01-20':'2014-01-22']) #Memilih data dari hari ke hari
#print(opsd_daily.loc['2012-02']) #Memilih data seluruh bulan Februari 2012
opsd_daily['Consumption'].plot(linewidth=0.5);
plt.show()