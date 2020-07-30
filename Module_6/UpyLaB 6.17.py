def check_rows(grid):
    """ fonction qui prend en paramètre une grille sous forme de matrice à deux dimensions
    et vérifie si toutes les lignes sont valides (c’est-à-dire que sur chaque ligne,
    chaque chiffre apparaît une et une seule fois). """

    numbers = '123456789'
    result = True
    for ligne in grid:
        for n in numbers:
            result &= int(n) in ligne

    return result


def check_cols(grid):
    """ fonction qui prend en paramètre une grille sous forme de matrice à deux dimensions
    et vérifie si toutes les colonnes sont valides (c’est-à-dire que sur chaque colonne,
    chaque chiffre apparaît une et une seule fois). """

    # inverse cols vers rows et check rows
    grid2 = [[grid[i][j] for i in range(len(grid))] for j in range(len(grid))]

    return check_rows(grid2)


def check_regions(grid):
    """ fonction qui prend en paramètre une grille sous forme de matrice à deux dimensions
    et vérifie si toutes les régions sont valides (c’est-à-dire que dans chaque région,
    chaque chiffre apparaît une et une seule fois). """

    # inverse region vers rows et check rows
    x = [[0 for i in range(len(grid))] for j in range(len(grid))]
    for i in range(9):
        for j in range(9):
            x[i][j] = grid[j % 3 + (i//3 * 3)][j // 3 + (i - i//3 * 3) * 3]

    return check_rows(x)


def check_sudoku(grid):
    """ fonction capable de vérifier si la grille passée en paramètre, sous forme d’une matrice 9 x 9 d’entiers,
    est une solution au problème du sudoku. La fonction retournera la réponse (True ou False). """

    return check_rows(grid) and check_cols(grid) and check_regions(grid)


print(check_sudoku(  [[9, 6, 3, 1, 7, 4, 2, 5, 8],
                      [1, 7, 8, 3, 2, 5, 6, 4, 9],
                      [2, 5, 4, 6, 8, 9, 7, 3, 1],
                      [8, 2, 1, 4, 3, 7, 5, 9, 6],
                      [4, 9, 6, 8, 5, 2, 3, 1, 7],
                      [7, 3, 5, 9, 6, 1, 8, 2, 4],
                      [5, 8, 9, 7, 1, 3, 4, 6, 2],
                      [3, 1, 7, 2, 4, 6, 9, 8, 5],
                      [6, 4, 2, 5, 9, 8, 1, 7, 3]]))
# True

print(check_sudoku(  [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                      [2, 3, 4, 5, 6, 7, 8, 9, 1],
                      [3, 4, 5, 6, 7, 8, 9, 1, 2],
                      [4, 5, 6, 7, 8, 9, 1, 2, 3],
                      [5, 6, 7, 8, 9, 1, 2, 3, 4],
                      [6, 7, 8, 9, 1, 2, 3, 4, 5],
                      [7, 8, 9, 1, 2, 3, 4, 5, 6],
                      [8, 9, 1, 2, 3, 4, 5, 6, 7],
                      [9, 1, 2, 3, 4, 5, 6, 7, 8]]))
# False

print(check_regions( [[9, 6, 3, 1, 7, 4, 2, 5, 8],
                      [1, 7, 8, 3, 2, 5, 6, 4, 9],
                      [2, 5, 4, 6, 8, 9, 7, 3, 1],
                      [8, 2, 1, 4, 3, 7, 5, 9, 6],
                      [4, 9, 6, 8, 5, 2, 3, 1, 7],
                      [7, 3, 5, 9, 6, 1, 8, 2, 4],
                      [5, 8, 9, 7, 1, 3, 4, 6, 2],
                      [3, 1, 7, 2, 4, 6, 9, 8, 5],
                      [6, 4, 2, 5, 9, 8, 1, 7, 3]]))
# True

print(check_regions( [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                      [2, 3, 4, 5, 6, 7, 8, 9, 1],
                      [3, 4, 5, 6, 7, 8, 9, 1, 2],
                      [4, 5, 6, 7, 8, 9, 1, 2, 3],
                      [5, 6, 7, 8, 9, 1, 2, 3, 4],
                      [6, 7, 8, 9, 1, 2, 3, 4, 5],
                      [7, 8, 9, 1, 2, 3, 4, 5, 6],
                      [8, 9, 1, 2, 3, 4, 5, 6, 7],
                      [9, 1, 2, 3, 4, 5, 6, 7, 8]]))
# False

print(check_cols(  [[9, 6, 3, 1, 7, 4, 2, 5, 8],
                    [1, 7, 8, 3, 2, 5, 6, 4, 9],
                    [2, 5, 4, 6, 8, 9, 7, 3, 1],
                    [8, 2, 1, 4, 3, 7, 5, 9, 6],
                    [4, 9, 6, 8, 5, 2, 3, 1, 7],
                    [7, 3, 5, 9, 6, 1, 8, 2, 4],
                    [5, 8, 9, 7, 1, 3, 4, 6, 2],
                    [3, 1, 7, 2, 4, 6, 9, 8, 5],
                    [6, 4, 2, 5, 9, 8, 1, 7, 3]]))
# True

print(check_cols(  [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [2, 3, 4, 5, 6, 7, 8, 9, 1],
                    [3, 4, 5, 6, 7, 8, 9, 1, 2],
                    [4, 5, 6, 7, 8, 9, 1, 2, 3],
                    [5, 6, 7, 8, 9, 1, 2, 3, 4],
                    [6, 7, 8, 9, 1, 2, 3, 4, 5],
                    [7, 8, 5, 1, 2, 3, 4, 9, 6],
                    [8, 9, 1, 2, 3, 4, 5, 6, 7],
                    [9, 1, 2, 3, 4, 5, 6, 7, 8]]))
# False

print(check_rows(  [[9, 6, 3, 1, 7, 4, 2, 5, 8],
                    [1, 7, 8, 3, 2, 5, 6, 4, 9],
                    [2, 5, 4, 6, 8, 9, 7, 3, 1],
                    [8, 2, 1, 4, 3, 7, 5, 9, 6],
                    [4, 9, 6, 8, 5, 2, 3, 1, 7],
                    [7, 3, 5, 9, 6, 1, 8, 2, 4],
                    [5, 8, 9, 7, 1, 3, 4, 6, 2],
                    [3, 1, 7, 2, 4, 6, 9, 8, 5],
                    [6, 4, 2, 5, 9, 8, 1, 7, 3]]))
# True

print(check_rows(  [[9, 6, 3, 1, 7, 4, 2, 5, 8],
                    [1, 7, 8, 3, 2, 5, 6, 4, 9],
                    [2, 5, 4, 6, 8, 9, 7, 3, 1],
                    [8, 2, 1, 4, 3, 7, 5, 9, 6],
                    [4, 9, 6, 8, 4, 2, 3, 1, 7],
                    [7, 3, 5, 9, 6, 1, 8, 2, 4],
                    [5, 8, 9, 7, 1, 3, 4, 6, 2],
                    [3, 1, 7, 2, 4, 6, 9, 8, 5],
                    [6, 4, 2, 5, 9, 8, 1, 7, 3]]))
# False