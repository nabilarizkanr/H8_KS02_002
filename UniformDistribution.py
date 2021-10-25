import matplotlib.pyplot as plt
from IPython.display import Math, Latex
from IPython.core.display import Image
from scipy.stats import uniform
import seaborn as sns 

#settings for seaborn plotting style
sns.set(color_codes=True)
sns.set(rc={'figure.figsize' :(5,5)})

n = 10000
start = 10
width = 20
data_uniform = uniform.rvs(size = n, loc = start, scale = width)

#Menggunakan distplot seaborn = memplot histogram distribusi
ax = sns.distplot(data_uniform,
                bins = 100, #Menentukan jumlah bins
                kde = True, #Menentukan density plot option
                color = 'skyblue', #Warna Histogram
                hist_kws = {"linewidth" : 15, 'alpha' : 1}) #Menentukan linewidth
ax.set(xlabel = 'Uniform Distribution', ylabel = 'Frequency')
plt.show()

