"""
Nombre: Diana Belen Luna Hernández
Fecha: 12/11/2024
Descripción:
"""



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
    elif opcion==2:
        print("**** Lista de películas de la A-Z****")
    elif opcion==3:
        print("****Lista de películas de la Z-A****")
    elif opcion==4:
        print("****Añade una película****")
    elif opcion==5:
        print("****Añade varias películas****")
    elif opcion==6:
        print("****Elimina una película****")

def main():
    print("**********Lista de películas por ver**********")
    while True:
        menu()
        opcion=int(input("Seleccione la opción que desee realizar: "))

        if opcion == 0:
            print("Saliendo del programa...")
            break

    

main()