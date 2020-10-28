# El usuario define n e ingresa n numeros
# el programa regresa el mayor

n = int(input("Ingrese n: "))
lista = []
for x in range(n):
    nums = int (input("Ingrese número: "))
    lista.append(nums)
print("El mayor es:", max(lista))