""" trace une étoile à n côtés, si elle peut l'être sans lever la plume"""

import turtle
from math import gcd # fonction du module math qui calcule le pgcd de 2 nombres

LONGUEUR = 100 # taille de chaque segment de l'étoile

n = int(input("Combien de branches désirez-vous ? : "))
inc = (n-1) // 2
while gcd(n, inc) > 1:
   inc = inc - 1
if inc == 1 :
   print("Impossible de dessiner une étoile à", n, "branches en un tenant")
else:
    angle =  180 - (n - 2 * inc) * 180 / n
#    turtle.begin_fill()
    for i in range(n):
        turtle.forward(LONGUEUR)
        turtle.left(angle)
#    turtle.end_fill()
turtle.done()