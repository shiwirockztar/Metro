# Implemente aquí los menús y el programa principal que invoca las funciones de los otros módulos

# from metro import load_stations, menu_estaciones #incluyo metro.py # si solo voy a usar esas dos funciones
import metro as mt
import stations as st
import system as sys
import time

estaciones = mt.load_stations('stations.info') # Cargar las estaciones desde el archivo
usuarios = mt.load_metro_log('metro.log') # Cargar los registros de viajes desde el archivo
print("Bienvenido al sistema de estadísticas del metro") # 1. Mostrar mensaje de bienvenida

while True:
    print("\033[39m")  # Secuencia de escape ANSI para restablecer el color del texto
        
    # 2. Mostrar el menú principal de opciones
    opciones = {"1":"Consultar estadísticas generales", "2":"Consultar estadísticas de una estación específica", "3":"Salir del programa"}
    # 3. Preguntar al usuario qué opción desea elegir:
    opcion = mt.menu(opciones)
    
    if opcion == '1':  # Estadísticas generales
        time.sleep(0.5)  # Pausa de 0.5 segundos antes de limpiar la pantalla
        mt.limpiar_pantalla()
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
            mt.limpiar_pantalla()
            print("\033[32m")  # color morado
            print("Ha seleccionado la opción a: Número total de usuarios y viajes")
            print(f"Total de usuarios: {len(usuarios)} y total de viajes: {sys.contar_salidas(usuarios)}")
            pass  # Aquí debes escribir el código para manejar la opción 1
        
        if opcion_general == 'b':
            time.sleep(1)  # Pausa de 1 segundos antes de limpiar la pantalla
            mt.limpiar_pantalla()
            print("\033[32m")  # color verde
            print("Ha seleccionado la opción b: Hora pico")
            hora_pico = sys.hora_pico(usuarios)
            print(f"La hora pico es a las {hora_pico}:00 horas")
            pass  # Aquí debes escribir el código para manejar la opción 2
        
        if opcion_general == 'c':
            time.sleep(1)  # Pausa de 1 segundos antes de limpiar la pantalla
            mt.limpiar_pantalla()
            print("\033[32m")  # color verde
            print("Ha seleccionado la opción c: Estaciones más usadas")
            estaciones_mas_usadas = sys.estaciones_mas_usadas(usuarios, estaciones) # {'Parque Berrio': 6, 'Bello': 2, 'Niquía': 6, 'Caribe': 2}
            
            print("Las estaciones más usadas son:")
            for estacion, usos in estaciones_mas_usadas.items():
                print(f"- {estacion}: {usos} usos")
            pass  # Aquí debes escribir el código para manejar la opción 3
        
        if opcion_general == 'd':
            time.sleep(1)  # Pausa de 1 segundos antes de limpiar la pantalla
            mt.limpiar_pantalla()
            print("\033[32m")  # color verde
            print("Ha seleccionado la opción d: Distancia promedio de viaje")
            distancia_promedio = sys.distancia_promedio_viaje(usuarios, estaciones)
            print(f"La distancia promedio de viaje es de {distancia_promedio:.2f} metros")
            pass  # Aquí debes escribir el código para manejar la opción 4

        if opcion_general == 'e':
            time.sleep(1)  # Pausa de 1 segundos antes de limpiar la pantalla
            mt.limpiar_pantalla()
            print("\033[32m")  # color verde
            print("Ha seleccionado la opción e: Ingresos totales")
            print(f"Total de entradas: {sys.contar_entradas(usuarios)}")
            # Aquí debes escribir el código para manejar la opción 5
            pass

        if opcion_general == 'f':
            time.sleep(1)  # Pausa de 1 segundos antes de limpiar la pantalla
            mt.limpiar_pantalla()
            print("\033[32m")  # color verde
            print("Ha seleccionado la opción f: Número promedio de viajes")
            promedio_viajes = sys.contar_salidas(usuarios)/len(usuarios)
            print(f"El número promedio de viajes es de {promedio_viajes:.2f}")
            pass  # Aquí debes escribir el código para manejar la opción 6

        if opcion_general == 'g':
            time.sleep(1)  # Pausa de 1 segundos antes de limpiar la pantalla
            mt.limpiar_pantalla()
            print("\033[32m")  # color verde
            print("Ha seleccionado la opción g: Los 5 trayectos más populares")
            top_trayectos = sys.top_trayectos_populares(usuarios, estaciones)
            print("Los 5 trayectos más populares son:")
            for (origen, destino), conteo in top_trayectos:
                print(f"- {origen} -> {destino}: {conteo} viajes")
            # Aquí debes escribir el código para manejar la opción 7
            pass

        if opcion_general == 'h':  # Volver al menú principal
            continue
        pass  

    elif opcion == '2':  # Estadísticas por estación

        time.sleep(1)  # Pausa de 1 segundos antes de limpiar la pantalla
        mt.limpiar_pantalla()
        print("\033[36m")  # Secuencia de escape ANSI para restablecer el color del texto
        print("Ha seleccionado la opción 2: Consultar estadísticas de una estación específica")
        # 5. Mostrar el menú de estaciones y permitir al usuario seleccionar una estación
        print("Seleccione una estación:")
        lista_estaciones = st.listar_estaciones(estaciones)
        estacion_seleccionada = mt.menu(lista_estaciones)
        mt.limpiar_pantalla()

        # 6. Mostrar el submenú para estadísticas de estación
        print(f"Estadísticas para la estación: {lista_estaciones[estacion_seleccionada]}")
        opciones_estacion = {"a": "Total de viajes en la estación",
                             "b": "Horas pico de ingreso y salida",
                             "c": "Estaciones de origen y destino más comunes",
                             "d": "Cantidad de usuarios que ingresaron por hora",
                             "e": "Cantidad de usuarios que salieron por hora",
                             "f": "Volver al menú principal"
                    }
        opcion_estacion = mt.menu(opciones_estacion)

        # 7. Ejecutar la opción seleccionada y mostrar la estadística correspondiente
        if opcion_estacion == 'a':
            time.sleep(1)  # Pausa de 1 segundos antes de limpiar la pantalla
            mt.limpiar_pantalla()
            print("\033[32m")  # color morado
            print("Ha seleccionado la opción a: Total de viajes en la estación", lista_estaciones[estacion_seleccionada])
            total_viajes = st.total_viajes_estacion(usuarios, estacion_seleccionada)
            print(f'Total de viajes en la estación seleccionada: {total_viajes}')
            pass  # Aquí debes escribir el código para manejar la opción 1

        if opcion_estacion == 'b':
            time.sleep(1)  # Pausa de 1 segundos antes de limpiar la pantalla
            mt.limpiar_pantalla()
            print("\033[32m")  # color verde
            print("Ha seleccionado la opción b: Horas pico de ingreso y salida")
            hora_pico = st.hora_pico_estacion(usuarios, estacion_seleccionada)
            print(f'La hora pico de la estación seleccionada es: {hora_pico}:00 horas')
            pass  # Aquí debes escribir el código para manejar la opción 2

        if opcion_estacion == 'c':
            time.sleep(1)  # Pausa de 1 segundos antes de limpiar la pantalla
            mt.limpiar_pantalla()
            print("\033[32m")  # color verde
            print("Ha seleccionado la opción c: Estaciones de origen y destino más comunes")
            estaciones_origen = st.estaciones_origen(usuarios, estacion_seleccionada)
            print(f'La estación origen más común de la estación seleccionada es: {estaciones[estaciones_origen]["nombre"]}')
            estaciones_destino = st.estaciones_destino(usuarios, estacion_seleccionada)
            print(f'La estación destino más común de la estación seleccionada es: {estaciones[estaciones_destino]["nombre"]}')  
            pass  # Aquí debes escribir el código para manejar la opción 2

        if opcion_estacion == 'd':
            time.sleep(1)  # Pausa de 1 segundos antes de limpiar la pantalla
            mt.limpiar_pantalla()
            print("\033[32m")  # color verde
            print("Ha seleccionado la opción d: Cantidad de usuarios que ingresaron por hora")
            usuarios_hora = st.numero_usuarios_Ingreso_hora(usuarios, estacion_seleccionada)
            for hora, conteo in enumerate(usuarios_hora):
                print(f'Hora: {hora}:00 - Número de usuarios que ingresaron: {conteo}')
            pass  # Aquí debes escribir el código para manejar la opción 2

        if opcion_estacion == 'e':
            time.sleep(1)  # Pausa de 1 segundos antes de limpiar la pantalla
            mt.limpiar_pantalla()
            print("\033[32m")  # color verde
            print("Ha seleccionado la opción e: Cantidad de usuarios que salieron por hora")
            usuarios_hora_salida = st.numero_usuarios_Salida_hora(usuarios, estacion_seleccionada)
            for hora, conteo in enumerate(usuarios_hora_salida):
                print(f'Hora: {hora}:00 - Número de usuarios que salieron: {conteo}')
            pass  # Aquí debes escribir el código para manejar la opción 2

        if opcion_estacion == 'f':  # Volver al menú principal
            continue
        
        pass  # Aquí debes escribir el código para manejar la opción 2

    elif opcion == '3':  # Salir del programa
        # 8. Mostrar mensaje de despedida
        break  # Salir del bucle principal y terminar el programa

    else:
        # 9. Si la opción no es válida, pedir al usuario que ingrese una opción válida
        print("Opción no válida. Por favor, elija una opción correcta.")
        


