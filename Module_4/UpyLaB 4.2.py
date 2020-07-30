def soleil_leve(a, b, c):
    a = a % 24
    b = b % 24

    if a == b == 0:
        return True
    elif a == b == 12:
        return False
    elif a <= b:
        return a <= c < b
    else:
        return (a <= c <= 23) or (0 <= c < b)


e1515a = int(input())
e1515b = int(input())
e666a = int(input())
e666b = int(input())

for i in range(24):
    leve = soleil_leve(e1515a, e1515b, i) or soleil_leve(e666a, e666b, i)
    print(i, ' *' * (not leve), sep='')
