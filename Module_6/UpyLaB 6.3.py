def top_3_candidats(moyennes):
    """
    moyennes : dictionnaire contenant comme clés les noms des candidats et comme valeurs la moyenne que chacun a obtenue.
    La fonction retourne un tuple contenant les noms des trois meilleurs candidats, par ordre décroissant de leurs moyennes.
    """
    result = []
    for i in sorted(moyennes.items(), key=lambda x: -x[1]):
        result.append(i[0])
    return tuple(result[:3])

print(top_3_candidats({'Candidat 7': 2, 'Candidat 2': 38, 'Candidat 6': 85, 'Candidat 1': 8, 'Candidat 3': 17, 'Candidat 5': 83, 'Candidat 4': 33}))
# ('Candidat 6', 'Candidat 5', 'Candidat 2')

print(top_3_candidats({'Candidat 1': 84, 'Candidat 5': 94, 'Candidat 4': 22, 'Candidat 2': 76, 'Candidat 3': 43}))
# ('Candidat 5', 'Candidat 1', 'Candidat 2')
print(top_3_candidats({'Candidat 2': 76, 'Candidat 5': 94, 'Candidat 4': 22, 'Candidat 1': 84, 'Candidat 3': 43}))
# ('Candidat 5', 'Candidat 1', 'Candidat 2')
print(top_3_candidats({'Candidat 2': 4, 'Candidat 6': 17, 'Candidat 5': 20, 'Candidat 1': 24, 'Candidat 3': 34, 'Candidat 4': 29, 'Candidat 7': 45, 'Candidat 9': 11, 'Candidat 10': 49, 'Candidat 8': 64}))
# ('Candidat 8', 'Candidat 10', 'Candidat 7')
print(top_3_candidats({'Candidat 2': 28, 'Candidat 5': 10, 'Candidat 1': 6, 'Candidat 3': 37, 'Candidat 4': 30, 'Candidat 6': 1}))
# ('Candidat 3', 'Candidat 4', 'Candidat 2')
print(top_3_candidats({'Candidat 2': 52, 'Candidat 5': 68, 'Candidat 1': 33, 'Candidat 3': 89, 'Candidat 4': 71, 'Candidat 6': 23}))
# ('Candidat 3', 'Candidat 4', 'Candidat 5')
print(top_3_candidats({'Candidat 2': 57, 'Candidat 5': 42, 'Candidat 1': 75, 'Candidat 3': 49, 'Candidat 4': 80, 'Candidat 6': 69}))
# ('Candidat 4', 'Candidat 1', 'Candidat 6')
print(top_3_candidats({'Candidat 2': 12, 'Candidat 5': 57, 'Candidat 1': 73, 'Candidat 3': 24, 'Candidat 4': 23, 'Candidat 6': 88}))
# ('Candidat 6', 'Candidat 1', 'Candidat 5')
