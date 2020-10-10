# el programa dira si el usuario ingresó un número par o impar
num_user = input("ingrese un número entero: ")
num_user_int = int(num_user)
num, res_int = divmod(num_user_int, 2)
print("el residuo: ", res_int)
if res_int == 0:
    print("El número que introdujiste es par")

else:
    print("El número que introdujiste es impar")
