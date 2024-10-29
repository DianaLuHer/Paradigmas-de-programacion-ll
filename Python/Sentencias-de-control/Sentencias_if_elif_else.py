"""
Nombre: Diana Belen Luna Hernández
Fecha: 23/10/2024
Descripción: Este programa clasifica a una persona en un grupo de edad basado en la edad ingresada.
"""

print("----- Grupo de edad -----")

# Solicita al usuario que ingrese su edad y convierte la entrada en un número entero
edad = int(input("Ingrese su edad: "))

# Verifica si la edad es menor a 15
if edad < 15:
    # Si es menor a 15, clasifica como "Niño o adolescente"
    print("Eres Niño o adolescente")
# Verifica si la edad está entre 15 y 24
elif edad <= 24:
    # Si cumple, clasifica como "Joven"
    print("Eres joven")
# Verifica si la edad está entre 25 y 44
elif edad <= 44:
    # Si cumple, clasifica como "Adulto joven"
    print("Adultos jóvenes")
# Verifica si la edad está entre 45 y 60
elif edad <= 60:
    # Si cumple, clasifica como "Adulto maduro"
    print("Adultos maduros")
# Si la edad es mayor a 60
elif edad > 60:
    # Clasifica como "Adulto mayor"
    print("Adultos mayores")
