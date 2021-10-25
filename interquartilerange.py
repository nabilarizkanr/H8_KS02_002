import math
import statistics 
import numpy as np
import scipy.stats
import pandas as pd

x = [-5.0, -1.1, 0.1, 2.0, 8.0, 12.8, 21.0, 25.8, 41.0]
y = np.array(x)
y_with_nan = np.insert(y, 2, np.nan)
z, z_with_nan = pd.Series(y), pd.Series(y_with_nan)

quartiles = np.quantile(y, [0.25, 0.75])
print(quartiles[1] - quartiles[0])
