"""
Nombre: Diana Belen Luna Hernández
Fecha: 24/10/2024
Descripción: Programa que calcula la suma acumulativa entre dos números ingresados por el usuario.
"""

print("Programa que calcula la suma acumulativa entre dos números")

# Solicita al usuario que ingrese dos números y los convierte a tipo entero
num1, num2 = int(input("Ingresa el primer número: ")), int(input("Ingresa el segundo número: "))

# Inicializa 'i' con el valor de num1, que se usará para iterar
i = num1

# Inicializa 'ban' en 0, que almacenará la suma acumulativa
ban = 0

# Bucle while que se ejecuta mientras 'i' sea menor o igual a num2
while i <= num2:
    # Acumula el valor de 'i' en 'ban'
    ban = ban + i
    # Incrementa 'i' en 1 para la siguiente iteración
    i = i + 1

# Imprime el resultado final de la suma acumulativa entre num1 y num2
print(f"La suma del número {num1} hasta {num2} es: {ban}")
