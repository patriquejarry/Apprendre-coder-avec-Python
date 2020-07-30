# suite de Collatz ou suite de Syracuse

n = int(input('Valeur du nombre n dont on veut tester la conjecture : '))
while n != 1:
    if n % 2 == 0 :  # si un nombre entier modulo 2 vaut 0, il est pair
        n = n // 2
    else:                 # cas où le nombre est impair
        n = 3 * n + 1
    print(n)