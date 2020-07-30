import random

MY_PRECIOUS = 1
TRAP = -1


def create_map(size, trapsNbr):
    """ fonction qui reçoit deux entiers en paramètres, size, compris entre 2 et 100, et trapsNbr,
    de valeur strictement inférieure à size x size, et qui retourne un dictionnaire implémentant comme dans
    l’exemple précédent une carte de taille size et dans laquelle figurent trapsNbr cases contenant un piège
    (modélisé par la valeur -1) et une case contenant un trésor (modélisé par la valeur 1).
    L’emplacement de ces cases sera aléatoire. """

    my_map = {}
    while len(my_map) < trapsNbr:
        my_map.setdefault((random.randint(1, size), random.randint(1, size)), TRAP)

    while len(my_map) < trapsNbr + 1:
        my_map.setdefault((random.randint(1, size), random.randint(1, size)), MY_PRECIOUS)

    return my_map


def play_game(map_size, treasure_map):
    """ fonction qui reçoit un entier et une carte de taille map_size x map_size, telle que celles obtenues
    grâce à la fonction create_map, et qui demande à l’utilisateur d’entrer les coordonnées d’une case,
    jusqu’à tomber sur une case occupée. Si l’utilisateur a trouvé le trésor, la fonction retourne la valeur True,
    sinon l’utilisateur est tombé sur un piège et la fonction retourne False. """

    while True:
        coord = input().split()
        if len(coord) == 2 and coord[0].isdigit() and coord[1].isdigit():
            i, j = int(coord[0]), int(coord[1])
            if i in range(map_size + 1) and j in range(map_size + 1):
                if (i, j) in treasure_map:
                    return treasure_map.get((i, j)) == MY_PRECIOUS


print(play_game(5, {(3, 4): -1, (4, 1): 1, (2, 3): -1, (1, 5): -1}))
# 4 2
# 4 4
# 1 3
# 4 4
# 3 1
# 4 4
# 4 3
# 1 1
# 3 1
# 3 2
# 2 1
# 4 3
# 1 2
# 4 1
# True


print(play_game(5, {(3, 4): -1, (4, 1): 1, (2, 3): -1, (1, 5): -1}))
# 4 7
# 4 3
# 2 5
# 2 3
# False


print(create_map(4, 5))
# {(3, 1): 1, (4, 2): -1, (1, 1): -1, (1, 4): -1, (2, 2): -1, (4, 4): -1}
