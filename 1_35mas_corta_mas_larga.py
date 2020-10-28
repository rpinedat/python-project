# el usuario ingresa un número entero n, que indica cuántas palabras ingresará
# después el usuario ingresa n palabras.
# La salida es la palabra mas larga

n = int(input("Ingrese la cantidad de palabras: "))
lista = []
longitudes = []

for i in range(n):
    palabra = str(input("Palabra "))
    lista.append(palabra)
for j in range(n):
    longitudes.append(len(lista[j]))

larga = longitudes.index(max(longitudes))
corta = longitudes.index(min(longitudes))

print("La palabra más larga es: ", lista[larga])
print("La palabra más corta es: ", lista[corta])
