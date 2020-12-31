# reciba como entrada el multiplicador y el multiplicando,
# y entrege como resultado el producto de ambos,
# calculado mediante el método de multiplicación rusa.

multiplicador = int(input("Ingrese multiplicador: "))
multiplicando = int(input("Ingrese multiplicando: "))
suma = 0
def par(var):
    res, mod = divmod(var, 2)
    if mod == 0:
        return True
    else:
        return False

while multiplicador >= 1:
    if par(multiplicador):
        multiplicando = multiplicando * 2
        multiplicador, mod = divmod(multiplicador, 2)



    else:


        suma = multiplicando + suma
        multiplicando = multiplicando * 2
        multiplicador, mod = divmod(multiplicador, 2)



print("Resultado:", suma)