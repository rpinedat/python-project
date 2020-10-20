# Se ingresan dos núms y el resultado es la suma de los que estan entre ellos

num_1 = int(input("ingrese num 1: "))
num_2 = int(input("ingrese num 2: "))

res = int()
res2 = int()
for i in range(num_1, num_2):
    res2 = i + res2
print("Res2: ", res2 - num_1)
