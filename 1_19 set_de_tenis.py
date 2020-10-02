#  el usuario da el puntaje que lleva un partido de tenis y el programa regresa
# cuál es el estado del partido
#Rocio Pineda



while True:
    try:

     jug_a = int(input("Juegos ganados por A: "))
     jug_b = int(input("Juegos ganados por B: "))

    except ValueError:
     print("Debes escribir un número")
     continue
    else:
       if jug_a <= 7 and jug_b <= 7 :


          if jug_a == 6 and jug_b == 4 :
                print ("Ganó A ")
                break

          if jug_b == 6 and jug_a == 4:
                print ("Ganó B ")
                break
          elif jug_a ==7 and jug_b== 7:
                print ("Entrada inválida")

          elif jug_a < 0 or jug_b < 0 :
              print ("entrada invalida")
          elif jug_a == 7 and (jug_b > 4 and jug_b < 7) :
             print ("Ganó A")

          elif jug_b == 7 and (jug_a > 4 and jug_a <7) :
             print ("Ganó B")

          elif jug_a == 7 and jug_b < 5:
              print ("entrada inválida")

          elif jug_b == 7 and jug_a < 5:
              print ("entrada inválida")
          else:
               print ("Aún no termina")

       else: print("Entrada inválida")
    break
