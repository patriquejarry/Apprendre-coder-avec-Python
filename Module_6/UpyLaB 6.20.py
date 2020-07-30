""" programme qui lit depuis l’entrée deux chaînes de caractères, représentant les noms des deux fichiers décrits
 ci-dessus (dans l’ordre, le fichier de type “result-pass-fail.csv” suivi du fichier du type “result-count-0.csv”),
 et qui imprime la liste des intitulés, un par ligne, dans l’ordre décroissant des « valeurs » calculées comme suit.
 La « valeur » d’un intitulé est le nombre des « apprenants fiables » ayant réussi l’exercice correspondant.
 Un « apprenant fiable » est un apprenant qui n’a jamais testé plus de 10x chacun des codes qu’il a essayé de valider.
 Par exemple, si un apprenant n’a testé que trois exercices en soumettant respectivement 1, 2 et 10 essais,
 il est réputé « fiable ». Si un autre apprenant a testé tous les exercices,
 mais en soumettant 11 essais pour l’un d’entre eux, il n’est pas considéré comme « fiable ».
 """


def file_to_list(filename):

    liste = list()
    for ligne in open(filename, encoding="UTF-8"):
        liste.append(ligne.strip().split(";"))
    return liste


def get_lignes_to_ignore(list_count):

    lignes_to_ignore = set()
    for i, ligne in enumerate(list_count):
        if i > 0:
            for c in ligne:
                if c != '' and int(c) > 10:
                    lignes_to_ignore.add(i)

    return lignes_to_ignore


def get_total_pass_fail(list_pass_fail, lignes_to_ignore):
    total_pass_fail = {}
    for i, ligne in enumerate(list_pass_fail):
        if i > 0 and i not in lignes_to_ignore:
            for j, vf in enumerate(ligne):
                if vf == 'VRAI':
                    k = list_pass_fail[0][j]
                    total_pass_fail[k] = total_pass_fail.get(k, 0) + 1
    return total_pass_fail


def inverse_dict(dictionaire):
    inv_dict = {}
    for k, v in dictionaire.items():
        inv_dict[v] = inv_dict.get(v, list())
        inv_dict[v].append(k)
        inv_dict[v] = sorted(inv_dict[v], reverse=True)

    return inv_dict


def process_files(file_pass_fail, file_count):

    list_file_count = file_to_list(file_count)
    lignes_to_ignore = get_lignes_to_ignore(list_file_count)
    list_file_pass_fail = file_to_list(file_pass_fail)
    total_pass_fail_by_title = get_total_pass_fail(list_file_pass_fail, lignes_to_ignore)
    total_pass_fail_by_total = inverse_dict(total_pass_fail_by_title)
    title_ordered = [v for k, v in sorted(total_pass_fail_by_total.items(), key=lambda item: item[0], reverse=True)]
    for i in title_ordered:
        for j in i:
            print(j)


# process_files(input(), input())

process_files("files/result-pass-fail-0.csv", "files/result-count-0.csv")
# ex2
# ex3
# ex1

process_files("files/result-pass-fail-1.csv", "files/result-count-1.csv")
# 1.1. Imprime Bonjour UpyLaB !
# 2.1. Assignations simples
# 2.2. Moyenne arithmetique
# 2.3. La regle de trois
# 2.4. Moyenne arithmetique 2
# 2.6. Volume d'une sphere
# 2.8. Impressions de textes
# 2.7. Impression d'expressions diverses
# 2.5. Sommets d'un hexagone
# 3.2. Simple test sur un entier a lu
# 3.1. Teste egalite parmi 3 nombres
# 3.3. Teste abc
# 3.4. Parite
# 3.7. Moyenne geometrique
# 3.5. a diviseur ou divise par b
# 3.8. Polyedres reguliers
# 3.6. Roulette
# 3.9. Moyenne d'une suite de nombres
# 3.12. Carre de 'X'
# 3.13. Triangle superieur de 'X'
# 3.10. Petit jeu
# 3.14. Somme de valeurs lues
# 3.11. Programme qui evalue sin(x)
