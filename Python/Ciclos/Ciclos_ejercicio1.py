"""
Nombre: Diana Belen Luna Hernandez
Fecha: 24/10/2024
Descripción: Programa que calcula la suma acumulativa de números desde 0 hasta un número ingresado por el usuario.
"""

print("Programa que calcula la suma acumulativa")

# Solicita al usuario que ingrese un número final y lo convierte a tipo entero
num = int(input("Ingresa el número final: "))

# Inicializa 'i' en 0, que se usará para iterar
i = 0

# Inicializa 'ban' en 0, que almacenará la suma acumulativa
ban = 0

# Bucle while que se ejecuta mientras 'i' sea menor o igual al número ingresado
while i <= num:
    # Acumula el valor de 'i' en 'ban'
    ban = ban + i
    # Incrementa 'i' en 1 para la siguiente iteración
    i = i + 1

# Imprime el resultado final de la suma acumulativa
print(f"La suma de 0 hasta {num} es: {ban}")
