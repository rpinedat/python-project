# desarrolla un programa que calcule el siguiente par de números amistosos que se encuentre
# en el rango de [100,1500]
# http://progra.usm.cl/apunte/ejercicios/1/numeros-amistosos.html
# Rocio Pineda

lista_divisores = list()


def divisores(var):

    suma = 0
    for i in range(1, var):
        divisor, res = divmod(var, i)
        if res == 0:
            suma = i + suma
            lista_divisores.append(divisor)

    return suma


def compara(var_1, var_2):
    divisores(var_2)

    if var_1 == divisores(var_2):
        print(var_1, "y", divisores(var_2), "Son números amigos")


for j in range(100, 1501):
    compara(j, divisores(j))
    j = j+1
