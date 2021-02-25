# Escriba un programa llamado mersenne.py que pregunte al usuario un número n,
# y muestre como salida los primeros n primos de Mersenne:

from modulo_primos2 import es_primo
# i_esimo_primo, primeros_primos, primos_hasta


def mersenne(n):
    count = 0
    j = 2
    while count < n:
        if es_primo(j):
            mers = pow(2, j) - 1
            if es_primo(mers):
                print("", mers)
                count = count + 1
                j = j + 1
            else:
                j = j + 1
        else:
            j = j + 1


mersenne(7)

