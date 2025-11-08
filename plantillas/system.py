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