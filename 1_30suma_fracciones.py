# Desarrolle un programa que permita trabajar con las potencias fraccionales de dos, es decir:
# El programa debe mostrar tres columnas que contengan la siguiente información:
# El programa debe terminar cuando la fracción decimal sea menor o igual a 0.000001.
# n = int(input("Escriba n: "))
i = 1
j = 1
p = 1
suma = float()
print("potencia         Fraccion               Suma")
while p >= .0001:
    j = j * 2
    p = j**-1
    suma = suma + p
    i = i + 1
    tupla = i-1,  p, suma
    print("  {:<15}  {:^1}  {:>20}  ".format(i-1, p, suma)) 
