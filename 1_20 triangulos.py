# Recibe medida de tres lados de un triangulo
# El programa entrega si es un triangulo válido y de que tipo.
while True:
    try:

        a = float(input("Ingrese a: "))
        b = float(input("Ingrese b: "))
        c = float(input("Ingrese c: "))
    except ValueError:
        print("Debe ingresar un número")
        continue
    else:
        if a+b > c and b+c > a and c+a > b:

            if a != b and b != c and a != c:
                print("Es un triángulo escaleno")

            if a == b == c:
                print("Es un triángulo equilatero")

            if a == b or a == c or b == c:
                print("Es un triángulo isóceles")

        else:
            print("No es un triángulo válido")

    break