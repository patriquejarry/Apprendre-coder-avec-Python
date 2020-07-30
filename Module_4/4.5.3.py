"""
Exemple de code avec paramètres :
yin et yang dessiné avec turtle
"""
import turtle


def yin_yang(rayon, color1='black', color2='white'):

    def yin(color_a, color_b, color_yang, r):

        # dessine le yang externe
        turtle.color(color_a, color_b)  # contour noir, remplissage blanc

        turtle.down()
        turtle.begin_fill()
        turtle.circle(-r/2, 180)
        turtle.circle(-r, -180)
        turtle.circle(-r/2, -180)
        turtle.end_fill()
        turtle.up()

        # dessine le yang interne
        yang(color_yang, color_yang, rayon)  # couleur blanche

        return

    def yang(color_a, color_b, r):

        # tracé du disque yin interne au yang
        turtle.color(color_a, color_b)

        # déplace la tortue au bon endroit
        turtle.right(90)
        turtle.forward(r*0.4)
        turtle.left(90)

        # trace le disque
        turtle.down()
        turtle.begin_fill()
        turtle.circle(-r*0.1)
        turtle.end_fill()
        turtle.up()

        # se replace au centre
        turtle.left(90)
        turtle.forward(r*0.4)
        turtle.right(90)
        return

    turtle.width(2)  # grosseur du tracé de 2 points

    # dessine le yin externe
    yin(color1, color1, color2, rayon)

    # dessine le yang externe
    yin(color1, color2, color1, rayon)


# code principal

""" dessine un logo yin-yang de rayon 300 """
yin_yang(300)  # réalise le logo
yin_yang(200, 'red')  # réalise le logo
yin_yang(100, 'green')  # réalise le logo
yin_yang(50, 'yellow')  # réalise le logo

turtle.hideturtle()
turtle.done()
