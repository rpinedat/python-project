#el usuario introduce dos palabras y el programa dice cual es mas
#grande y por cuantos caracteres o si son iguales

palabra1 = input("Introduce la primer palabra: ")
palabra2 = input("Introduce la segunda palabra: ")

long_palabra1 = (len(palabra1))
long_palabra2 =(len(palabra2))

if long_palabra1 == long_palabra2 :
    print("las palabras tienen el mismo número de caracteres: ",long_palabra1)

elif long_palabra1 > long_palabra2 :
    res = long_palabra1 - long_palabra2

    print("las palabra",palabra1," es mayor por ", res,"caracteres")

elif long_palabra2 > long_palabra1 :
    res = long_palabra2 - long_palabra1

    print("las palabra",palabra2," es mayor por ", res,"caracteres")

else:


    print("no introdujiste una palabra correcta")
