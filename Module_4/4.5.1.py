import turtle


def spirale(couleur, largeur_trait):

    turtle.reset()
    turtle.width(largeur_trait)  # grosseur du tracé de 2 points
    turtle.color(couleur)  # le tracé et le remplissage seront en noir
    turtle.speed(30)
    turtle.down()  # met la plume en mode tracé (si ce n'était déjà le cas)

    for i in range(100):
        # demi cercle intérieur tournant vers la droite
        turtle.circle(i*(largeur_trait/2), 90)


while (True):
    spirale('red', 10)
