"""
Nombre: Diana Belen Luna Hernández
Fecha: 25/10/2024
Descripción: Ejercicio 3 de ciclos "While" Programa que realiza una calculadora.
"""

# Imprime el encabezado de la calculadora
print("------------ Calculadora -------------")

# Inicializa la variable de control para el bucle
continuar = True

# Bucle que se ejecuta mientras continuar sea verdadero
while continuar:
    # Muestra el menú de operaciones
    print("------------------------------")
    print("--- 1.- Suma               ---")
    print("--- 2.- Resta              ---")
    print("--- 3.- Multiplicación     ---")
    print("--- 4.- División           ---")
    print("--- 5.- División entera    ---")
    print("--- 6.- Exponenciación     ---")
    print("--- 0.- Salir              ---")
    print("------------------------------")

    # Solicita al usuario que ingrese la operación que desea realizar
    op = int(input("Ingrese el número de operación que desee realizar: "))

    # Opción para salir del programa
    if op == 0:
        print("Saliendo del programa...")
        continuar = False  # Cambia la variable de control a False para salir del bucle

    # Opción de suma
    elif op == 1:
        num1, num2 = float(input("Ingresa el número 1: ")), float(input("Ingresa el número 2: "))
        suma = num1 + num2
        print(f"La suma de los números {num1} y {num2} es: {suma}")

    # Opción de resta
    elif op == 2:
        num1, num2 = float(input("Ingresa el número 1: ")), float(input("Ingresa el número 2: "))
        resta = num1 - num2
        print(f"La resta de los números {num1} y {num2} es: {resta}")

    # Opción de multiplicación
    elif op == 3:
        num1, num2 = float(input("Ingresa el número 1: ")), float(input("Ingresa el número 2: "))
        multi = num1 * num2
        print(f"La multiplicación de los números {num1} y {num2} es: {multi}")

    # Opción de división
    elif op == 4:
        num1, num2 = float(input("Ingresa el número 1: ")), float(input("Ingresa el número 2: "))
        # Verifica que no se divida por cero
        if num2 != 0:
            div = num1 / num2
            print(f"La división de los números {num1} y {num2} es: {div}")
        else:
            print("Error: No se puede dividir por cero.")

    # Opción de división entera
    elif op == 5:
        num1, num2 = float(input("Ingresa el número 1: ")), float(input("Ingresa el número 2: "))
        # Verifica que no se divida por cero
        if num2 != 0:
            diventera = num1 // num2
            print(f"La división entera de los números {num1} y {num2} es: {diventera}")
        else:
            print("Error: No se puede dividir por cero.")

    # Opción de exponenciación
    elif op == 6:
        num1, num2 = float(input("Ingresa el número 1: ")), float(input("Ingresa el número 2: "))
        expo = num1 ** num2
        print(f"La exponenciación de los números {num1} y {num2} es: {expo}")

    # Opción no válida
    else:
        print("Opción no válida. Por favor, elige una opción del menú.")

