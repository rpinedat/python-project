# El usuario introduce un caracter y el program dice si es letra o num
# Si es letra determina si es mayúscula o minúscula

caracter = input("Introduce un caracter: ")
longitud = len(caracter)

if len(caracter) == 1:

    if caracter.isdigit():
        print("Es número")
    elif caracter.isalpha():
        if caracter.isupper():
            print("Es letra mayúscula")

        else:
            print("Es letra minúscula")
    else:
        print("No es ni número ni caracter")
else:
    print("Introduce sólo un caracter")
