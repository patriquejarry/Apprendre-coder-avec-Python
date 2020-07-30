

""" auteur: Thierry Massart
   date: 7 décembre 2017
   Trace avec turtle une étoile dont les extrémités sont bleues
"""
import turtle          # importation du module turtle
turtle.up()            # tant que la tortue est en mode “up”,
                       # son déplacement ne trace rien
turtle.shape('turtle') # change la forme de la tortue (en tortue)
turtle.goto(-80,0)     # la tortue se place en coordonnées (-80, 0)
                       # (-80 pour l’axe des "x" et 0 l’axe des "y")
turtle.color('blue')   # la tortue est bleue
turtle.down()          # tant que la tortue est “down”,
                       # elle tracera la ligne de ses déplacements
turtle.begin_fill()    # va remplir l’intérieur de ce qui est tracé entre
                       # maintenant et le turtle.end_fill() ultérieur
turtle.forward(300)    # la tortue avance de 300 (à droite)
turtle.right(144)      # la tortue effectue une rotation de 144° à droite
turtle.forward(300)    # avance dans la nouvelle direction
turtle.right(144)      # rotation
turtle.forward(300)    # avance
turtle.right(144)      # ...
turtle.forward(300)    #
turtle.right(144)      #
turtle.forward(300)    #
turtle.right(144)      #
turtle.end_fill()      # remplit ce qui a été tracé entre le begin_fill
                       # et cette instruction
turtle.hideturtle()    # cache la tortue
turtle.done()          # laisse l'utilisateur fermer la fenêtre

