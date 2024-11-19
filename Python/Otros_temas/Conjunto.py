"""
Nombre:
"""


#Conjunto vacio
conjunto1=set()
conjunto2={10,5,24,11,8,7,21,9}
print(conjunto2)
#Añadir elementos
conjunto1.add(80)
conjunto1.add(111)
conjunto1.add(10)
conjunto1.add(5)
conjunto1.add(24)
print(conjunto1)
conjunto1.add(80)
print(conjunto1)
#el REMOVE funciona unicamente si el elemento existe
conjunto1.remove(111)
#Tambien es para borrar, solo que no genera error si el dato no existe
conjunto1.discard(111)
conjunto1.discard(10)
print(conjunto1)
conjunto_union=conjunto1|conjunto2
print(conjunto_union)
conjunto_interseccion=conjunto1&conjunto2
print(conjunto_interseccion)
resta_conjuntos=conjunto2-conjunto1
print(resta_conjuntos)

alumnos_lista=["Beto","Kevin","Elton","Diana","Chendo","Amelia","Sergio"]
alumnos_lista.append("Elton")
#Transforma una lista a un conjunto
alumnos_conjunto=set(alumnos_lista)
print(alumnos_lista)
print(alumnos_conjunto)
print()

nombre=input("Ingrese su nombre: ")
#strip Remueve los espacios iniciales y finales
#Lower transforama los caracteres de mayuscula a minuscula
nombre=nombre.strip().lower()
if nombre in alumnos_conjunto: #Revisa que nombre esté en alumnos_conjuntos
    print("Se encuentra en el conjunto")
else:
    print("Se añadió al conjunto")
alumnos_conjunto.add(nombre)



