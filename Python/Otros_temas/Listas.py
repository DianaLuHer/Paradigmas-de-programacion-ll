"""
Nombre: Diana Belen Luna Hernández
Fecha:
Descripción:
"""
#Lista vacia 
alumno=[]
alumnos=["Amelia","Beto"]
print(alumnos)
#añade un lemento al final de la lista
alumnos.append("Kevin")
print(alumnos)
alumnos.append("Diana")
print(alumnos)
alumnos.insert(3,"Elton") #añade un elemento en un indice especifico
print(alumnos)
alumnos.insert(4,"Magdiel")
alumnos.append("Eden")
alumnos.append("Sergio")
print(alumnos)
alumnos.insert(7,"Magdiel")
alumnos.append("Magdiel")
print(alumnos)
#Borra un elemento por su valor
alumnos.remove("Magdiel")
print(alumnos)
#Borrar por su indice
alumnos.pop(6)
print(alumnos)
#otra manera de eliminar por indice
del alumnos[7]
print(alumnos)
alumnos.len()
alumnos.sort()
alumnos.sort(reverse=True)
