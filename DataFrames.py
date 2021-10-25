import math
import statistics 
import numpy as np
from numpy.lib.function_base import cov
import scipy.stats
import pandas as pd

a = np.array([[1, 1, 1],
              [2, 3, 1],
              [4, 9, 2],
              [8, 27, 4],
              [16, 1, 1]])
row_names = ['first', 'second', 'third', 'fourth', 'fifth']
col_names = ['A', 'B', 'C']
df = pd.DataFrame(a, index=row_names, columns=col_names)
print(df)
print(df.mean())
print(df.var())
print(df.mean(axis=1))
print(df.var(axis=1))
print(df['A'])
print(df['A'].mean())
print(df['A'].var())
print(df.values)
print(df.to_numpy())
print(df.describe())
print(df.describe().at['mean', 'A'])
print(df.describe().at['50%', 'B'])
