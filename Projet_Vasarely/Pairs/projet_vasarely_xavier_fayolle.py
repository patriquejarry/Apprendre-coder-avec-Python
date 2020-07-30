import turtle
from math import pi, sin, cos, sqrt, acos, asin, atan2

def deformation(p, centre, rayon):
    """
    Auteur : MOOC
    Date : inconnue
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
    if rayon**2 > zc**2:
        zc = zc if zc <= 0 else -zc
        r = sqrt(
            (x - xc) ** 2 + (y - yc) ** 2)                  # distance horizontale depuis le point à dessiner jusqu'à l'axe de la sphère
        rayon_emerge = sqrt(rayon ** 2 - zc ** 2)           # rayon de la partie émergée de la sphère
        rprim = rayon * sin(acos(-zc / rayon) * r / rayon_emerge)
        if 0 < r <= rayon_emerge:                           # calcul de la déformation dans les autres cas
            xprim = xc + (x - xc) * rprim / r               # les nouvelles coordonnées sont proportionnelles aux anciennes
            yprim = yc + (y - yc) * rprim / r
        if r <= rayon_emerge:
            beta = asin(rprim / rayon)
            zprim = zc + rayon * cos(beta)
            if centre[2] > 0:
                zprim = -zprim
    return (xprim, yprim, zprim)

def point_plan (i, long):
    """
        Auteur : Xavier Fayolle
        Date : 25 mars 2020

        Retourne la longueur correspondant aux centre et sommets de l'hexagone
        paramètres :
            - i permet de sélectionner un sommet de l'hexagone
            - long : longueur de chaque côté de l'hexagone
            - res : retourne la longueur correspondant aux centre et sommets de l'hexagone
    """

    a = complex(cos(pi / 3), sin(pi / 3))  # a est le rayon de l'hexagone  dans le plan complexe pour une arete de longueur 1

    if i == 0 or i == 4 or i == 8 or i == 12 :
        res = ( 0, 0, 0)
    elif i == 1 or i == 5 :
        res = (long, 0, 0)
    elif i == 2 :
        a5 = a**5
        res = (long * a5.real, long * a5.imag, 0)
    elif i == 3 or i == 11 :
        a4 = a**4
        res = (long * a4.real, long * a4.imag, 0)
    elif i == 6 :
        res = (long * a.real, long * a.imag, 0)
    elif i == 7 or i == 9 :
        a2 = a**2
        res = (long * a2.real, long * a2.imag, 0)
    elif i == 10 :
        a3 = a**3
        res = (long * a3.real, long * a3.imag, 0)
    return res


def hexagone(point, longueur_arete, col, centre, rayon_def):
    """
    Auteur : Xavier Fayolle
    Date : 25 mars 2020

    Dessine avec turtle un hexagone en position ( abscisse_centre, ordonnee_centre, zenith_centre)
    paramètres :
        - point (abscisse_centre, ordonnee_centre, zenith_centre) : point centre de l'hexagone
        -  longueur_arete : longueur de chaque arête de l'hexagone
        - col (color1, color2, color3) : les couleurs des 3 hexagones
        - centre (c_x, c_y, c_z) : le centre de la sphere de déformation
        - rayon_def : rayon de la sphere de déformation """


    (abscisse_centre, ordonnee_centre, zenith_centre) = point
    (c_x, c_y, c_z) = centre
    turtle.up()
    turtle.goto(abscisse_centre, ordonnee_centre)  # On se positionne le cuseur sur l'élément de pavage
    color = list(col)                              # On convertit le tuple col en liste, car c'est un élément indexable
    # on calcule la déformation de l'origine de l'hexagone
    point2 = deformation(point_plan(0, longueur_arete) ,
                         (c_x - abscisse_centre, c_y - ordonnee_centre, c_z - zenith_centre), rayon_def)
    (x_prim, y_prim, z_prim) = point2
    turtle.goto(x_prim + abscisse_centre, y_prim + ordonnee_centre)
    for i in range(3):  # à chaque itération, trace un losange
        turtle.color(color[i])
        turtle.down()
        turtle.begin_fill()
        for j in range(1,5):  # à chaque itération, trace un segment
            point2 = deformation(point_plan(j+4*i,longueur_arete), ( c_x - abscisse_centre, c_y - ordonnee_centre, c_z - zenith_centre), rayon_def)
            (x_prim, y_prim, z_prim) = point2
            turtle.goto(x_prim + abscisse_centre, y_prim + ordonnee_centre)
        turtle.end_fill()






def pavage (inf_gauche, sup_droit, longueur, col, centre, rayon) :
    """
    Auteur : Xavier Fayolle
    Date : 25 mars 2020

    La fonction pavage peint les hexagones déformés dont les centres, avant déformation, se trouvent à l’intérieur
    de la fenêtre (bords inclus) avec l’hexagone en bas à gauche, avant déformation, centré sur
    le point (inf_gauche, inf_gauche).

    Entrée :
    - inf_gauche, sup_droit : des valeurs entières précisant les coordonnées d’une fenêtre dont le coin inférieur gauche est (inf_gauche, inf_gauche)
        et le coin supérieur droit est (sup_droit, sup_droit)
    - longueur_arete : longueur de chaque arête de l'hexagone avant déformation
    - col (color1, color2, color3) : les couleurs des 3 hexagones
    - centre = (x_c, y_c, z_c) : le centre de la sphere de déformation
    - rayon : rayon de la sphere de déformation  """


    decalage_x = longueur*3
    decalage_y = int(longueur_arete*3**0.5/2)
    j1=0
    for j in range(sup_droit, inf_gauche, -decalage_y): # Pas des hexagones selon Y

        j1 += 1
        if j1 % 2 == 0 :
            delta = 0
        else:
            delta = longueur_arete*3/2
        for i in range(inf_gauche, sup_droit, decalage_x) : # Pas des hexagones selon X
            hexagone((i + delta , j, 0), longueur, col, centre, rayon )


turtle.hideturtle()
turtle.speed(0)
turtle.reset()
if __name__ == "__main__": # code de test
    saisie = False   # Si saisie = True, alors on saisie les paramètres de la figure de Vasarely, sinon on prend les
                        # valeurs par défaut
    if saisie :
        inf_gauche = int(input ('Coin inférieur gauche(val, val) :'))
        sup_droit = int(input('Coin supérieur droit(val, val):'))
        longueur_arete = int(input("Longueur d'une arrête :"))
        col_1 = input('Couleur 1 :')
        col_2 = input('Couleur 2 :')
        col_3 = input('Couleur 3 :')
        col = (col_1, col_2, col_3)
        abscisse_centre = int(input('Abscisse du centre du cercle:'))
        ordonnée_centre = int(input('Ordonnée du centre du cercle:'))
        zenith_centre = int(input('Hauteur du centre du cercle:'))
        centre = (abscisse_centre, ordonnée_centre, zenith_centre)
        rayon = int(input('Rayon du cercle:'))
    else :
        inf_gauche = -300
        sup_droit = 300
        longueur_arete = 50
        col = ('blue', 'red', 'black')
        centre = (0, 0, 0)
        rayon = 500

    pavage(inf_gauche, sup_droit, longueur_arete, col, centre, rayon)

turtle.hideturtle()
turtle.done()
