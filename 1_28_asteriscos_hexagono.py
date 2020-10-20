# Dibuja un hexágono, el usuario da la medida de un lado
lado = int(input("Ingresa el tamaño del lado del hexágono: "))
i = int()

medio = (((lado-1)*2)+lado)  # representa la linea mas ancha
j = medio-lado

for i in range(lado, medio+1, 2):
    print(" " * j + "*" * i)
    j = j-1

j = j+1
while i != lado:
    i = i-2
    print(" "*j, "*"*i)
    j = j+1
