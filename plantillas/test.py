"""def load_stations(path):
    file = open(path,"r")
    info= file.read()
    print(info)"""

import metro as mt
import stations as st
import system as sys
import time

estaciones = mt.load_stations('stations.info') # Cargar las estaciones desde el archivo
#usuarios = mt.load_metro_log('prueba.log') # Cargar los registros de viajes desde el archivo
usuarios = mt.load_metro_log('metro.log') # Cargar los registros de viajes desde el archivo

top_trayectos = sys.top_trayectos_populares(usuarios, estaciones)
print( top_trayectos )
print("Los 5 trayectos más populares son:")
for (origen, destino), conteo in top_trayectos:
    print(f"- {origen} -> {destino}: {conteo} viajes")


import math

lat1, lon1 = 6.242926, -75.571411
lat2, lon2 = 6.247210, -75.569694

R = 6371e3  # radio de la Tierra en metros
phi1, phi2 = math.radians(lat1), math.radians(lat2)
dphi = math.radians(lat2 - lat1)
dl = math.radians(lon2 - lon1)

a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dl/2)**2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
d = R * c

print(d)  # distancia en metros
