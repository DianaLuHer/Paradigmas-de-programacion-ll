"""
Nombre: Diana Belen Luna Hernández
Fecha: 17/10/2024
Descripción: Este programa realiza operaciones matemáticas básicas entre dos números enteros.
"""
#Solicita al usuario que ingresen los números, especificando que sean enteros.
num1,num2 = int(input("Ingresa el primer número entero: ")),int(input("Ingresa el segundo número entero: "))

suma = num1+num2 # Realiza la suma entre número1 y número2.
resta = num1-num2 # Realiza la resta entre número1 y número 2.
mul= num1*num2 # Realiza la multiplicación entre número1 y número 2.
div= num1/num2 # Realiza la división flotante entre número1 y número 2.
mod= num1%num2 # Realiza el módulo (resto de la división) entre num1 y num2
exp= num1 ** num2 # Calcula el exponente (número1 elevado a la número2)
ddiv= num1 // num2 # Realiza la división entera entre num1 y num2

print(f"El resultado de la suma de {num1} y {num2} es: {suma}") #Imprime el resultado de la suma.
print(f"El resultado de la resta de {num1} y {num2} es: {resta}")#Imprime el resultado de la resta.
print(f"El resultado de la multiplicación de {num1} y {num2} es: {mul}") #Imprime el resultado de la multiplicación.
print(f"El resultado de la división de {num1} y {num2} es: {div:.3f}")#Imprime el resultado de la división flotante.
print(f"El resultado del módulo {num1} y {num2} es: {mod}") #Imprime el resultado del módulo.
print(f"El resultado del esponente de  {num1} y {num2} es: {exp}") #Imprime el resultado del exponente.
print(f"El resultado de la división entera de {num1} y {num2} es: {ddiv}") #Imprime el resultado de la división entera .





