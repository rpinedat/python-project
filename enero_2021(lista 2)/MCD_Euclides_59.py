# Realice un programa que obtenga el máximo común divisor con el algoritmo de Euclides
# https://www.superprof.es/apuntes/escolar/matematicas/aritmetica/divisibilidad/algoritmo-de-euclides.html
# https://stackoverrun.com/es/q/891555 (intersecion de listas) checar
# Rocio Pineda Tecpa

def euclides(num1, num2):
    mod = 1
    if num1 > num2:
        num_mayor = num1
        num_menor = num2

    else:
        num_mayor = num2
        num_menor = num1

    while mod != 0:

        res, mod = divmod(num_mayor, num_menor)

        num_mayor = num_menor
        num_menor = mod
    print("el mcd por euclides de", num1, "y", num2, "es: ", num_mayor)

# Aquí empieza el otro programa que realiza el MCD de forma típica como se calcula


def divisores(x):  # primero hago una función que saque los divisores de un número
    list_divisores = []
    y = 2
    while x != 1:
        res, mod = divmod(x, y)
        if mod == 0:
            x = res
            list_divisores.append(y)
        else:
            y = y+1
    return list_divisores


# print(divisores(10))

# print("divisores", divisores(5, 12))
# print(divisores(9, 6))
euclides(20, 50)
euclides(31, 19)


def mcd(num1, num2):

    list_num3 = []
    list_num1 = divisores(num1)
    list_num2 = divisores(num2)
    res = 1

    # print("lista1", list_num1)
    # print("lista2", list_num2)

    for i in list_num1:
        if i in list_num2:
            list_num3.append(i)
            res = res * i
            list_num2.remove(i)
            # print("Lista 3", list_num3)
            # print ("Res", res)

    print("El mcd de", num1, "y", num2, "es: ", res)


mcd(50, 20)
