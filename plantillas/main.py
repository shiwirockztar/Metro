# Implemente aquí los menús y el programa principal que invoca las funciones de los otros módulos

from metro import load_stations, menu_estaciones #incluyo metro.py 

estaciones = load_stations("stations.info") # Cargar las estaciones desde el archivo
#print(estaciones)

msj="010 69253198 04:03  IN"
#print(msj.split(" "))
for campo, i in enumerate(msj.split(" ")):
    print(f"{campo} : {i}")
# Cargar los registros de viajes

# Ejemplo de uso del menú de estaciones
#seleccion = menu_estaciones()
#print(f"Estación seleccionada: {seleccion}")