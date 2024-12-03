"""
Nombre: Diana Belen Luna Hernández
Fecha:
Descripción: Juego de Piedra, Papel o Tijera con diccionario.
"""

import random

"""
Un diccionario es una estructurade datos que almacena pares de clave-valor. Es similar a un diccionario físico, 
donde una palabra (clave) tiene una definición asociada (valor).
"""


# Función para determinar el ganador
def determinar_ganador(jugador, computadora):
    # Diccionario que define qué opción gana contra cuál.
    reglas = {"piedra": "tijera", "papel": "piedra", "tijera": "papel"}

    # Si el jugador y la computadora eligen lo mismo, es un empate.
    if jugador == computadora:
        return "Empate"
    # Si la elección del jugador gana según las reglas, el jugador es el ganador.
    elif reglas[jugador] == computadora:
        return "Jugador"
    # En cualquier otro caso, la computadora gana.
    else:
        return "Computadora"


def main():
    # Lista de opciones posibles para el juego.
    opciones = ["piedra", "papel", "tijera"]
    print("Juego de Piedra, Papel o Tijera.")

    continuar = True  # Variable para controlar el bucle del juego.

    while continuar:  # Bucle para jugar varias veces.
        # Solicita al jugador que elija una opción.
        jugador = input("Elige tu opción (piedra, papel, tijera): ")

        # La computadora elige aleatoriamente una opción.
        computadora = random.choice(opciones)
        print(f"La computadora eligió: {computadora}")  # Muestra la elección de la computadora.

        # Determina el ganador del juego actual.
        resultado = determinar_ganador(jugador, computadora)
        if resultado == "Empate":  # Si hay empate, lo indica.
            print("Es un empate")
        else:  # Si no es empate, muestra quién ganó.
            print(f"{resultado} ganó")

        # Pregunta si el jugador quiere jugar otra vez.
        seguir = input("\n¿Quieres jugar otra vez? (s/n): ")
        if seguir != "s":  # Si la respuesta no es 's', termina el juego.
            print("Gracias por jugar")
            break  # Sale del bucle.

main()
