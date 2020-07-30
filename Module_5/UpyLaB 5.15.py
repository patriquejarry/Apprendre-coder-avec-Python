def distance_mots(mot_1, mot_2):
    d = 0
    for a, b in zip(mot_1, mot_2):
        if a != b:
            d += 1
    return d


def correcteur(mot, liste_mots):
    if liste_mots.count(mot) == 0:
        for i in liste_mots:
            if len(i) == len(mot) and distance_mots(i, mot) == 1:
                return i
    return mot


liste = ["chien", "chat", "train", "voiture", "bonjour", "merci"]
print(correcteur("bonvour", liste))   # "bonjour"
print(correcteur("chat", liste))      # "chat"
