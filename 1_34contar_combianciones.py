# lanzar dos dados numerados de 1 a 6,el puntaje es la suma de ambos
# El programa pregunta al usuario el puntaje y el resultado
# es la cantidad de combinaciones con la que se puede obtener el puntaje

puntaje = int(input("Ingrese un puntaje del 2 al 12: "))
i = 1

l = int()
for i in range(i, 6+1):
    # print("i: ", i)
    j = 1
    for j in range(j, 6+1):
        # print("j: ",j)
        comb = i + j
        if comb == puntaje:
            l = l+1

print("Hay ", l, "combinaciones para obtener: ", puntaje)
