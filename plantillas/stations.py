# Módulo que contiene las funciones relacionadas con la generación de estadísticas para una estación específica

"""def estacion_seleccionada(estaciones):
    opciones = {str(i+1): est['nombre'] for i, est in enumerate(estaciones)}
    return mt.menu(opciones)"""

def listar_estaciones(estaciones):
    # Esta función retorna la lista de estaciones.
    # Argumentos:
    # options: Un diccionario donde las claves son las opciones del menú y los valores son las descripciones de las opciones.
    # Retorna:
    # La opción seleccionada por el usuario.
    
    # Ejemplo de uso:
    # opciones = {"1":"a", "2":"b","3":"c"}
    # menu(opciones) -> devuelve la opción seleccionada por el usuario.
    while True:
        #print(estaciones)
        nombre_estaciones = {}
        for key, estacion in estaciones.items():
            nombre_estaciones[key] = estacion["nombre"]
        return nombre_estaciones


def total_viajes_estacion(usuarios, estacion_seleccionada):
    # Esta función calcula el total de viajes en una estación específica.
    # Argumentos:
    # usuarios: Un diccionario con los registros de viajes de los usuarios.
    # estaciones: Un diccionario con la información de las estaciones.
    # estacion_seleccionada: La estación para la cual se desea calcular el total de viajes.
    # Retorna:
    # El total de viajes en la estación seleccionada.
    
    total_viajes = 0
    #nombre_estacion = estaciones[estacion_seleccionada]["nombre"]
    
    #print(usuarios)  # DEBUG
    #print(estacion_seleccionada)  # DEBUG
    #print(estaciones)  # DEBUG
    #print(nombre_estacion)
    for usuario in usuarios.values():
        for viaje in usuario:
                if viaje["EVENT_TYPE"] == "OUT" and viaje["STATION_ID"] == estacion_seleccionada:
                    total_viajes += 1
    return total_viajes

def hora_pico_estacion(usuarios, estacion_seleccionada):
    # Esta función determina la hora pico de una estación específica.
    # Argumentos:
    # usuarios: Un diccionario con los registros de viajes de los usuarios.
    # estaciones: Un diccionario con la información de las estaciones.
    # estacion_seleccionada: La estación para la cual se desea determinar la hora pico.
    # Retorna:
    # La hora pico de la estación seleccionada.
    
    horas = [0] * 24  # Lista para contar salidas por hora
    for usuario in usuarios.values():
        for viaje in usuario:
            if (viaje["EVENT_TYPE"] == "OUT" or viaje["EVENT_TYPE"] == "IN") and viaje["STATION_ID"] == estacion_seleccionada:
                hora = int(viaje["EVENT_TIME"].split(":")[0])  # Extraer la hora
                horas[hora] += 1  # Incrementar el conteo para esa hora
    hora_pico = horas.index(max(horas))  # Encontrar la hora con más salidas
    return hora_pico