import random

n = 0
fin = False
NB_ESSAIS_MAX = 6
secret = random.randint(0, 100)

while not fin:
    n += 1
    v = int(input())
    if v == secret:
        print("Gagné en", n, "essais !")
        fin = True
    elif n == NB_ESSAIS_MAX:
         print("Perdu ! Le secret était", secret)
         fin = True
    elif v > secret:
        print("Trop grand")
    elif v < secret:
        print("Trop petit")
