#Calcula la edad del usuario


#Checar datetime en python
#https://python-para-impacientes.blogspot.com/2014/02/operaciones-con-fechas-y-horas.html

from time import localtime
import calendar

t_act = localtime()  #fecha actual
d_act = int(t_act.tm_mday)
m_act = int(t_act.tm_mon)
a_act = int(t_act.tm_year)


dia_n = int ( input ("Ingrese su fecha de nacimiento \nDia: " ))  #fecha de nacimiento usuario
mes_n = int ( input ("Mes: "))
anio_n = int (input ("Anio: "))
edad = int
#while True:
 #   try:
x,y = calendar.monthrange(anio_n,mes_n)  #buscar que rango de años maneja calendar.monthrange
  #  except ValueError :
#print ("Escribe una fecha correcta1 ")


if (dia_n <= y): #Con esto checo si en ese año y ese mes hubo la cantidad de dias dentro del rango.

        edad = (a_act-anio_n)
        print ("Tu edad es: ",edad)

else:
         print("Escribe una fecha correcta2")


#print(x,y)
   # break

#print(t_act)
#print(m_act)
#print(a_act)


#print("Usted tiene ",edad, "anios")

