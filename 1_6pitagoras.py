# Teorema Pitágoras
import math
cateto_a_in = int(input("Ingrese cateto a: "))
cateto_b_in = int(input("Ingrese cateto b: "))
res_cat_a = pow(cateto_a_in, 2)
res_cat_b = pow(cateto_b_in, 2)
hipotenusa = math.sqrt(res_cat_a+res_cat_b)
print("La hipotenusa es: ", hipotenusa)
