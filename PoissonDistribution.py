import matplotlib.pyplot as plt
from IPython.display import Math, Latex
from IPython.core.display import Image
from scipy.stats import poisson
import seaborn as sns 

#settings for seaborn plotting style
sns.set(color_codes=True)
sns.set(rc={'figure.figsize' :(5,5)})

n = 10000
start = 10
width = 20
data_poisson = poisson.rvs(mu = 3, size = 10000)

#Menggunakan distplot seaborn = memplot histogram distribusi
ax = sns.distplot(data_poisson,
                bins = 30, #Menentukan jumlah bins
                kde = False, #Menentukan density plot option
                color = 'skyblue', #Warna Histogram
                hist_kws = {"linewidth" : 15, 'alpha' : 1}) #Menentukan linewidth
ax.set(xlabel = 'Poisson Distribution', ylabel = 'Frequency')
plt.show()