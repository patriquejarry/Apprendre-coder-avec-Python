# Écrivez la fonction histogram(s) qui reçoit une chaîne de caractère s
# et renvoie un dictionnaire dont les clés sont les lettres rencontrées
# et la valeur associée est la fréquence de la lettre dans s.

def histogram(s):
    """Renvoie le dictionnaire des lettres dans s avec leur fréquence."""
    d = {}   # dictionnaire vide
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


h = histogram('brontosaurus')
print(h)
#{'a': 1, 'b': 1, 'o': 2, 'n': 1, 's': 2, 'r': 2, 'u': 2, 't': 1}
