def rendre_monnaie(prix, x20, x10, x5, x2, x1):
    res20 = None
    res10 = None
    res5 = None
    res2 = None
    res1 = None

    entree_totale = x20 * 20 + x10 * 10 + x5 * 5 + x2 * 2 + x1
    if entree_totale >= prix:
        entree_totale -= prix
        res20 = entree_totale // 20
        entree_totale %= 20
        res10 = entree_totale // 10
        entree_totale %= 10
        res5 = entree_totale // 5
        entree_totale %= 5
        res2 = entree_totale // 2
        entree_totale %= 2
        res1 = entree_totale

    return res20, res10, res5, res2, res1


print(rendre_monnaie(38, 1, 1, 1, 1, 1))  # (0, 0, 0, 0, 0)
print(rendre_monnaie(56, 5, 0, 0, 0, 0))  # (2, 0, 0, 2, 0)
print(rendre_monnaie(80, 2, 2, 2, 3, 3))  # (None, None, None, None, None)
