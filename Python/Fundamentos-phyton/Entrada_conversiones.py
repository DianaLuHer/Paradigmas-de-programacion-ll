'''
Nombre: Diana Belen Luna Hernández
Fecha: 10 de Octubre del 2024.
Descripción: Conversión de cadenas a int, float y boolean mediante la interacción con consola.
'''

# Las funciones anidadas se refieren a cuando se llama una función dentro de otra.
# En este caso, estamos utilizando `input()` para leer datos y `int()`, `float()` o una comparación para convertirlos a otros tipos.
print("****   Datos de los alumnos    *****")
#input solicita al usuario que ingrese datos. El valor introducido es tratado como un string.
nombre = input("Ingresa el nombre: ") # Lee el nombre del alumno como cadena.
semestre = int(input("Ingresa el no. de semestre: ")) # Lee el semestre, lo convierte a entero
promedio = float(input("Ingresa el promedio: ")) # Lee el promedio, lo convierte a número decimal
es_mujer = input("¿Es mujer (Si/No)?: ") # Lee si es mujer o no, inicialmente como cadena de texto.


# No es posible convertir directamente una cadena a un valor booleano.
# Por ello, utilizamos la misma variable, convertimos a  minúsculas y lo comparamos con la cadena "si".
# Si el usuario ingresa "si", `es_mujer` será `True`. En cualquier otro caso, será `False`.
es_mujer = es_mujer.lower() == "si"

# Se imprimen los datos del alumno.
# "promedio:.2f" limita el número de decimales mostrados en el promedio a dos cifras.
print()
print(f"El alumno {nombre} cursa el {semestre} semestre con un promedio de {promedio:.2f}. Además, es mujer: {es_mujer}.")
