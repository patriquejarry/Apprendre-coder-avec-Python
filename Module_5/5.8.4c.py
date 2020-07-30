def has_doubles(mot, qtt_min):
    c = 0
    for i in range(len(mot) - 1):
        if mot[i] == mot[i+1]:
            c += 1
    return c >= qtt_min


def quadruple_doubles_lettres_non_consecutives(file):
    for ligne in open(file):
        if has_doubles(ligne, 4):
            print(ligne.strip())


#print(has_doubles('commiittee', 4))
print('quadruple_doubles_lettres_non_consecutives','files/mots.txt')
quadruple_doubles_lettres_non_consecutives('files/mots.txt')
print('quadruple_doubles_lettres_non_consecutives','files/words.txt')
quadruple_doubles_lettres_non_consecutives('files/words.txt')
