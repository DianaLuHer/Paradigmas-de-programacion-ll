"""
Nombre: Diana Belen Luna Hernández
Fecha: 17/10/24
Descripción: Programa que realiza varias operaciones de asignación.
"""

# Asignación múltiple: se asignan valores a las variables n1 y n2
num1, num2 = 7, 10
print(num1)  # Imprime el valor de n1
print(num2)  # Imprime el valor de n2

# Se asignan múltiples valores a diferentes variables
num3, cad, num4 = 11, "Hola", 9
print("")
print(num3)  # Imprime el valor de n3
print(cad)  # Imprime el valor de la cadena cad
print(num4)  # Imprime el valor de n4

# Se calcula la suma y la resta de los valores asignados
suma, resta = num1 + num2, num3 - num4
print("")
print(suma)  # Imprime el resultado de la suma
print(resta)  # Imprime el resultado de la resta

# Asignación encadenada: se asigna el mismo valor a n5, n6 y n7
num5 = num6 = num7 = 12
print("")  # Imprime una línea en blanco
print(num5)  # Imprime el valor de n5
print(num6)  # Imprime el valor de n6
print(num7)  # Imprime el valor de n7

# Intercambio de variables
print("Intercambio de variables")
num8 = int(input("Ingresa un número entero: "))  # Se solicita un número entero y se asigna a n8
print("")  # Imprime una línea en blanco
num9 = int(input("Ingresa un número entero: "))  # Se solicita otro número entero y se asigna a n9

print(num8, num9)  # Imprime los valores de n8 y n9

# Se intercambian los valores de n8 y n9
num9, num8 = num8, num9

# Imprime los valores intercambiados
print(num8, num9)
