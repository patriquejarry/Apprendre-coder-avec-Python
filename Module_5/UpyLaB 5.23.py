def init_mat(m, n):
    #return [[0]*n]*m
    return [[0]*n for i in range(m)]

print(init_mat(2, 3))   # [[0, 0, 0], [0, 0, 0]]
print(init_mat(0, 0))   # []
print(init_mat(4, 2))   # [[0, 0], [0, 0], [0, 0], [0, 0]]
print(init_mat(4, 1))   # [[0], [0], [0], [0]]
print(init_mat(1, 4))   # [[0, 0, 0, 0]]
