# Escriba la función tabla_de_verdad(predicado) que reciba como parámetro un predicado lógico de tres parámetros
# e imprima la tabla de verdad del predicado
# for anidados
# http://elclubdelautodidacta.es/wp/2012/11/python-los-operadores-logicos-y-sus-tablas-de-verdad/

booleanos = [True, False]

# Tabla de verdad de or

print('x\t\ty\t\tz \t\tx or y or z')
print('-' * 30)
for x in booleanos:
    for y in booleanos:
        for z in booleanos:
            print( x, y, z,  (not x) and (y or z), sep='\t')

print()

# Tabla de verdad de and

print('x\ty\tx and y')
print('-' * 22)
for x in booleanos:
    for y in booleanos:
        print(x, y, x and y, sep='\t')

print()

# Tabla de verdad de not

print('x\tnot x')
print('-' * 13)
for x in booleanos:
    print(x, not x, sep='\t')

print()

# Tabla de verdad de ^

print('x\ty\tx ^ y')
print('-' * 21)
for x in booleanos:
    for y in booleanos:
        print(x, y, x ^ y, sep='\t')