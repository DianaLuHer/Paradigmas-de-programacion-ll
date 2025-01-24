"""
Nombre: Diana Belen Luna Hernández.
"""

import random
from datetime import datetime

# Genera un número aleatorio entre 1 y 100 que el jugador debe adivinar
numero_adivinar = random.randint(1, 100)
intentos_maximos = 5  # Número máximo de intentos permitidos
intentos_realizados = []  # Lista para almacenar las adivinanzas del jugador

print("------------- Adivina el número -------------")  # Mensaje de bienvenida
print("Debes adivinar el número entre 1 y 100.")  # Instrucciones del juego
print(f"Tienes {intentos_maximos} intentos.")  # Indica la cantidad de intentos

# Variable para rastrear si el jugador ganó
gano = False

# Bucle que permite al jugador hacer hasta 'intentos_maximos'
for intento in range(1, intentos_maximos + 1):
    # Solicita al jugador que ingrese su número
    adivinanza = input(f"Intento {intento}: Ingresa tu número: ")

    # Solicita la adivinanza e intentar convertirla a un número
    try:
        adivinanza = int(adivinanza)  # Intenta convertir la entrada a un número entero
        intentos_realizados.append(adivinanza)  # Registra el intento actual
    except ValueError:
        print("Por favor, ingresa un número válido.")  # Si ocurre un error, indica que la entrada no es un número

        # Comprueba si el número es correcto
        if adivinanza == numero_adivinar:
            print(f"¡Felicidades! Adivinaste el número en el intento {intento}.")  # Mensaje de éxito
            gano = True  # Cambia el estado a ganado
            break  # Salir del bucle si el jugador adivina correctamente
        elif adivinanza < numero_adivinar:
            print("El número a adivinar es mayor.")  # Indica que el número es menor
        else:
            print("El número a adivinar es menor.")  # Indica que el número es mayor
    else:
        print("Por favor, ingresa un número válido.")  # Mensaje de error si la entrada no es un número

# Mensaje final si el jugador no adivina el número en el número de intentos permitidos
if not gano:  # Solo si no ganó, mostramos este mensaje
    print(f"PERDISTE. El número a adivinar era {numero_adivinar}.")  # Mensaje de derrota

# Mostrar el resumen del juego
resumen = "\n------------- Resumen del juego -------------\n"
for i, intento in enumerate(intentos_realizados, start=1):
    resumen += f"Intento {i}: {intento}\n"
resumen += f"Número total de intentos realizados: {len(intentos_realizados)}\n"
resumen += f"Resultado del juego: {'Ganaste' if gano else 'Perdiste'}\n"

# Imprimir el resumen en consola
print(resumen)

# Guarda el resumen en un archivo de texto
fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
try:
    with open("resultado_adivinanza.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"Fecha y hora: {fecha_actual}\n")
        archivo.write(resumen)
        archivo.write("\n")
except Exception as e:
    print(f"Error al escribir en el archivo: {e}")
