import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline

data = pd.ExcelFile('obes.xls')

ex = data.sheet_names
data_age = data.parse(u'7.2', skiprows=4, skipfooter=14)
data_age.rename(columns={u'Unnamed: 0' : u'Year'}, inplace=True) 
data_age.dropna(inplace=True)
data_age.set_index('Year', inplace=True)
data_age.head()
data_age.plot()
#<matplotlib.axes._subplots.AxesSubplot at 0x11b32bad0>
#data_age.set_index('Year', inplace=True)
data_age_minus_total = data_age.drop('Total', axis=1)
data_age_minus_total.plot()

#data_age['Under 16'].plot(label="Under 16", legend=True)
#data_age['35-44'].plot(label="35-44", legend=True)
plt.show()