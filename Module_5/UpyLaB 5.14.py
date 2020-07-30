def distance_mots(mot_1, mot_2):
    d = 0
    for a, b in zip(mot_1, mot_2):
        if a != b:
            d += 1
    return d


print(distance_mots("lire", "bise"))      # 2
print(distance_mots("Python", "Python"))  # 0
print(distance_mots("merci", "adieu"))    # 5
