'''
Nombre: Diana Belen Luna Hernández.
Fecha: 11 de octubre del 2024
Descripción: Conversión de tipos de datos (casting) en Python.
'''

# Notas
'''
La conversión de tipos de datos implica manipular datos que no están en el tipo de dato requerido. 
Ejemplos: de cadena a entero, de cadena a número flotante, y viceversa.
'''

# *****   Conversión de cadena a entero     *****
# Se toma una cadena numérica y se convierte en un número entero utilizando la función int().
var_cadena = "951"
var_int = int(var_cadena)

# La letra f significa que puedes incluir variables y expresiones dentro de las llaves {}
# y su valor será insertado en el texto final.
print("Conversión de cadena a entero.")
print(f"Número como cadena: {var_cadena}.")  # Mostramos la variable como cadena
print(f"Número como int más uno: {var_int + 1}.")  # Convertimos y sumamos 1 al valor entero


# *****   Conversión de cadena a flotante     *****
#convirtiendo a número flotante con la función float().
var_cadena = "8.88"
var_float = float(var_cadena)
print()
print("Conversión de cadena a flotante.")
print(f"Número como cadena: {var_cadena}.")  # Mostramos la variable como cadena
print(f"Número como float más cero punto uno: {var_float + 0.1}.")  # Convertimos y sumamos 0.1 al valor flotante

# *****   Conversión de número a cadena     *****
# Aquí convertimos números (enteros y flotantes) a cadenas utilizando la función str().
var_int = 123
var_float = 123.321
print()
print("Conversión de número a cadena.")
print(f"Los números {var_int} y {var_float} se convierten a cadena utilizando str(var_int): {str(var_int)}, y "
      f"str(var_float): {str(var_float)}.")  # Conversión a cadena y mostrando el resultado

# *****   Conversión a booleano     *****
# La función bool() convierte cualquier valor a booleano. Los valores como 0, cadena vacía ("") o None retornan False.
# Cualquier otro valor regresa True.
print()
print("Conversión a booleanos.")

var_int = 0
es_verdadero = bool(var_int)
print(f"¿El valor de {var_int} es verdadero? {es_verdadero}.")  # 0 se convierte a False
var_int = -30
es_verdadero = bool(var_int)
print(f"¿El valor de {var_int} es verdadero? {es_verdadero}.")  # Cualquier número distinto de 0 es True

var_float = 0.0
es_verdadero = bool(var_float)
print(f"¿El valor de {var_float} es verdadero? {es_verdadero}.")  # 0.0 se convierte a False
var_float = 0.01
es_verdadero = bool(var_float)
print(f"¿El valor de {var_float} es verdadero? {es_verdadero}.")  # Un flotante distinto de 0 es True

var_cadena = ""
es_verdadero = bool(var_cadena)
print(f"¿El valor de '{var_cadena}' es verdadero? {es_verdadero}.")  # Cadena vacía se convierte a False
var_cadena = None
es_verdadero = bool(var_cadena)
print(f"¿El valor de {var_cadena} es verdadero? {es_verdadero}.")  # None se convierte a False
var_cadena = " "
es_verdadero = bool(var_cadena)
print(f"¿El valor de '{var_cadena}' es verdadero? {es_verdadero}.")  # Cadena con un espacio se convierte a True
