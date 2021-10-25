import matplotlib.pyplot as plt
from IPython.display import Math, Latex
from IPython.core.display import Image
from scipy.stats import norm
import seaborn as sns 

#settings for seaborn plotting style
sns.set(color_codes=True)
sns.set(rc={'figure.figsize' :(5,5)})

n = 10000
start = 10
width = 20
#generate random numbers from N (0,1)
data_normal = norm.rvs(size = 10000, loc = 0, scale = 1)

#Menggunakan distplot seaborn = memplot histogram distribusi
ax = sns.distplot(data_normal,
                bins = 100, #Menentukan jumlah bins
                kde = True, #Menentukan density plot option
                color = 'skyblue', #Warna Histogram
                hist_kws = {"linewidth" : 15, 'alpha' : 1}) #Menentukan linewidth
ax.set(xlabel = 'Normal Distribution', ylabel = 'Frequency')
plt.show()
