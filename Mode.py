import math
import statistics 
import numpy as np
import scipy.stats
import pandas as pd

u = [2, 3, 2, 8, 12]
v = [12, 15, 12, 15, 21, 15, 12]
mode_ = max((u.count(item), item) for item in set(u))[1]
#print(mode_)

#mode dengan statistics.mode()
mode_ = statistics.mode(u)
#print(mode_)

#mode dengan scipy.stats.mode()
#u, v = np.array(u), np.array(v)
mode_ = scipy.stats.mode(u)
#print(mode_)

mode = scipy.stats.mode(v)
#print(mode_)

#mode dengan jumlah kemunculannya sebagai array NumPy dengan .
#print(mode_.mode)
#print(mode_.count)

#metode .mode() yang menangani nilai multimodal dengan baik dan mengabaikan nilai nan 
u, v, w = pd.Series(u), pd.Series(v), pd.Series([2, 2, math.nan])
print(u.mode())
print(v.mode())
print(w.mode())