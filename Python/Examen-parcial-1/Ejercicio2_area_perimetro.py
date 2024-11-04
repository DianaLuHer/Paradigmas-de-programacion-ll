"""
Nombre: Diana Belen Luna Hernández
Fecha: 30/10/2024
Descripción: Este programa determina el área y el perímetro de un rectangulo
o de un círculo.
"""

print("--------- Área o perímetro ---------")
# Inicializa la  variable para controlar el bucle
continuar = True

# Bucle principal del programa
while continuar:
    # Imprime el menú de opciones
    print("-------------------------------------------------")
    print("-- 1. Calcular el área de un rectángulo        --")
    print("-- 2. Calcular el perímetro de un rectángulo   --")
    print("-- 3. Calcular el área de un círculo           --")
    print("-- 4. Calcular el perímetro de un círculo      --")
    print("-- 0. Salir                                    --")
    print("-------------------------------------------------")
    # Solicita al usuario que elija una opción
    opcion = int(input("Ingrese la opción que desee realizar: "))

    # Opción para calcular el área de un rectángulo
    if opcion == 1:
        base = float(input("Ingrese la base del rectángulo: "))  # Solicitar la base
        altura = float(input("Ingrese la altura del rectángulo: "))  # Solicitar la altura

        area = base * altura  # Calcular el área
        print(f"El área del rectángulo es: {area:.3f}")
        print("___________________________________________")
        print()

    # Opción para calcular el perímetro de un rectángulo
    elif opcion == 2:
        base = float(input("Ingrese la base del rectángulo: "))  # Solicitar la base
        altura = float(input("Ingrese la altura del rectángulo: "))  # Solicitar la altura

        perimetro = (2 * base) + (2 * altura)  # Calcular el perímetro
        print(f"El perímetro del rectángulo es {perimetro:.3f}")
        print("___________________________________________")
        print()

    # Opción para calcular el área de un círculo
    elif opcion == 3:
        radio = float(input("Ingresa el radio del círculo: "))  # Solicitar el radio

        areaCir = 3.1416 * (radio ** 2)  # Calcular el área del círculo
        print(f"El área del círculo es: {areaCir:.3f}")
        print("___________________________________________")
        print()

    # Opción para calcular el perímetro de un círculo
    elif opcion == 4:
        diametro = float(input("Ingrese el diámetro del círculo: "))  # Solicitar el diámetro

        perimetroCir = diametro * 3.1416  # Calcular el perímetro del círculo
        print(f"El perímetro del círculo es: {perimetroCir:.3f}")
        print("___________________________________________")
        print()

    # Opción para salir del programa
    elif opcion == 0:
        continuar = False  # Cambiar la variable de control a False para salir del bucle
        print("Saliendo del programa...")
        print("___________________________________________")
        print()

    # Mensaje para opciones no válidas
    else:
        print("Opción no válida. Por favor, elija una opción del menú.")