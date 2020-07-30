"""
Auteur : Cecilia Castelli
Date : 23/04/2020
Description :
Le programme dessine un pavage composé d'hexagones, chaqun divisé
en trois losanges de trois couleurs différents; le pavage est
dessiné dans une fenêtre avec des éxtremitées choisies par
l'utilisateur et est déformé par une sphère emergente.
Le dessin est realizé par le module Turtle.
Entrées:
        inf_gauche : entier qui précise les coordonnées
                     (inf_gauche,inf_gauche) du coin inférieur
                     gauche de la fenêtre contenant le pavage
        sup_droit : entier qui précise les coordonnées
                     (sup_droit,sup_droit) du coin supérieur
                     droit de la fenêtre contenant le pavage
        longueur : float qui précise la distance entre le
                   centre et n'importe quel sommet de l'hexagone
                   (étant un hexagone régulier, il représente
                   aussi la longueur des arrêtes)
        coulor : trois strings contenant les couleurs des trois
                 losanges par lesquels l'hexagone est divisé
        centre : trois entiers qui représentent les coordonnées
                 (x,y,z) du centre de la sphère émergente
        rayon : float qui précise le rayon de la sphère
                émergente
Sorties:
        pavage hexagonal dessiné pas Turtle
"""

import turtle #import le module turtle entier
from math import sin, cos, pi, sqrt, acos, asin, atan2 #import des
#fonctions spécifiques du module math

