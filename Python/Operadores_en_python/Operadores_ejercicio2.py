"""
Nombre: Diana Belen Luna Hernández
Fecha: 19/10/2024
Descripción: Este programa verifica si una persona es parte de la comunidad UNSIJ.
"""

print("*********** COMUNIDAD UNSIJ **********")
# Pregunta si la persona es profesor de la UNSIJ y almacena la respuesta en la variable 'profe'
profe = input("¿Eres profesor de la UNSIJ? [si/no]: ")
# Pregunta si la persona es alumno de la UNSIJ y almacena la respuesta en la variable 'alumno'
alumno = input("¿Eres alumno de la UNSIJ? [si/no]: ")

# Convierte la respuesta de 'profe' en un valor booleano (True si respondió "si", False en caso contrario)
esProfe = profe.lower() == "si"
# Convierte la respuesta de 'alumno' en un valor booleano (True si respondió "si", False en caso contrario)
esAlumno = alumno.lower() == "si"

# Verifica si la persona es profesor o alumno, y si cumple al menos una de estas condiciones, indica que forma parte de la comunidad UNSIJ
print(f"La persona forma parte de la comunidad UNSIJ: {esProfe or esAlumno}")
