import math
import statistics 
import numpy as np
import scipy.stats
import pandas as pd

x = [8.0, 1, 2.5, 4, 28.0]

gmean = 1
for item in x:
    gmean *= item

gmean **= 1 / len(x)
print(gmean)

atau 
#print(scipt.stats.gmean(y))
#print(scipt.stats.gmean(z))