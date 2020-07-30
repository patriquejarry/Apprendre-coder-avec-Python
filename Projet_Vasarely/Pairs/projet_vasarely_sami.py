""" Projet_Vasarely Fun Mooc Vasarely
    Auteur Sami Chine
    Date 19 Octobre 2019
"""
# importation des bibliotheques
import turtle
import math


def deformation(p, centre, rayon):
    """ Calcul des coordonnées d'un point suite à la déformation engendrée par la sphère émergeante
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
        r = math.sqrt(
            (x - xc) ** 2 + (y - yc) ** 2) # distance horizontale depuis le point à dessiner jusqu'à l'axe de la sphère
        rayon_emerge = math.sqrt(rayon ** 2 - zc ** 2)  # rayon de la partie émergée de la sphère
        rprim = rayon * math.sin(math.acos(-zc / rayon) * r / rayon_emerge)
        if 0 < r <= rayon_emerge:                 # calcul de la déformation dans les autres cas
            xprim = xc + (x - xc) * rprim / r     # les nouvelles coordonnées sont proportionnelles aux anciennes
            yprim = yc + (y - yc) * rprim / r
        if r <= rayon_emerge:
            beta = math.asin(rprim / rayon)
            zprim = zc + rayon * math.cos(beta)
            if centre[2] > 0:
                zprim = -zprim
    return (xprim, yprim, zprim)


#Sous programme qui dessine un cube
def hexagone (coordonnee,longueur,col,centre,rayon):
    turtle.speed(0) # vitesse d'excution du dessin: vitesse lente
    turtle.up()
    x=coordonnee[0]  #coordonnes d'origine du premier cube: cela correspond au coinf inferieur gauche et coin sup droite
    y=coordonnee[1] # de la fenetre du dessin
    turtle.goto(x,y) # deplacement de la tortue au point d'origine du dessin
    turtle.down()

    # dessin de la premiere face du cube
    turtle.color(col[0])  # couleur de la face sup
    turtle.begin_fill()  # debuter le remplissage
    x = x + longueur * (math.cos(0))  # abscisse avant deformation
    y = y + longueur * (math.sin(0))  # ordonnée avant deformation
    p = (x, y, 0)
    pprim = deformation(p, centre, rayon)  # coordonnées apres deformation
    turtle.goto(pprim[0], pprim[1])  # la tortue va au point déformé

    x = x + longueur * (math.cos(-1 * math.pi / 3))
    y = y + longueur * (math.sin(-1 * math.pi / 3))
    p = (x, y, 0)
    pprim = deformation(p, centre, rayon)
    turtle.goto(pprim[0], pprim[1])

    x = x + longueur * (math.cos(-1 * math.pi))
    y = y + longueur * (math.sin(-1 * math.pi))
    p = (x, y, 0)
    pprim = deformation(p, centre, rayon)
    turtle.goto(pprim[0], pprim[1])

    x = x + longueur * (math.cos(-120 * math.pi / 180))
    y = y + longueur * (math.sin(120 * math.pi / 180))
    p = (x, y, 0)
    pprim = deformation(p, centre, rayon)
    turtle.goto(pprim[0], pprim[1])
    turtle.end_fill()

    # dessin de la deuxieme face du cube
    turtle.color(col[1])
    turtle.begin_fill()
    x=x+longueur*(math.cos(-60*math.pi/180))
    y=y+longueur*(math.sin(-60*math.pi/180))
    p = (x, y, 0)
    pprim = deformation(p, centre, rayon)
    turtle.goto(pprim[0],pprim[1])

    x=x+longueur*(math.cos(-120*math.pi/180))
    y=y+longueur*(math.sin(-120*math.pi/180))
    p = (x, y, 0)
    pprim = deformation(p, centre, rayon)
    turtle.goto(pprim[0],pprim[1])

    x=x+longueur*(math.cos(-240*math.pi/180))
    y=y+longueur*(math.sin(-240*math.pi/180))
    p = (x, y, 0)
    pprim = deformation(p, centre, rayon)
    turtle.goto(pprim[0],pprim[1])

    x = x + longueur * (math.cos(60 * math.pi / 180))
    y = y + longueur * (math.sin(60 * math.pi / 180))
    p = (x, y, 0)
    pprim = deformation(p, centre, rayon)
    turtle.goto(pprim[0], pprim[1])
    turtle.end_fill()




# dessin de la    troisieme face du cube
    turtle.color(col[2])
    turtle.down()
    turtle.begin_fill()
    x=x+longueur*(math.cos(0*math.pi/180))
    y=y+longueur*(math.sin(0*math.pi/180))
    p = (x, y, 0)
    pprim = deformation(p, centre, rayon)
    turtle.goto(pprim[0],pprim[1])
    x=x+longueur*(math.cos(-120*math.pi/180))
    y=y+longueur*(math.sin(-120*math.pi/180))
    p = (x, y, 0)
    pprim = deformation(p, centre, rayon)
    turtle.goto(pprim[0],pprim[1])
    x=x+longueur*(math.cos(-180*math.pi/180))
    y=y+longueur*(math.sin(-180*math.pi/180))
    p = (x, y, 0)
    pprim = deformation(p, centre, rayon)
    turtle.goto(pprim[0],pprim[1])
    x = x + longueur * (math.cos(60 * math.pi / 180))
    y = y + longueur * (math.sin(60 * math.pi / 180))
    p = (x, y, 0)
    pprim = deformation(p, centre, rayon)
    turtle.goto(pprim[0], pprim[1])
    turtle.end_fill()


#dessine un pave de cubes
def pavage (inf_gauche, sup_droit, longueur,col,centre,rayon):
    n = 1 #compteur de ligne de polygones
    angle = math.pi / 3 #
    sup_droit1 = sup_droit # nouvelle position en hauteur  du polygone apres chaque ligne
    pas = 3 * longueur # espacement entre deux polygones
    new_inf_gauche = int(inf_gauche - longueur * (1 + math.cos(angle))) # position de depart  du polygone pour les lignes  paires
    new_sup_droit = int(sup_droit + longueur * (1 + math.cos(angle)))# position de finale  du polygone pour les lignes  paires

    while sup_droit1 > inf_gauche: #tant le polygone n'est pas arrivé a la derniere ligne  de la fenetre
        if n % 2 != 0: #cas d'une ligne impaire
            for x in range(inf_gauche, sup_droit, pas):
                coordonnees = (x, sup_droit1)
                print(coordonnees)
                hexagone(coordonnees,longueur,col,centre, rayon)
            n+=1
        else: #cas d'une ligne paire
            for x in range(new_inf_gauche, new_sup_droit, pas):
                coordonnees = (x, sup_droit1)
                hexagone(coordonnees,longueur,col,centre, rayon)
            n+=1
        sup_droit1 = sup_droit1-longueur *  math.sin(angle)



inf_gauche = -300
sup_droit = 200
longueur = 30
col1='red'
col2= "blue"
col3= 'black'
col=(col1,col2,col3)
centre1=-50
centre2=-50
centre3=-50
col=(col1,col2,col3)
centre=(centre1,centre2,centre3)
rayon=200
pavage(inf_gauche, sup_droit, longueur,col,centre,rayon)
turtle.getcanvas().postscript(file="pavage_deformation1.eps")
turtle.done()