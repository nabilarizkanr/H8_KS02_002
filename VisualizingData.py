import math
import statistics 
import numpy as np
from numpy.lib.function_base import cov
import scipy.stats
import pandas as pd
import matplotlib.pyplot as plt
#plt.style.use('gpplot')

#Box Plots
np.random.seed(seed=0)
x = np.random.randn(1000)
y = np.random.randn(100)
z = np.random.randn(10)

fig, ax = plt.subplots()
ax.boxplot((x,y,z), vert=False, showmeans=True, meanline=True, labels=('x', 'y', 'z'), patch_artist=True,
 medianprops={'linewidth' : 2, 'color':'purple'}, 
 meanprops={'linewidth' : 2, 'color': 'red'})
#plt.show()

#Histograms
hist, bin_edges = np.histogram(x, bins=10)
fig, ax = plt.subplots()
#ax.hist(x, bin_edges, cumulative=False)
ax.hist(x, bin_edges, cumulative=True)
ax.set_xlabel('x')
ax.set_ylabel('Frequency')
plt.show()

#Pie Charts
x,y,z = 128, 256, 1024

fig, ax = plt.subplots()
ax.pie((x,y,z), labels=('x', 'y', 'z'), autopct='%1.1f%%')
plt.show()

#Bar Charts
x = np.arange(21)
y = np.random.randint(21, size=21)
err = np.random.randn(21)

fig, ax = plt.subplots()
ax.bar(x,y, yerr=err)
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()

#X-Y Plots
x = np.arange(21)
y = 5 +2 * x + 2 * np.ranodm.randn(21)
slope, intercept, r, *__ = scipy.stats.linregress(x,y)
line = f'Regression line: y = {intercept:.2f} + {slope:2.f}x, r = {r:.2f}'

fig, ax = plt.subplots()
ax.plot(x,y,linewidth = 0, marker = 's', label = 'Data Points')
ax.plot(x, intercept + slope * x, label = line)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend(facecolor = 'white')
plt.show()

#Heatmaps
#matrix = npcov(x,y).round(decimals = 2)
matrix = np.corrcoef(x,y).round(decimals = 2)
fig, ax = plt.subplots()
ax.imshow(matrix)
ax.grid(False)
ax.xaxis.set(ticks = (0,1), ticklabels=('x', 'y'))
ax.yaxis.set(ticks=(0,1), ticklables=('x', 'y'))
ax.set_ylim(1.5, -0.5)
for i in range(2) :
    for j in range(2):
        ax.text(j,i,matrix[i, j], ha='center', va='center', color='w')
        plt.show()