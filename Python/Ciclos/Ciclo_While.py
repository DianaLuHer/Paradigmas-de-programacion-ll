"""
Nombre: Diana Belen Luna Hernández
Fecha: 24/10/2024
Descripción: Este programa imprime números enteros en dos secciones: primero imprime todos los números del 1 al número ingresado, y luego imprime los números pares hasta otro número ingresado.
"""

"""
Sintaxis: while condicion:
    # Código mientras 
    # La condición sea verdadera
"""

print("------------ imprimir números ------------")

# Solicita al usuario que ingrese un número entero.
num = int(input("Ingresa un número entero: "))

# Inicializa la variable 'i' para contar desde 1
i = 1

# Imprime el mensaje indicando el rango de números a mostrar
print(f"Los números del 1 al {num} son: ")

# Bucle while que se ejecuta mientras 'i' sea menor o igual a 'num'
while i <= num:
    # Imprime el valor de 'i' sin un salto de línea
    print(i, end=" ")
    # Incrementa 'i' en 1
    i = i + 1

# Imprime un mensaje indicando que se ha terminado la impresión
print("\nFin de la impresión")

# Imprime el encabezado para la segunda sección
print("------- Imprime los números pares -------")

# Solicita al usuario que ingrese otro número entero
num2 = int(input("Ingresa un número entero: "))

# Inicializa 'i' en 0 para contar desde 0
i = 0

# Bucle while que se ejecuta mientras 'i' sea menor o igual a 'num2'
while i <= num2:
    # Verifica si 'i' es par
    if i % 2 == 0:
        # Imprime el valor de 'i' sin un salto de línea
        print(i, end=" ")
    # Incrementa 'i' en 1
    i = i + 1
