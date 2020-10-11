# Devuelve la masa corporal y el riesgo de enfemedades coronarias
# Rocio Pineda

estatura = float(input("Ingrese su estatura en mts: "))
peso = float(input("Ingrese su peso en kg: "))
edad = int(input("Ingrese su edad: "))

mc, res = divmod(peso, pow(estatura, 2))

print("Su masa corporal es: ", mc)

if edad < 45 and mc < 22:
    print("Su riesgo coronario es bajo")
if edad < 45 and mc >= 22:
    print("Su riesgo es medio")
if edad >= 45 and mc < 22:
    print("Su riesgo es medio")
if edad >= 45 and mc >= 22:
    print("Su riesgo es alto")
