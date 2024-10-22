'''
Nombre: Diana Belen Luna Hernández.
Fecha: 10 de Octubre del 2024.
Descripción: Programa que pide los datos de los profesores y muestra los resultados con diferentes tipos de datos.
'''

# Se solicita al usuario que ingrese el nombre del profesor.
# La función input() recibe siempre una cadena de texto. En este caso, no es necesario hacer ningún casting
nombre = input("Ingrese el nombre del profesor: ")
# Aquí se pide el número de cubículo al usuario.
# El valor que el usuario ingresa es una cadena, por lo que se usa int para convertir ese valor en un número entero .
cubiculo = int(input("Ingrese el número de cubículo: "))
# Se solicita la cantidad de horas que el profesor imparte clases a la semana por lo que se usa float para convertir ese valor en un número flotante.
horas_clase = float(input("Ingrese las horas de clase a la semana con 3 decimales: "))
# Se pregunta al usuario si el profesor tiene más de 5 años de antigüedad en la UNSIJ, y se espera una respuesta en forma de "Si" o "No".
tiene_mas_5_anios = input("¿Tiene más de 5 años en la UNSIJ? (Si/No): ")  # Pregunta si tiene más de 5 años

# Convertir la respuesta a booleano
# Para convertir la respuesta a un valor booleano, primero convertimos la respuesta a minúsculas usando lower().
tiene_mas_5_anios = tiene_mas_5_anios.lower() == "si"

# Mostrar los datos de forma adecuada
print("\nDatos del profesor:")
print(f"Nombre: {nombre}") #Imprime el nombre del profesor.
print(f"Número de cubículo: {cubiculo}") #Imprime el número de cubiculo.
print(f"Horas que imparte clase a la semana: {horas_clase:.3f}")  #Imprime la cantidad de horas de clase a la semana. El formato `:.3f`, se muestre con 3 decimales.
print(f"Tiene más de 5 años en la UNSIJ: {tiene_mas_5_anios}") # Imprime si el profesor tiene más de 5 años en la UNSIJ es un valor booleano.
