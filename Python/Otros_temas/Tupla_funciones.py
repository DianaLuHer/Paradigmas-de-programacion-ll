def promedio_FINAL_funcion(cp1, cp2, cp3, ordinario):
    promedioParcial = (cp1 + cp2 + cp3) / 3
    promedioFinal = (promedioParcial + ordinario) / 2
    return promedioParcial, promedioFinal


# Código a nivel de módulo
print("*********** CALIFICACIONES DE PARCIAL *************")
cp1 = float(input("Ingresa la calificación de PRIMER parcial: "))
cp2 = float(input("Ingresa la calificación de SEGUNDO parcial: "))
cp3 = float(input("Ingresa la calificación de TERCER parcial: "))
ordinario = float(input("Ingresa la calificación de ORDINARIO: "))

print()
promedioParcial,promedioFinal = promedio_FINAL_funcion(cp1, cp2, cp3, ordinario)
print(f"Tu promedio parcial es {promedioParcial:.2f} y tu promedio final es {promedioFinal:.2f}")