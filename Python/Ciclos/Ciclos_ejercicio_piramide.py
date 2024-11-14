"""
Nombre: Diana Belen Luna Hernández
Fecha: 07/11/2024
Descripción:
"""

filas= int(input("Ingrese el número de filas: "))
asterisco="*"
espacio=" "

for i in range(filas+1):
    asteriscos=asterisco*i
    espacios=espacio * (filas-i)
    print(f"{espacios}{asteriscos}")
print("")
for i in range(filas+1):
    asteriscos=asterisco*i
    espacios=espacio * (filas-i)
    print(f"{asteriscos}{espacios}")

print("")
for i in range(1, filas + 1):
    asteriscos = asterisco * (2 * i - 1)
    espacios = espacio * (filas - i)
    print(f"{espacios}{asteriscos}{espacios}")
print("")

for i in range(filas, 0, -1):
    asteriscos = asterisco * i
    espacios = espacio * (filas - i)
    print(f"{espacios}{asteriscos}")
print("")

for i in range(filas, 0, -1):
    asteriscos = asterisco * i
    print(asteriscos)
print("")
for i in range(filas, 0, -1):
    asteriscos = asterisco * (2 * i - 1)  
    espacios = espacio * (filas - i)
    print(f"{espacios}{asteriscos}{espacios}")