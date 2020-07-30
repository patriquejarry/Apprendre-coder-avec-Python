def wc(filename_in):
    t_c = 0
    t_m = 0
    t_l = 0

    for ligne in open(filename_in, encoding="UTF-8"):
        t_l += 1
        t_c += len(ligne)
        for lettre in ligne:
            if not lettre.isalnum():
                ligne = ligne.replace(lettre, ' ')
        lst = ligne.strip().split()
        t_m += len([i for i in lst if len(i) > 0])

    return t_c, t_m, t_l


print(wc('files/wc1.txt'))              # (8, 2, 1)
print(wc('files/Zola.txt'))             # (1356, 219, 1)
print(wc('files/le-petit-prince.txt'))  # (82650, 15317, 1550)
