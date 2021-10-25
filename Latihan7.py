import numpy as np
import pandas as pd
import datetime as dt

string_date_rng2 = ['June-01-2020', 'june-02-2020', 'JUNE-03-2020']
timestamp_date = [dt.datetime.strptime(str(x), '%B-%d-%Y') for x in string_date_rng2]
df = pd.DataFrame(timestamp_date, columns=['Date'])

#df[df.index.day == 2]
print(df)