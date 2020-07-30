from math import pi, sin, cos
import turtle
import random
import time

def pave(abscisse_centre, ordonnee_centre, longueur_arete, color1, color2, color3):

#    n = 4
    angle = 120
    turtle.up()
    turtle.goto(abscisse_centre, ordonnee_centre)
    turtle.down()
    for color in (color1, color2, color3): # à chaque itération, trace un losange
        turtle.right(120)
        turtle.color(color, color)
        turtle.begin_fill()
        #for i in range(1, n + 1):
            #turtle.goto(abscisse_centre + longueur_arete * cos(i * 2 * pi / n), ordonnee_centre + longueur_arete * sin(i * 2 * pi / n))
        for j in range(4): # à chaque itération, trace un segment
            angle = 180 - angle
            turtle.left(angle)
            turtle.forward(longueur_arete)
        turtle.end_fill()


turtle.hideturtle()
turtle.speed(100)
turtle.reset()

while True:
    pave(random.randint(-300, 300), random.randint(-300, 300), random.randint(10, 50), 'black', 'red', 'blue')
    pave(random.randint(-300, 300), random.randint(-300, 300), random.randint(10, 50), 'white', 'grey', 'black')

turtle.done()
