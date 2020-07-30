def rotation(carre, r):
    n = len(carre)
    rot = [[0]*n for i in range(n)]
    for i, l in enumerate(carre):
        for j, e in enumerate(l):
            if r == 'D':
                rot[j][n-1-i] = e
            elif r == 'G':
                rot[n-1-j][i] = e
            elif r == 'V':
                rot[i][n-1-j] = e
            elif r == 'H':
                rot[n-1-i][j] = e

    return rot


def rotation2(carre, r):
    """ Solution du professeur """
    n = len(carre)
    if r == 'D':
        return [[carre[i][j] for i in range(n - 1, -1, -1)] for j in range(n)]
    elif r == 'G':
        return [[carre[i][j] for i in range(n)] for j in range(n - 1, -1, -1)]
    elif r == 'V':
        return [[carre[j][i] for i in range(n - 1, -1, -1)] for j in range(n)]
    elif r == 'H':
        return [[carre[j][i] for i in range(n)] for j in range(n - 1, -1, -1)]


m = [[x for x in range(1, 4)], [x for x in range(4, 7)], [x for x in range(7, 10)]]
print(m)                 # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(rotation(m, 'D'))  # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
print(rotation(m, 'G'))  # [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
print(rotation(m, 'V'))  # [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
print(rotation(m, 'H'))  # [[7, 8, 9], [4, 5, 6], [1, 2, 3]]

print(rotation2(m, 'D'))  # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
print(rotation2(m, 'G'))  # [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
print(rotation2(m, 'V'))  # [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
print(rotation2(m, 'H'))  # [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
