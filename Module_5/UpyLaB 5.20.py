def nouveaux_heros1(filename_in, filename_out):
    HERO1 = ['Pierre', 'Paul', 'Jacqueline']
    HERO2 = ['Paul', 'Tom', 'Mathilde']

    file_out = open(filename_out, 'w', encoding="UTF-8")
    for ligne in open(filename_in, encoding="UTF-8"):
        ligne_ar = ligne.split()
        for i, mot in enumerate(ligne_ar):
            for h1, h2 in zip(HERO1, HERO2):
                if mot == h1:
                    ligne_ar[i] = h2
        file_out.write(" ".join(ligne_ar) + '\n')
    file_out.close()


def nouveaux_heros(filename_in, filename_out):
    HERO1 = ['Pierre', 'Paul', 'Jacqueline']
    HERO2 = ['Paul', 'Tom', 'Mathilde']
    HEROX = ['%HERO1%', '%HERO2%', '%HERO3%']

    file_out = open(filename_out, 'w', encoding="UTF-8")
    for ligne in open(filename_in, encoding="UTF-8"):
        for i, hero in enumerate(HERO1):
            ligne = ligne.replace(hero, HEROX[i])
        for i, hero in enumerate(HEROX):
            ligne = ligne.replace(hero, HERO2[i])
        file_out.write(ligne)
    file_out.close()


nouveaux_heros('files/histoire_1.txt','files/histoire_1b.txt')
nouveaux_heros('files/histoire_2.txt','files/histoire_2b.txt')
