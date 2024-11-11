"""
Nombre: Diana Belen Luna Hernández
Fecha: 07/11/2024
Descripción:Este código realiza la función de una calculadora básica, mediante el lladado de funciones al main
"""

"""
Las funciones en programación son bloques de código que se utilizan para realizar una tarea específica.
una función permite agrupar un conjunto de instrucciones bajo un nombre, de modo que puedes ejecutar esa 
tarea simplemente llamando a la función por su nombre. Esto facilita mucho la organización y reutilización 
del código en programas grandes.
"""


def menu():
    #Función que muestra el menú de opciones
    print("------------------------------")
    print("--- 1.- Suma               ---")
    print("--- 2.- Resta              ---")
    print("--- 3.- Multiplicación     ---")
    print("--- 4.- División           ---")
    print("--- 0.- Salir              ---")
    print("------------------------------")

#Función que realiza la operación seleccionada
def operaciones(opcion, numero1, numero2):
    # Selecciona la operación según la opción ingresada retornando lo operacion realizada
    if opcion == 1:
        return numero1 + numero2
    elif opcion == 2:
        return numero1 - numero2
    elif opcion == 3:
        return numero1 * numero2
    elif opcion == 4:
        return numero1 / numero2
    else:
        return "Opción no válida."


def main():
    print("Bienvenido a la calculadora.")

    while True:
        #Muestra el menú de opciones llamando a la función menú
        menu()
        #Solicita al usuario la opcion que desee realizar
        opcion = int(input("Selecciona la opción que desee realizar: "))

        #Si la opción es 0 el programa termina
        if opcion == 0:
            print("Saliendo del programa...")
            break
        #Solicita lo números para realizar la operación
        numero1 = float(input("Ingresa el número 1: "))
        numero2 = float(input("Ingresa el número 2: "))

        #Llama a la función operaciones y muestra el resultado
        resultado = operaciones(opcion, numero1, numero2)
        print("Resultado:", resultado)

# Llamada al main para iniciar el programa
main()
