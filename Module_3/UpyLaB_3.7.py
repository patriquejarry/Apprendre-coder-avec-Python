parie = int(input())
sorti = int(input())
montant = 10

if parie >= 0 and parie <= 12 and parie == sorti :
    print(montant * 12)
elif parie == 13 and sorti % 2 == 0 :
    print(montant * 2)
elif parie == 14 and sorti % 2 != 0 :
    print(montant * 2)
elif parie == 15 and (sorti == 1 or sorti == 3 or sorti == 5 or sorti == 7 or sorti == 9 or sorti == 12) :
    print(montant * 2)
elif parie == 16 and (sorti == 2 or sorti == 4 or sorti == 6 or sorti == 8 or sorti == 10 or sorti == 11) :
    print(montant * 2)
else:
    print("0")