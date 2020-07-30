def perc_mots_sans_string(str_exclu, file):
    lignes_exclu = 0
    lignes_total = 0
    for ligne in open(file):
        lignes_total += 1
        if str_exclu not in ligne:
            lignes_exclu += 1
            #print(ligne)
    return str(lignes_exclu * 100 // lignes_total) + '%'


print(perc_mots_sans_string('a', 'files/mots.txt'))
print(perc_mots_sans_string('e', 'files/mots.txt'))
print(perc_mots_sans_string('i', 'files/mots.txt'))
print(perc_mots_sans_string('o', 'files/mots.txt'))
print(perc_mots_sans_string('u', 'files/mots.txt'))