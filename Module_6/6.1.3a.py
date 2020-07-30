# Dans la section 5 du module 5, nous avons déjà écrit un code pour trouver la liste des lettres communes à deux mots.
# Ceci se fait de façon immédiate en utilisant des ensembles avec le code :
list(set("pommeee") & set("banane")) #liste des lettres communes ['e']

# En détail
a = set("pommeee")
print(a)
b = set("banane")
print(b)
c = a & b
print(c)
d = list(c)
print(d)
