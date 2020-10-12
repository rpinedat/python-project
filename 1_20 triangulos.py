# Recibe medida de tres lados de un triangulo
# El programa entrega si es un triangulo válido y de que tipo.

a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))

if a+b > c and b+c > a and c+a > b:

    if a != b and b != c:
        print("Es un triángulo escaleno")

    elif a == b and b == c:
        print("Es un triángulo equilatero")

    else:
        print("Es un triángulo isóceles")

else:
    print("No es un triangulo válido")
