#Teorema Pitágoras
import math

cateto_a_in=input("Ingrese cateto a: ")
cateto_b_in=input("Ingrese cateto b: ")
cateto_a_int=int(cateto_a_in)
cateto_b_int=int(cateto_b_in)

hipotenusa=math.sqrt((cateto_a_int*cateto_a_int)+(cateto_b_int*cateto_b_int))
print("La hipotenusa es: ",hipotenusa)
