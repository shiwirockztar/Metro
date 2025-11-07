import stations as st
import system as sys

opcion = ''
# 1. Mostrar mensaje de bienvenida
while True:
    # 2. Mostrar el menú principal de opciones
    # 3. Preguntar al usuario qué opción desea elegir:
    #    a. Consultar estadísticas generales
    #    b. Consultar estadísticas de una estación específica
    #    c. Salir del programa
    
    if opcion == '1':  # Estadísticas generales
        # 4. Mostrar el submenú para estadísticas generales
        #    a. Número total de usuarios y viajes
        #    b. Hora pico
        #    c. Estaciones más usadas
        #    d. Distancia promedio de viaje
        #    e. Ingresos totales
        #    f. Número promedio de viajes
        #    g. Los 5 trayectos más populares
        # 5. Ejecutar la opción seleccionada y mostrar la estadística correspondiente
        pass  # Aquí debes escribir el código para manejar la opción 1
    
    elif opcion == '2':  # Estadísticas por estación
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
