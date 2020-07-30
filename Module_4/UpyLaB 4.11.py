import random

PIERRE = 0
FEUILLE = 1
CISEAUX = 2


def bat(joueur_1, joueur_2):

    res = False
    if joueur_1 != joueur_2:
        res |= (joueur_1 == CISEAUX and joueur_2 == FEUILLE)
        res |= (joueur_1 == FEUILLE and joueur_2 == PIERRE)
        res |= (joueur_1 == PIERRE and joueur_2 == CISEAUX)

    return res


def coup_nom(coup):
    nom = ""
    if coup == 0:
        nom = "Pierre"
    elif coup == 1:
        nom = "Feuille"
    elif coup == 2:
        nom = "Ciseaux"
    return nom


def jeu(joueur_1, joueur_2, points):
    if joueur_1 == joueur_2:
        res = "annule"
    elif bat(joueur_1, joueur_2):
        res = "bat"
        points -= 1
    else:
        res = "est battu par"
        points += 1

    print(coup_nom(joueur_1), res, coup_nom(joueur_2), ":", points)

    return points


points = 0
s = int(input())
random.seed(s)
for i in range(5):
    coup_o = random.randint(0,2)
    coup_j = int(input())
    points = jeu(coup_o, coup_j, points)

if points < 0:
    print("Perdu")
elif points == 0:
    print("Nul")
else:
    print("Gagné")

"""
65
0
1
2
1
0
doit afficher :
Feuille bat Pierre : -1
Feuille annule Feuille : -1
Feuille est battu par Ciseaux : 0
Ciseaux bat Feuille : -1
Pierre annule Pierre : -1
Perdu
"""

"""
1515
0
1
2
1
0

doit afficher :
Ciseaux est battu par Pierre : 1
Feuille annule Feuille : 1
Pierre bat Ciseaux : 0
Ciseaux bat Feuille : -1
Ciseaux est battu par Pierre : 0
Nul
"""