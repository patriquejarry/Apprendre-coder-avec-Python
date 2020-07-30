def gagnant_gen(grille, couleur, range_ligne, range_colonne, offset_ligne, offset_colonne):
    """Recherche generique"""

    winner = False
    for ligne in range(range_ligne):
        for colonne in range(range_colonne[0], range_colonne[1]):
            if not winner:
                if couleur == grille[ligne][colonne] \
                        and couleur == grille[ligne + offset_ligne * 1][colonne + offset_colonne * 1] \
                        and couleur == grille[ligne + offset_ligne * 2][colonne + offset_colonne * 2] \
                        and couleur == grille[ligne + offset_ligne * 3][colonne + offset_colonne * 3]:
                    winner = True
    return winner


def gagnant_d_g(grille, couleur):
    """ Gagnant diagonale gauche"""
    return gagnant_gen(grille, couleur, 3, (3, 7), 1, -1)


def gagnant_d_d(grille, couleur):
    """Gagnant diagonale droite"""
    return gagnant_gen(grille, couleur, 3, (0, 4), 1, 1)


def gagnant_h(grille, couleur):
    """Gagnant horizontale"""
    return gagnant_gen(grille, couleur, 6, (0, 4), 0, 1)


def gagnant_v(grille, couleur):
    """Gagnant verticale"""
    return gagnant_gen(grille, couleur, 3, (0, 7), 1, 0)


def gagnant(grille):
    """ fonction où grille est la grille de jeu sous forme de matrice."""
    result = None

    for c in ['R','J']:
        if gagnant_v(grille, c) or gagnant_h(grille, c) or gagnant_d_d(grille, c) or gagnant_d_g(grille, c):
            result = c

    return result


print(gagnant(  [['V', 'V', 'V', 'V', 'R', 'R', 'J'],
                 ['V', 'V', 'V', 'R', 'V', 'J', 'R'],
                 ['V', 'V', 'V', 'V', 'J', 'J', 'J'],
                 ['V', 'V', 'V', 'J', 'V', 'V', 'J'],
                 ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                 ['V', 'V', 'V', 'V', 'V', 'V', 'V']]))
# 'J'

print(gagnant(  [['V', 'V', 'V', 'J', 'J', 'R', 'V'],
                 ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                 ['V', 'V', 'V', 'V', 'V', 'V', 'R'],
                 ['V', 'V', 'V', 'V', 'V', 'V', 'R'],
                 ['V', 'V', 'V', 'V', 'V', 'V', 'R'],
                 ['V', 'V', 'V', 'V', 'V', 'V', 'R']]))
# R

print(gagnant(  [['V', 'V', 'V', 'J', 'J', 'J', 'J'],
                 ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                 ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                 ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                 ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                 ['V', 'V', 'V', 'V', 'V', 'V', 'V']]))
# J

print(gagnant(  [['J', 'J', 'J', 'J', 'R', 'R', 'V'],
                 ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                 ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                 ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                 ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                 ['V', 'V', 'V', 'V', 'V', 'V', 'V']]))
# J

print(gagnant(  [['V', 'J', 'J', 'J', 'J', 'R', 'V'],
                 ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                 ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                 ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                 ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                 ['V', 'V', 'V', 'V', 'V', 'V', 'V']]))
# J

print(gagnant(  [['V', 'R', 'J', 'J', 'J', 'R', 'V'],
                 ['V', 'J', 'V', 'V', 'V', 'V', 'V'],
                 ['V', 'R', 'V', 'V', 'V', 'V', 'V'],
                 ['V', 'R', 'V', 'V', 'V', 'V', 'V'],
                 ['V', 'R', 'V', 'V', 'V', 'V', 'V'],
                 ['V', 'R', 'V', 'V', 'V', 'V', 'V']]))
# R

print(gagnant(  [['V', 'V', 'V', 'J', 'R', 'R', 'J'],
                 ['V', 'V', 'V', 'R', 'J', 'R', 'R'],
                 ['V', 'V', 'V', 'V', 'R', 'J', 'J'],
                 ['V', 'V', 'V', 'V', 'V', 'V', 'J'],
                 ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                 ['V', 'V', 'V', 'V', 'V', 'V', 'V']]))
