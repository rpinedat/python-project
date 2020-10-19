# Genera desde la 0-ésima potencia de 2 hasta la ingresada

num_veces = int(input("Ingrese numero entero: "))
for i in range(num_veces+1):
    x = pow(2, i)
    print(x)


