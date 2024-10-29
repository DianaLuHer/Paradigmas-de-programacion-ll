"""
Nombre: Diana Blena Luna Hernandez
Fecha: 23/10/2024
Descripción: Este programa determina cuál de los dos números ingresados es menor.
"""

print("------- Programa que determina cuál de los dos números es menor -------")

# Solicita al usuario que ingrese dos números y los convierte a tipo flotante
num1, num2 = float(input("Ingresa un número: ")), float(input("Ingresa otro número: "))

# Compara los dos números y determina cuál es menor
if num1 < num2:
    # Si num1 es menor que num2, imprime el resultado
    print(f"El número {num1} es menor que {num2}.")
elif num2 < num1:
    # Si num2 es menor que num1, imprime el resultado
    print(f"El número {num2} es menor que {num1}.")

