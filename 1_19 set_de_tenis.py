# el usuario da el puntaje que lleva un partido de tenis y el programa regresa
# cuál es el estado del partido
# Rocio Pineda
jug_a = int(input("Juegos ganados por A: "))
jug_b = int(input("Juegos ganados por B: "))

if jug_a <= 7 and jug_b <= 7:

    if jug_a == 6 and jug_b == 4:
        print("Ganó A ")

    elif jug_b == 6 and jug_a == 4:
        print("Ganó B ")

    elif jug_a == 7 and jug_b == 7:
        print("Entrada inválida")

    elif jug_a < 0 or jug_b < 0:
        print("entrada invalida")

    elif jug_a == 7 and jug_b > 4 and jug_b < 7:
        print("Ganó A")

    elif jug_b == 7 and jug_a > 4 and jug_a < 7:
        print("Ganó B")

    elif jug_a == 7 and jug_b < 5:
        print("entrada inválida")

    elif jug_b == 7 and jug_a < 5:
        print("entrada inválida")

    else:
        print("Aún no termina")
else:
    print("Entrada inválida")
