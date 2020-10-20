# Dibuja un rectángulo con asteriscos

altura_rect = int(input("Escriba la altura del rectángulo: "))
ancho_rect = int(input("Escriba el ancho del rectángulo: "))

for i in range(altura_rect):
    print("*"*ancho_rect)
