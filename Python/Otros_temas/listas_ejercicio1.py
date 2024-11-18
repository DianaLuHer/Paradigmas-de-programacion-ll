"""
Nombre: Diana Belen Luna Hernández
Fecha: 12/11/2024
Descripción:
"""
peliculas=[]
def menu ():
    # Función que muestra el menú de opciones
    print("-------------------------------------------------")
    print("--- 1.- Ver películas por ver                 ---")
    print("--- 2.- Ver películas por ver en orden A-Z    ---")
    print("--- 3.- Ver películas por ver en orden Z-A    ---")
    print("--- 4.- Añade una película por ver            ---")
    print("--- 5.- Añadir varias películas               ---")
    print("--- 6.- Eliminar                              ---")
    print("--- 0.- Salir                                 ---")
    print("-------------------------------------------------")

def operaciones (opcion):

    if opcion==1:
        print("**** Lista de películas ****")
        if peliculas:
            for pelicula in peliculas:
                print(pelicula)
        else:
            print("No hay películas en la lista.")

    elif opcion==2:
        print("**** Lista de películas de la A-Z****")
        if peliculas:
            for pelicula in sorted(peliculas):
                print(pelicula)
        else:
            print("No hay películas en la lista.")

    elif opcion==3:
        print("****Lista de películas de la Z-A****")
        if peliculas:
            for pelicula in sorted(peliculas, reverse=True):
                print(pelicula)
        else:
            print("No hay películas en la lista.")
    elif opcion==4:
        print("****Añade una película****")
        pelicula=input("Añade una nueva pelicula: ")
        peliculas.append(pelicula)
        print(f"La pelicula '{pelicula}' fue añadida a la lista")

    elif opcion==5:
        print("****Añade varias películas****")
        num_peliculas = int(input("Ingrese el número de peliculas que desee agregar: "))
        for pelis in range(num_peliculas):
            pelicula=input("Ingrese el numbre de la pelicula: ")
            peliculas.append(pelicula)
        print(f"{num_peliculas} han sido añadidas a la lista...")

    elif opcion==6:
        print("****Elimina una película****")
        pelicula = input("Ingresa el nombre de la pelicula que desea eliminar: ")
        if pelicula in peliculas:
            peliculas.remove(pelicula)
            print(f"La pelicula '{pelicula}' ha sido eliminada de la lista")
        else:
            print(f"La pelicula '{pelicula}' no existe en la lista")

def main():
    print("********** Lista de películas por ver **********")
    continuar = True  # Bandera para controlar el bucle

    while continuar:
        menu()
        opcion = input("Seleccione la opción que desee realizar: ")

        if opcion == 0:
            print("Saliendo del programa...")
            continuar = False  # Cambia la bandera para salir del bucle
        elif 1 <= opcion <= 6:
            operaciones(opcion)  # Llama a la función correspondiente
        else:
            print("La opción no es válida. Por favor, ingrese un número entre 0 y 6.")

main()
