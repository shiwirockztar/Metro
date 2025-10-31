# Implemente aquí los menús y el programa principal que invoca las funciones de los otros módulos

from metro import load_stations, menu_estaciones #incluyo metro.py 

estaciones = load_stations("stations.info") # Cargar las estaciones desde el archivo
print(estaciones)