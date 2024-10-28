"""
Nombre: Diana Belen Luna Hernández
Fecha: 17/10/2024
Descripción: Este código proporciona ejemplos de cómo se utilizan los operadores de asignación como, asignación múltiples, asignación encadenada, intercambio de variables
"""
"""
En programación, las operaciones de asignación se utilizan para almacenar un valor en una variable. 
Es decir, se establece una relación entre un nombre (la variable) y un valor en la memoria de la computadora.
"""

# Asignación múltiple: Permite asignar varios valores a múltiples variables al mismo tiempo, lo que puede incluir diferentes tipos de datos (cadenas, enteros, decimales)
print("   ***   Asignación múltiple   ***")
nombre, primer_apellido, segundo_apellido = "Diana Belen", "Luna", "Hernández"
# Imprime el nombre completo almacenado en las variables
print(f"Asignación múltiple de cadenas: {nombre} {primer_apellido} {segundo_apellido}")

entero1, entero2 = 1, 2
# Imprime los enteros asignados
print(f"Asignación múltiple de enteros: {entero1} y {entero2}")

decimal1, decimal2, decimal3, decimal4 = 3.14, 3.1416, 3.14159, 3.141592
print(f"Asignación múltiple de decimales: {decimal1}, {decimal2}, {decimal3} y {decimal4}")

# Asignación múltiple con diferentes tipos de datos
nombre, entero1, decimal4 = "Diana", 12, 3.1415926            # Es posible combinar tipos de datos.
print(f"Asignación múltiple: {nombre}, {entero1} y {decimal4}")

suma, resta = entero1 + entero2, decimal1 - decimal2
# Realiza operaciones (suma y resta) y asigna los resultados a nuevas variables.
print(f"Asignaciones de operaciones: suma {suma} y resta {resta:.4f}") # Imprime resultados con formato


# Asignación encadenada: Permite asignar el mismo valor a varias variables en una sola línea.
print()
print("   ***   Asignación encadenada   ***")

entero3 = entero4 = entero5 = 10    # Se les asigna el mismo valor (10) a todas las variables.
print(f"Asignación encadenada de: {entero3} = {entero4} = {entero5} = 10")


# Intercambio de variables: Muestra cómo se pueden intercambiar los valores de dos variables usando una sola línea de código, incluso si estas variables contienen diferentes tipos de datos.
print()
print("   ***   Intercambio de variables   ***")

entero5, entero6 = 5, 6
# Imprime los valores asignados antes del intercambio
print(f"Valores asignados: entero5 = {entero5} y entero6 = {entero6}")

# Intercambia los valores de entero5 y entero6
entero6, entero5 = entero5, entero6
# Imprime los valores después del intercambio
print(f"Valores intercambiados: entero5 = {entero5} y entero6 = {entero6}")

# intercambio de valores entre variables de diferentes tipos
variable_prueba1, variable_prueba2 = 100, "Hola mundo"
# Intercambia los valores entre las variables
variable_prueba1, variable_prueba2 = variable_prueba2, variable_prueba1
# Imprime los valores asignados y después del intercambio
print(f"Valores asignados: variable_prueba1 = {variable_prueba1} y variable_prueba2 = {variable_prueba2}")
print(f"Valores intercambiados: variable_prueba1 = {variable_prueba1} y variable_prueba2 = {variable_prueba2}")