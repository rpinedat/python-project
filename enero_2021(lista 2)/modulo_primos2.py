
# 1. Escriba la función es_divisible(n, d) que indique si n es divisible por d:
# 2.Usando la función es_divisible,escriba la función es_primo(n) que determine
#   si un número es primo o no.
# 3. Usando la función es_primo, escriba la función i_esimo_primo(i) que entregue el i-ésimo número primo.
# 4. Usando las funciones anteriores, escriba la función primeros_primos(m) que entregue una lista de
#    los primeros m números primos.
# http://progra.usm.cl/apunte/ejercicios/2/funciones-numeros-primos.html
# 5. Usando las funciones anteriores, escriba la función primos_hasta(m) que entregue una lista de los
#   primos menores o iguales que m:

# 1
def es_divisible(x, y):
    res, mod = divmod(x, y)
    if mod == 0:
        return True
    else:
        return False


    # print(es_divisible(15, 5))
# print(es_divisible(15, 6))

# 2
def es_primo(n):
    if n >= 2:
        for i in range(2, n):
            # return not es_divisible(n, i)
            if es_divisible(n, i):
                return False

        return True
    else:
        return False



# print("es primo", es_primo(2))

# 3

def i_esimo_primo(i):
    count = 0
    j = 2
    while count < i:

        if es_primo(j):

            count = count + 1
            j = j+ 1
        else:

            j = j + 1

    return j - 1


# print(i_esimo_primo(2))


# 4

def primeros_primos(m):
    count = 0
    j = 2
    lista_primos = []
    while count < m:

        if es_primo(j):
            # print(j)
            count = count + 1
            lista_primos.append(j)
            j = j + 1
        else:
            # print(j)
            j = j + 1

    return lista_primos


# print(primeros_primos(25))


# 5
def primos_hasta(m):
    count = 0
    j = 2
    lista_primos = []
    while j <= m:

        if es_primo(j):
            # print(j)
            count = count + 1
            lista_primos.append(j)
            j = j + 1
        else:
            # print(j)
            j = j + 1

    return lista_primos


