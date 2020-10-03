# Devuelve la masa corporal y el riesgo de enfemedades coronarias
# Rocio Pineda
while True:
    try:
        estatura = float(input("Ingrese su estatura en mts: "))
        peso = float(input("Ingrese su peso en kg: "))
        edad = int(input("Ingrese su edad: "))
    except ValueError:
        print("Debes escribir un número")
        continue
    else:
        est_2 = float(pow(estatura, 2))
        mc ,res = divmod(peso,est_2)

        print("Su masa corporal es: ", mc)

        if edad < 45 and mc < 22:
            print("Su resgo coronario e bajo")
        if edad < 45 and mc >= 22:
            print("Su riesgo es medio")
        if edad >= 45 and mc < 22:
            print("Su riesgo es medio")
        if edad >= 45 and mc >= 22:
            print("Su riego es alto")

    break