import numpy as np
import pandas as pd
import folium
from folium import plugins

df_incidents = pd.read_csv('Police_Department_Incidents_-_Previous_Year__2016_.csv')
#print('Dataset Downloaded and read into a pandas dataframe')

#Item Pertama dalam dataset
#print(df_incidents.head())

#Banyaknya entri di kumpulan data
#print(df_incidents.shape)


#Dikarenakan dataframe ada 150.500 kejahatan, maka kita akan mengambil 100 insiden pertama
limit = 100
df_incidents = df_incidents.iloc[0:limit, :]
#Mengkonfirmasi hanya 100 Kejahatan
#print(df_incidents.shape)

#Memvisualisasi kejahatan yang terjadi di San Fransico 
latitude = 37.77
longitude = -122.42
#Create a map
sanfran_map = folium.Map(location=[latitude,longitude], zoom_start=12)
#sanfran_map.save('sanfran.html')
#How to put crime on the map, creating feature group
#incidents = folium.map.FeatureGroup()
#Instantiate a mark cluster a clean copy
incidents = plugins.MarkerCluster().add_to(sanfran_map)
#Loop through the 100 crimes, add each to incidents feature group
for lat, lng,label in zip(df_incidents.Y, df_incidents.X, df_incidents.Category):
    #incidents.add_child(
        #folium.CircleMarker(
        folium.Marker(
            #[lat,lng],
            location = [lat, lng],
            #radius=5, #define how big you want the cricle markers
            #color='yellow',
            #fill=True,
            icon=None,
            popup=label,
           # fill_color='blue',
            #fill_opacity=0.6
        ).add_to(incidents)
  #  )
#Add incidents to map
#sanfran_map.add_child(incidents) 
#sanfran_map.save('sanfran.html')
#Adding pop-up text on markers
#latitudes = list(df_incidents.Y)
#longitudes = list(df_incidents.X)
#labels = list(df_incidents.Category)

#for lat, lng, label in zip(latitudes, longitudes, labels):
#    folium.Marker([lat,lng], popup=label).add_to(sanfran_map)
#sanfran_map.add_child(incidents)
sanfran_map.save('sanfran.html')


