# la suma se detiene cuando la diferencia entre dos sumandos es menor que .0001
import math
e = float()
i = 0
dif = 1
sustraendo = float()


while dif > .0001:

    fact = math.factorial(i)
    e = e + (1/fact)
    dif = e - sustraendo
    sustraendo = e
    # print("i: ", i,"fact", 1/fact, "e = ", e,"dif", dif)
    print("i: ", i, "    e:", e, "    diferencia:", dif)
    i = i+1