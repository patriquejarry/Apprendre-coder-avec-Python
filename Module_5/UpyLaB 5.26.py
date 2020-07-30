def antisymetrique(m):
    s = True
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] != -m[j][i]:
                s = False
    return s


print(antisymetrique([[0, 1, 1], [-1, 0, 1], [-1, -1, 0]]))   # True
print(antisymetrique([[0, 1], [1, 0]]))                       # False
print(antisymetrique([[1, -2], [2, 1]]))                      # False
