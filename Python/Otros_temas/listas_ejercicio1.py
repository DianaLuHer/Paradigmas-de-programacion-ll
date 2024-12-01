"""
Nombre: Diana Belen Luna Hernández
Fecha: 12/11/2024
Descripción: Este programa gestiona una lista de películas por ver mediante un menú.
"""

"""
Una lista es una estructura de datos que organiza y almacena elementos de manera secuencial 
y ordenada. Las listas permiten almacenar múltiples valores bajo un solo nombre y acceder 
a ellos mediante índices.
"""

# Se define una lista vacía para almacenar las películas pendientes por ver
peliculas = []

# Función que muestra el menú de opciones disponibles
def menu():
    # Muestra las opciones del menú numeradas del 1 al 6 y la opción para salir
    print("-------------------------------------------------")
    print("--- 1.- Ver películas por ver                 ---")
    print("--- 2.- Ver películas por ver en orden A-Z    ---")
    print("--- 3.- Ver películas por ver en orden Z-A    ---")
    print("--- 4.- Añade una película por ver            ---")
    print("--- 5.- Añadir varias películas               ---")
    print("--- 6.- Eliminar                              ---")
    print("--- 0.- Salir                                 ---")
    print("-------------------------------------------------")

# Función que realiza las operaciones según la opción seleccionada
def operaciones(opcion):
    # Opción 1: Ver la lista de películas
    if opcion == 1:
        print("**** Lista de películas ****")
        if peliculas:  # Comprueba si la lista tiene elementos
            for pelicula in peliculas:  # Itera sobre cada película en la lista
                print(pelicula)  # Imprime cada película
        else:
            print("No hay películas en la lista.")  # Mensaje si la lista está vacía

    # Opción 2: Ver la lista de películas ordenadas de la A a la Z
    elif opcion == 2:
        print("**** Lista de películas de la A-Z****")
        if peliculas:  # Comprueba si la lista tiene elementos
            for pelicula in sorted(peliculas):  # Ordena la lista alfabéticamente
                print(pelicula)  # Imprime cada película ordenada
        else:
            print("No hay películas en la lista.")

    # Opción 3: Ver la lista de películas ordenadas de la Z a la A
    elif opcion == 3:
        print("****Lista de películas de la Z-A****")
        if peliculas:  # Comprueba si la lista tiene elementos
            for pelicula in sorted(peliculas, reverse=True):  # Ordena la lista en orden inverso
                print(pelicula)  # Imprime cada película ordenada
        else:
            print("No hay películas en la lista.")

    # Opción 4: Añadir una nueva película a la lista
    elif opcion == 4:
        print("****Añade una película****")
        pelicula = input("Añade una nueva película: ")  # Solicita al usuario el nombre de la película
        peliculas.append(pelicula)  # Agrega la película al final de la lista
        print(f"La película '{pelicula}' fue añadida a la lista.")

    # Opción 5: Añadir varias películas a la lista
    elif opcion == 5:
        print("****Añade varias películas****")
        num_peliculas = int(input("Ingrese el número de películas que desee agregar: "))  # Solicita el número de películas a agregar
        for i in range(num_peliculas):  # Itera tantas veces como el número ingresado
            pelicula = input("Ingrese el nombre de la película: ")  # Solicita el nombre de cada película
            peliculas.append(pelicula)  # Agrega cada película a la lista
        print(f"{num_peliculas} películas han sido añadidas a la lista...")

    # Opción 6: Eliminar una película de la lista
    elif opcion == 6:
        print("****Elimina una película****")
        pelicula = input("Ingresa el nombre de la película que desea eliminar: ")  # Solicita el nombre de la película a eliminar
        if pelicula in peliculas:  # Comprueba si la película está en la lista
            peliculas.remove(pelicula)  # Elimina la película de la lista
            print(f"La película '{pelicula}' ha sido eliminada de la lista.")
        else:
            print(f"La película '{pelicula}' no existe en la lista.")

def main():
    print("********** Lista de películas por ver **********")
    continuar = True  # Bandera para controlar el bucle del programa

    # Bucle principal para mostrar el menú y gestionar las opciones
    while continuar:
        menu()  # Llama a la función que muestra el menú
        opcion = int(input("Seleccione la opción que desee realizar: "))  # Solicita la opción al usuario y la convierte en entero

        if opcion == 0:  # Opción para salir del programa
            print("Saliendo del programa...")
            continuar = False  # Cambia la bandera para detener el bucle
        elif 1 <= opcion <= 6:  # Verifica que la opción esté entre las válidas
            operaciones(opcion)  # Llama a la función que ejecuta la operación seleccionada
        else:
            print("La opción no es válida. Por favor, ingrese un número entre 0 y 6.")

main()
