#programa que al dividir dos números dice si la división es exacta o si
#tiene un residuo y cual es

import math

dividendo = input("Dividendo: ")
divisor = input ("Divisor: ")
dividendo_int = int (dividendo)
divisor_int = int (divisor)

cociente,residuo = divmod(dividendo_int,divisor_int)

print(cociente)
print(residuo)

if residuo == 0:
    print ("La división es exacta")
    print("Cociente: ",cociente)
    print("residuo: ", residuo)

else:
    print("La división no es exacta")
    print("Cociente: ", cociente)
    print("residuo: ", residuo)
