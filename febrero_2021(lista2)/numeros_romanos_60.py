# Números Romanos por Rocio Pineda Tecpa


def romanos(numero):
    res = 0
    i = 0
    count = 0
    long = len(numero)

    valores = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1,

    }

    while count < long:

        if numero[i] in valores:

            a = valores.get(numero[i])

            j = i + 1
            if j < long:
                b = valores.get(numero[j])

                if a >= b:
                    res = res + a
                    i = i + 1
                    count = count + 1

                if a < b:
                    res = res + (b - a)

                    i = i + 1
                    count = count + 1
                    j = j+1
                    if j == long:
                        break
                    else:
                        i = i + 1
            else:
                res = res + a
                print("resultado:", res)
                break

        else:
            print("no es número válido")
            break


romano_in = input("Número romano: ").upper()


romanos(romano_in)
