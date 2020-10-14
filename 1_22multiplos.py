# Muestra la tabla de multiplicar del 1 al 10 del número ingresado por el usuario

num = input("Ingresa un dígito del 1 al 10: ")
if num.isdigit():
    num_multiplica = int(num)
    if (num_multiplica <= 10) and (num_multiplica > 0):
        i = 1
        while i <= 10:
            print("", num_multiplica, "x", i, "=", num_multiplica*i)
            i = i+1
    else:
        print("No es un dígito válido")
else:
    print("No es un dígito")
