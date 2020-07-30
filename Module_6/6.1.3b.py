# Trouver et afficher la liste des mots du fichier «mots.txt » qui contiennent
# toutes les voyelles ('a', 'e', 'i','o', 'u', 'y').

with open('files/mots.txt') as f:
    print([w.strip() for w in f if {'a','e','i','o','u','y'} <= set(w)])
