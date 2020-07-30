""" Exemple de code sans paramètre :
yin et yang dessiné avec turtle
"""
import turtle

def yin_yang():
    """ dessine un logo yin-yang de rayon 200 """
    turtle.down()  # met la plume en mode tracé (si ce n'était déjà le cas)
    turtle.width(2)  # grosseur du tracé de 2 points
    # dessine le yin externe
    turtle.color("black", "black")  # le tracé et le remplissage seront en noir
    turtle.begin_fill()  # la ou les formes suivantes seront remplies
    turtle.circle(-100, 180)  # demi cercle intérieur tournant vers la droite
    turtle.circle(-200, -180)  # demi cercle extérieur, en marche arrière
    turtle.circle(-100, -180)  # demi cercle intérieur qui complète le yin
    turtle.end_fill() # remplissage
    # dessine le yang interne
    turtle.color("white") # couleur blanche
    turtle.up() # on ne trace pas ce qui suit
    # déplace la tortue au bon endroit
    turtle.right(90)
    turtle.forward(80)
    turtle.left(90)
    # tracé du disque yang (blanc) interne au yin
    turtle.down()
    turtle.begin_fill()
    turtle.circle(-20)
    turtle.end_fill()
    # se replace au centre
    turtle.up()
    turtle.left(90)
    turtle.forward(80)
    turtle.right(90)
    # dessine le yang externe
    turtle.down()
    turtle.color("black", "white") # contour noir, remplissage blanc
    turtle.begin_fill()
    turtle.circle(-100, 180)
    turtle.circle(-200, -180)
    turtle.circle(-100, -180)
    turtle.end_fill()
    # tracé du disque yin (noir) interne au yang

    turtle.color("black")
    # déplace la tortue au bon endroit
    turtle.up()
    turtle.right(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.down()
    # trace le disque
    turtle.begin_fill()
    turtle.circle(-20)
    turtle.end_fill()
    # se replace au centre
    turtle.up()
    turtle.left(90)
    turtle.forward(80)
    turtle.right(90)
    turtle.down()
    turtle.hideturtle()
    return

#code principal
yin_yang() #réalise le logo