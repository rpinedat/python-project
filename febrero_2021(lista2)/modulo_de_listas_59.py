# Desarrolle un módulo llamado listas.py que contenga las siguientes funciones.
# http://progra.usm.cl/apunte/ejercicios/2/modulo-listas.html


# 1. Una función promedio(l), cuyo parámetro l sea una lista de números
# reales, y que entregue el promedio de los números:


def promedio(l):
    res = 0
    long = len(l)
    for i in l:
        res = res + i
    return print(res / long)


#promedio([1, 2, 3, 4, 5, 9.9])

# 2. Una función cuadrados(l), que entregue una lista con los cuadrados de los valores de l:


def cuadrados(l):

    list2 = []
    for i in l:
        res = i*i
        list2.append(res)

    return print(list2)


#cuadrados([2, 3, 8, 3])

# Una función mas_largo(palabras), cuyo parámetro palabras es una lista de strings,
# que entregue cuál es el string más largo


def mas_largo(palabras):
    long = len(palabras)
    a = 0

    print(long)
    list2 = []
    for i in palabras:
        long_p = len(i)
        if long_p > a:
            a = long_p
            list2.append(i)

    return print(list2.pop())


#mas_largo(["**", "*", "********", "*****"])
