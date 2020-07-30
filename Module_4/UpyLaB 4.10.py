def bat(joueur_1, joueur_2):

    res = False
    if joueur_1 != joueur_2:
        res |= (joueur_1 == 2 and joueur_2 == 1)
        res |= (joueur_1 == 1 and joueur_2 == 0)
        res |= (joueur_1 == 0 and joueur_2 == 2)

    return res


print(bat(0, 0))  # False
print(bat(0, 1))  # False
print(bat(2, 1))  # True
