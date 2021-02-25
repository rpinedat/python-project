# Escriba un programa que intente adivinar el número pensado por el usuario del 1 al 100.
# Cada vez que el computador haga un intento,
# el usuario debe ingresar <, > o =,
# dependiendo si el intento es menor, mayor o correcto.
# http://progra.usm.cl/apunte/ejercicios/1/adivinar-numero.html



from random import randrange
n = randrange(101)
menor = 0
mayor = 100

# print(n)
counter = 1

print("Intento ", counter, ": ", n, "\n")

pista = input("")

while pista != "=":
    if pista == ">":
        menor = n
        n = round(((mayor - menor)/2) + n)

        counter = counter + 1
        print("Intento ", counter, ": ", n, "\n")
        pista = input("")
    elif pista == "<":
        mayor = n
        n = round(((mayor - menor)/2)+menor)
        counter = counter + 1
        print("Intento ", counter, ": ", n, "\n")
        pista = input("")


print("Adivine en: ", counter, "intentos")