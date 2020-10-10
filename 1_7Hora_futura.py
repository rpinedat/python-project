# Pregunta la hora actual y la cantidad de horas que quiere saber serán a futuro
hora_act = int(input("Introduce la hora actual: "))
hora_next = int(input("Cantidad de horas: "))
res_hora = hora_act+hora_next
cociente, residuo = divmod(res_hora, 24)
print("En", hora_next, "horas, el reloj marcará las:", residuo, "hrs.")
