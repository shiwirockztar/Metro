#estaciones ={"001":["Niquia","6.3337783",""]}
estaciones ={"001":{"nombre":"Niquia", "latitud":"6.3337783","longitud":""}}


#NombreNiquia = estaciones["001"][0]
NombreNiquia = estaciones["001"]["nombre"]


"""def load_stations(path):
    file = open(path,"r")
    info= file.read()

    print(info)"""

import metro as mt
#from metro import load_stations, menu_estaciones #incluyo metro.py 
import time
estaciones = mt.load_stations("stations.info") # Cargar las estaciones desde el archivo
#print(estaciones)

print("1) Listar estaciones")
print("Introduzca una opcion para continuar...")
opcion =input("Introduzca una opcion para continuar...")

msj="010 69253198 04:03  IN"
#print(msj.split(" "))
for campo, i in enumerate(msj.split(" ")):
    print(f"{campo} : {i}")
# Cargar los registros de viajes

# Ejemplo de uso del menú de estaciones
#seleccion = menu_estaciones()
#print(f"Estación seleccionada: {seleccion}")

time.sleep(2)  # Pausa de 2 segundos antes de limpiar la pantalla
print("\033[2J")  # Secuencia de escape ANSI para limpiar la pantalla
print("\033[39m")  # Secuencia de escape ANSI para restablecer el color del texto
print("\033[36m") # Secuencia de escape ANSI para establecer el color del texto a cian
# Secuencia de escape ANSI para establecer el color del texto a rojo: \033[31m
#