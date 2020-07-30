def belongs_to_file(word, filename):
    """ fonction reçoit deux chaînes de caractères en paramètre.
    La première correspond à un mot, et la deuxième au nom d’un fichier contenant une liste de mots,
    chacun sur sa propre ligne. La fonction vérifie si le mot figure dans cette liste,
    et retourne True si c’est bien le cas, False sinon. """

    result = False
    with open(filename) as f:
        result = word in f.read().splitlines()

    return result


print(belongs_to_file("fretful\n", "files/words.txt"))  # True
print(belongs_to_file("aaaaa\n", "files/words.txt"))    # False

print(belongs_to_file('prince', 'files/words.txt'))     # True
print(belongs_to_file('princess', 'files/words.txt'))   # True
print(belongs_to_file('soeur', 'files/words.txt'))      # False
print(belongs_to_file('pri', 'files/words.txt'))        # False
