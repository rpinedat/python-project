# recibe el radio de un círculo y entrga como salida área y perímetro
radio = int(input("ingrese el radio del círculo: "))
pi = 3.14159
per = radio*2*pi
area = pow(radio, 2)*pi
print("El perímetro del círculo es", per)
print("El area del círculo es", area)
