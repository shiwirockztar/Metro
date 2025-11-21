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

def estaciones_destino(usuarios, estacion_seleccionada):
    # Esta función determina las estaciones más comunes relacionadas con una estación específica.
    # Argumentos:
    # usuarios: Un diccionario con los registros de viajes de los usuarios.
    # estacion_seleccionada: La estación para la cual se desea determinar las estaciones comunes.
    # Retorna:
    # Un diccionario con las estaciones más comunes y su conteo.
    
    salidas = {}
    for estaciones in usuarios.values():
        #estaciones:  linea por linea [{'STATION_ID': '010', 'EVENT_TIME': '04:03', 'EVENT_TYPE': 'IN'}]
        if len(estaciones) > 1:
            for evento in estaciones:
                if evento["STATION_ID"] == estacion_seleccionada:
                    indice = estaciones.index(evento)
                    if evento["EVENT_TYPE"] == "IN":
                        id_estacion = estaciones[indice+1]["STATION_ID"]   # obtengo el id de la siguiente estación
                        if id_estacion in salidas:
                            salidas[id_estacion] += 1
                        else:
                            salidas[id_estacion] = 1
    # Salidas: {'002': 3, '019': 5, '004': 2, '011': 6, '013': 2, '008': 1, '010': 4, '014': 3, '017': 1, '001': 2, '007': 1, '003': 2, '018': 3, '006': 1, '015': 1}             
    destino_comun = max(salidas, key=salidas.get)
    return destino_comun

def estaciones_origen(usuarios, estacion_seleccionada):
    # Esta función determina las estaciones más comunes relacionadas con una estación específica.
    # Argumentos:
    # usuarios: Un diccionario con los registros de viajes de los usuarios.
    # estacion_seleccionada: La estación para la cual se desea determinar las estaciones comunes.
    # Retorna:
    # Un diccionario con las estaciones más comunes y su conteo.
    
    entradas = {}
    for estaciones in usuarios.values():
        #estaciones:  linea por linea [{'STATION_ID': '010', 'EVENT_TIME': '04:03', 'EVENT_TYPE': 'IN'}]
        if len(estaciones) > 1:
            for evento in estaciones:
                if evento["STATION_ID"] == estacion_seleccionada:
                    indice = estaciones.index(evento)
                    if evento["EVENT_TYPE"] == "OUT":
                        id_estacion = estaciones[indice-1]["STATION_ID"]   # obtengo el id de la siguiente estación
                        if id_estacion in entradas:
                            entradas[id_estacion] += 1
                        else:
                            entradas[id_estacion] = 1
                   
    # entradas: {'002': 3, '019': 5, '004': 2, '011': 6, '013': 2, '008': 1, '010': 4, '014': 3, '017': 1, '001': 2, '007': 1, '003': 2, '018': 3, '006': 1, '015': 1}
    origen_comun = max(entradas, key=entradas.get)
    return origen_comun

def numero_usuarios_Ingreso_hora(usuarios, estacion_seleccionada):
    # esta funcion calcula el numero de usuarios que ingresan cada hora en una estacion especifica
    # Argumentos:
    # usuarios: Un diccionario con los registros de viajes de los usuarios.
    # estacion_seleccionada: La estación para la cual se desea calcular el número de usuarios por hora.
    # Retorna:
    # Un diccionario con el número de usuarios que ingresan por hora.       
    horas = [0] * 24  # Lista para contar ingresos por hora
    for eventos in usuarios.values():
        for evento in eventos:
            hora = int(evento["EVENT_TIME"].split(":")[0])  # Extraer la hora
            if evento["EVENT_TYPE"] == "IN" and evento["STATION_ID"] == estacion_seleccionada:
                horas[hora] += 1  # Incrementar el conteo para esa hora
    return horas    

def numero_usuarios_Salida_hora(usuarios, estacion_seleccionada):
    # esta funcion calcula el numero de usuarios que salen cada hora en una estacion especifica
    # Argumentos:
    # usuarios: Un diccionario con los registros de viajes de los usuarios.
    # estacion_seleccionada: La estación para la cual se desea calcular el número de usuarios por hora.
    # Retorna:
    # Un diccionario con el número de usuarios que salen por hora.       
    horas = [0] * 24  # Lista para contar salidas por hora
    for eventos in usuarios.values():
        for evento in eventos:
            hora = int(evento["EVENT_TIME"].split(":")[0])  # Extraer la hora
            if evento["EVENT_TYPE"] == "OUT" and evento["STATION_ID"] == estacion_seleccionada:
                horas[hora] += 1  # Incrementar el conteo para esa hora
    return horas