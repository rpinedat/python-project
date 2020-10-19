# Muestra la tabla de multiplicar del 1 al 10 del número ingresado por el usuario

num_multiplica = int(input("Ingresa un dígito del 1 al 10: "))

if (num_multiplica <= 10) and (num_multiplica > 0):
    for i in range(11):
        print("", num_multiplica, "x", i, "=", num_multiplica*i)
else:
    print("No es un dígito válido")
