"""
Nombre: Diana Belen Luna Hernández.
Fecha: 29/10/2024
Descripción: Este programa es el juego "piedra, papel o tijera", el contrincante será el CPU.
"""

import random  # Importar el módulo random para generar elecciones aleatorias

print("----------- Piedra, papel o tijera -----------")

# Contadores de victorias y empates
victorias_jug = 0  # Contador de victorias del jugador
victorias_cpu = 0  # Contador de victorias de la CPU
empates = 0        # Contador de empates

continuar = True  # Variable de control para el bucle principal

while continuar:
    # Mostrar el menú de opciones
    print("----------------------------")
    print("--  1. Piedra             --")
    print("--  2. Papel              --")
    print("--  3. Tijera             --")
    print("--  4. Salir              --")
    print("----------------------------")

    # Solicitar la opción del jugador
    opcion = int(input("Elige una opción: "))
    eleccion_CPU = random.randint(1, 3)  # CPU elige aleatoriamente entre 1 y 3

    # Evaluar la opción seleccionada por el jugador
    if opcion == 1:  # Si el jugador elige Piedra
        print("Tú eliges: Piedra")
        if eleccion_CPU == 1:  # La CPU también elige Piedra
            print("La CPU elige: Piedra")
            print("¡Es un empate!")  # Empate
            empates += 1
        elif eleccion_CPU == 2:  # La CPU elige Papel
            print("La CPU elige: Papel")
            print("La CPU gana esta ronda.")  # La CPU gana
            victorias_cpu += 1
        else:  # La CPU elige Tijera
            print("La CPU elige: Tijera")
            print("¡Ganaste esta ronda!")  # El jugador gana
            victorias_jug += 1

    elif opcion == 2:  # Si el jugador elige Papel
        print("Tú eliges: Papel")
        if eleccion_CPU == 1:  # La CPU elige Piedra
            print("La CPU elige: Piedra")
            print("¡Ganaste esta ronda!")  # El jugador gana
            victorias_jug += 1
        elif eleccion_CPU == 2:  # La CPU elige Papel
            print("La CPU elige: Papel")
            print("¡Es un empate!")  # Empate
            empates += 1
        else:  # La CPU elige Tijera
            print("La CPU elige: Tijera")
            print("La CPU gana esta ronda.")  # La CPU gana
            victorias_cpu += 1

    elif opcion == 3:  # Si el jugador elige Tijera
        print("Tú eliges: Tijera")
        if eleccion_CPU == 1:  # La CPU elige Piedra
            print("La CPU elige: Piedra")
            print("La CPU gana esta ronda.")  # La CPU gana
            victorias_cpu += 1
        elif eleccion_CPU == 2:  # La CPU elige Papel
            print("La CPU elige: Papel")
            print("¡Ganaste esta ronda!")  # El jugador gana
            victorias_jug += 1
        else:  # La CPU elige Tijera
            print("La CPU elige: Tijera")
            print("¡Es un empate!")  # Empate
            empates += 1

    elif opcion == 4:  # Si el jugador elige Salir
        print("Gracias por jugar!")  # Mensaje de despedida
        continuar = False  # Cambiar la variable de control a False para salir del bucle

    else:  # Opción no válida
        print("Opción no válida, intenta de nuevo.")  # Mensaje de error

    # Mostrar marcador actual después de cada ronda, si el juego continúa
    if continuar:
        print("\nMarcador:")
        print(f"Victorias del Jugador: {victorias_jug}")  # Mostrar victorias del jugador
        print(f"Victorias de la CPU: {victorias_cpu}")  # Mostrar victorias de la CPU
        print(f"Empates: {empates}")  # Mostrar empates
