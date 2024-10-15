"""
Diana Belen Luna Hernández.
07 de septiembre del 2024
Ejercicio del tema TIPO DE DATOS.
"""

# Día 1
#Detalles de los gastos
dia1 = "lunes" #Nombre del dia
pasaje1 = 20  #Gasto de pasaje del dia lunes
comida1 = 135.5 #Gasto de comida del dia lunes
otros_gastos1 = 34.5 #Otros gastos para el dia lunes
presupuesto = 150 #El presupuesto maximo

print("*** Gastos diarios ***")
print(f"Día: {dia1}") #Imprimimos el dia
print(f"Pasaje: {pasaje1}") #Imprimimos el gasto de pasaje
print(f"Comida: {comida1}") #Imprimimos el gasto de comida
print(f"Otros gastos: {otros_gastos1}") #Imprimimos los otros gastos

# Calculamos el total de gastos del día 1 sumando pasaje, comida y otros gastos
total_gastos1 = pasaje1 + comida1 + otros_gastos1
print(f"¿Fue mayor a mi presupuesto?: {total_gastos1 > presupuesto}") # Imprimimos el resultado (True/False)
print()

# Día 2
dia2 = "martes"  # Nombre del día
pasaje2 = 12  # Gasto en pasaje para el dia martes
comida2 = 45.5  # Gasto en comida para el dia martes
otros_gastos2 = 4.5  # Otros gastos para el dia martes

print("*** Gastos diarios ***")
print(f"Día: {dia2}")  # Imprimimos el día
print(f"Pasaje: {pasaje2}")  # Imprimimos el gasto en pasaje
print(f"Comida: {comida2}")  # Imprimimos el gasto en comida
print(f"Otros gastos: {otros_gastos2}")  # Imprimimos los otros gastos

# Calculamos el total de gastos del día 2 sumando pasaje, comida y otros gastos
total_gastos2 = pasaje2 + comida2 + otros_gastos2

# Verificamos si los gastos totales del día 2 superan el presupuesto
print(f"¿Fue mayor a mi presupuesto?: {total_gastos2 > presupuesto}")  # Imprimimos el resultado (True/False)