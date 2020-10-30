# En cada ronda del juego del cachipún, los dos competidores deben elegir entre jugar tijera, papel o piedra.
puntos_a = int()
puntos_b = int()

while puntos_a < 3 and puntos_b < 3:
    a = input("A: ")
    b = input("B: ")

    if a == "piedra":
        if b == "tijera":
            puntos_a = puntos_a + 1
            print(puntos_a, " - ", puntos_b)
        elif b == "papel":
            puntos_b = puntos_b + 1
            print(puntos_a, " - ", puntos_b)

    if a == "tijera":
        if b == "papel":
            puntos_a = puntos_a + 1
            print(puntos_a, " - ", puntos_b)
        elif b == "piedra":
            puntos_b = puntos_b + 1
            print(puntos_a, " - ", puntos_b)

    if a == "papel":
        if b == "piedra":
            puntos_a = puntos_a + 1
            print(puntos_a, " - ", puntos_b)
        elif b == "tijera":
            puntos_b = puntos_b + 1
            print(puntos_a, " - ", puntos_b)

    if a == b:
        puntos_a = puntos_a
        print(puntos_a, " - ", puntos_b)


if puntos_a == 3:
    print("A es el ganador")
else:
    print("B es el ganador")
