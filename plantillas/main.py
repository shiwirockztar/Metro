# Implemente aquí los menús y el programa principal que invoca las funciones de los otros módulos

# from metro import load_stations, menu_estaciones #incluyo metro.py # si solo voy a usar esas dos funciones
import metro as mt
import stations as st
import system as sys
import time

estaciones = mt.load_stations('stations.info') # Cargar las estaciones desde el archivo
#usuarios = mt.load_metro_log('metro.log') # Cargar los registros de viajes desde el archivo
usuarios = mt.load_metro_log('prueba.log') # Cargar los registros de viajes desde el archivo

print("Bienvenido al sistema de estadísticas del metro") # 1. Mostrar mensaje de bienvenida

while True:
    print("\033[39m")  # Secuencia de escape ANSI para restablecer el color del texto
        
    # 2. Mostrar el menú principal de opciones
    opciones = {"1":"Consultar estadísticas generales", "2":"Consultar estadísticas de una estación específica", "3":"Salir del programa"}
    # 3. Preguntar al usuario qué opción desea elegir:
    opcion = mt.menu(opciones)

    #lista_estaciones = mt.menu(estaciones)
    # 001 )  {'nombre': 'Niquía', 'latitud': '6.337783', 'longitud': '-75.544365'}
    # 002 )  {'nombre': 'Bello', 'latitud': '6.330476', 'longitud': '-75.553434'}    
    
    if opcion == '1':  # Estadísticas generales
        time.sleep(0.5)  # Pausa de 0.5 segundos antes de limpiar la pantalla
        print("\033[2J")  # Secuencia de escape ANSI para limpiar la pantalla
        print("\033[36m")  # Secuencia de escape ANSI para restablecer el color del texto
        # 4. Mostrar el submenú para estadísticas generales
        opciones_generales = {
            "a":"Número total de usuarios y viajes", #    a. Número total de usuarios y viajes
            "b":"Hora pico", #    b. Hora pico
            "c":"Estaciones más usadas", #    c. Estaciones más usadas
            "d":"Distancia promedio de viaje", #    d. Distancia promedio de viaje
            "e":"Ingresos totales", #    e. Ingresos totales
            "f":"Número promedio de viajes", #    f. Número promedio de viajes
            "g":"Los 5 trayectos más populares", #    g. Los 5 trayectos más populares
            "h":"Volver al menú principal"
        }
        
        # 5. Ejecutar la opción seleccionada y mostrar la estadística correspondiente
        opcion_general = mt.menu(opciones_generales)
        
        if opcion_general == 'a':
            time.sleep(1)  # Pausa de 1 segundos antes de limpiar la pantalla
            print("\033[2J")  # Secuencia de escape ANSI para limpiar la pantalla
            print("\033[32m")  # color morado
            print("Ha seleccionado la opción a: Número total de usuarios y viajes")
            print(f"Total de usuarios: {len(usuarios)} y total de viajes: {sys.contar_salidas(usuarios)}")
            pass  # Aquí debes escribir el código para manejar la opción 1
        
        if opcion_general == 'b':
            time.sleep(1)  # Pausa de 1 segundos antes de limpiar la pantalla
            print("\033[2J")  # Secuencia de escape ANSI para limpiar la pantalla
            print("\033[32m")  # color verde
            print("Ha seleccionado la opción b: Hora pico")
            hora_pico = sys.hora_pico(usuarios)
            print(f"La hora pico es a las {hora_pico}:00 horas")
            pass  # Aquí debes escribir el código para manejar la opción 2
        
        if opcion_general == 'c':
            time.sleep(1)  # Pausa de 1 segundos antes de limpiar la pantalla
            print("\033[2J")  # Secuencia de escape ANSI para limpiar la pantalla
            print("\033[32m")  # color verde
            print("Ha seleccionado la opción c: Estaciones más usadas")
            estaciones_mas_usadas = sys.estaciones_mas_usadas(usuarios, estaciones) # {'Parque Berrio': 6, 'Bello': 2, 'Niquía': 6, 'Caribe': 2}
            
            print("Las estaciones más usadas son:")
            for estacion, usos in estaciones_mas_usadas.items():
                print(f"- {estacion}: {usos} usos")
            pass  # Aquí debes escribir el código para manejar la opción 3
        
        if opcion_general == 'd':
            time.sleep(1)  # Pausa de 1 segundos antes de limpiar la pantalla
            print("\033[2J")  # Secuencia de escape ANSI para limpiar la pantalla
            print("\033[32m")  # color verde
            print("Ha seleccionado la opción d: Distancia promedio de viaje")
            distancia_promedio = sys.distancia_promedio_viaje(usuarios, estaciones)
            print(f"La distancia promedio de viaje es de {distancia_promedio:.2f} metros")
            pass  # Aquí debes escribir el código para manejar la opción 4

        if opcion_general == 'e':
            time.sleep(1)  # Pausa de 1 segundos antes de limpiar la pantalla
            print("\033[2J")  # Secuencia de escape ANSI para limpiar la pantalla
            print("\033[32m")  # color verde
            print("Ha seleccionado la opción e: Ingresos totales")
            # Aquí debes escribir el código para manejar la opción 5
            pass
        
        if opcion_general == 'h':  # Volver al menú principal
            continue
        pass  

    elif opcion == '2':  # Estadísticas por estación

        time.sleep(1)  # Pausa de 1 segundos antes de limpiar la pantalla
        print("\033[2J")  # Secuencia de escape ANSI para limpiar la pantalla
        print("\033[36m")  # Secuencia de escape ANSI para restablecer el color del texto
        
        # Aquí va la sangría correspondiente
        # 6. Mostrar el submenú para estadísticas de estación
        #    a. Total de viajes en la estación
        #    b. Horas pico de ingreso y salida
        #    c. Estaciones de origen y destino más comunes
        #    d. Cantidad de usuarios que ingresaron por hora
        #    e. Cantidad de usuarios que salieron por hora
        # 7. Ejecutar la opción seleccionada y mostrar la estadística correspondiente
        pass  # Aquí debes escribir el código para manejar la opción 2

    elif opcion == '3':  # Salir del programa
        # 8. Mostrar mensaje de despedida
        break  # Salir del bucle principal y terminar el programa

    else:
        # 9. Si la opción no es válida, pedir al usuario que ingrese una opción válida
        print("Opción no válida. Por favor, elija una opción correcta.")
        
# 10. Función para consultar estadísticas generales
def mostrar_estadisticas_generales(opcion):
    # 11. Dependiendo de la opción seleccionada, mostrar las estadísticas generales
    #     a. Número total de usuarios y viajes
    #     b. Hora pico
    #     c. Estaciones más usadas
    #     d. Distancia promedio de viaje
    #     e. Ingresos totales
    #     f. Número promedio de viajes
    #     g. Los 5 trayectos más populares
    pass  # Implementar lógica de estadísticas generales

# 12. Función para consultar estadísticas de una estación específica
def mostrar_estadisticas_estacion(id_estacion):
    # 13. Dependiendo de la estación seleccionada, mostrar las estadísticas
    #     a. Total de viajes en la estación
    #     b. Horas pico de ingreso y salida
    #     c. Estaciones de origen y destino más comunes
    #     d. Cantidad de usuarios que ingresaron por hora
    #     e. Cantidad de usuarios que salieron por hora
    pass  # Implementar lógica de estadísticas para una estación
