def compteur_lettres(texte):
    """ La fonction renvoie un dictionnaire contenant toutes les lettres de l’alphabet
    associées à leur nombre d’apparition dans texte."""

    dic = {}.fromkeys('abcdefghijklmnopqrstuvwxyz', 0)
    for t in texte.lower():
        if t in dic:
            dic[t] = dic.get(t, 0) + 1

    return dic


print(compteur_lettres("Dessine-moi un mouton !"))
# {'a': 0, 'b': 0, 'c': 0, 'd': 1, 'e': 2,
#  'f': 0, 'g': 0, 'h': 0, 'i': 2, 'j': 0,
#  'k': 0, 'l': 0, 'm': 2, 'n': 3, 'o': 3,
#  'p': 0, 'q': 0, 'r': 0, 's': 2, 't': 1,
#  'u': 2, 'v': 0, 'w': 0, 'x': 0, 'y': 0,
#  'z': 0}
