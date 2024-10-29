"""
Nombre: Diana Belen Luna Hernández
Fecha: 25/10/2024
Descripción: Ejercicio 4 "Bienvenido a tu cuenta de banco Azteca"
"""

print("********** Bienvenido a tu cuenta de BANCO AZTECA **********")

# Inicializa el saldo de la cuenta
saldo = 0.0

# Se establece una variable de control para el bucle
continuar = True

# Bucle que se ejecuta mientras continuar sea True
while continuar:
    print("----------------------------------------")
    print("--- [1]  Consulta tu saldo           ---")
    print("--- [2]  Ingresar dinero             ---")
    print("--- [3]  Retirar dinero              ---")
    print("--- [0]  Salir                       ---")
    print("----------------------------------------")

    # Solicita al usuario que ingrese la operación que desea realizar
    op = int(input("Ingresa la operación que desee realizar: "))

    if op == 1:
        print(f"Su saldo es: ${saldo:.2f}")  # Muestra el saldo formateado a dos decimales
    elif op == 2:
        ingresar_dinero = float(input("Ingresa la cantidad a depositar: "))
        saldo += ingresar_dinero  # Actualiza el saldo sumando la cantidad ingresada
        print(f"Tu saldo actualizado es: ${saldo:.2f}")
    elif op == 3:
        retirar_dinero = float(input("Ingrese la cantidad a retirar: "))  # Solicita la cantidad a retirar
        if retirar_dinero > saldo:  # Verifica que haya suficiente saldo
            print("Error: Saldo insuficiente.")
        else:
            saldo -= retirar_dinero  # Actualiza el saldo restando el dinero retirado
            print(f"Saldo actual: ${saldo:.2f}")
    elif op == 0:
        continuar = False  # Cambia la variable de control a False para salir del bucle
        print("Saliendo de su cuenta. Gracias por usar Banco Azteca.")
    else:
        print("Opción no válida. Por favor, elija una opción del menú.")
