from math import cos, sin, pi
import turtle


def polygone_turtle(n, x, y, rayon, couleur, fill):

    turtle.color(couleur, couleur)
    turtle.goto(x, y)
    turtle.down()
    if fill:
        turtle.begin_fill()
    for i in range(n):
        turtle.left(360/n)
        turtle.forward(rayon)
    if fill:
        turtle.end_fill()
    turtle.up()


def polygone_turtle_aide(n, x, y, rayon, couleur, fill):

    turtle.color(couleur, couleur)
    turtle.goto(x + rayon, y)
    turtle.down()
    if fill:
        turtle.begin_fill()
    for i in range(1, n + 1):
        turtle.goto(x + rayon * cos(i * 2 * pi / n), y + rayon * sin(i * 2 * pi / n))
    if fill:
        turtle.end_fill()
    turtle.up()


turtle.speed(1)
turtle.circle(2)

polygone_turtle(4, 0, 0, 100, 'red', False)
polygone_turtle(6, 200, 200, 100, 'yellow', False)
polygone_turtle(8, -200, -200, 100, 'orange', False)

polygone_turtle_aide(4, 0, 0, 100, 'red', True)
polygone_turtle_aide(6, 200, 200, 100, 'yellow', True)
polygone_turtle_aide(8, -200, -200, 100, 'orange', True)

turtle.done()