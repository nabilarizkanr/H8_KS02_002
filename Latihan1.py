import numpy as np
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/ardhiraka/PFDS_sources/master/nbaallelo.csv')
print(len(df)) #melihat jumlah baris
df.shape
print(df.shape) #melihat dimensi
print(df.head()) #melihat 5 baris pertama

#Menampilkan semua 23 kolom 
pd.set_option("display.max.columns", None)
pd.set_option("display.precision", 2)

print(df.tail(3)) #Mencetak 3 baris terakhir DataFrame

#Exploring Dataset
#Memeriksa seberapa sering nilai tertentu muncul dalam kolom
df['team_id'].value_counts()
df["fran_id"].value_counts()
#mencari tahu tim "Lakers" lainnya
df.loc[df['fran_id']=='Lakers', 'team_id'].value_counts() 
#mengetahui kapan NYK melakukan pertandingan
df.loc[df['team_id']=='NYK', 'date_game'].agg(('max', 'min'))
#mengetahui semua pertandingan yang dimainkan NYK
df.loc[df['team_id']=='NYK', 'pts'].sum()
