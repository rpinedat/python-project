#El ususario ingresa un número entero con decimalesy la salida son solo
#los decimales, cehcar la función math.modf ya que regresa decimales al final que no corresponden

import math

num_entra=input("introduce un número que contenga decimales: ")
num_float=float(num_entra)
part_decimal,part_entera=math.modf(num_float)
print("La parte decimal del número es: ",part_decimal)

