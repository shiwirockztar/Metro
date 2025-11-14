
"""def load_stations(path):
    file = open(path,"r")
    info= file.read()

    print(info)"""


import metro as mt
import stations as st
import system as sys
import time

estaciones = mt.load_stations('stations.info') # Cargar las estaciones desde el archivo
usuarios = mt.load_metro_log('prueba.log') # Cargar los registros de viajes desde el archivo

distancia_promedio = sys.distancia_promedio_viaje(usuarios, estaciones)
print(f"La distancia promedio de viaje es de {distancia_promedio:.2f} metros")