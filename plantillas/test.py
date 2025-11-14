
"""def load_stations(path):
    file = open(path,"r")
    info= file.read()

    print(info)"""


import metro as mt
import stations as st
import system as sys
import time

estaciones = mt.load_stations('stations.info') # Cargar las estaciones desde el archivo
usuarios = mt.load_metro_log('metro.log') # Cargar los registros de viajes desde el archivo

top_trayectos = sys.top_trayectos_populares(usuarios)
print( top_trayectos )