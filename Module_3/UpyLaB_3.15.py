saut = int(input())
position_cible = int(input())

fin = False
position_courante = 0

while not fin:
    position_courante += saut
    position_courante %= 100
    if position_courante == position_cible:
        print("Cible atteinte")
        fin = True
    elif position_courante == 0:
        print("0\nPas trouvé")
        fin = True
    else:
        print(position_courante)
