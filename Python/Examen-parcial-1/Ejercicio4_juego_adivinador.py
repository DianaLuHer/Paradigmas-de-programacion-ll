"""
Nombre: Diana Belen Luna Hernández
Fecha: 29/10/2024
Descripción: Este programa es un juego de adivinanza en el que el jugador tiene que adivinar un número secreto generado aleatoriamente entre 1 y 100.
El jugador tiene un número limitado de intentos para hacerlo.
"""

import random  # Importar el módulo random para generar números aleatorios

# Genera un número aleatorio entre 1 y 100 que el jugador debe adivinar
numero_adivinar = random.randint(1, 100)
intentos = 5  # Número máximo de intentos permitidos

print("------------- Adivina el número -------------")  # Mensaje de bienvenida
print("Debes adivinar el número entre 1 y 100.")  # Instrucciones del juego
print(f"Tienes {intentos} intentos.")  # Indicar la cantidad de intentos

# Bucle que permite al jugador hacer hasta 'intentos' intentos
for intento in range(1, intentos + 1):
    # Solicita al jugador que ingrese su número
    adivinanza = int(input(f"Intento {intento}: Ingresa tu número: "))

    # Comprobar si el número es correcta
    if adivinanza == numero_adivinar:
        print(f"¡Felicidades! Adivinaste el número en el intento {intento}.")  # Mensaje de éxito
        break  # Salir del bucle si el jugador adivina correctamente
    elif adivinanza < numero_adivinar:
        print("El número a adivinar es mayor.")  # Indicar que el número es menor
    else:
        print("El número a adivinar es menor.")  # Indicar que el número es mayor

# Mensaje final si el jugador no adivina el número en el número de intentos permitidos
if adivinanza != numero_adivinar:
    print(f"PERDISTE. El número a adivinar era {numero_adivinar}.")  # Mensaje de derrota
