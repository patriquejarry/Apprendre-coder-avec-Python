"""
Projet_Vasarely Vasarely dans le cadre du cours FunMooc ULB
Auteur : Emmanuel Confrere
Date   : 26 avril 2020
"""

import turtle
import time
from math import pi, sin, cos, sqrt, acos, asin, atan2


def deformation(p, centre, rayon):
    """ Fonction de déformation a été récupérée sur le site Fun du cours Python
        Calcul des coordonnées d'un point suite à la déformation engendrée par la sphère émergeante
        Entrées :
          p : coordonnées (x, y, z) du point du dalage à tracer (z = 0) AVANT déformation
          centre : coordonnées (X0, Y0, Z0) du centre de la sphère
          rayon : rayon de la sphère
        Sorties : coordonnées (xprim, yprim, zprim) du point du dallage à tracer APRÈS déformation
    """
    x, y, z = p
    xprim, yprim, zprim = x, y, z
    xc, yc, zc = centre
    if rayon ** 2 > zc ** 2:
        zc = zc if zc <= 0 else -zc
        r = sqrt((x - xc) ** 2 + (y - yc) ** 2)  # distance horizontale depuis le point à dessiner jusqu'à
        # l'axe de la sphère
        rayon_emerge = sqrt(rayon ** 2 - zc ** 2)  # rayon de la partie émergée de la sphère
        rprim = rayon * sin(acos(-zc / rayon) * r / rayon_emerge)
        if 0 < r <= rayon_emerge:  # calcul de la déformation dans les autres cas
            xprim = xc + (x - xc) * rprim / r  # les nouvelles coordonnées sont proportionnelles aux anciennes
            yprim = yc + (y - yc) * rprim / r
        if r <= rayon_emerge:
            beta = asin(rprim / rayon)
            zprim = zc + rayon * cos(beta)
            if centre[2] > 0:
                zprim = -zprim
    return (xprim, yprim, zprim)


def dessiner_losange(points, couleur):
    """Cette fonction dessine un polygone de 4 arrêtes dont les points sont
       definie par une liste de 4 points passé en parametre et une couleur de remplissage
       Entrée : points  -> liste de 4 tuples (x,y)
                           représentant les 4 sommets du polygone
                couleur -> Couleur de remplissage
       Sortie : Affichage graphique du polygone
    """
    turtle.color(couleur)
    turtle.up()
    turtle.goto(points[0][0], points[0][1])  # Deplacement au premier point sans tracer
    turtle.begin_fill()
    for i in range(1, 4):
        turtle.goto(points[i][0], points[i][1])
    turtle.goto(points[0][0], points[0][1])
    turtle.end_fill()


def hexagone(point, longueur, col, centre, rayon):
    """Cette fonction calcul les points definissant
       le centre d un hexagone et ces 6 points peripheriques, sur le plan (z=0).
       Elle expose ensuite les points a la fonction de deformation,
       puis dessine l hexagone déformé avec 3 losanges via la fonction dessiner_losange()
       Entrées : point    -> Coordonnées 3D du centre de l'hexagone (x,y,z)
                 longueur -> Rayon du cercle dans lequel s'inscrit l'hexagone
                 col      -> triplet representant les couleurs des 3 losanges
                             composant l'hexagone
                 centre   -> Coordonnées 3D du centre de la sphere de déformation
                 rayon    -> Rayon de la sphere de déformation

       Sortie : Affichage graphique d un hexagone déformé
    """
    # Initialisation d une liste de 7 points definissant un hexagone
    # Le point points[0] est le centre de l'hexagone et sera fixe dans la suite de cette fonction
    points = [(0, 0, 0)] * 7
    # Initialisation d une liste de 4 points definissant les sommets d un polygone de 4 arrêtes
    losanges = [(0, 0, 0)] * 4
    # Calcul de la deformation appliquée au centre de l'hexagone
    # et initialisation du centre de l'hexagone.
    points[0] = deformation(point, centre, rayon)
    # Les 6 points peripherique (sommet de l hexagone) sont calculé ...
    for n in range(6):
        # Calcul des coordonnées du sommet "n+1" sans deformation
        points[n + 1] = ((point[0] + longueur * cos(n * pi / 3)),
                         (point[1] + longueur * sin(n * pi / 3)),
                         point[2])
        # Puis on applique la deformation
        points[n + 1] = deformation(points[n + 1], centre, rayon)

    # Dessiner les losanges inscrit dans l hexagone points[]
    turtle.hideturtle()
    losanges[0] = points[0]  # centre de l hexagone ( depart de tout les losanges )
    for l in range(3):  # 3 losange a dessiner (0, 1, 2)
        for i in range(1, 4):  # 3 points a ajouter (le premier etant invariable car centre de l hexagone)
            if (2 * l + i) % 7 == 0:  # On ferme l'hexagone
                losanges[i] = points[1]
            else:
                losanges[i] = points[2 * l + i]
        dessiner_losange(losanges, col[l])


