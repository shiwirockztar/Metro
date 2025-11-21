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


#total_viajes = st.total_viajes_estacion(usuarios, '012')
#print(f'Total de viajes en la estación seleccionada: {total_viajes}')
#lista_estaciones = st.listar_estaciones(estaciones)
#estacion_seleccionada = mt.menu(lista_estaciones)
#print(estacion_seleccionada)
#hora_pico = st.hora_pico_estacion(usuarios, '020')
#print(f'La hora pico de la estación seleccionada es: {hora_pico}:00 horas')

#estaciones_comunes = st.estaciones_origen(usuarios, '012')
destino_comun = st.estaciones_destino(usuarios, '012')
print(f'La estación destino más común de la estación seleccionada es: {estaciones[destino_comun]["nombre"]}')



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
