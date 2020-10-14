# Se ingresan dos núms y el resultado es la suma de los que estan entre ellos

num_1 = input("ingrese num 1: ")
num_2 = input("ingrese num 2: ")

if num_1.isdigit() and num_2.isdigit():
    num_1 = int(num_1)
    num_2 = int(num_2)
    y = num_1 + 1
    res = y
    while y < (num_2-1):
        y = y + 1
        res = res + y

    print("La suma es:", res)
else:
    print("No es un dígito válido")
