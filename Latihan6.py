import numpy as np
import pandas as pd
import datetime

date_rng = pd.date_range(start='1/01/2020', end='1/08/2020', freq='H')
string_date_rng = [str(x) for x in date_rng]
print(string_date_rng)

timestamp_date_rng = pd.to_datetime(string_date_rng, infer_datetime_format=True)
print(timestamp_date_rng)