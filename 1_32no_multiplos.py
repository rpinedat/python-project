# Muestra los num naturales menores o igules a n (1...n)
# No deben ser múltiplos  ni de 3 ni de 7.
i = 1
n = int(input("Ingresa n: "))

for i in range(i, n+1):
    x, res1 = divmod(i, 3)
    y, res2 = divmod(i, 7)

    if (res1 != 0) and (res2 != 0):
        print(" ", i)
