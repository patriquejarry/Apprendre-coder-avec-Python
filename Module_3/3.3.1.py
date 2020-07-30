import random
secret = random.randint(0, 5)

if int(input("Veuillez choisir un numéro entre 0 et 5 : ")) == secret :
    print("gagné !")
else :
    print("perdu !  La valeur était ", secret)
