"""
Nombre: Diana Belen Luna Hernández.
Fecha:30/10/2024
Descripción: Este programa imprime en consola los números, separados por comas,
del 1 hasta un número ingresado por el usuario, los multiplos de 3 sustituidos por la palabra "licenciatura"
y los multiplos de 5 sustituidos por la palabra "Informatica".
"""

# Solicitar al usuario el número
numero = int(input("Ingresa un número: "))

# Iterar del 1 hasta el número ingresado
for i in range(1, numero + 1):
    # Verificar si el número es múltiplo de 3
    if i % 3 == 0:
        print("Licenciatura", end=", ") #Si es múltiplo de 3 imprime la palabra "Licenciatura"
    # Verificar si el número es múltiplo de 5
    elif i % 5 == 0:
        print("Informática", end=", ") #Si es múltiplo de 3 imprime la palabra "Informática"
    # Si no es múltiplo de 3 ni de 5, imprimir el número
    else:
        print(i, end=", " if i < numero else "")

