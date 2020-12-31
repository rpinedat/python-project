# recibe como entrada un número entero n,
# y entrega como salida el n-ésimo número de Fibonacci
a = 0
b = 1
c = 0
count = 2
num_usuario = int(input("Ingrese un número: "))
# print("", a)
# count = count +1
if num_usuario > 2:
    while count < num_usuario:
        count = count + 1
        c = a + b
        a = b
        b = c

    print("F", num_usuario, "=", c)

elif num_usuario == 1:
    print("F", num_usuario, "=", c)
elif num_usuario == 2:
    print("F", num_usuario, "=", b)
elif num_usuario <= 0:
    print("número de usuario no válido")