# 'J'

print(gagnant(  [['V', 'R', 'J', 'J', 'J', 'R', 'V'],
                 ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                 ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                 ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                 ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                 ['V', 'V', 'V', 'V', 'V', 'V', 'V']]))
# None

print(gagnant([['V', 'R', 'J', 'J', 'J', 'R', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V']])) # None
print(gagnant([['J', 'R', 'J', 'J', 'J', 'R', 'R'], ['V', 'V', 'R', 'J', 'V', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V']])) # None
print(gagnant([['J', 'R', 'J', 'J', 'J', 'R', 'R'], ['V', 'R', 'R', 'J', 'R', 'V', 'V'], ['V', 'V', 'R', 'V', 'J', 'V', 'V'], ['V', 'V', 'V', 'V', 'J', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V']])) # None
print(gagnant([['J', 'R', 'J', 'J', 'J', 'R', 'R'], ['V', 'R', 'R', 'J', 'R', 'J', 'V'], ['V', 'V', 'R', 'V', 'J', 'V', 'V'], ['V', 'V', 'V', 'V', 'J', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V']])) # None
print(gagnant([['J', 'R', 'J', 'J', 'J', 'R', 'R'], ['V', 'R', 'R', 'J', 'R', 'J', 'V'], ['V', 'V', 'R', 'V', 'J', 'V', 'V'], ['V', 'V', 'R', 'V', 'J', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V']])) # None
print(gagnant([['J', 'R', 'J', 'J', 'J', 'R', 'R'], ['V', 'R', 'R', 'J', 'R', 'J', 'J'], ['V', 'V', 'R', 'V', 'J', 'V', 'V'], ['V', 'V', 'R', 'V', 'J', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V']])) # None
print(gagnant([['J', 'R', 'J', 'J', 'J', 'R', 'R'], ['V', 'R', 'R', 'J', 'R', 'J', 'J'], ['V', 'V', 'R', 'V', 'J', 'V', 'R'], ['V', 'V', 'R', 'V', 'J', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V']])) # None
print(gagnant([['J', 'R', 'J', 'J', 'J', 'R', 'R'], ['V', 'R', 'R', 'J', 'R', 'J', 'J'], ['V', 'J', 'R', 'V', 'J', 'V', 'R'], ['V', 'V', 'R', 'V', 'J', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V']])) # None
print(gagnant([['J', 'R', 'J', 'J', 'J', 'R', 'R'], ['R', 'R', 'R', 'J', 'R', 'J', 'J'], ['J', 'J', 'R', 'R', 'J', 'V', 'R'], ['V', 'V', 'R', 'V', 'J', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V']])) # "R"
print(gagnant([['J', 'R', 'J', 'J', 'R', 'R', 'J'], ['V', 'R', 'R', 'J', 'J', 'R', 'R'], ['V', 'R', 'J', 'J', 'R', 'J', 'R'], ['V', 'J', 'R', 'J', 'V', 'V', 'V'], ['V', 'R', 'J', 'V', 'V', 'V', 'V'], ['V', 'J', 'R', 'V', 'V', 'V', 'V']])) # "J"
print(gagnant([['J', 'J', 'R', 'J', 'J', 'J', 'J'], ['R', 'V', 'J', 'R', 'V', 'J', 'R'], ['R', 'V', 'J', 'R', 'V', 'J', 'R'], ['V', 'V', 'V', 'J', 'V', 'R', 'R'], ['V', 'V', 'V', 'R', 'V', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V']])) # "J"
print(gagnant([['J', 'R', 'J', 'J', 'J', 'R', 'J'], ['R', 'R', 'R', 'J', 'J', 'J', 'R'], ['R', 'R', 'V', 'R', 'J', 'J', 'V'], ['V', 'R', 'V', 'V', 'V', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V']])) # "R"
