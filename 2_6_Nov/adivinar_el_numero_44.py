# El usuario debe ingresar su intento, y el programa debe decir
# si el número pensado es mayor, menor, o el correcto:
# http://progra.usm.cl/apunte/ejercicios/1/adivinar-numero.html

from random import randrange
n = randrange(101)
# print(n)
counter = 0
adivina = int(input("Adivine el número: "))

while adivina != n:
    if adivina < n:
        counter = counter + 1
        print("Intento: ", counter)
        print("Es mayor que: ", adivina)
        adivina = int(input("Adivine el número: "))

    if adivina > n:
        counter = counter + 1
        print("Intento: ", counter)
        print("Es menor que: ", adivina)
        adivina = int(input("Adivine el número: "))


print("Felicidades, adivinaste en", counter + 1, "intentos")
