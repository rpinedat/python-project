# Desarrolle un programa que calcule el dígito verificador de un rol UTFSM.


dig = int()
res = int()
j = 2


rol = int(input("Ingrese el rol: "))
rol_int = rol
rol = str(rol)
rol_inv = rol[::-1] # invierto la cadena
#rol_inv_int = int[rol_inv]
rol_long = len(rol_inv) # longitud de la cadena

for i in range(rol_long):
    if j != 7:
        j == 2
        dig = rol_inv[i]
        dig = int(dig)
        #print("dig", dig)
        res_suma = dig * j + res
        j = 1 + j

    else:
        j = 2

x, modulo = divmod(res_suma,11)
restar = 11 - modulo
cod_verificador = rol_int -restar
print("código verificador", cod_verificador)


