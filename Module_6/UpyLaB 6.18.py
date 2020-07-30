"""
index des regions:
0 1 2  - Chaque region est formée par une grille 3 x 3
3 4 5
6 7 8
"""
import copy


def get_elements_row(grid, index):
    """ retourne une liste avec les elements de la ligne """
    return [e for e in grid[index] if e != 0]


def get_elements_col(grid, index):
    """ retourne une liste avec les elements de la colonne """
    return [grid[y][index] for y in range(len(grid)) if grid[y][index] != 0]


def get_elements_region(grid, index):
    """ retourne une liste avec les elements de la region """
    j = (index // 3) * 3
    i = (index % 3) * 3
    return [grid[y][x] for y in range(j, 3 + j) for x in range(i, 3 + i) if grid[y][x] != 0]


def x_y_to_index_region(coord):
    """ retourne l'index d'une region basé sur les coordonnées x y
    coord : tuple(x, y) où x : index de la colonne, y index de la ligne """
    x, y = coord
    return (y // 3) * 3 + x // 3


def get_elements(grid, coord):
    """ retourne une liste avec les elements de la ligne, colonne et region
    coord : tuple(x, y) où x : index de la colonne, y index de la ligne """
    x, y = coord
    el = get_elements_col(grid, x) + get_elements_row(grid, y) + get_elements_region(grid, x_y_to_index_region(coord))
    return list(set(el))


def get_possible_elements(grid, coord):
    """ retourne une liste avec les elements possibles pour la case
       coord : tuple(x, y) où x : index de la colonne, y index de la ligne """
    el = get_elements(grid, coord)
    return [e for e in range(1, 10) if e not in el]


def is_place_empty(grid, coord):
    """ retourne un boolean qu'indique si la place est vide
       coord : tuple(x, y) où x : index de la colonne, y index de la ligne """
    x, y = coord
    return grid[y][x] == 0


def is_grid_completed(grid):
    """ retourne un boolean qu'indique si la grid est complète
       coord : tuple(x, y) où x : index de la colonne, y index de la ligne """
    resolu = True
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            resolu &= not is_place_empty(grid, (x, y))
    return resolu


def naked_single(grid):
    """ fonction qui reçoit en paramètre une matrice 9 x 9 d’entiers représentant une grille de sudoku,
    et qui renvoie un couple de valeurs :
    un booléen ok qui indique si la grille peut être résolue en utilisant cette seule méthode du candidat unique,
    la grille complétée si ok est égal à True, None sinon. """
    resolu = False
    grid_aux = copy.deepcopy(grid)

    for i in range(9 * 9):  # nombre max de tentatives pour resoudre
        resolu |= is_grid_completed(grid_aux)
        if not resolu:
            for y in range(len(grid)):
                for x in range(len(grid[y])):
                    coord = (x, y)
                    if is_place_empty(grid_aux, coord):
                        pe = get_possible_elements(grid_aux, coord)
                        if len(pe) == 1:
                            grid_aux[y][x] = pe[0]

    return resolu, (grid_aux if resolu else None)


print(naked_single(  [[4, 0, 3, 0, 9, 6, 0, 1, 0],
                      [0, 0, 2, 8, 0, 1, 0, 0, 3],
                      [0, 1, 0, 0, 0, 0, 0, 0, 7],
                      [0, 4, 0, 7, 0, 0, 0, 2, 6],
                      [5, 0, 7, 0, 1, 0, 4, 0, 9],
                      [1, 2, 0, 0, 0, 3, 0, 8, 0],
                      [2, 0, 0, 0, 0, 0, 0, 7, 0],
                      [7, 0, 0, 2, 0, 9, 8, 0, 0],
                      [0, 6, 0, 1, 5, 0, 3, 0, 2]]))
# (True, [[4, 7, 3, 5, 9, 6, 2, 1, 8],
#         [6, 5, 2, 8, 7, 1, 9, 4, 3],
#         [9, 1, 8, 3, 2, 4, 5, 6, 7],
#         [3, 4, 9, 7, 8, 5, 1, 2, 6],
#         [5, 8, 7, 6, 1, 2, 4, 3, 9],
#         [1, 2, 6, 9, 4, 3, 7, 8, 5],
#         [2, 9, 5, 4, 3, 8, 6, 7, 1],
#         [7, 3, 1, 2, 6, 9, 8, 5, 4],
#         [8, 6, 4, 1, 5, 7, 3, 9, 2]])

print(naked_single(  [[0, 0, 6, 0, 4, 0, 1, 0, 0],
                      [0, 5, 0, 0, 9, 0, 0, 6, 0],
                      [8, 0, 0, 0, 0, 0, 0, 0, 5],
                      [0, 0, 0, 3, 0, 4, 0, 0, 0],
                      [3, 1, 0, 0, 0, 0, 0, 4, 8],
                      [0, 0, 0, 8, 0, 7, 0, 0, 0],
                      [6, 0, 0, 0, 0, 0, 0, 0, 9],
                      [0, 2, 0, 0, 3, 0, 0, 5, 0],
                      [0, 0, 1, 0, 5, 0, 7, 0, 0]]))
# (False, None)

print(naked_single([[0, 0, 3, 0, 2, 0, 6, 0, 0], [9, 0, 0, 3, 0, 5, 0, 0, 1], [0, 0, 1, 8, 0, 6, 4, 0, 0], [0, 0, 8, 1, 0, 2, 9, 0, 0], [7, 0, 0, 0, 0, 0, 0, 0, 8], [0, 0, 6, 7, 0, 8, 2, 0, 0], [0, 0, 2, 6, 0, 9, 5, 0, 0], [8, 0, 0, 2, 0, 3, 0, 0, 9], [0, 0, 5, 0, 1, 0, 3, 0, 0]]))
#           (True, [[4, 8, 3, 9, 2, 1, 6, 5, 7], [9, 6, 7, 3, 4, 5, 8, 2, 1], [2, 5, 1, 8, 7, 6, 4, 9, 3], [5, 4, 8, 1, 3, 2, 9, 7, 6], [7, 2, 9, 5, 6, 4, 1, 3, 8], [1, 3, 6, 7, 9, 8, 2, 4, 5], [3, 7, 2, 6, 8, 9, 5, 1, 4], [8, 1, 4, 2, 5, 3, 7, 6, 9], [6, 9, 5, 4, 1, 7, 3, 8, 2]])
