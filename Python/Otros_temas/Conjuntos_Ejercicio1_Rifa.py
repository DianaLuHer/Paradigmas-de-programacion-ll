"""
Nombre: Diana Belen Luna Hernández
Fecha:
Descripción: Este programa que gestiona una rifa.
"""

"""
Un conjunto es una colección desordenada de valores no repetidos. 
"""

# Importa la biblioteca 'random'.
import random

# Define un conjunto vacío para almacenar los nombres de los participantes
participantes = set()

def menu():
    print("-------------------------------------------------")
    print("--- 1.- Ver participantes                     ---")
    print("--- 2.- Añadir participante                   ---")
    print("--- 3.- Eliminar participante                 ---")
    print("--- 4.- Seleccionar ganador                   ---")
    print("--- 5.- Salir                                 ---")
    print("-------------------------------------------------")

# Función para realizar las operaciones según la opción seleccionada
def operaciones(opcion):
    if opcion == 1:  # Opción para ver la lista de participantes
        print("**** Ver participantes ****")
        total_participantes = len(participantes)  # Cuenta el total de participantes
        if total_participantes > 0:
            print(f"Actualmente hay {total_participantes} participante(s):")  # Muestra la cantidad
            for persona in participantes:  # Itera sobre cada participante
                print(f"- {persona}")  # Imprime cada participante
        if total_participantes == 0:
            print("No hay participantes en la lista.")

    if opcion == 2:  # Opción para añadir un participante
        print("**** Añadir participante ****")
        persona = input("Añade un nuevo participante: ")  # Solicita el nombre del participante
        if persona:  # Si se ingresó un nombre
            participantes.add(persona)  # Añade el nombre al conjunto
            print(f"'{persona}' ha sido añadido al conjunto de participantes.")

    if opcion == 3:  # Opción para eliminar un participante
        print("**** Eliminar participante ****")
        persona = input("Ingresa el nombre del participante que deseas eliminar: ")  # Solicita el nombre
        if persona in participantes:  # Si el participante existe en el conjunto
            participantes.remove(persona)  # Elimina el nombre del conjunto
            print(f"'{persona}' ha sido eliminado de la rifa.")
        if persona not in participantes:
            print(f"'{persona}' no se encuentra entre los participantes.")

    if opcion == 4:  # Opción para seleccionar un ganador
        print("**** Seleccionar ganador ****")
        if participantes:  # Si hay participantes en el conjunto
            ganador = random.choice(list(participantes))  # Convierte el conjunto en lista y selecciona un elemento aleatorio
            print(f"¡El ganador es: {ganador}!")  # Muestra el ganador
        if not participantes:
            print("No hay participantes para elegir un ganador.")

def main():
    print("********** Rifa de Participantes **********")
    continuar = True  # Bandera para controlar el bucle principal

    while continuar:  # Mientras la bandera esté activa
        menu()  # Muestra el menú de opciones
        opcion = int(input("Seleccione la opción que desee realizar: "))  # Solicita la opción al usuario y asume que será un número entero
        if opcion == 5:
            print("Saliendo del programa...")
            continuar = False  # Cambia la bandera para salir del bucle
        if 1 <= opcion <= 4:  # Si la opción está dentro del rango válido
            operaciones(opcion)  # Llama a la función que ejecuta la operación correspondiente


main()
