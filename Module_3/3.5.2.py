import turtle
import random

angle = 120
turtle.colormode(255)
turtle.down()
for i in range(3) : # à chaque itération, trace un losange
    turtle.right(120)
    turtle.fillcolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    turtle.begin_fill()
    for j in range(4) : # à chaque itération, trace un segment
        angle = 180 - angle
        turtle.left(angle)
        turtle.forward(100)
    turtle.end_fill()
turtle.hideturtle()
turtle.done()