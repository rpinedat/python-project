#El usuario introduce un caracter y el program dice si es letra o num
#Si es letra determina si es mayúscula o minúscula

#Ya valida las entradas

caracter = input("Introduce un caracter: ")
longitud = len(caracter)

if len(caracter) == 1 :

   if caracter.isdigit() == 1:
       print ("Es número")
   elif caracter.isalpha() == 1:
       if caracter.isupper() == 1:
           print ("Es letra mayúscula")

       else: print("Es letra minúscula")
   else: print("No es ni número ni caracter")
else: print("Introduce sólo un caracter")





#print(type(caracter.upper()))
#print(caracter.isdigit())
#print(caracter.isalpha())
# print(caracter.isalnum()) checa si es numero y cadena
#print(longitud)
#print (type(caracter))

#def isinteger(a):      Checar esta función
 #   try:
  #      int(a)
   #     return True
   # except ValueError:
    #    return False

