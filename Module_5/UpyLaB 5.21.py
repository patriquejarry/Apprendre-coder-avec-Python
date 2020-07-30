def liste_des_mots(filename_in):
    liste = set()
    delim_default = ' '
    delim = "-'\"?!:;.,*=()1234567890"
    for ligne in open(filename_in, encoding="UTF-8"):
        for l in ligne:
            if l in delim or not l.isalpha():
                ligne = ligne.replace(l, delim_default)
        for mot in ligne.strip().lower().split(delim_default):
            if len(mot) > 0:
                liste.add(mot)

    return sorted(liste)


print(liste_des_mots('files/Zola.txt'))
print(liste_des_mots('files/le-petit-prince.txt'))
