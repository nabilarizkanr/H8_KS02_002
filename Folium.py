import numpy as np
import pandas as pd
import folium


#define the world map
#world_map = folium.Map()
#world_map.save('world_map.html')

#define Semarang
semarang_map = folium.Map(location=[-6.992620, 110.428009], zoom_start=13, tiles='Stamen Toner')
semarang_map.save('Semarang.html')

#define Hacktiv8
hacktiv8_map = folium.Map(location=[-6.2607187, 106.7794275], zoom_start=15, tiles='Stamen Terrain')
hacktiv8_map.save('Hacktiv8.html')