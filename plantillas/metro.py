#estaciones ={"001":["Niquia","6.3337783",""]}
estaciones ={"001":{"nombre":"Niquia", "latitud":"6.3337783","longitud":""}}


#NombreNiquia = estaciones["001"][0]
NombreNiquia = estaciones["001"]["nombre"]


"""def load_stations(path):
    file = open(path,"r")
    info= file.read()

    print(info)"""

def load_stations(path):
    with open(path,"r") as file:
        file.readline() # lee la primera linea y apunta el cursero e la siguiente linea
        estaciones = {}
        for line in file:
            #aux = line[:-1].split(",") # [:-1] para quitar salto de linea
            aux = line.rstrip().split(",") # Funcion para crear una lista de elementos separados por que tienen una coma para este caso
            estaciones[aux[1]] = {"nombre":aux[0],"latitud":aux[2],"longitud":aux[3]}
        print(estaciones)
        return estaciones


def menu(options) :
    while True:
        for k, v in options.items() :
            print(f"{k} )  {v}")
        ele = input("introduzca la opcion")
        if ele in options :
            return ele
    
"""opciones = {"1":"a", "2":"b","3":"c"}
menu(opciones)"""

def menu_estaciones():
    #nombre_estaciones = list(estaciones.values()) # opcion 1

    """l = []
    for estacion in estaciones.values():
        L.append(estacion["nombre"])"""
    
    nombre_estaciones = {}
    for i, estacion in enumerate(estaciones.values()):
        nombre_estaciones[i] = estacion["nombre"]
        estacion = menu(nombre_estaciones)
        return estacion
