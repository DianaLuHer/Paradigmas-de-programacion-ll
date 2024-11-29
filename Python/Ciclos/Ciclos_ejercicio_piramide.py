"""
Nombre: Diana Belen Luna Hernández
Fecha: 07/11/2024
Descripción: Este programa genera diferentes patrones, variando segun el número de filas
ingresado.
"""

# Solicita al usuario el número de filas para los patrones
filas = int(input("Ingrese el número de filas: "))
asterisco = "*"  # Define el carácter para los patrones
espacio = " "    # Define el carácter para los espacios

# Genera un triángulo rectángulo invertido (alineado a la derecha)
for i in range(filas + 1):
    asteriscos = asterisco * i           # Calcula la cantidad de asteriscos en cada fila
    espacios = espacio * (filas - i)     # Calcula la cantidad de espacios en cada fila
    print(f"{espacios}{asteriscos}")     # Imprime los espacios seguidos de los asteriscos

print("")  # Salto de línea

# Genera un triángulo rectángulo normal (alineado a la izquierda)
for i in range(filas + 1):
    asteriscos = asterisco * i           # Calcula la cantidad de asteriscos en cada fila
    espacios = espacio * (filas - i)     # Calcula los espacios restantes (opcional)
    print(f"{asteriscos}{espacios}")     # Imprime los asteriscos seguidos de los espacios (espacios redundantes aquí)

print("")  # Salto de línea

# Genera una pirámide completa
for i in range(1, filas + 1):
    asteriscos = asterisco * (2 * i - 1) # Calcula los asteriscos como números impares
    espacios = espacio * (filas - i)     # Calcula los espacios para centrar la pirámide
    print(f"{espacios}{asteriscos}{espacios}")  # Imprime los espacios, los asteriscos y los espacios nuevamente

print("")  # Salto de línea

# Genera un triángulo rectángulo invertido al reves
for i in range(filas, 0, -1):
    asteriscos = asterisco * i           # Calcula la cantidad de asteriscos
    espacios = espacio * (filas - i)     # Calcula los espacios
    print(f"{espacios}{asteriscos}")     # Imprime los espacios seguidos de los asteriscos

print("")  # Salto de línea

# Genera un triángulo al reves alineado a la izquierda
for i in range(filas, 0, -1):
    asteriscos = asterisco * i           # Calcula los asteriscos
    print(asteriscos)                    # Imprime directamente los asteriscos

print("")  # Salto de línea

# Genera una pirámide invertida con base centrada
for i in range(filas, 0, -1):
    asteriscos = asterisco * (2 * i - 1) # Calcula los asteriscos como números impares
    espacios = espacio * (filas - i)     # Calcula los espacios para centrar la pirámide
    print(f"{espacios}{asteriscos}{espacios}")  # Imprime los espacios, los asteriscos y los espacios nuevamente
