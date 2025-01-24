"""
Nombre: Diana Belen Luna Hernández
Fecha:19/11/2024
Descripción: Juego piedra, papel, tijera, lagarto, spock
"""

import random
from datetime import datetime

def determinar_ganador(jugador, computadora):
    # Se delimita su comportamiento
    reglas = {
        "piedra": ["tijera", "lagarto"],
        "papel": ["piedra", "spock"],
        "tijera": ["papel", "lagarto"],
        "lagarto": ["spock", "papel"],
        "spock": ["tijera", "piedra"]
    }

    if jugador == computadora:
        return "Empate"
    elif computadora in reglas[jugador]:
        return "Jugador"
    else:
        return "Computadora"


def main():
    opciones = ["piedra", "papel", "tijera", "lagarto", "spock"]
    print("Juego de Piedra, Papel, Tijera, Lagarto, Spock.")

    continuar = True

    # Variables para guardar resultados
    victorias_jugador = 0
    victorias_computadora = 0
    empates = 0
    rondas = []  # Lista para registrar cada ronda
    numero_ronda = 1  # Contador de rondas

    while continuar:
        jugador = input("Elige tu opción (piedra, papel, tijera, lagarto, spock): ").lower()

        # Validación para asegurar que la opción ingresada sea válida
        if jugador not in opciones:
            print("Opción no válida. Por favor elige entre piedra, papel, tijera, lagarto, o spock.")
            continue  # Salta esta ronda y vuelve a preguntar

        computadora = random.choice(opciones)
        print(f"La computadora eligió: {computadora}")

        # Determina el ganador del juego actual
        resultado = determinar_ganador(jugador, computadora)
        if resultado == "Empate":
            print("Es un empate")
            empates += 1
        elif resultado == "Jugador":
            print("¡Ganaste esta ronda!")
            victorias_jugador += 1
        else:
            print("La computadora ganó esta ronda")
            victorias_computadora += 1

        # Guardar los detalles de la ronda con el número de ronda
        rondas.append(
            f"Ronda {numero_ronda}:\n  Jugador eligió: {jugador.capitalize()}\n  Computadora eligió: {computadora.capitalize()}\n  Resultado: {resultado}\n"
        )
        numero_ronda += 1  # Incrementar el número de ronda

        # Pregunta si el jugador quiere jugar otra vez
        seguir = input("\n¿Quieres jugar otra vez? (s/n): ")
        if seguir.lower() != "s":
            print("Gracias por jugar")

            # Obtener la fecha y hora actual
            fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Intentar escribir los resultados en un archivo
            try:
                with open("piedra_papel_tijera_archivos.txt", "w", encoding="utf-8") as archivo:
                    archivo.write("Resultados del juego Piedra, Papel, Tijera, Lagarto, Spock:\n")
                    archivo.write(f"Fecha y hora: {fecha_actual}\n\n")
                    archivo.write(f"Victorias del jugador: {victorias_jugador}\n")
                    archivo.write(f"Victorias de la computadora: {victorias_computadora}\n")
                    archivo.write(f"Empates: {empates}\n\n")
                    archivo.write("Detalle de las rondas:\n")
                    for detalle in rondas:
                        archivo.write(f"{detalle}\n")
                print("Los resultados han sido guardados en 'piedra_papel_tijera_archivos.txt'.")
            except Exception as e:
                print(f"Error al guardar los resultados: {e}")
            break  # Sale del bucle

main()
