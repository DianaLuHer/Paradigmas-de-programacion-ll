"""
Nombre: Diana Belen Luna Hernández
Fecha: 23/10/2024
Descripción:Este programa calcula la calificación final de un estudiante basada en sus calificaciones de tres parciales y un examen ordinario.
"""


# Solicita al usuario que ingrese las calificaciones de los parciales y del examen ordinario.
# Se utilizan la función input() para recibir las calificaciones como texto y se convierten a float para realizar los cálculos.
parcial1 = float(input("Ingresa la calificación del Parcial 1: "))
parcial2 = float(input("Ingresa la calificación del Parcial 2: "))
parcial3 = float(input("Ingresa la calificación del Parcial 3: "))
ordinario = float(input("Ingresa la calificación del Ordinario: "))

# Calcula el promedio de las calificaciones de los tres parciales
# Se suma el total de las calificaciones de los parciales y se divide entre 3
# Luego se suma la calificación del examen ordinario, que se pondera dividiendo entre 2
promedio = ((parcial1 + parcial2 + parcial3) / 3) + (ordinario / 2)

# Comprueba si el promedio calculado es mayor o igual a 6
if promedio >= 6:
    # Si el promedio es mayor o igual a 6, imprime el promedio y un mensaje de felicitaciones
    print(f"La calificación final es: {promedio:.2f}. ¡Felicidades! Aprobaste ")
else:
    # Si el promedio es menor que 6, imprime el promedio y un mensaje indicando que se ha reprobado
    print(f"La calificación final es: {promedio:.2f}. ¡Lastima! Reprobaste")