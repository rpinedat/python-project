#Pregunta la hora actual y la cantidad de horas que quiere saber serán a futuro
#Falta agregar la opción de que si el usuario introduce que son las 12 hrs y le suma 12hrs exacatmente,
# el resultado debe ser 24 hrs
hora_act= input("Introduce la hora actual: ")
hora_next=input("Cantidad de horas: ")
hora_act_int=int(hora_act)
hora_next_int=int(hora_next)
horas,res_residuo=divmod(hora_next_int,12)

res_hora=hora_act_int+res_residuo

print("En",hora_next_int, "horas, el reloj marcará las:",res_hora,"hrs.")

