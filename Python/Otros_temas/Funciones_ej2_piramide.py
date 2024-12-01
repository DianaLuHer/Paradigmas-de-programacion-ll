"""
Nombre: Diana Belen Luna Hernández
Fecha: 07/11/2024
Descripción: Este programa genera diferentes patrones, variando según el número de filas ingresado.
"""

# Función para generar un triángulo rectángulo invertido (alineado a la derecha)
def triangulo_rectangulo_invertido(filas, asterisco="*", espacio=" "):
    for i in range(filas + 1):
        asteriscos = asterisco * i
        espacios = espacio * (filas - i)
        print(f"{espacios}{asteriscos}")
    print("")  # Salto de línea

# Función para generar un triángulo rectángulo normal (alineado a la izquierda)
def triangulo_rectangulo_normal(filas, asterisco="*", espacio=" "):
    for i in range(filas + 1):
        asteriscos = asterisco * i
        print(f"{asteriscos}")
    print("")  # Salto de línea

# Función para generar una pirámide completa
def piramide_completa(filas, asterisco="*", espacio=" "):
    for i in range(1, filas + 1):
        asteriscos = asterisco * (2 * i - 1)
        espacios = espacio * (filas - i)
        print(f"{espacios}{asteriscos}{espacios}")
    print("")  # Salto de línea

# Función para generar un triángulo rectángulo invertido al revés
def triangulo_invertido_reves(filas, asterisco="*", espacio=" "):
    for i in range(filas, 0, -1):
        asteriscos = asterisco * i
        espacios = espacio * (filas - i)
        print(f"{espacios}{asteriscos}")
    print("")  # Salto de línea

# Función para generar un triángulo invertido alineado a la izquierda
def triangulo_izquierda_invertido(filas, asterisco="*"):
    for i in range(filas, 0, -1):
        asteriscos = asterisco * i
        print(asteriscos)
    print("")  # Salto de línea

# Función para generar una pirámide invertida con base centrada
def piramide_invertida(filas, asterisco="*", espacio=" "):
    for i in range(filas, 0, -1):
        asteriscos = asterisco * (2 * i - 1)
        espacios = espacio * (filas - i)
        print(f"{espacios}{asteriscos}{espacios}")
    print("")  # Salto de línea

# Función principal
def main():
    # Solicita al usuario el número de filas para los patrones
    filas = int(input("Ingrese el número de filas: "))

    #Llamada de funciones
    triangulo_rectangulo_invertido(filas)

    triangulo_rectangulo_normal(filas)

    piramide_completa(filas)

    triangulo_invertido_reves(filas)

    triangulo_izquierda_invertido(filas)

    piramide_invertida(filas)

main()
