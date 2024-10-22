'''
Nombre: Diana Belen Luna Hernández
Fecha: 15 de octubre del 2024
Descripción:
Entrada de datos por consola para interacturar con el usuario con valores dinámicos, los números son leídos como cadenas de texto, por lo que al sumar estos valores sin hacer un casting a un tipo numérico.
'''
# La función input permite al usuario introducir datos por consola.
numero1_cadena = input("Introduce un número decimal: ") #Lee el primer número
numero2_cadena = input("Introduce otro número decimal: ") #Lee el sengundo número
# Aquí se está concatenando (uniendo) las dos cadenas introducidas por el usuario.
# Al no hacer un casting de tipos de variables, las dos cadenas se tratan como texto.
resultado_cadena = numero1_cadena + numero2_cadena # Verificar qué es lo que realiza esta instrucción (ver el print).
print()
print(" ****  Recibir número sin un casting de varibles  ****")
# Muestra las dos cadenas concatenadas.
print(f"El resultado de {numero1_cadena} y {numero2_cadena} es: {resultado_cadena}")

# El "casting" de variables convierte una variable de un tipo a otro.
# se convierte la cadena introducida por el usuario a un tipo de dato flotante .
numero1_float = float(numero1_cadena)
numero2_float = float(numero2_cadena)
# Aquí, los valores convertidos se suman como números reales, no como texto.
resultado_float = numero1_float + numero2_float # Verificar qué es lo que realiza de esta manera y compáralo.
print()
print(" ****  Casting de varibles  ****")
# Muestra el resultado de la suma de los dos números decimales.
print(f"El resultado de {numero1_float} y {numero2_float} es: {resultado_float}")

