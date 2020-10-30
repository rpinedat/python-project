# programa que reciba como entrada una palabra e indique si es palíndromo o no sin acentos ni mayusculas

palabra = input("Ingrese palabra: ")
palabra2 = palabra[::-1]
if palabra == palabra2:
    print("Es palíndromo")
else:
    print("No es palíndromo") 