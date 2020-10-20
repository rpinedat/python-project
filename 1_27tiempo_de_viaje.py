# usuario ingresa en minutos el tiempo de cada tramo,
# se calcula el tiempo total en horas
# cuando el usuario ingresa 0 se hace la suma
tramo_min = 1
suma_min = int()

while tramo_min != 0:
    tramo_min = int(input("ingrese los minutos del tramo: "))
    suma_min = tramo_min + suma_min
if suma_min < 60:
    print("Tiempo total del viaje: ", suma_min, "minutos")
elif suma_min > 60:
    hora, minutos = divmod(suma_min, 60)
    print("Tiempo total del viaje: ", hora, "hora(s)", minutos, "minutos")
