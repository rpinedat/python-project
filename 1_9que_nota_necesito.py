# Programa que saca el promedio de una calificación final
# que consta de el promedio de 3 calificaciones que son el30%
# y la calificación del laboratorio que es el 70% de la califciación final
# El alumno ingresará solo dos calificaciones y el laboratorio
# el programa dirá cual debe ser el mínimo en su 3era calificación
# para pasarla materia.
nota_1 = int(input("ingrese nota de certamen 1: "))
nota_2 = int(input("ingrese nota de certamen 2: "))
nota_lab = int(input("ingrese nota de laboratorio: "))
nota_min = float
nota_prom = ((nota_1+nota_2)/3)  # Nota promedio de 3 calif
nota_final = ((nota_prom*.7)+(nota_lab*.3))  # Nota final
if nota_final >= 60:
    print("felicidades,ya pasaste la materia con un mínimo de: ", nota_final)
else:
    prom_min = 60-(nota_lab * .3)  # Busca promedio minimo de las 3 calif
    divide = float(prom_min / .7)  # operación inversa para despejar c3_int
    calf_min_final = int((divide*3)-(nota_1+nota_2))
    print("La calificación mínima que debes obtener es:", calf_min_final)
