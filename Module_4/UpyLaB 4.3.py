def premier(n):
    """ renvoie vrai si n est un nombre premier"""
    res = True
    if n < 2:
        res = False
    else:
        for i in range(2, n):
            if n % i == 0:
                res = False

    return res


a = int(input())
for i in range(a):
    if premier(i):
        print(i)

