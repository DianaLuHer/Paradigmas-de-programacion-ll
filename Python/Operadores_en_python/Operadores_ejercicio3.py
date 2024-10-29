"""
Nombre: Diana Belen Luna Hernández.
Fecha: 20/10/2024
Descripción: Este programa simula un sistema de acceso seguro que verifica si el usuario y la contraseña son correctos.
"""

# Define el usuario y la contraseña correctos
usuario1 = "dianaluher"
contrasena1 = "elzapatito"

print("****** Sistema de acceso seguro ******")

# Solicita al usuario que ingrese su nombre de usuario y almacena la entrada en la variable usuario
usuario = input("Ingresa tu usuario: ")

# Solicita al usuario que ingrese su contraseña y almacena la entrada en la variable contrasena
contrasena = input("Ingresa tu contraseña: ")

# Verifica si tanto el usuario como la contraseña ingresados coinciden con los valores definidos
# Imprime "True" si ambos coinciden y "False" en caso contrario
print(f"\nEl acceso es correcto: {usuario1 == usuario and contrasena1 == contrasena}")
