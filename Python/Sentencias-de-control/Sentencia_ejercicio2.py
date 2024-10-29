"""
Nombre: Diana Belen Luna Hernandez
Fecha: 23/10/2024
Descripción: Este programa determina la estación del año en función del número del mes ingresado por el usuario.
"""

print("------ Programa que determina la estación del año ------")

# Solicita al usuario que ingrese el número del mes y lo convierte a entero
mes = int(input("Ingresa el número del mes (1-12): "))

# Inicializa la variable estacion para almacenar el resultado
estacion = ""

# Determina la estación del año según el número del mes
if mes == 3 or mes == 4 or mes == 5:
    estacion = "Primavera"
elif mes == 6 or mes == 7 or mes == 8:
    estacion = "Verano"
elif mes == 9 or mes == 10 or mes == 11:
    estacion = "Otoño"
elif mes == 12 or mes == 1 or mes == 2:
    estacion = "Invierno"
else:
    # Si el número ingresado no es válido, imprime un mensaje de error
    print("Número incorrecto. Por favor, ingresa un número del 1 al 12.")

# Si la estación fue determinada, imprime el resultado
if estacion:
    print(f"La estación es: {estacion}.")
