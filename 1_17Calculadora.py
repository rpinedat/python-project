# Minicalculadora que recibe números reales y hace las operaciones básicas +-/* y **
import math
while True:
    try:
        num1 = float (input("primer número: "))
        num2 = float (input("segundo número: "))
    except ValueError :
        print ("Debes escribir un número.")
        continue
    else:

        operador = input("Introducir operador: ")
       # suma = str("+")
        if operador == "+":
            print(num1,"+",num2,"=",num1+num2)
        elif operador == "-":
            print(num1, "-", num2, "=", num1 - num2)
        elif operador == "*":
            print(num1, "*", num2, "=", num1 * num2)
        elif operador == "/":
            try:
             print(num1, "/", num2, "=", num1 / num2)
            except: print("No se permite la división por cero")
        elif operador == "**":
            print (num1, "**", num2, "=" ,math.pow(num1,num2))
        else: print ("No es un operador válido")



        break
