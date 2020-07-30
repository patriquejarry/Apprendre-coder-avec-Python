import turtle

n = int(input("Entrer le nombre de côtes : "))

for i in range(n):
    turtle.forward(100)
    turtle.left(360/n)

if n >= 5 and n % 2 != 0 :
    turtle.goto(0,0)
    turtle.begin_fill()
    for i in range(n):
        turtle.forward(100)
        turtle.left((n-1)*180/n)
    turtle.end_fill()

turtle.done()
