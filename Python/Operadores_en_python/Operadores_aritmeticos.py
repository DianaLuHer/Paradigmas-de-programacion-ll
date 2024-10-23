"""
Diana Belen Luna Hernández
17/10/2024
"""
num1 = int(input("Ingresa el primer número entero: "))
num2 = int(input("Ingresa el segundo número entero: "))

suma = num1+num2
resta = num1-num2
mul= num1*num2
div= num1/num2 #division flotante
mod= num1%num2
exp= num1 ** num2 #exponente
ddiv= num1 // num2 #divicion entera

print(f"El resultado de la suma de {num1} y {num2} es: {suma}")
print(f"El resultado de la resta de {num1} y {num2} es: {resta}")
print(f"El resultado de la multiplicación de {num1} y {num2} es: {mul}")
print(f"El resultado de la división de {num1} y {num2} es: {div:.3f}")
print(f"El resultado del módulo {num1} y {num2} es: {mod}")
print(f"El resultado del esponente de  {num1} y {num2} es: {exp}")
print(f"El resultado de la división entera de {num1} y {num2} es: {ddiv}")





