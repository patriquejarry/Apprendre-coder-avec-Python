def symetrie_horizontale(m):
    n = len(m)
    return [[m[j][i] for i in range(n)] for j in range(n - 1, -1, -1)]


print(symetrie_horizontale([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))   # [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
print(symetrie_horizontale([['a', 'b'], ['c', 'd']]))            # [['c', 'd'], ['a', 'b']]
print(symetrie_horizontale([]))                                  # []
