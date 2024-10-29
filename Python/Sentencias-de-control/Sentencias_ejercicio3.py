"""
Nombre: Diana Belen Luna Hernández
Fecha: 23/10/2024
Descripción: Este programa simula un sistema de descuentos en la Cona
"""

print("**** L a  c o n a ****")

# Solicita al usuario que ingrese la cantidad comprada
compra = float(input("Ingresa la cantidad comprada: "))

# Pregunta al usuario si cuenta con una membresía
membresia = input("¿Cuenta con la membresía? ")

# Convierte la respuesta a minúsculas y verifica si el usuario tiene membresía
tieneMembresia = membresia.lower() == "si"  # Cambio de nombre de la variable

# Si el usuario tiene membresía
if tieneMembresia:
    # Si la compra es mayor o igual a 1000, aplica un descuento del 8%
    if compra >= 1000:
        print("Tu descuento es del 8%")
        print(f"El total es de: $ {compra * 0.92}")  # Calcula el total después del descuento
    else:
        # Si la compra es menor de 1000, aplica un descuento del 5%
        print("Tu descuento es de 5%")
        print(f"El total es de: $ {compra * 0.95}")  # Calcula el total después del descuento
else:
    # Si el usuario no tiene membresía, le invita a hacerse miembro
    print("Se te invita a ser miembro de la tienda para obtener un descuento de hasta el 8%")
    print(f"El total es de: $ {compra}")  # Muestra el total sin descuento
