def question_1_anagramme_str1(a, b):
    res = False
    for i in a:
        res = (i in b)
    return res


def question_2_anagramme_str2(a, b):
    res = True
    for i in a:
        if i not in b:
            res = False
    return res


def question_3_anagramme_0(a, b):
    return sorted(a) == sorted(b)


def question_4_anagramme_1(a, b):
    a.sort()
    b.sort()
    return a == b


def question_5_anagramme_2(a, b):
    liste_a = list(a)
    liste_a = liste_a.sort()
    liste_b = list(b)
    liste_b = liste_b.sort()
    return liste_a == liste_b


def question_6_anagramme_3(a, b):
    liste_a = list(a)
    liste_a.sort()
    liste_b = list(b)
    liste_b.sort()
    return liste_a == liste_b


def question_7_anagramme_dico(a,b):
    res = False
    if len(a) == len(b):
        dic_a = {}
        dic_b = {}
        for i in a:
            dic_a[i] = dic_a.get(i, 0) + 1
        for i in b:
            dic_b[i] = dic_b.get(i, 0) + 1
        res = dic_a == dic_b
    return res


def question_8_anagramme_dico2(a,b):
    res = False
    if len(a) == len(b):
        dic_a = {}
        dic_b = {}
        for i in a:
            dic_a[i] = dic_a.setdefault(i, 0) + 1
        for i in b:
            dic_b[i] = dic_b.setdefault(i, 0) + 1
        res = dic_a == dic_b
    return res


def question_9_anagramme_list(a, b):
    res = False
    if len(a) == len(b):
        liste_b = list(b)
        res = True
        for i in a:
            if i in liste_b:
                liste_b.remove(i)
            else:
                res = False
    return res


# Correct : Question_3_anagramme_0, Question_6_anagramme_3, question_7_anagramme_dico, question_8_anagramme_dico2, question_9_anagramme_list
# Peut être faux : Question_1_anagramme_str1, Question_2_anagramme_str2, Question_5_anagramme_2
# Se planter : Question_4_anagramme_1,
for f in (question_1_anagramme_str1, question_2_anagramme_str2, question_3_anagramme_0,
          question_5_anagramme_2, question_6_anagramme_3,
          question_7_anagramme_dico, question_8_anagramme_dico2, question_9_anagramme_list):
    print("Avec la fonction", f.__name__)
    print(f('bonjour', 'jourbon') == True)
    print(f('gare', 'gare') == True)
    print(f('gare', 'rage') == True)
    print(f('garé', 'rage') == False)
    print(f('garé', 'ragé') == True)
    print(f('rage', 'garee') == False)
    print(f('raege', 'garee') == True)
    print(f('Banana', 'banana') == False)
    print(f('banana', 'ana') == False)
    print(f('ana', 'banana') == False)
    print(f('anb', 'banana') == False)
    print(f('banana', 'anb') == False)
    print(f('banana', 'ana') == False)
    print(f('abc', 'def') == False)
    print(f('aaaaa', 'aaacc') == False)
    print(f('aaacc', 'aaaaa') == False)
    print(f('aaaccaa', 'ccaaaaa') == True)
    print(f('caaaaac', 'ccaaaaa') == True)
    print(f('caaaaac', 'aaaccaa') == True)
    print(f('a', 'aaa') == False)
    print(f('aaaccaaã', 'ccaaaaaa') == False)
    print(f('caaaaacã', 'ccaaaaaã') == True)
