def valeurs(dico):
    """ fonction retourne, à partir du dictionnaire donné en paramètre,
    une liste des valeurs du dictionnaire triées selon leur clé. """

    # ret = []
    # for k in sorted(dico.keys()):
    #     ret.append(dico[k])
    # return ret
    return [dico[k] for k in sorted(dico.keys())]


print(valeurs({'three': 'trois', 'two': 'deux', 'one': 'un'}))
# ['un', 'trois', 'deux']
