"""
Nombre: Diana Belen Luna Hernández
Fecha:
Descripción: Este programa gestiona una rifa, almacena los ganadores en un archivo y permite visualizar los ganadores previos.
"""

# Importa la biblioteca 'random'.
import random
from datetime import datetime

# Define un conjunto vacío para almacenar los nombres de los participantes
participantes = set()

# Nombre del archivo donde se guardarán los ganadores
ARCHIVO_RIFA = "archivo_rifa.txt"

# Función para mostrar el menú
def menu():
    print("-------------------------------------------------")
    print("--- 1.- Ver participantes                     ---")
    print("--- 2.- Añadir participante                   ---")
    print("--- 3.- Eliminar participante                 ---")
    print("--- 4.- Seleccionar ganador                   ---")
    print("--- 5.- Mostrar ganadores previos            ---")
    print("--- 6.- Salir                                 ---")
    print("-------------------------------------------------")

# Función para inicializar el archivo con el encabezado "GANADORES" si no existe
def inicializar_archivo():
    try:
        archivo = open(ARCHIVO_RIFA, "r", encoding="utf-8")
        contenido = archivo.read()
        archivo.close()
        if not contenido.startswith("GANADORES"):
            raise FileNotFoundError  # Forzamos la reescritura del encabezado si no está
    except FileNotFoundError:
        try:
            archivo = open(ARCHIVO_RIFA, "w", encoding="utf-8")
            archivo.write("********GANADORES********\n")
            archivo.close()
        except Exception as e:
            print(f"Error al inicializar el archivo: {e}")

# Función para escribir un ganador en el archivo
def registrar_ganador(ganador):
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        archivo = open(ARCHIVO_RIFA, "a", encoding="utf-8")
        archivo.write(f"{fecha_actual} - {ganador}\n")  # Guarda la fecha junto con el ganador
        archivo.close()
        print(f"El ganador '{ganador}' ha sido registrado en el archivo.")
    except Exception as e:
        print(f"Error al escribir en el archivo: {e}")

# Función para leer y mostrar los ganadores desde el archivo
def mostrar_ganadores():
    try:
        archivo = open(ARCHIVO_RIFA, "r", encoding="utf-8")
        ganadores = archivo.readlines()
        archivo.close()
        if len(ganadores) > 1:  # Comprueba que haya ganadores más allá del encabezado
            print("**** Ganadores previos ****")
            for i, ganador in enumerate(ganadores[1:], start=1):  # Ignora el encabezado
                print(f"{i}. {ganador.strip()}")
        else:
            print("No hay ganadores registrados todavía.")
    except FileNotFoundError:
        print("El archivo de ganadores no existe. No hay ganadores registrados.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")

# Función para realizar las operaciones según la opción seleccionada
def operaciones(opcion):
    if opcion == 1:  # Opción para ver la lista de participantes
        print("**** Ver participantes ****")
        total_participantes = len(participantes)  # Cuenta el total de participantes
        if total_participantes > 0:
            print(f"Actualmente hay {total_participantes} participante(s):")  # Muestra la cantidad
            for persona in participantes:  # Itera sobre cada participante
                print(f"- {persona}")  # Imprime cada participante
        else:
            print("No hay participantes en la lista.")

    elif opcion == 2:  # Opción para añadir un participante
        print("**** Añadir participante ****")
        persona = input("Añade un nuevo participante: ")  # Solicita el nombre del participante
        if persona:  # Si se ingresó un nombre
            participantes.add(persona)  # Añade el nombre al conjunto
            print(f"'{persona}' ha sido añadido al conjunto de participantes.")

    elif opcion == 3:  # Opción para eliminar un participante
        print("**** Eliminar participante ****")
        persona = input("Ingresa el nombre del participante que deseas eliminar: ")  # Solicita el nombre
        if persona in participantes:  # Si el participante existe en el conjunto
            participantes.remove(persona)  # Elimina el nombre del conjunto
            print(f"'{persona}' ha sido eliminado de la rifa.")
        else:
            print(f"'{persona}' no se encuentra entre los participantes.")

    elif opcion == 4:  # Opción para seleccionar un ganador
        print("**** Seleccionar ganador ****")
        if participantes:  # Si hay participantes en el conjunto
            ganador = random.choice(list(participantes))  # Convierte el conjunto en lista y selecciona un elemento aleatorio
            print(f"¡El ganador es: {ganador}!")  # Muestra el ganador
            registrar_ganador(ganador)  # Registra al ganador en el archivo
            participantes.remove(ganador)  # Elimina al ganador del conjunto de participantes
        else:
            print("No hay participantes para elegir un ganador.")

    elif opcion == 5:  # Opción para mostrar ganadores previos
        mostrar_ganadores()

def main():
    print("********** Rifa de Participantes **********")
    inicializar_archivo()  # Asegura que el archivo tenga el encabezado
    continuar = True  # Bandera para controlar el bucle principal

    while continuar:  # Mientras la bandera esté activa
        menu()  # Muestra el menú de opciones
        try:
            opcion = int(input("Seleccione la opción que desee realizar: "))  # Solicita la opción al usuario
            if opcion == 6:
                print("Saliendo del programa...")
                continuar = False  # Cambia la bandera para salir del bucle
            elif 1 <= opcion <= 5:  # Si la opción está dentro del rango válido
                operaciones(opcion)  # Llama a la función que ejecuta la operación correspondiente
            else:
                print("Por favor, seleccione una opción válida.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

# Ejecuta el programa principal
main()
