# programa que reciba como entrada las coordenadas en que se encuentra un
# caballo, y entregue como salida
# todas las casillas hacia las cuales el caballo puede desplazarse.
# http://progra.usm.cl/apunte/ejercicios/1/caballo-de-ajedrez.html
lista_xy = []
x = int()
y = int()
print("Ingrese coordenadas del caballo: ")
fila = int(input("Fila: "))
column = int(input("Columna: "))

if (fila > 1 and fila <= 8) and (column > 1 and column <= 8):

    print("El caballo puede saltar de: ", fila, "", column, "a:")

    if fila + 2 <= 8:
        x = fila + 2

        if column+1 <= 8:
            y = column+1
            print("", x, "", y)
        if column-1 >= 0:
            y = column-1
            print("", x, "", y)

    if fila - 2 >= 1:
        x = fila - 2

        if column + 1 <= 8:
            y = column + 1
            print("", x, "", y)
        if column - 1 >= 0:
            y = column - 1
            print("", x, "", y)

    if column + 2 <= 8:
        y = column + 2

        if fila + 1 <= 8:
            x = fila + 1
            print("", x, "", y)
        if fila - 1 >= 0:
            x = fila - 1
            print("", x, "", y)

    if column - 2 >= 0:
        y = column - 2

        if fila + 1 <= 8:
            x = fila + 1
            print("", x, "", y)
        if fila - 1 >= 0:
            x = fila - 1
            print("", x, "", y)
else:
    print("Fuera de rango")
