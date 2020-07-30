"""
    Projet_Vasarely Vasarely
    FUN MOOC - Apprendre à coder avec Python
    Auteur : Patrique Jarry
    Date : 22 Mai 2020
    Affiche un tableau d’art optique en dessinant des pavages hexagonaux, vus d’en haut,
    formés avec des losanges de couleurs différentes, déformés par une boule.
    Entrée :
        Les positions inférieur gauche et supérieur droit qui delimitent le tableau.
        La longueur d'une arrête de l'hexagone.
        Les couleurs des trois losanges.
        Les coordonnées (abscisse, ordonnée, hauteur) du centre de la boule.
        Le rayon de la boule.
    Résultat : Affiche le tableau et le sauvegarde en ficher sur disque.
"""
# Importation des modules
import turtle  # module graphique utilisé pour dessiner le tableau
import math    # module mathematique utilisé pour les calcules géométriques
import random

def deformation(p, centre, rayon):
    """ Calcul des coordonnées d'un point suite à la déformation engendrée par la sphère émergente
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
        # distance horizontale depuis le point à dessiner jusqu'à l'axe de la sphère
        r = math.sqrt((x - xc) ** 2 + (y - yc) ** 2)
        rayon_emerge = math.sqrt(rayon ** 2 - zc ** 2)  # rayon de la partie émergée de la sphère
        rprim = rayon * math.sin(math.acos(-zc / rayon) * r / rayon_emerge)
        if 0 < r <= rayon_emerge:                       # calcul de la déformation dans les autres cas
            xprim = xc + (x - xc) * rprim / r           # les nouvelles coordonnées sont proportionnelles aux anciennes
            yprim = yc + (y - yc) * rprim / r
        if r <= rayon_emerge:
            beta = math.asin(rprim / rayon)
            zprim = zc + rayon * math.cos(beta)
            if centre[2] > 0:
                zprim = -zprim
    return (xprim, yprim, zprim)


def trace(x, y, centre, rayon):
    """ La fonction trace un bord de la face de l'hexagone en allant au prochain point après la déformation.
        Entrées :
            x, y : coordonnées (X, Y) du trace à peindre avant déformation
            centre : triple (c_x, c_y, c_z) qui donne le centre de la sphère de déformation.
            rayon : rayon de la sphère de déformation.
        Sorties : Pas de sortie, sortie visuelle seulement
    """
    p_final = (x, y, 0)                                 # point final du trace avant déformation
    p_final_def = deformation(p_final, centre, rayon)   # point final après déformation
    turtle.goto(p_final_def[0], p_final_def[1])         # trace le bord en avançant la tortue


def face(couleur, points, centre, rayon):
    """ La fonction peint une face de l'hexagone en traçant des lignes droites entre les points passés.
        Entrées :
            couleur : couleur de la face.
            points : tuple contenant quatre tuples des coordonnées (X, Y) de la face à peindre avant déformation.
            centre : triple (c_x, c_y, c_z) qui donne le centre de la sphère de déformation.
            rayon : rayon de la sphère de déformation.
        Sorties : Pas de sortie, sortie visuelle seulement
    """
    turtle.penup()                                    # evite traçage accidentel
    trace(points[0][0], points[0][1], centre, rayon)  # positionne la tortue au premier point
    turtle.pendown()                                  # commence à dessiner
    turtle.color(couleur)                             # define la couleur de la face
    turtle.begin_fill()                               # debut de la delimitation de remplissage de la face
    for i in range(1, 5):                             # trace les bords du losange
        trace(points[i % 4][0], points[i % 4][1], centre, rayon)
    turtle.end_fill()                                 # fin de la delimitation
    turtle.penup()                                    # arrete de dessiner


def hexagone(point, longueur, col, centre, rayon):
    """ La fonction peint un hexagone déformé en traçant des lignes droites entre le centre et les extrémités
        dont la position est calculée avec la fonction deformation.
        Entrées :
            point : coordonnées (X0, Y0, Z0) du centre avant déformation de l’hexagone à peindre.
            longueur : distance (avant déformation) entre le centre et n’importe quel sommet de l’hexagone.
            col : tuple contenant trois couleurs (col1, col2, col3) qui vont être utilisées pour dessiner les hexagones.
                col1 représente la couleur du pavé Sud-Est (en bas à droite).
                col2 représente la couleur du pavé Nord-Est (en haut à droite).
                col3 représente la couleur du pavé Ouest (à gauche).
            centre : triple (c_x, c_y, c_z) qui donne le centre de la sphère de déformation.
            rayon : rayon de la sphère de déformation.
        Sorties : Pas de sortie, sortie visuelle seulement
    """
    # Points de la face Nord-Est
    p0 = (point[0] + longueur, point[1])
    p1 = (point[0] + longueur - longueur * math.sin(math.pi/6), point[1] + longueur * math.cos(math.pi/6))
    p2 = (point[0] - longueur * math.sin(math.pi/6), point[1] + longueur * math.cos(math.pi/6))
    p3 = (point[0], point[1])
    # Trace la face
    face(col[0], (p0, p1, p2, p3), centre, rayon)

    # Points de la face Ouest
    p0 = (point[0] - longueur * math.sin(math.pi/6), point[1] + longueur * math.cos(math.pi/6))
    p1 = (point[0] - longueur, point[1])
    p2 = (point[0] - longueur * math.sin(math.pi/6), point[1] - longueur * math.cos(math.pi/6))
    p3 = (point[0], point[1])
    # Trace la face
    face(col[1], (p0, p1, p2, p3), centre, rayon)

    # Points de la face Sud-Est
    p0 = (point[0], point[1])
    p1 = (point[0] + longueur, point[1])
    p2 = (point[0] + longueur - longueur * math.sin(math.pi/6), point[1] - longueur * math.cos(math.pi/6))
    p3 = (point[0] - longueur * math.sin(math.pi/6), point[1] - longueur * math.cos(math.pi/6))
    # Trace la face
    face(col[2], (p0, p1, p2, p3), centre, rayon)


def pavage(inf_gauche, sup_droit, longueur, col, centre, rayon):
    """ La fonction peint les hexagones déformés dont les centres,
            avant déformation, se trouvent à l’intérieur de la fenêtre (bords inclus) avec l’hexagone en bas à gauche,
            avant déformation, centré sur le point (inf_gauche, inf_gauche).
        Entrées :
            inf_gauche, sup_droit : des valeurs entières inf_gauche, sup_droit précisant les coordonnées d’une fenêtre,
                sachant que l’on ne prend en compte que les axes x et y, l'hauteur avant transformation étant égale à 0.
                inf_gauche : entière des coordonnées d’une fenêtre, coin inférieur gauche est (inf_gauche, inf_gauche).
                sup_droit : entière des coordonnées d’une fenêtre, coin supérieur droit est (sup_droit, sup_droit).
            point : coordonnées (X0, Y0, Z0) du centre avant déformation de l’hexagone à peindre.
            longueur : distance (avant déformation) entre le centre et n’importe quel sommet de l’hexagone.
            col : tuple contenant les trois couleurs (col1, col2, col3) qui vont dessiner les hexagones.
                col1 représente la couleur du pavé Sud-Est (en bas à droite).
                col2 représente la couleur du pavé Nord-Est (en haut à droite).
                col3 représente la couleur du pavé Ouest (à gauche).
            centre : triple (c_x, c_y, c_z) qui donne le centre de la sphère de déformation.
            rayon : rayon de la sphère de déformation.
        Sorties : Pas de sortie, sortie visuelle seulement
    """
    n = 1                      # index des lignes
    pas = 3 * longueur         # distance horizontale entre les hexagones
    angle = math.pi / 3        # angle de decalage

    # Abscisse (initiale) du premier hexagone pour les lignes paires
    new_inf_gauche = int(inf_gauche - longueur * (1 + math.cos(angle)))
    # Abscisse (finale) du dernier hexagone pour les lignes paires
    new_sup_droit = int(sup_droit + longueur * (1 + math.cos(angle)))
    # Ordonnée de chaque ligne
    inf_gauche_aux = inf_gauche

    # loop vertical
    while inf_gauche_aux < sup_droit:
        if n % 2 == 0:
            g, d = new_inf_gauche, new_sup_droit    # ligne paire
        else:
            g, d = inf_gauche, sup_droit            # ligne impaire
        # loop horizontal
        for x in range(g, d, pas):
            #a = random.randint(0, 255)
            #b = random.randint(0, 255)
            #c = random.randint(0, 255)
            #a = (abs(x) + 200) % 255
            #b = (abs(x) + 100) % 255
            #c = (abs(x) + 0) % 255
            #col = ((a, a, a), (b, b, b), (c, c, c))
            #col = ((a, b, a), (b, c, b), (c, a, c))
            #col = ((a, b, c), (b, c, a), (c, a, b))
            hexagone((x, inf_gauche_aux, 0), longueur, col, centre, rayon)
        # incrément l'ordonnée d'une ligne
        inf_gauche_aux += longueur * math.sin(angle)
        n += 1


# ################################################################
# Code principal
# ################################################################

# ##############################################
# Entrées
# ##############################################
# Fenêtre du tableau
# Coins inférieur et supérieur
#p_inf_gauche = int(input("Coin inférieur gauche (x,x)  (int) : "))
#p_sup_droit = int(input("Coin supérieur droit  (x,x)  (int) : "))

# Hexagones
# Longueur de l'arrête et couleurs de chaque face
#p_longueur = int(input( "Longueur d'une arrête        (int) : "))
#p_col1 = input("Couleur 1                          : ")
#p_col2 = input("Couleur 2                          : ")
#p_col3 = input("Couleur 3                          : ")

# Boule
# Coordonnées tridimensionnel et rayon de la boule
#p_centre_x = int(input("Abscisse du centre du cercle (int) : "))
#p_centre_y = int(input("Ordonnée du centre du cercle (int) : "))
#p_centre_z = int(input("Hauteur du centre du cercle  (int) : "))
#p_rayon = int(input("Rayon du cercle              (int) : "))

# Tests
p_inf_gauche = -305
p_sup_droit = 305
p_longueur = 10
p_col1 = "green2"
p_col2 = "gold"
p_col3 = "green"
p_centre_x = 0
p_centre_y = 0
p_centre_z = 0
p_rayon = 350

# ##############################################
# Exécution
# ##############################################
print("Allez hop ! C'est parti...")
turtle.speed(0)
turtle.tracer(1000)
#turtle.tracer(0,0)
turtle.colormode(255)
pavage(p_inf_gauche, p_sup_droit, p_longueur, (p_col1, p_col2, p_col3), (p_centre_x, p_centre_y, p_centre_z), p_rayon)
turtle.hideturtle()
turtle.update()
turtle.getcanvas().postscript(file="projet_vasarely_patrique_jarry2.eps")
turtle.done()
