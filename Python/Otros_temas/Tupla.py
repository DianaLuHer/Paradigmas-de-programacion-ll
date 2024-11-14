

#A una tupla no se le pueden hacer modificaciones, como insertar, eliminar
#Creación de una tupla

calificaciones_parcial1=(9.6,6.3,6.0,8.7,5.0) #Se definen calificaciones
poo,bd,redes,arq,ing_soft=calificaciones_parcial1 #Asignación múltiple
print(calificaciones_parcial1) #Imprime las calificaciones
#Impresión de tupla
#range-secuencia

for calificacion in calificaciones_parcial1:
    print(calificacion,end=" ")

    #Promedio
    #sum= funcion para realizar la suma suma de una tupla
    # Len Determina el tamaño de la Tupla

promedio_parcial=sum(calificaciones_parcial1)/len(calificaciones_parcial1)
print()
print(f"Promedio:{promedio_parcial}")