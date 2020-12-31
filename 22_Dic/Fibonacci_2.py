# recibe como entrada un número entero e indique si es o no Fibonacci

num_usuario = int(input("Ingrese un número: "))

a = 0
b = 1
c = 0
count = 0
if num_usuario == 0:
    print("", num_usuario, "Es número Fibonacci")


else:
    while count <= num_usuario:
        count = count + 1
        a = b
        b = c
        c = a + b


        if c == num_usuario:
            print("", num_usuario, "Es número Fibonacci")
            break
    if c != num_usuario:
        print("", num_usuario, "No es número de Fibonacci")
