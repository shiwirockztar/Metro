
def load_stations(path = 'stations.info'):
    # Esta función retorna un diccionario con la información de las estaciones del metro.
    # Argumentos:
    # path: Ruta del archivo de estaciones.
    # Retorna:
    # Un diccionario con la información de las estaciones.
    with open(path,"r") as file:
        file.readline() # lee la primera linea y apunta el cursor e la siguiente linea
        estaciones = {}
        for line in file:
            #aux = line[:-1].split(",") # [:-1] para quitar salto de linea
            aux = line.rstrip().split(",") # Funcion para crear una lista de elementos separados por que tienen una coma para este caso
            estaciones[aux[1]] = {"nombre":aux[0],"latitud":aux[2],"longitud":aux[3]}
        return estaciones

def load_metro_log(path = 'metro.log'):
    # Esta función retorna un diccionario con la información de los viajes en el metro.
    # Argumentos:
    # path: Ruta del archivo de log del metro.
    # Retorna:
    # Un diccionario con la información de los viajes.
    with open(path,"r") as file:
        file.readline() # lee la primera linea y apunta el cursor e la siguiente linea
        viajes = {}
        for line in file:
            aux = line.rstrip().split(" ")
            viajes[aux[1]] = {"STATION_ID":aux[0],"EVENT_TIME":aux[2],"EVENT_TYPE":aux[3]}
    return viajes
    
    # Ejemplo de uso:
    # opciones = {"1":"a", "2":"b","3":"c"}
    # menu(opciones) -> devuelve la opción seleccionada por el usuario.
    with open(path,"r") as file:
        file.readline() # lee la primera linea y apunta el cursero e la siguiente linea
        viajes = {}
        for line in file:
            aux = line.rstrip().split(" ") 
            viajes[aux[1]] = {"nombre":aux[0],"latitud":aux[2],"longitud":aux[3]}
        return viajes


def menu(options) :
    # Esta función imprime el menú de opciones y devuelve la opción seleccionada por el usuario.
    # Argumentos:
    # options: Un diccionario donde las claves son las opciones del menú y los valores son las descripciones de las opciones.
    # Retorna:
    # La opción seleccionada por el usuario.
    
    # Ejemplo de uso:
    # opciones = {"1":"a", "2":"b","3":"c"}
    # menu(opciones) -> devuelve la opción seleccionada por el usuario.
    while True:
        for k, v in options.items() :
            print(f"{k} )  {v}")
        ele = input("Seleccione una opción: ")
        if ele in options :
            return ele
    
estaciones ={'001': {'nombre': 'Niquía', 'latitud': '6.337783', 'longitud': '-75.544365'}, '002': {'nombre': 'Bello', 'latitud': '6.330476', 'longitud': '-75.553434'}}
def menu_estaciones():
    # Esta función retorna la estación seleccionada por el usuario.
    # Argumentos:
    # options: Un diccionario donde las claves son las opciones del menú y los valores son las descripciones de las opciones.
    # Retorna:
    # La opción seleccionada por el usuario.
    
    # Ejemplo de uso:
    # opciones = {"1":"a", "2":"b","3":"c"}
    # menu(opciones) -> devuelve la opción seleccionada por el usuario.
    while True:
    
        nombre_estaciones = {}
        for i, estacion in enumerate(estaciones.values()):
            nombre_estaciones[i] = estacion["nombre"]
            estacion = menu(nombre_estaciones)
            return estacion

