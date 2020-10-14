# Escribe tabla de multiplicar del 1 al 10 en forma de matriz alineado a la derecha
i = 1
j = 1
while i <= 10 and j <= 10:
    if i*j < 10:
        print(" ", i*j, end=" ")
        i = i + 1
        if i == 11:
            i = 1
            j = j + 1
            print("\n")

    elif i*j >= 10:
        print("", i * j, end=" ")
        i = i + 1
        if i == 11:
            i = 1
            j = j + 1
            print("\n")
    else:
        print(" ", i * j, end=" ")
        i = i + 1
        if i == 11:
            i = 1
            j = j + 1
            print("\n")
