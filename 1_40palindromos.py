# Programa que indique si el número natural ingresado es o no palíndromo:

n = input("Ingrese un número: ")

n1 = n[::-1]
n = int(n)
n1 = int(n1)
if n == n1:
    print(n, "Es palíndromo")
else:
    print(n, "No es palíndromo")
