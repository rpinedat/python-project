# Escriba la función invertir_digitos(n) que reciba un número entero n y
# entregue como resultado el número n con los dígitos en el orden inverso

def invertir_digitos(var):
    return var[::-1] # Invierte una cadena


digitos = input("ingrese n: ")
if invertir_digitos(digitos) == digitos:
    print("Es palíndromo")
