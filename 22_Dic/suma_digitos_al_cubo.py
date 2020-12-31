# Desarrolle un programe que pueda determinar los números que sumando al cubo cada uno de sus dígitos
# de el mismo número en el rango de 150 a 410

def desglosa(num):
    centena_res, centena_mod = divmod(num, 100)  # P/e divide 153 / 100
    decena_res_temp = num % 100  # saco el 53
    decena_res, decena_mod = divmod(decena_res_temp, 10)  # Ahora divido 53/10
    unidad_res = num % 10  # no necesito sacarlo porque con % saco el número a la derecha

    #print("unidad", unidad_res, "decena", decena_res, "centena", centena_res)

    compara(i, suma_cubos(unidad_res, decena_res, centena_res))

def suma_cubos(var1, var2, var3):
    suma = (pow(var1, 3)) + (pow(var2, 3)) + (pow(var3, 3))
    #print(suma)
    return suma


def compara(num_1, num_2):
    if num_1 == num_2:
        print(num_1, "Esta compuesto por la suma de sus cubos")


for i in range(150, 411):

    desglosa(i)



