# Se ingresan dos núms y el resultado es la suma de los que estan entre ellos

num_1 = int(input("ingrese num 1: "))
num_2 = int(input("ingrese num 2: "))
menor = int()
mayor = int()
res = int()

if num_1 >= num_2:
    mayor = num_1
    menor = num_2
else:
    mayor = num_2
    menor = num_1

for i in range(menor, mayor):
    res = i + res
print("Res: ", res - menor)
