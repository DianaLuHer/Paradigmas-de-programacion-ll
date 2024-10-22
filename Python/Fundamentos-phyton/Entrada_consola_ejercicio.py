"""
Nombre: Diana Belen Luna Hernández
Fecha: 18 de octubre del 2024
Descripción: Programa que solicita dos números decimales al usuario y realiza operaciones matemáticas básicas.
"""
# Solicitar dos números decimales al usuario.
# La función input() lee el dato ingresado como cadena, pero el casting a float convierte esa cadena en un número decimal.
num1 = float(input("Ingrese el primer número decimal: "))
num2 = float(input("Ingrese el segundo número decimal que sea diferente a 0: "))

#Operaciones matemáticas
suma = num1 + num2 # Suma los dos números.
resta = num1 - num2 # Resta el segundo número al primero.
multiplicacion = num1 * num2 # Multiplica los dos números.
division = num1 / num2 # Divide el primer número entre el segundo que debe ser diferente de cero.

# Mostrar los resultados
print(f"Suma: {num1} + {num2} = {suma}") # Imprime el resultado de la suma.
print(f"Resta: {num1} - {num2} = {resta}") # Imprime el resultado de la resta.
print(f"Multiplicación: {num1} * {num2} = {multiplicacion}") # Imprime el resultado de la multiplicación.
print(f"División: {num1} / {num2} = {division}") # Imprime el resultado de la suma. # Imprime el resultado de la división.
