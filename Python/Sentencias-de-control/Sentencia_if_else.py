"""
Nombre: Diana Belen Luna Hernández
Fecha: 23/10/2024
Descripción: Este programa verifica si un número ingresado por el usuario es par o impar.
"""

print("-------- Números pares --------")

# Solicita al usuario que ingrese un número y lo convierte a un entero
num = int(input("Ingrese el primer número: "))

# Verifica si el número es par utilizando el operador módulo (%)
if num % 2 == 0:
    # Si el número es par, imprime un mensaje indicando que es par
    print("Este número es par")
else:
    # Si el número no es par, imprime un mensaje indicando que es impar
    print("Este número no es par")  # La tabulación es importante
