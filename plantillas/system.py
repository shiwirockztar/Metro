# Módulo que contiene las funciones relacionadas con la generación de estadísticas generales del sistema metro

from math import *

def geodistance(P1,P2):
    """
    Calcula la distancia entre dos estaciones consecutivas del metro
    de acuerdo a sus coordenadas geográficas
    
    Args:
        P1 (list): Coordenadas (latitud, longitud) del primer punto en grados.
        P2 (list): Coordenadas (latitud, longitud) del segundo punto en grados
	Retorna:
		D (float): Distancia en metros entre los dos puntos.
	
    Ejemplo:
		P1 = [6.2442, -75.5812]
		P2 = [6.2518, -75.5636]
		distancia = geodistance(P1, P2)
    """
    h=1600 # Altura sobre el nivel del mar en metros (aproximada)
    pi = 3.141592
    R = 6371009 # Radio medio de la Tierra en metros
    theta1 = pi/2 - (P1[0]*pi/180) 
    phi1=P1[1]*pi/180
    rho1=R+h
    #Conversion de coordenadas esféricas a cartesianas
    theta2=pi/2 - (P2[0]*pi/180)
    phi2=P2[1]*pi/180
    rho2=R+h
    #Conversion de coordenadas esféricas a cartesianas
    x1=rho1*sin(theta1)*cos(phi1)
    x2=rho2*sin(theta2)*cos(phi2)
    y1=rho1*sin(theta1)*sin(phi1)
    y2=rho2*sin(theta2)*sin(phi2)
    z1=rho1*cos(theta1)
    z2=rho2*cos(theta2)
    #Cálculo de la distancia euclidiana entre los dos puntos
    D=((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**(1/2)
    return D

def contar_salidas_por_usuario(usuarios): 
    # Esta función cuenta el número de salidas de cada usuario.
    # Argumentos:
    # usuarios: Un diccionario con la información de los viajes.
    # Retorna:
    # Un diccionario con el conteo de salidas por usuario.
    salidas = {}
    for user_id, eventos in usuarios.items():
        count = 0
        for evento in eventos:
            if evento["EVENT_TYPE"] == "OUT":
                count += 1
        salidas[user_id] = count  
    return salidas

def contar_salidas(usuarios): 
    # Esta función cuenta el número total de salidas en el sistema.
    # Argumentos:
    # usuarios: Un diccionario con la información de los viajes.
    # Retorna:
    # El número total de salidas.
    total_salidas = 0
    for eventos in usuarios.values():
        for evento in eventos:
            if evento["EVENT_TYPE"] == "OUT":
                total_salidas += 1
    return total_salidas

def hora_pico(usuarios):
    # Esta función determina la hora pico del sistema.
    # Argumentos:
    # usuarios: Un diccionario con la información de los viajes.
    # Retorna:
    # La hora pico (entera) del sistema.
    horas = [0] * 24  # Lista para contar salidas por hora
    for eventos in usuarios.values():
        for evento in eventos:
            hora = int(evento["EVENT_TIME"].split(":")[0])  # Extraer la hora
            horas[hora] += 1  # Incrementar el conteo para esa hora
    hora_pico = horas.index(max(horas))  # Encontrar la hora con más salidas
    return hora_pico

def estaciones_mas_usadas(usuarios, estaciones):
    # Esta función determina las estaciones más usadas en el sistema.
    # Argumentos:
    # usuarios: Un diccionario con la información de los viajes.
    # estaciones: Un diccionario con la información de las estaciones.
    # Retorna:
    # Un diccionario con las estaciones más usadas y su conteo.
    uso_estaciones = {}
    for eventos in usuarios.values():
        for evento in eventos:
            estacion_id = evento["STATION_ID"]
            if estacion_id in uso_estaciones:
                uso_estaciones[estacion_id] += 1
            else:
                uso_estaciones[estacion_id] = 1
    # Convertir IDs a nombres de estaciones {'010': 6, '002': 2, '001': 6, '006': 2}
    uso_estaciones_nombres = {}
    for estacion_id, conteo in uso_estaciones.items():
        # '010': {'nombre': 'Parque Berrio', 'latitud': '6.250490', 'longitud': '-75.568243'},
        nombre_estacion = estaciones.get(estacion_id).get("nombre")
        #nombre_estacion = estaciones.get(estacion_id, {}).get("nombre", "Desconocido")
        uso_estaciones_nombres[nombre_estacion] = conteo
    return uso_estaciones_nombres

def distancia_promedio_viaje(usuarios, estaciones):
    # Esta función calcula la distancia promedio de los viajes en el sistema.
    # Argumentos:
    # usuarios: Un diccionario con la información de los viajes.
    # estaciones: Un diccionario con la información de las estaciones.
    # Retorna:
    # La distancia promedio de los viajes en metros.
    total_distancia = 0
    total_viajes = 0
    for viajes in usuarios.values():
        #'42433478': [{'STATION_ID': '011', 'EVENT_TIME': '04:12', 'EVENT_TYPE': 'IN'}, {'STATION_ID': '012', 'EVENT_TIME': '04:19', 'EVENT_TYPE': 'OUT'}
        #print(viajes)
        if len(viajes) > 1:
            for i in viajes:
                #print(i)
                if(i["EVENT_TYPE"] == "IN"):
                    #print(i) {'STATION_ID': '021', 'EVENT_TIME': '22:53', 'EVENT_TYPE': 'IN'}
                    P1 = [float(estaciones[i["STATION_ID"]]["latitud"]), float(estaciones[i["STATION_ID"]]["longitud"])]
                    P2 = [float(estaciones[viajes[viajes.index(i)+1]["STATION_ID"]]["latitud"]), float(estaciones[viajes[viajes.index(i)+1]["STATION_ID"]]["longitud"])]
                    distancia = geodistance(P1, P2)
                    total_distancia += distancia
                    total_viajes += 1
    if total_viajes == 0:
        return 0
    distancia_promedio = total_distancia / total_viajes
    return distancia_promedio


def contar_entradas(usuarios): 
    # Esta función cuenta el número total de salidas en el sistema.
    # Argumentos:
    # usuarios: Un diccionario con la información de los viajes.
    # Retorna:
    # El número total de entradas.
    total_entradas = 0
    for eventos in usuarios.values():
        for evento in eventos:
            if evento["EVENT_TYPE"] == "IN":
                total_entradas += 1
    return total_entradas


def top_trayectos_populares(usuarios, estaciones):
    # Esta función determina los 5 trayectos más populares en el sistema.
    # Argumentos:
    # usuarios: Un diccionario con la información de los viajes.
    # Retorna:
    # Una lista con los 5 trayectos más populares y su conteo.
    trayectos = {}
    for eventos in usuarios.values():
        #print(eventos) # [{'STATION_ID': '011', 'EVENT_TIME': '22:57', 'EVENT_TYPE': 'IN'}, {'STATION_ID': '012', 'EVENT_TIME': '23:12', 'EVENT_TYPE': 'OUT'}]
        print("\n")
        if len(eventos) > 1 :
            for eve in eventos:
                if eve["EVENT_TYPE"] == "IN" and eventos[eventos.index(eve)+1]["EVENT_TYPE"] == "OUT":
                    origen = eve["STATION_ID"]
                    destino = eventos[eventos.index(eve)+1]["STATION_ID"]
                    #trayecto = (origen, destino)
                    trayecto = (estaciones[origen]["nombre"], estaciones[destino]["nombre"] )
                    if trayecto in trayectos:
                        trayectos[trayecto] += 1
                    else:
                        trayectos[trayecto] = 1
    # Ordenar los trayectos por conteo y obtener los 5 más populares
    top_5_trayectos = sorted(trayectos.items(), key=lambda x: x[1], reverse=True)[:5]
    return top_5_trayectos