# El usuario introduce su fecha de nacimiento y el programa regresa la edad.
#Rocio Pineda
import calendar
from datetime import date


while True:
    try:
        dia_user = int (input("Ingresa el día: "))
        mes_user = int (input("Ingresa el mes: "))
        anio_user = int (input("Ingresa el anio: "))

    except ValueError :
          print("Error ingrese una fecha válida")

          continue
    else:
         dias_mes = calendar._monthlen(anio_user,mes_user)#revisa los dias del mes introducido, falta checar
         #print("",dias_mes)                  # como poner un excepcion aqui para evitar si el año o mes no es vaido

         today = date.today() #Obtiene la fecha de hoy

         #print("",today.year)
         edad = today.year - anio_user

    if dias_mes >= dia_user and edad>=0:

            if mes_user < today.month:
               print ("Su edad es: ", edad)
            if mes_user > today.month:
               print ("Su edad es: ", edad-1)
            if mes_user == today.month:
                if dia_user <= today.day:
                     print("Su edad es: ", edad)
                else:
                      print("Su edad es: ", edad-1)
    else:
            print("Escriba una fecha válida")


    break








