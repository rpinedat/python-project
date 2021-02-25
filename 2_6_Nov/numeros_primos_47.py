# http://progra.usm.cl/apunte/ejercicios/1/numeros-primos.html

# Escriba un programa que reciba como entrada un número natural,
# e indique si es primo o compuesto
i = int()
num = int(input("Ingrese un número: "))

for i in range(2, num):

    x, y = divmod(num, i)

    if y == 0:
        print("Es compuesto")
        break


    else:
        print("Es primo", num)
        break
