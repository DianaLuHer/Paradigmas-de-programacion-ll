"""
Nombre: Diana Belen Luna Hernández
Fecha: 19/10/2024
Descripción: Este programa determina si el usuario aplica para una bonificación del Buen Fin.
"""

print("--------- Buen fin ---------")
# Solicita al usuario ingresar la cantidad gastada y la convierte en un valor flotante
cantidad = float(input("Ingresa la cantidad gastada: "))

# Verifica si la cantidad es mayor a 5000 para determinar si cumple con el primer requisito de bonificación
comprobacion = bool(cantidad > 5000)
# Pregunta al usuario si la compra fue realizada a meses sin intereses y convierte la respuesta a minúsculas
MSI = input("¿La compra fue a meses sin intereses?: ")
# Convierte la respuesta en un valor booleano
compraMSI = MSI.lower() == "si"
# Imprime si el usuario aplica para la bonificación, basada en que la compra sea mayor a 5000 y a meses sin intereses
print(f"¿Aplica bonificación de buen fin?: {comprobacion and compraMSI}")
