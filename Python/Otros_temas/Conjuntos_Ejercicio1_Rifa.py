import random  # Importar la biblioteca para elegir al azar

# Conjunto para almacenar los participantes
participantes = set()

def menu():
    # Función que muestra el menú de opciones
    print("-------------------------------------------------")
    print("--- 1.- Ver participantes                     ---")
    print("--- 2.- Añadir participante                   ---")
    print("--- 3.- Eliminar participante                 ---")
    print("--- 4.- Seleccionar ganador                   ---")
    print("--- 5.- Salir                                 ---")
    print("-------------------------------------------------")

def operaciones(opcion):
    if opcion == 1:
        print("**** Ver participantes ****")
        total_participantes = len(participantes)  # Almacena el total de participantes
        if total_participantes > 0:
            print(f"Actualmente hay {total_participantes} participante(s):")
            for persona in participantes:
                print(f"- {persona}")
        else:
            print("No hay participantes en la lista.")
    elif opcion == 2:
        print("**** Añadir participante ****")
        persona = input("Añade un nuevo participante: ")
        if persona:
            participantes.add(persona)
            print(f"'{persona}' ha sido añadido al conjunto de participantes.")

    elif opcion == 3:
        print("**** Eliminar participante ****")
        persona = input("Ingresa el nombre del participante que deseas eliminar: ")
        if persona in participantes:
            participantes.remove(persona)
            print(f"'{persona}' ha sido eliminado de la rifa.")
        else:
            print(f"'{persona}' no se encuentra entre los participantes.")

    elif opcion == 4:
        print("**** Seleccionar ganador ****")
        if participantes:
            ganador = random.choice(list(participantes))  # Conversión explícita a lista
            print(f"¡El ganador es: {ganador}!")
        else:
            print("No hay participantes para elegir un ganador.")
def main():
    print("********** Rifa de Participantes **********")
    continuar = True  # Bandera para controlar el bucle

    while continuar:
        menu()
        try:
            opcion = int(input("Seleccione la opción que desee realizar: "))
            if opcion == 5:
                print("Saliendo del programa...")
                continuar = False  # Cambia la bandera para salir del bucle
            elif 1 <= opcion <= 4:
                operaciones(opcion)  # Llama a la función correspondiente
            else:
                print("La opción no es válida. Por favor, ingrese un número entre 1 y 5.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

# Ejecutar el programa
main()
