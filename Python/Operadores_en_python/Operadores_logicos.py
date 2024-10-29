"""
Nombre: Diana Belen Luna Hernández
Fecha: 18/10/2024
Descripción: Ejemplos de uso de los operadores lógicos.
"""

"""
Los operadores lógicos son símbolos o palabras clave en programación que permiten combinar o manipular expresiones booleanas 
para crear condiciones complejas en los programas. En términos simples, los operadores lógicos ayudan a
evaluar si una o más condiciones son verdaderas o falsas y suelen usarse en decisiones (por ejemplo, en sentencias if), ciclos, 
y otras estructuras de control.
"""

# Se solicita al usuario que ingrese un valor ("si" o "no") para la variable a.
a = input("a = ingresa si/no: ")

# La entrada del usuario se convierte en minúsculas y luego en un valor booleano.
# Si el usuario ingresó "si", p será True; de lo contrario, será False.
a = a.lower() == "si"

# Se solicita al usuario que ingrese otro valor ("si" o "no") para la variable b.
b = input("b = ingresa si/no: ")

# La entrada se convierte en minúsculas y luego en un valor booleano.
# Si el usuario ingresó "si", q será True; de lo contrario, será False.
b = b.lower() == "si"

# Se imprimen los resultados de las operaciones lógicas entre a y b.
print(f"a and b: {a and b}")  # True si ambos a y b son True
print(f"a or b: {a or b}")    # True si al menos uno de a o b es True
print(f"not a: {not a}")      # Muestra el valor contrario de a
print(f"not b: {not b}")      # Muestra el valor contrario de b
