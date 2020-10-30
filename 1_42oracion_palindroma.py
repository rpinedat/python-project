# Modifique programa para que reconozca oraciones palíndromas, hay que ignorar los espacios:

oracion = input("Ingrese oración: ")
oracion2 = oracion.replace(" ","")  # Quito los espacios y lo vuelvo una palabra
oracion3 = oracion2[::-1]

if oracion3 == oracion2:
    print("Es palíndromo: ")
else:
    print("No es palíndromo")
