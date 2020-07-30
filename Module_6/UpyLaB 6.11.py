import math


def bonne_planete(diametre):
    """ fonction booléenne qui reçoit en paramètre un nombre représentant le diamètre, en mètres, du planète candidate.
    La fonction retourne la valeur True ou False selon que la planète convient ou non. """

    area = math.pi * diametre ** 2
    return area >= (50 * 1000)


if bonne_planete(float(input())):
    print("Bonne planète")
else:
    print("Trop petite")

# 500 => "Bonne planète"
# 10 => "Trop petite"
