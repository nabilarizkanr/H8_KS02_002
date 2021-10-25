from matplotlib.transforms import Bbox
import pandas as pd
import seaborn as sns
import scipy.stats as stats
import numpy as np
import random
import warnings
import matplotlib.pyplot as plt

sns.set(rc = {'figure.figsize' : (13, 7.5)})
sns.set_context('talk')

#Generate dua ditribusi normal menggunakan metode numpy random module's normal() untuk pria dan wanita
#Menggabungkan dua array dan assign ke kolom us_people_mass_pounds di df_ppl_mass Data Frame

np.random.seed(42)
normal_distribution_us_male_mass_pounds = np.random.normal(loc = 181, scale = 24, size = 6000)
normal_distribution_us_female_mass_pounds = np.random.normal(loc = 132, scale = 22, size = 6500)
all_mass_values = np.concatenate((normal_distribution_us_male_mass_pounds, normal_distribution_us_female_mass_pounds), axis = 0)
df_ppl_mass = pd.DataFrame(data = {'us_people_mass_pounds' : all_mass_values})
print(df_ppl_mass.head())

#View Distribution of U.S People' Mass
#Menggunakan seaborn distplot() untuk membuat histogram di kolom us_people_mass_pounds
#sns.distplot(df_ppl_mass['us_people_mass_pounds'],
#color = "darkslategrey")
#plt.xlabel("mass [pounds]", labelpad=14)
#plt.ylabel("probability of occurence", labelpad=14)
#plt.title("Distribution of Mass of People in U.S.", y=1.015, fontsize = 20);
#plt.show()


#Calculation Population Mean 
pop_mean_mass = df_ppl_mass['us_people_mass_pounds'].mean()
print(pop_mean_mass)

#Calculate Population Standard Deviation
pop_std_dev_mass = df_ppl_mass['us_people_mass_pounds'].std()
print(pop_std_dev_mass)

#Menyimpan semua sample means dalam list sample_means
#dan menghitung rata - rata tiap sampel
sample_means = []
n = 25
for sample in range(0, 300) :
    #Random sampling done with replacement
    sample_values = np.random.choice(a = df_ppl_mass['us_people_mass_pounds'], size = n)
    sample_mean = np.mean(sample_values)
    sample_means.append(sample_mean)

#View Distribution of Sample Means 
#sns.distplot(sample_means)
#plt.title("Distribution of Sample Means ($n = 25$) of People's Mass in Pounds", y = 1.015, fontsize = 20)
#plt.xlabel("Sample Mean Mass [pounds]", labelpad = 14)
#plt.ylabel("Frequency of Occurence", labelpad = 14);
#plt.show()

#Calculate Median of Sample Means 
median_of_sample_means = np.median(sample_means)
print(median_of_sample_means)

#Calculate Mean of Sample Means
mean_of_sample_means = np.mean(sample_means)
print(mean_of_sample_means)

#Calculate Standard Deviation of Sample Means
std_dev_of_sample_means = np.std(sample_means)
print(std_dev_of_sample_means)

#Equation for Standard Deviation of Sampling Distribution
#Persamaan Standar Error
standard_error = pop_std_dev_mass / np.sqrt(n)
print(standard_error)

#Critical Z- Scores
tail = 1 - stats.norm.cdf(1.96)
print(tail)

#The area under the curve between the z - critical scores is approximately 0.95
print(1 - (tail * 2 ))

#Menghitung batas yang tepat untuk area di mana 95% mean sampel berada di mean populasi
lower_95_perc_bound = mean_of_sample_means - 1.96 * standard_error
print(lower_95_perc_bound)
upper_95_perc_bound = mean_of_sample_means + 1.96 * standard_error
print(upper_95_perc_bound)

kde = stats.gaussian_kde(sample_means)
pos = np.linspace(np.min(sample_means), np.max(sample_means), 10000)
plt.plot(pos, kde(pos), color = 'teal')
shade = np.linspace(lower_95_perc_bound, upper_95_perc_bound, 300)
plt.fill_between(shade, kde(shade), alpha = 0.45, color = 'teal')
plt.text( x = 154, y = 0.1, horizontalalignment = 'center', fontsize = 17,
            s="95% of sample means fall within\nthis shaded area of plus or minus\n1.96 z-scores from the mean",
            bbox = dict(facecolor='whitesmoke', boxstyle='round, pad=0.1'))
plt.title("Distribution of Sample Means ($n = 25$) of People's Mass in Pounds", y = 1.015, fontsize = 20)
plt.xlabel("Sample Mean Mass [Pounds]", labelpad= 14) 
plt.ylabel("Frequency of Occurence", labelpad= 14);
plt.show()  