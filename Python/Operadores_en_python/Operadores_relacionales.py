# Nombre: Diana Belen Luna Hernández.
# Fecha: 18/10/2024
# Descripción: Ejemplos de uso de los operadores relacionales.

"""
Los operadores relacionales son símbolos que se utilizan en programación y matemáticas para comparar dos valores.
 El resultado de una operación relacional es un valor booleano, es decir, True (verdadero) o False (falso).
"""

print("------ Operadores relacionales ------")
# Se solicitan dos números al usuario y se convierten a tipo flotante
num1, num2 = float(input("Ingresa un numero: ")), float(input("Ingresa otro: "))

# Se verifica si num1 es mayor que num2 y se almacena el resultado en 'resultado'
resultado = num1 > num2
# Se imprime el resultado de la comparación
print(f"¿El número {num1} es mayor que {num2}?: {resultado}")

# Se verifica si num1 es mayor o igual que num2
resultado = num1 >= num2
print(f"¿El número {num1} es mayor o igual que {num2}?: {resultado}")

# Se verifica si num1 es menor que num2
resultado = num1 < num2
print(f"¿El número {num1} es menor que {num2}?: {resultado}")

# Se verifica si num1 es menor o igual que num2
resultado = num1 <= num2
print(f"¿El número {num1} es menor o igual que {num2}?: {resultado}")

# Se verifica si num1 es igual a num2
resultado = num1 == num2
print(f"¿El número {num1} es igual que {num2}?: {resultado}")

# Se verifica si num1 es distinto de num2
resultado = num1 != num2
print(f"¿El número {num1} es distinto que {num2}?: {resultado}")
