# estimar el valor de pi, el user dará numero entero que indique cuántos términos dela suma se utilizarán
# π=4(1−1/3+1/5−1/7+…)
n = int(input("Introduzca n: "))
# negativos = 0
# positivos = 0
#
#
# for i in range(3, n, 4):
#     negativos = negativos + 1/i
#     print("-", negativos, "i", i)
#
# for j in range(1, n, 4):
#     positivos = positivos + 1/(j)
#     print("+", positivos, "j", j)
#
#
# pi = 4*(positivos - negativos)
# print(" pi:  ", pi)
#---------------------
s = 0
t = 0
for k in range(1, n + 1):
    s += (-1) ** (k + 1) / (2 * k - 1)

for l in range(1, n+1):
    t += ((pow(-1, k + 1))/(2*k-1))

res= 4 * s
res2 = 4 * t
print("res", res, "res2: ", res2)
