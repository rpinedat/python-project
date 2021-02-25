# Escriba la función par(x) que retorne True si x es par, y False si es impar:
# http://progra.usm.cl/apunte/ejercicios/2/numero-par.html

def par(x):
    res, mod = divmod(x, 2)
    if mod == 0:
        return True
    else:
        return False


print(par(16))
print(par(29))
print(par("hola"))
