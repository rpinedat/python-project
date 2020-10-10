# Minicalcula recibe números reales y hace  operaciones básicas +-/* y **
import math

num1 = float(input("primer número: "))
num2 = float(input("segundo número: "))
operador = input("Introducir operador: ")

if operador == "+":
    print(num1, "+", num2, "=", num1+num2)
elif operador == "-":
    print(num1, "-", num2, "=", num1 - num2)
elif operador == "*":
    print(num1, "*", num2, "=", num1 * num2)
elif operador == "/":
    if num2 == 0:
        print("No se permite la división por cero")
    else:
        print(num1, "/", num2, "=", num1 / num2)
elif operador == "**":
    print(num1, "**", num2, "=", math.pow(num1, num2))
else:
    print("No es un operador válido")
