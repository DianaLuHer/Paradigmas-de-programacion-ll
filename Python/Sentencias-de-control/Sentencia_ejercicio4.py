"""
Nombre: Diana Belen Luna Hernández
Fecha: 23/10/2024
Descripción: Este programa determina si se permite la entrada a la negra.
"""

print("**** Acceso a la negra ****")
# Solicita la edad y el presupuesto del usuario.
edad, presupuesto= int(input("Ingresa tu edad: ")), int(input("Ingresa tu presupuesto: "))

if edad > 18:
    # Verifica que el usuario sea mayor de 18 años.
    print("¡Bienvenido a tu mejor bar!")
elif presupuesto > 250:
    # Verifica que el usuario tenga un presupuesto superior a 250.
    print("¡Bienvenido a tu mejor bar!")
else:
    # Se le imprime este mesnaje al usuario.
    print("Lo sentimos, ya estamos por cerrar....")