def pavage(inf_gauche, sup_droit, longueur, col, centre, rayon):
    """ Imprime un dallage avec des hexagones dont on calcul les centres.
        Les hexagone sont inscrit dans un cercle de rayon "longueur" auquel
        une deformation est appliquée.
        Entrée : inf_gauche -> Coordonnés du point(x,y) inferieure gauche
                 sup_droit  -> Coordonnés du point(x,y) superieur droit
                 longueur   -> Rayon du cercle dans lequel s'inscrit l'hexagone
                 col        -> triplet representant les couleurs des 3 losanges
                               composant l'hexagone
                 centre     -> Coordonnées (x,y,z) du centre de la sphere de déformation
                 rayon      -> Rayon de la sphere de déformation

        Sortie : Affichage graphique d'un pavage composé d'hexagones eventuellement déformés.
    """
    turtle.speed(0)
    turtle.reset()
    # Borne inferieure gauche
    x, y = inf_gauche
    # Distance séparant le centre de 2 hexagones consécutif sur la même ligne
    pas_x = 2 * longueur * (1 + cos(pi / 3))
    # Hauteur séparant le centre de 2 hexagones entre deux lignes consécutive
    pas_y = longueur * sin(pi / 3)
    # "num_ligne" sera utilise pour determiner le décalage selon l'axe X
    num_ligne = 0
    # Pour dessiner le dallage on par de la ligne inferieur pour remonter
    # et nous dessinons les hexagones de la gauche vers la droite.
    # Sur les lignes impair on applique un decalage selon l'axe X.
    # L avancement selon l'axe X, se fait avec le pas constant "pas_x", et
    # selon l'axe Y avec le pas constant "pas_y"
    while y <= sup_droit[1]:
        decalage = (num_ligne % 2) * longueur * (1 + cos(pi / 3))
        x = inf_gauche[0] + decalage  # Commencement de la ligne a gauche
        while x <= sup_droit[0]:
            hexagone((x, y, 0), longueur, col, centre, rayon)
            x += pas_x  # On passe a l hexagone suivant (à droite)
        y += pas_y  # On continu avec la ligne superieur
        num_ligne += 1  # Numero de ligne pour calculer un eventuel decalage du depart de ligne


# -- Debut du programme principal --
# -- ---------------------------- --

# -- Initialisation des bornes inferieure et superieur de la fenetre graphique
#val = int(input('Borne inférieur gauche (val, val) :'))
#borne_inf = (val, val)
#val = int(input('Borne supérieur droit  (val, val) :'))
#borne_sup = (val, val)

# -- Initialisation du rayon des hexagone
#longueur = int(input('Longueur d''une arrête : '))

# -- Initialisation des couleurs
#couleur1 = input('Couleur 1 :')
#couleur2 = input('Couleur 2 :')
#couleur3 = input('Couleur 3 :')
#col = (couleur1, couleur2, couleur3)

# -- Initialisation des coordonnées du centre de la sphere
#xc = int(input('Abscisse du centre du cercle :'))
#yc = int(input('Ordonnée du centre du cercle :'))
#zc = int(input('Hauteur du centre du cercle :'))
#centre_sphere = (xc, yc, zc)
#rayon_sphere = int(input('Rayon du cercle :'))


# Tests
p_inf_gauche = -205
p_sup_droit = 205
p_longueur = 50
p_col1 = "black"
p_col2 = "lightgrey"
p_col3 = "grey"
p_centre_x = 0
p_centre_y = 0
p_centre_z = 0
p_rayon = 200

borne_inf = (p_inf_gauche, p_inf_gauche)
borne_sup = (p_sup_droit, p_sup_droit)
longueur = p_longueur
col = (p_col1, p_col2, p_col3)
centre_sphere = (p_centre_x, p_centre_y, p_centre_z)
rayon_sphere = p_rayon

# -- Dessiner le pavage "Vasarely"
pavage(borne_inf, borne_sup, longueur, col, centre_sphere, rayon_sphere)

# -- Pause pour observer
#time.sleep(30)
turtle.done()
