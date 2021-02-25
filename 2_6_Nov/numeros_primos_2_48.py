# http://progra.usm.cl/apunte/ejercicios/1/numeros-primos.html
# https://www.youtube.com/watch?v=bCXL8_loqzQ
# Escriba un programa que muestre los n primeros números primos,
# donde n es ingresado por el usuario:

i = int()

def num_primos(numero):

    for i in range(2, numero):

        x, y = divmod(numero, i)

        if y == 0:

            return False

    return True


def seriePrimo(num):
    counter = 0
    j = 1

    while counter < num:
        j = j + 1
        if num_primos(j):
            counter = counter +1
            print(j)


num = int(input("Ingrese el número de primos: "))
seriePrimo(num)
