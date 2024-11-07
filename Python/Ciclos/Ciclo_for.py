"""
Nombre: Diana Belen Luna Hernández
Fecha: 29/10/2024
Descripción:
"""

print("****** Ejemplo de ciclo for ******")

cadena=input("Ingrese una frase: ")

for caracter in cadena:
    print(caracter,end="-")
print("Fin de la cadena")

print()
print("****** ALUMNOS ******")

alumnos=["Albert","Kevin","Elton","Diana","Eden","Amelia","Sergio"]

for alumno in alumnos:
    print(f"Hola {alumno}")