from math import pi, sin, cos, sqrt, acos, asin
import turtle
#module de gestion des fenetres de dialogue
from tkinter.messagebox import *
#liste des couleurs possibles
couleurs = ['blue','green','red','cyan','magenta','yellow','black','white']
def hexagone (point, longueur,col,centre,rayon):
    """Un hexagone avant déformation est un assemblage de 3 losanges.
    La fonction peint un hexagone déformé en traçant des lignes droites
    entre le centre - 3 coordonnées - et les extrémités dont la position est calculée
    avec la fonction deformation.
    Entrées:
    point, 3 composantes du point à déformer
    longueur, longueur de chaque arete
    col, 3 couleurs pour chacun des 3 losanges
    centre, 3 composantes du centre de la sphère de déformation
    rayon, rayon de la sphère de déformation
    Sortie:
    hexagone peint déformé"""
    turtle.up()
    # Calcul coordonnées du centre déformé
    xc_def = deformation((point[0],point[1],point[2]),centre,rayon)[0]
    yc_def = deformation((point[0],point[1],point[2]),centre,rayon)[1]
    # La tortue y va
    turtle.goto(xc_def,yc_def)
    turtle.down()
    # trace les 3 losanges - ordre : sup droit, inf droit, gauche
    for i in range (3):
        # couleur de remplissage du losange
        turtle.color(col[i])
        turtle.begin_fill()
        for j in range (3):
            # trace un coté du losange
            # Calcul coordonnées sommet suivant avant déformation
            x_j = point[0] + (longueur * cos (((2*i+j)*pi)/3))
            y_j = point[1] + (longueur * sin (((2*i+j)*pi)/3))
            # calcul coordonnées sommet suivant après déformation
            x_j_def = deformation((x_j,y_j,point[2]), centre, rayon)[0]
            y_j_def = deformation((x_j,y_j,point[2]), centre, rayon)[1]
            # on trace le coté
            turtle.goto (x_j_def, y_j_def)
        # retour au centre après 3 sommets
        turtle.goto(xc_def,yc_def)
        turtle.end_fill()
    return
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
    if rayon**2 > zc**2:
        zc = zc if zc <= 0 else -zc
        r = sqrt(
            (x - xc) ** 2 + (y - yc) ** 2)  # distance horizontale
            # depuis le point à dessiner jusqu'à l'axe de la sphère
        rayon_emerge = sqrt(rayon ** 2 - zc ** 2) # rayon de la partie
            # émergée de la sphère
        rprim = rayon * sin(acos(-zc / rayon) * r / rayon_emerge)
        if 0 < r <= rayon_emerge: # calcul de la déformation
            # dans les autres cas
            xprim = xc + (x - xc) * rprim / r # les nouvelles coordonnées
            # sont proportionnelles aux anciennes
            yprim = yc + (y - yc) * rprim / r
        if r <= rayon_emerge:
            beta = asin(rprim / rayon)
            zprim = zc + rayon * cos(beta)
            if centre[2] > 0:
                zprim = -zprim
    return (xprim, yprim, zprim)

def pavage(inf_gauche, sup_droit, longueur, col, centre, rayon):
    """ Pave la surface avec les hexagones déformés
    Pour cela, elle utilise la fonction hexagone.
    Entrées:
    inf_gauche, coordonnées x,y du coin inférieur gauche de la fenetre de traçé
    sup_droit, coordonnées x,y du coin supérieur droit de la fenetre de traçé
    longueur, col, centre,rayon, voir fonction hexagone
    Sortie:
    La fonction pavage peint les hexagones déformés
    dont les centres, avant déformation, se trouvent à l’intérieur de la
    fenêtre (bords inclus) avec l’hexagone en bas à gauche, avant déformation,
    centré sur le point (inf_gauche, inf_gauche)."""
    # On va au point inférieur gauche
    x = inf_gauche
    y = inf_gauche
    # Calcul du nombre d'hexagones sur chaque ligne - indice i
    nb_hex_ligne = 1 + (sup_droit - inf_gauche) // (3 * longueur)
    # calcul du nombre d'hexagones sur une colonne - indice j
    nb_hex_col = 1 + int ((sup_droit - inf_gauche) / (longueur * sin(pi / 3)))
    # Traçage des hexagones sur une colonne
    for j in range (nb_hex_col):
        # Traçage des hexagones sur une ligne - le nb d'hexagones n'est pas le meme sur chaque ligne
        i = 0
        while i < nb_hex_ligne:
            hexagone((x,y, 0), longueur, col, centre,rayon)
            # Trace l'hexagone suivant sur la meme ligne
            # son centre est à 3 longueurs du précédent
            x += 3 * longueur
            i += 1
        # Fin de ligne - On passe à la ligne suivante, elle est à sin pi/3 * longueur de la ligne précédente
        y += longueur * sin(pi / 3)
        # Sur la nouvelle ligne, on démarre à 1.5 ou 0 longueur par rapport au démarrage de la ligne précédente
        x_lig = inf_gauche + ((j + 1) % 2) * 1.5 * longueur
        x = x_lig
        # Calcul du nb d'hexagones sur cette ligne
        nb_hex_ligne = 1 + (sup_droit - x_lig) // (3 * longueur)
    turtle.up()
    return
