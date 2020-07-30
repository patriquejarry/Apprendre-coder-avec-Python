def has_doubles_consecutives(mot, qtt_min, qtt_doubles):
    c = 0
    length_min = 2 * qtt_doubles - 1
    if len(mot) > length_min:
        for i in range(len(mot) - length_min):
            ok = True
            for j in range(qtt_doubles):
                ok &= mot[i+2*j] == mot[i+2*j + 1]
            if ok:
                c += 1
    return c >= qtt_min


def triple_doubles_lettres_consecutives(file):
    for ligne in open(file):
        if has_doubles_consecutives(ligne, 1, 3):
            print(ligne.strip())


#print(has_doubles_consecutives('commtteeii', 1, 3))
print('triple_doubles_lettres_consecutives','files/mots.txt')
triple_doubles_lettres_consecutives('files/mots.txt')
print('triple_doubles_lettres_consecutives','files/words.txt')
triple_doubles_lettres_consecutives('files/words.txt')
