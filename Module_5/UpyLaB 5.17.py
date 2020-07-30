def decompresse(t):
    return [i[1] for i in t for j in range(i[0])]
    #   m = []
    #   for i in t:
    #       for j in range(i[0]):
    #           m.append(i[1])
    #   return m


print(decompresse([(4, 1), (0, 2), (2, 'test'), (3, 3), (1, 'bonjour')]))   # [1, 1, 1, 1, 'test', 'test', 3, 3, 3, 'bonjour']
