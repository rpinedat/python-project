#programa que calcula si el año que introduce el usuario fue o sera bisiesto.
#https://docs.python.org/3/library/calendar.html  pagina de donde saque la funcion

import calendar


anio = input("introduce el año: ")
anio1= int(anio)
x= int ()
y= int ()
cal = calendar.Calendar()
x,y = calendar.monthrange(anio1,2)#en realidad devuelve cuantos dias de fines de semana hay en el mes, y cuantos dias tiene ese mes
                                  #por lo que solo utilizo cuantos dias tendra febrero ese año para saber si es bisiestro o no.

if y == 29:
    print (anio,"es año bisiestro ")

else: print (anio, "no es año bisiestro")







