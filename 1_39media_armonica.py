# Desarrolle un programa que calcule la media armónica de una secuencia de números.
denominador = 0
n = int(input("Cuántos números: "))

for i in range(1, n+1):
    print("n", i, ": ", end="")
    x = int((input()))
    print(i)
    denominador = (1/x) + denominador

print("H = ", (n/denominador)) 
