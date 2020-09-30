###Programa que saca el promedio de una calificación final
# que consta de el promedio de 3 calificaciones que son el30%
### y la calificación del laboratorio que es el 70% de la califciación final
###El alumno ingresará solo dos calificaciones y el laboratorio
#el programa dirá cual debe ser el mínimo en su 3era calificación para pasarla materia.

cert_1 = input("ingrese nota de certamen 1: ")
cert_2 = input("ingrese nota de certamen 2: ")
lab = input("ingrese nota de laboratorio: ")
##Aqui convierto a enteros las variables que voy a utilizar
c1_int = int(cert_1)
c2_int = int(cert_2)
Nl = int(lab)
Nc = float
Nc_min = float
Nc = ((c1_int+c2_int)/3) #Nota promedio de 3 calif
Nf = ((Nc*.7)+(Nl*.3)) ##Nota final

if Nf >= 60:
  print("felicidades,ya pasaste la materia con un mínimo de: ",Nf)
else:
    Nc_min = 60-(Nl*.3) #Busca el promedio minimo de las 3 calificaciones que debe tener
    divide = float (Nc_min /.7)# empieza la operación inversa para despejar c3_int
    c3_int = int((divide*3)-(c1_int+c2_int))

     #print("imprime Nv_min: ", Nc_min)
     #print ("imprime divide: ", divide )
    print("La calificación mínima que debes obtener es:", c3_int)

