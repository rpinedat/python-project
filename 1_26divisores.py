# Entrega todos los divisores del número ingresado

num = input("Ingrese un número entero: ")
if num.isdigit():
    num = int(num)
    i = 1
    while i <= num:
        cociente, residuo = divmod(num, i)
        if residuo == 0:
            print(" ", i, end="")
            i = i+1
        else:
            print(end="")
            i = i + 1
else:
    print("No es un número válido")

