# muestre los m primeros números de Fibonacci,
# donde m es un número ingresado por el usuario

num_user = int(input("Ingrese m: "))

a = 0
b = 1
c = 0
count = 3

if num_user == 1:

    print("Los", num_user, "primeros números de Fibonacci son:")
    print(" 0 ")

elif num_user == 2:

    print("Los", num_user, "primeros números de Fibonacci son:")
    print(" 0 ")
    print(" 1 ")

elif num_user >= 3:
    print("Los", num_user, "primeros números de Fibonacci son:")
    print(" 0 ")
    print(" 1 ")
    while count <= num_user:
        c = a + b
        a = b
        b = c
        count = count + 1
        print("", c)

else:
    print("Número no válido")