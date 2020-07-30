def placer_pion(couleur, colonne, grille):
    """ couleur est la couleur du pion, qui peut être soit 'R' (rouge), soit 'J' (jaune),
        colonne est l’indice de la colonne où le joueur souhaite placer le pion (allant de 0 à 6),
        grille est la grille de jeu sous forme de matrice.
    """
    result = False
    for i in range(len(grille)):
        if not result and grille[i][colonne] == 'V':
            result = True
            grille[i][colonne] = couleur

    return result, grille


print(placer_pion("R", 3, [  ['V', 'V', 'V', 'J', 'V', 'V', 'V'],
                             ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                             ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                             ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                             ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                             ['V', 'V', 'V', 'V', 'V', 'V', 'V']]))
# (True, [['V', 'V', 'V', 'J', 'V', 'V', 'V'],
#         ['V', 'V', 'V', 'R', 'V', 'V', 'V'],
#         ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
#         ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
#         ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
#         ['V', 'V', 'V', 'V', 'V', 'V', 'V']])

print(placer_pion("J", 4, [  ['J', 'J', 'J', 'J', 'R', 'R', 'R'],
                             ['R', 'R', 'R', 'R', 'R', 'V', 'V'],
                             ['J', 'J', 'J', 'J', 'J', 'V', 'V'],
                             ['V', 'R', 'J', 'R', 'J', 'V', 'V'],
                             ['V', 'V', 'V', 'V', 'J', 'V', 'V'],
                             ['V', 'V', 'V', 'V', 'R', 'V', 'V']]))

# (False, [['J', 'J', 'J', 'J', 'R', 'R', 'R'],
#          ['R', 'R', 'R', 'R', 'R', 'V', 'V'],
#          ['J', 'J', 'J', 'J', 'J', 'V', 'V'],
#          ['V', 'R', 'J', 'R', 'J', 'V', 'V'],
#          ['V', 'V', 'V', 'V', 'J', 'V', 'V'],
#          ['V', 'V', 'V', 'V', 'R', 'V', 'V']])
