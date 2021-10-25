import math
import statistics 
import numpy as np
import scipy.stats
import pandas as pd

x = [8.0, 1, 2.5, 4, 28.0]
hmean = len(x) / sum(1 /item for item in x)
#print(hmean)

#atau
hmean = statistics.harmonic_mean(x)
print(hmean)