def pavage(inf_gauche,sup_droit,longueur,col,centre,rayon):
    """Dessine un pavage formé par la répétition d'un hexagone
       de trois couleurs et déformé par un sphère émergente;
       utilise la fonction hexagone
       Entrées :
        inf_gauche : entier qui précise les coordonnées
                     (inf_gauche,inf_gauche) du coin inférieur
                     gauche de la fenêtre contenant le pavage
        sup_droit : entier qui précise les coordonnées
                     (sup_droit,sup_droit) du coin supérieur
                     droit de la fenêtre contenant le pavage
        longueur : float qui précise la distance entre le
                   centre et n'importe quel sommet de l'hexagone
                   (étant un hexagone régulier, il représente
                   aussi la longueur des arrêtes)
        col : triple contenant les couleurs des trois losanges
              par lesquels l'hexagone est divisé
        centre : triple contenant le coordonnées (x,y,z)
                 du centre de la sphère émergente
        rayon : float qui précise le rayon de la sphère
                émergente
       Sorties:
        dessin du pavage
    """

    def hexagone(point, longueur, col, centre, rayon):
        """Dessine un hexagone divisé en trois losanges de différents
           couleurs et déformé par une sphère émergente; utilise la
           fonction deformation
           Entrées :
            point : triple contenant les coordonnées (x,y,z) du
                    centre de l'hexagone avant déformation
            longueur : float qui précise la distance entre le
                   centre et n'importe quel sommet de l'hexagone
                   (étant un hexagone régulier, il represent
                   aussi la longueur des arrête)
            col : triple contenant les couleurs des trois losanges
                  par lesquels l'hexagone est divisé
            centre : triple contenant le coordonnées (x,y,z)
                     du centre de la sphère émergente
            rayon : float qui précise le rayon de la sphère
                    émergente
           Sorties:
            dessin de l'hexagone
        """

        def deformation(p, centre, rayon):
            """ Calcul des coordonnées d'un point suite à la déformation
                engendrée par la sphère émergeante
                Entrées :
                  p : coordonnées (x, y, z) du point du dalage à tracer
                     (z = 0) AVANT déformation
                  centre : coordonnées (X0, Y0, Z0) du centre de la sphère
                  rayon : rayon de la sphère
                Sorties : coordonnées (xprim, yprim, zprim) du point du dallage
                     à tracer APRÈS déformation
            """
            x, y, z = p
            xprim, yprim, zprim = x, y, z
            xc, yc, zc = centre
            if rayon ** 2 > zc ** 2:
                zc = zc if zc <= 0 else -zc
                r = sqrt(
                    (x - xc) ** 2 + (y - yc) ** 2)  # distance horizontale
                # depuis le point à dessiner jusqu'à l'axe de la sphère
                rayon_emerge = sqrt(rayon ** 2 - zc ** 2)  # rayon de la partie
                # émergée de la sphère
                rprim = rayon * sin(acos(-zc / rayon) * r / rayon_emerge)
                if 0 < r <= rayon_emerge:  # calcul de la déformation
                    # dans les autres cas
                    xprim = xc + (x - xc) * rprim / r  # les nouvelles coordonnées
                    # sont proportionnelles aux anciennes
                    yprim = yc + (y - yc) * rprim / r
                if r <= rayon_emerge:
                    beta = asin(rprim / rayon)
                    zprim = zc + rayon * cos(beta)
                    if centre[2] > 0:
                        zprim = -zprim
            return (xprim, yprim, zprim)


        cen=deformation(point,centre,rayon) #calcule les coordonnées du
        #centre de l'hexagone après déformation
        v1=deformation((point[0]+longueur,point[1],point[2]),centre,rayon)
        #calcule les coordonnées du sommet droit de l'hexagone après
        #déformation
        v2=deformation((point[0]+(1/2)*longueur,point[1]+
                          sin(pi/3)*longueur,point[2]),centre,rayon)
        #calcule les coordonnées du sommet supérieur-droit de l'hexagone
        #après déformation
        v3=deformation((point[0]-(1/2)*longueur,point[1]+
                          sin(pi/3)*longueur,point[2]),centre,rayon)
        #calcule les coordonnées du sommet supérieur-gauche de l'hexagone
        #après déformation
        v4=deformation((point[0]-longueur,point[1],point[2]),centre,rayon)
        #calcule les coordonnées du sommet gauche de l'hexagone après
        #déformation
        v5=deformation((point[0]-(1/2)*longueur,point[1]-
                          sin(pi/3)*longueur,point[2]),centre,rayon)
        #calcule les coordonnées du sommet inférieur-gauche de l'hexagone
        #après déformation
        v6=deformation((point[0]+(1/2)*longueur,point[1]-
                          sin(pi/3)*longueur,point[2]),centre,rayon)
        #calcule les coordonnées du sommet inférieur-droit de l'hexagone
        #après déformation
        turtle.up()
        turtle.goto(cen[0], cen[1]) #positionne la tortue au centre de
        #l'hexagone
        turtle.down()
        for i in range(3): #dessine une losange de l'hexagone par loop
            #dans l'ordre: haut-droit, gauche, bas-droit
            a=v1 #sommets de la losange en haut-droit
            b=v2
            c=v3
            if i==1: #variation des sommets de la losange à gauche par
                #rapport à la losange en haut-droit
                a=v5
                b=v4
            elif i==2: #variation des sommets de la losange en bas-droit
                #par rapport à la losange en haut-droit
                b=v6
                c=v5
            turtle.color(col[i]) #sélectionne la couleur parmi
            #les trois donnés en triple
            turtle.begin_fill()
            turtle.goto(a[0],a[1])
            turtle.goto(b[0],b[1])
            turtle.goto(c[0],c[1])
            turtle.goto(cen[0],cen[1])
            turtle.end_fill()
        return


    point=(inf_gauche,inf_gauche,0) #positionne le centre du premier hexagone
    #sur le bord inférieur gauche du dessin
    while point[1]<=sup_droit: #s'assure que le pavage ne dépasse pas la
        #limite supérieur
        while point[0]<=sup_droit: #s'assure que le pavage ne dépasse pas
            #la limite droite
            hexagone(point,longueur,col,centre,rayon)
            point=point[0]+3*longueur,point[1],point[2] #dessine une ligne
            #d'hexagones en direction gauche-droite
        point=point[0]-(9/2)*longueur,point[1]+sin(pi/3)*longueur,point[2]
        #remonte d'une ligne et ramène en arrière le centre
        while point[0]>=inf_gauche: #s'assure que le pavage ne dépasse pas
            #la limite gauche
            hexagone(point,longueur,col,centre,rayon)
            point=point[0]-3*longueur,point[1],point[2] #dessine une ligne
            #d'hexagones en direction droite-gauche
        point=point[0]+(3/2)*longueur,point[1]+sin(pi/3)*longueur,point[2]
        #remonte d'une ligne et ramène à l'avant le centre
    turtle.hideturtle() #cache la tortue
    turtle.done() #fixe l'affichage de la fenêtre turtle
    return


#corps du programme: demande les parametres de la fonction pavage
#comme input à l'utilizateur; chaque input affiche une string
#qui specifie quel valeur est demandé à chaque moment
#inf_gauche=int(input("Coin inférieur gauche (val , val) : "))
#sup_droit=int(input("Coin supérieur droit (val , val) : "))
#longueur=float(input("Longueur d'un arrête : "))
#color=(input("Couleur 1 : "),input("Couleur 2 : "),
#       input("Couleur 3 : "))
#centre=(int(input("Abscisse du centre de la sphère : ")),
#        int(input("Ordonnée du centre de la sphère : ")),
#            int(input("Hauteur du centre de la sphère : ")))
#r=float(input("Rayon de la sphère : "))

inf_gauche = -305
sup_droit = 305
longueur = 20
color = ("blue", "black", "red")
centre = (-50, -50, -50)
r = 200

pavage(inf_gauche,sup_droit,longueur,color,centre,r)
#utilize la fonction pavage