#  Programme principal
"""
Auteur: Mab66
Date : 18:04/2020
Objectif: Sur le modèle de Vasarely, il s'agit de dessiner des pavages hexagonaux, vus d’en haut, 
formés avec des losanges de couleurs différentes, 
déformés par une boule."""
# Taille de la fenetre où s'inscrit le pavage - Controle saisie de valeurs entières
typea = 0
while typea != 1:  # Tant que typea est différent de 1 alors...
    try:  # On demande à l'utilisateur de rentrer un nombre entier...
        inf_gauche = int(input("Coin inférieur gauche - Entrez un nombre entier :"))
        typea = +1  # Si le nombre est un entier positif tout va bien on sort de la boucle.
    except:  # si pas bon alors on lui affiche message.
        print("Veuillez entrer un nombre entier")
typea = 0
while typea != 1:
    try:
        sup_droit = int(input("Coin supérieur droit - Entrez un nombre entier :"))
        typea = +1
    except:
        print("Veuillez entrer un nombre entier")
# Taille d'une arete de chaque hexagone
typea = 0
while typea != 1:
    try:
        longueur = int(input("Longueur d'une arête  - Entrez un nombre entier :"))
        typea = +1
    except:
        print("Veuillez entrer un nombre entier")
# Couleurs des 3 losanges de chaque hexagone
i=0
col =[]
#Boucle de saisie des couleurs avec controle valeur saisie
for i in range (3):
    col_ok=0
    while col_ok == 0:
        libelle_question = 'Couleur ' + str(i+1)+ ' à choisir dans blue,green,red,cyan,magenta,yellow,black,white : '
        reponse = input(libelle_question)
        if reponse in couleurs:
            col_ok = 1
            col.append(reponse)
    i += 1
# Paramètres de la boule de déformation, centre et rayon
float_ok=0
while float_ok != 1:
    try:
        xc = float(input("Abscisse du centre du cercle - entrez un nombre : "))
        float_ok = 1
    except:
        print("Veuillez entrer un nombre")
float_ok = 0
while float_ok != 1:
    try:
        yc = float(input("Ordonnée du centre du cercle - entrez un nombre : "))
        float_ok = 1
    except:
        print("Veuillez entrer un nombre")
float_ok=0
while float_ok != 1:
    try:
        zc = float(input("Hauteur du centre du cercle - entrez un nombre : "))
        float_ok = 1
    except:
        print("Veuillez entrer un nombre")
float_ok=0
while float_ok != 1:
    try:
        rayon = float(input("Rayon de la boule - entrez un nombre : "))
        float_ok = 1
    except:
        print("Veuillez entrer un nombre")
# Appel de la fonction de pavage avec déformation
pavage (inf_gauche, sup_droit, longueur, (col[0],col[1],col[2]),(xc,yc,zc),rayon)
# Stockage du dessin résultat
if askyesno('Sauvegarder ?', 'Voulez vous sauvegarder ?'):
    showwarning('Sauvegarde', 'Ok on sauvegarde...')
    turtle.getcanvas().postscript(file="pavage.eps")
else:
    showinfo('Pas de sauvegarde', "D'accord on ne sauvegarde pas")
turtle.done()


