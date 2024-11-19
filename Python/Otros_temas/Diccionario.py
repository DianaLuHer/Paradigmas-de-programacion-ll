"""
Se almacenan en forma de key-valor
diccionario tambien se almacena en llaves
"""
#diccionario={'key1':valor1,'key2':valor2}

profesor={'nombre':"alberto",'correo':"alberto.mtba@unsij.com",'cubo':"12"}
print(profesor)

correo=profesor.get("correo")
cubo=profesor["nombre"]

print(correo)
print(cubo)